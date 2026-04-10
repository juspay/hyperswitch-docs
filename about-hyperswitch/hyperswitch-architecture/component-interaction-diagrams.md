# Component Interaction Diagrams

**Purpose**: Visual documentation of component interactions and data flow within Hyperswitch architecture.

**Last Updated**: April 2026

## Overview

This document provides detailed interaction diagrams showing how different components of Hyperswitch communicate and process data throughout various payment flows.

## Table of Contents

1. [High-Level Architecture](#high-level-architecture)
2. [Payment Flow Interactions](#payment-flow-interactions)
3. [System Component Communications](#system-component-communications)
4. [Data Flow Patterns](#data-flow-patterns)
5. [Security Boundaries](#security-boundaries)

---

## High-Level Architecture

### System Context Diagram

```mermaid
graph TB
    subgraph "External Systems"
        MERCHANT["Merchant Application<br/>Web/Mobile App"]
        CUSTOMER["Customer<br/>End User"]
    end
    
    subgraph "Hyperswitch Platform"
        HS["Hyperswitch Core<br/>Payment Orchestrator"]
        CC["Control Center<br/>Admin Dashboard"]
        VAULT["Card Vault<br/>PCI Zone"]
    end
    
    subgraph "Payment Ecosystem"
        STRIPE["Stripe"]
        ADYEN["Adyen"]
        PAYPAL["PayPal"]
        OTHER["Other PSPs<br/>(34+ Connectors)"]
    end
    
    subgraph "Supporting Infrastructure"
        DB[(PostgreSQL<br/>Primary & Replicas)]
        CACHE[(Redis<br/>Cache & Queue)]
        MONITORING["Monitoring Stack<br/>(Prometheus/Grafana)"]
    end
    
    CUSTOMER -->|"Initiates Payment"| MERCHANT
    MERCHANT -->|"Payment Request<br/>REST API"| HS
    HS -->|"Admin Operations<br/>REST API"| CC
    HS <-->|"Tokenize/Detokenize<br/>gRPC"| VAULT
    HS -->|"Process Payment<br/>Connector APIs"| STRIPE
    HS -->|"Process Payment<br/>Connector APIs"| ADYEN
    HS -->|"Process Payment<br/>Connector APIs"| PAYPAL
    HS -->|"Process Payment<br/>Connector APIs"| OTHER
    HS <-->|"Read/Write<br/>SQL"| DB
    HS <-->|"Cache/Queue<br/>Redis Protocol"| CACHE
    HS -->|"Metrics & Logs<br/>OTLP/HTTP"| MONITORING
    
    style HS fill:#f96,stroke:#333,stroke-width:4px
    style VAULT fill:#faa,stroke:#333,stroke-width:2px
```

### Component Overview

```mermaid
graph LR
    subgraph "Client Layer"
        SDK["Hyperswitch SDK<br/>(Web/iOS/Android)"]
        API_CLIENT["Direct API Client"]
    end
    
    subgraph "API Gateway Layer"
        LB["Load Balancer<br/>(ALB/NGINX)"]
        API["Router API<br/>(Rust/Actix)"]
    end
    
    subgraph "Core Services"
        ROUTER["Payment Router"]
        CONNECTOR["Connector Manager"]
        SCHEDULER["Task Scheduler"]
        VAULT_SVC["Vault Service"]
    end
    
    subgraph "Data Layer"
        DB[(PostgreSQL)]
        CACHE_REDIS[(Redis)]
        LOCKER[(Card Vault)]
    end
    
    SDK -->|"HTTPS/WebSocket"| LB
    API_CLIENT -->|"HTTPS"| LB
    LB -->|"HTTP"| API
    API -->|"Internal API"| ROUTER
    ROUTER -->|"Route Payment"| CONNECTOR
    ROUTER -->|"Schedule Task"| SCHEDULER
    ROUTER -->|"Secure Tokenization"| VAULT_SVC
    CONNECTOR -->|"Read Config"| CACHE_REDIS
    ROUTER -->|"CRUD Operations"| DB
    SCHEDULER -->|"Queue Jobs"| CACHE_REDIS
    VAULT_SVC -->|"Encrypt/Decrypt"| LOCKER
    
    style ROUTER fill:#f96,stroke:#333,stroke-width:3px
    style CONNECTOR fill:#69f,stroke:#333,stroke-width:2px
```

---

## Payment Flow Interactions

### Standard Payment Flow

```mermaid
sequenceDiagram
    participant C as Customer
    participant M as Merchant App
    participant SDK as Hyperswitch SDK
    participant API as Router API
    participant CACHE as Redis Cache
    participant DB as PostgreSQL
    participant ROUTER as Payment Router
    participant SMART as Smart Router
    participant CONN as Connector Manager
    participant PSP as Payment Processor
    participant VAULT as Card Vault

    C->>M: Initiate Checkout
    M->>SDK: Load Payment Form
    SDK->>API: POST /sessions
    API->>CACHE: Fetch Merchant Config
    CACHE-->>API: Config Data
    API->>DB: Validate API Key
    DB-->>API: Key Valid
    API->>DB: Create Payment Intent
    DB-->>API: Payment Intent ID
    API-->>SDK: Session Token + Methods
    SDK-->>C: Display Payment Options
    
    C->>SDK: Enter Card Details
    SDK->>VAULT: Tokenize Card (PCI)
    VAULT-->>SDK: Payment Method Token
    
    C->>SDK: Confirm Payment
    SDK->>API: POST /payments/{id}/confirm
    API->>ROUTER: Process Payment
    ROUTER->>CACHE: Get Routing Rules
    CACHE-->>ROUTER: Active Rules
    ROUTER->>SMART: Determine Connector
    SMART-->>ROUTER: Selected Connector
    
    ROUTER->>CONN: Execute Payment
    CONN->>PSP: API Call (e.g., Stripe)
    PSP-->>CONN: Authorization Response
    CONN-->>ROUTER: Connector Response
    
    ROUTER->>DB: Update Payment Status
    DB-->>ROUTER: Acknowledged
    
    ROUTER->>API: Payment Result
    API-->>SDK: Confirmation
    SDK-->>M: Payment Complete
    M-->>C: Order Confirmation
    
    Note over API,PSP: Async Webhook Processing
    PSP->>CONN: Webhook Notification
    CONN->>API: POST /webhooks/{psp}
    API->>DB: Update Payment Status
    API->>M: Merchant Webhook
```

### 3D Secure Authentication Flow

```mermaid
sequenceDiagram
    participant C as Customer
    participant SDK as SDK
    participant API as Router API
    participant ROUTER as Payment Router
    participant THREEDS as 3DS Service
    participant ACS as Issuer ACS
    participant CONN as Connector
    participant PSP as Payment Processor

    C->>SDK: Confirm Payment
    SDK->>API: POST /payments/confirm
    API->>ROUTER: Process Payment
    ROUTER->>CONN: Send Authorization
    CONN->>PSP: Attempt Authorization
    PSP-->>CONN: 3DS Required (Step-Up)
    CONN-->>ROUTER: Authentication Required
    
    ROUTER->>THREEDS: Initiate 3DS
    THREEDS->>ACS: Authentication Request
    ACS-->>THREEDS: Challenge URL
    THREEDS-->>API: 3DS Method Data
    API-->>SDK: 3DS Challenge URL
    
    SDK->>ACS: Present Challenge (Iframe/Redirect)
    C->>ACS: Complete Authentication
    ACS-->>SDK: Authentication Result
    SDK->>API: POST /3ds/authentication
    
    API->>THREEDS: Verify Authentication
    THREEDS->>ACS: Validate
    ACS-->>THREEDS: Authentication Successful
    THREEDS-->>API: CAVV/ECI Values
    
    API->>ROUTER: Resume Payment
    ROUTER->>CONN: Authorization with 3DS
    CONN->>PSP: Final Authorization
    PSP-->>CONN: Approved
    CONN-->>ROUTER: Success
    ROUTER-->>API: Payment Complete
    API-->>SDK: Confirmation
```

### Smart Routing Decision Flow

```mermaid
graph TD
    A[Payment Request Received] --> B{Has Active<br/>Routing Rules?}
    
    B -->|Yes| C[Evaluate Rules]
    B -->|No| D[Use Default Fallback]
    
    C --> E{Rule Type}
    E -->|Volume Based| F[Distribute by %]
    E -->|Rule Based| G[Match Conditions]
    E -->|Cost Based| H[Select Lowest Cost]
    
    F --> I{Eligible Connector?}
    G --> I
    H --> I
    
    I -->|Yes| J[Check Connector Health]
    I -->|No| K[Try Fallback List]
    
    J -->|Healthy| L[Route to Connector]
    J -->|Unhealthy| M[Log & Try Next]
    
    M --> N{More Connectors?}
    N -->|Yes| O[Select Next Connector]
    N -->|No| P[Return Error]
    
    O --> J
    
    K --> Q{Connector Eligible<br/>for Payment Method?}
    Q -->|Yes| J
    Q -->|No| N
    
    D --> R[Get Priority List]
    R --> Q
    
    L --> S[Execute Payment]
    P --> T[Return Failure]
    
    style A fill:#f96,stroke:#333,stroke-width:2px
    style L fill:#6f6,stroke:#333,stroke-width:2px
    style P fill:#f66,stroke:#333,stroke-width:2px
```

---

## System Component Communications

### Router Internal Architecture

```mermaid
graph TB
    subgraph "Router Core"
        CORE["Core Module"]
        API_L["API Layer<br/>Handlers"]
        CORE_M["Core Module<br/>Business Logic"]
        
        subgraph "Domain Modules"
            PAYMENT["Payments"]
            REFUND["Refunds"]
            DISPUTE["Disputes"]
            PAYOUT["Payouts"]
        end
        
        subgraph "Services"
            AUTH["Authentication"]
            VALID["Validation"]
            TRANSFORM["Data Transform"]
            ENCRYPT["Encryption"]
        end
    end
    
    subgraph "Connectors"
        CM["Connector Manager"]
        STRIPE["Stripe Adapter"]
        ADYEN["Adyen Adapter"]
        PAYPAL["PayPal Adapter"]
        CUSTOM["Custom Connectors"]
    end
    
    subgraph "External"
        CLIENT["API Client"]
        PSP["Payment Processors"]
    end
    
    CLIENT -->|"HTTP Request"| API_L
    API_L -->|"Validate & Route"| CORE_M
    CORE_M -->|"Process"| PAYMENT
    CORE_M -->|"Process"| REFUND
    
    PAYMENT -->|"Authenticate"| AUTH
    PAYMENT -->|"Validate Data"| VALID
    PAYMENT -->|"Transform"| TRANSFORM
    PAYMENT -->|"Encrypt PII"| ENCRYPT
    
    PAYMENT -->|"Execute"| CM
    CM -->|"Stripe API"| STRIPE
    CM -->|"Adyen API"| ADYEN
    CM -->|"PayPal API"| PAYPAL
    CM -->|"Other"| CUSTOM
    
    STRIPE -->|"HTTPS"| PSP
    ADYEN -->|"HTTPS"| PSP
    PAYPAL -->|"HTTPS"| PSP
    
    style CORE fill:#f96,stroke:#333,stroke-width:2px
```

### Scheduler Job Processing

```mermaid
sequenceDiagram
    participant ROUTER as Payment Router
    participant DB as PostgreSQL
    participant PROD as Producer
    participant CACHE as Redis Queue
    participant CONS as Consumer
    participant EXEC as Job Executor
    participant WEBHOOK as Webhook Service

    ROUTER->>DB: Insert Scheduled Task
    Note over ROUTER,DB: e.g., Delete expired token<br/>Notify API key expiry
    
    loop Producer Polling
        PROD->>DB: Query Due Tasks
        DB-->>PROD: List of Tasks
        PROD->>PROD: Batch Tasks
        PROD->>CACHE: Push to Queue<br/>RPUSH job_queue
    end
    
    loop Consumer Processing
        CONS->>CACHE: Pull Job<br/>BLPOP job_queue
        CACHE-->>CONS: Job Data
        CONS->>EXEC: Execute Job
        
        alt Success
            EXEC->>DB: Update Job Status<br/>COMPLETED
            EXEC->>WEBHOOK: Send Notification
        else Failure
            EXEC->>DB: Retry Count++
            EXEC->>CACHE: Requeue if retries < max
        end
    end
```

### Vault Service Interactions

```mermaid
graph TB
    subgraph "PCI Zone"
        VAULT["Card Vault"]
        ENCRYPT["Encryption Engine"]
        KMS["Key Management<br/>AWS KMS/HashiCorp"]
        STORAGE["Encrypted Storage"]
    end
    
    subgraph "Application Zone"
        ROUTER["Payment Router"]
        TOKEN["Token Generator"]
        VALIDATOR["Request Validator"]
    end
    
    subgraph "Audit & Compliance"
        AUDIT_LOG["Audit Logger"]
        SIEM["SIEM/Splunk"]
    end
    
    ROUTER -->|"1. Store Card"| VALIDATOR
    VALIDATOR -->|"2. Validate"| VAULT
    VAULT -->|"3. Encrypt PAN"| ENCRYPT
    ENCRYPT -->|"4. Get DEK"| KMS
    KMS -->|"5. DEK"| ENCRYPT
    ENCRYPT -->|"6. Store Encrypted"| STORAGE
    VAULT -->|"7. Generate Token"| TOKEN
    TOKEN -->|"8. Return Token"| ROUTER
    
    VAULT -->|"Log Access"| AUDIT_LOG
    AUDIT_LOG -->|"Forward"| SIEM
    
    style VAULT fill:#faa,stroke:#333,stroke-width:3px
    style STORAGE fill:#faa,stroke:#333,stroke-width:2px
```

---

## Data Flow Patterns

### Write Path (Payment Creation)

```mermaid
flowchart LR
    A[Client Request] -->|"POST /payments"| B{Validate API Key}
    B -->|Invalid| C[401 Unauthorized]
    B -->|Valid| D[Parse Request]
    
    D --> E{Validate Schema}
    E -->|Invalid| F[400 Bad Request]
    E -->|Valid| G[Generate ID]
    
    G --> H[Create PaymentIntent]
    H --> I[Write to PostgreSQL]
    I --> J{Success?}
    J -->|No| K[500 Database Error]
    J -->|Yes| L[Cache in Redis]
    
    L --> M[Return 201 Created]
    M --> N[Async: Emit Event]
    N --> O[Kafka/Event Bus]
    
    style I fill:#69f,stroke:#333
    style L fill:#69f,stroke:#333
```

### Read Path (Payment Status)

```mermaid
flowchart LR
    A[GET /payments/:id] --> B{API Key Valid?}
    B -->|No| C[401 Unauthorized]
    B -->|Yes| D{Cache Hit?}
    
    D -->|Yes| E[Return Cached Data]
    D -->|No| F[Query PostgreSQL]
    
    F --> G{Found?}
    G -->|No| H[404 Not Found]
    G -->|Yes| I[Populate Cache]
    I --> J[Return 200 OK]
    
    style E fill:#6f6,stroke:#333
    style F fill:#69f,stroke:#333
```

### Webhook Processing Flow

```mermaid
sequenceDiagram
    participant PSP as Payment Processor
    participant GW as API Gateway
    participant WH as Webhook Handler
    participant VALID as Signature Validator
    participant PROC as Event Processor
    participant DB as Database
    participant QUEUE as Kafka/Queue
    participant MERCHANT as Merchant Endpoint

    PSP->>GW: POST /webhooks/:provider
    GW->>WH: Forward Request
    WH->>VALID: Validate Signature
    
    alt Invalid Signature
        VALID-->>WH: Validation Failed
        WH-->>GW: 401 Unauthorized
        GW-->>PSP: 401 Response
    else Valid Signature
        VALID-->>WH: Validated
        WH->>PROC: Process Webhook
        PROC->>DB: Update Payment Status
        DB-->>PROC: Updated
        
        par Async Processing
            PROC->>QUEUE: Emit Status Change Event
        and Merchant Notification
            PROC->>MERCHANT: POST Merchant Webhook
            MERCHANT-->>PROC: 200 OK
        end
        
        PROC-->>WH: Processed
        WH-->>GW: 200 OK
        GW-->>PSP: 200 Response
    end
```

---

## Security Boundaries

### Network Security Zones

```mermaid
graph TB
    subgraph "DMZ / Edge"
        LB["Load Balancer<br/>ALB/Cloudflare"]
        WAF["WAF<br/>Rate Limiting"]
    end
    
    subgraph "Application Zone"
        API["API Servers<br/>Kubernetes Pods"]
        CACHE["Redis Cache"]
    end
    
    subgraph "Data Zone"
        DB[(PostgreSQL<br/>Master/Replica)]
        VAULT["Card Vault<br/>Isolated Network"]
    end
    
    subgraph "External"
        INTERNET["Internet"]
        MERCHANT["Merchant Systems"]
        PSP["Payment Processors"]
    end
    
    INTERNET -->|"HTTPS:443"| LB
    MERCHANT -->|"API:443"| LB
    LB -->|"HTTP"| WAF
    WAF -->|"Filtered"| API
    
    API <-->|"TLS"| CACHE
    API <-->|"mTLS"| DB
    API <-->|"gRPC mTLS"| VAULT
    
    API -->|"HTTPS + Auth"| PSP
    
    style VAULT fill:#faa,stroke:#f00,stroke-width:3px
    style DB fill:#faa,stroke:#f00,stroke-width:2px
```

### Authentication Flow

```mermaid
sequenceDiagram
    participant CLIENT as Client
    participant API as API Gateway
    participant AUTH as Auth Service
    participant CACHE as Redis
    participant DB as PostgreSQL

    CLIENT->>API: Request + API Key Header
    API->>AUTH: Authenticate
    
    AUTH->>CACHE: Lookup Key Hash
    
    alt Cache Hit
        CACHE-->>AUTH: Key Data + Permissions
    else Cache Miss
        AUTH->>DB: Query API Keys
        DB-->>AUTH: Key Record
        AUTH->>CACHE: Cache Result
    end
    
    AUTH->>AUTH: Validate Key
    
    alt Invalid Key
        AUTH-->>API: 401 Unauthorized
        API-->>CLIENT: 401 Response
    else Expired Key
        AUTH-->>API: 401 Key Expired
        API-->>CLIENT: 401 Response
    else Valid Key
        AUTH-->>API: AuthContext + Permissions
        API->>API: Check Permissions
        
        alt Insufficient Permissions
            API-->>CLIENT: 403 Forbidden
        else Authorized
            API->>API: Process Request
            API-->>CLIENT: 200 OK + Data
        end
    end
```

---

## Deployment Architecture

### Kubernetes Deployment Pattern

```mermaid
graph TB
    subgraph "Kubernetes Cluster"
        subgraph "Namespace: hyperswitch"
            INGRESS["Ingress Controller<br/>NGINX/Traefik"]
            
            subgraph "Payment Tier"
                ROUTER_POD1["Router Pod 1"]
                ROUTER_POD2["Router Pod 2"]
                ROUTER_POD3["Router Pod 3"]
                HPA["HPA<br/>Auto Scaler"]
            end
            
            subgraph "Background Jobs"
                PROD_POD["Producer Pod"]
                CONS_POD1["Consumer Pod 1"]
                CONS_POD2["Consumer Pod 2"]
            end
            
            subgraph "Configuration"
                CONFIG["ConfigMap"]
                SECRETS["Secrets"]
            end
        end
        
        subgraph "Namespace: data"
            DB_POD["PostgreSQL"]
            REDIS_POD["Redis Cluster"]
            VAULT_POD["Card Vault"]
        end
        
        subgraph "Namespace: monitoring"
            PROM["Prometheus"]
            GRAFANA["Grafana"]
            JAEGER["Jaeger/Tempo"]
        end
    end
    
    INGRESS -->|"Route"| ROUTER_POD1
    INGRESS -->|"Route"| ROUTER_POD2
    INGRESS -->|"Route"| ROUTER_POD3
    
    HPA -.->|"Scale"| ROUTER_POD1
    HPA -.->|"Scale"| ROUTER_POD2
    HPA -.->|"Scale"| ROUTER_POD3
    
    ROUTER_POD1 -->|"Query"| DB_POD
    ROUTER_POD1 -->|"Cache"| REDIS_POD
    ROUTER_POD1 -->|"Tokenize"| VAULT_POD
    ROUTER_POD1 -->|"Schedule"| PROD_POD
    
    PROD_POD -->|"Enqueue"| REDIS_POD
    CONS_POD1 -->|"Dequeue"| REDIS_POD
    CONS_POD2 -->|"Dequeue"| REDIS_POD
    
    ROUTER_POD1 -->|"Metrics"| PROM
    ROUTER_POD1 -->|"Traces"| JAEGER
    
    PROM -->|"Visualize"| GRAFANA
```

---

## Key Design Decisions

### Stateless Architecture

```mermaid
graph LR
    subgraph "Stateless Services"
        A[API Server 1]
        B[API Server 2]
        C[API Server 3]
    end
    
    subgraph "Shared State Stores"
        DB[(Database)]
        CACHE[(Redis)]
    end
    
    CLIENT["Client"] -->|"Request 1"| A
    CLIENT -->|"Request 2"| B
    CLIENT -->|"Request 3"| C
    
    A <-->|"Read/Write"| DB
    B <-->|"Read/Write"| DB
    C <-->|"Read/Write"| DB
    
    A <-->|"Cache"| CACHE
    B <-->|"Cache"| CACHE
    C <-->|"Cache"| CACHE
```

**Benefits:**
- Horizontal scaling without sticky sessions
- Easy rolling updates and rollbacks
- Fault tolerance (any pod can handle any request)
- Simplified deployment architecture

### Async Processing Pattern

```mermaid
graph TB
    A[Synchronous Path<br/>Customer-Facing] -->|"Fast Response"| B[Immediate Result]
    A -->|"Emit Event"| C[Kafka/SQS]
    
    C --> D[Async Workers]
    D --> E[Webhook Delivery]
    D --> F[Analytics Update]
    D --> G[Notifications]
    D --> H[Reconciliation]
    
    B --> I[Customer Continues]
    
    style A fill:#f96,stroke:#333,stroke-width:2px
    style C fill:#69f,stroke:#333,stroke-width:2px
```

---

## Tools for Viewing Diagrams

These diagrams use **Mermaid** syntax and can be viewed in:
- GitHub/GitLab Markdown preview
- VS Code with Mermaid extension
- [Mermaid Live Editor](https://mermaid.live)
- [Notion](https://notion.so) (Mermaid block)
- [Obsidian](https://obsidian.md) (with plugin)

## Contributing

When adding new diagrams:
1. Follow existing naming conventions
2. Use consistent styling
3. Include explanatory text
4. Test in Mermaid Live Editor
5. Update this table of contents

---

**Document Owner**: Architecture Team  
**Review Frequency**: Quarterly  
**Last Review**: April 2026  
**Next Review**: July 2026