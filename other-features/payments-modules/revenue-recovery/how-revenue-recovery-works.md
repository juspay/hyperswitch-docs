---
description: >-
  Understand how Revenue Recovery works with your existing setup to reduce
  involuntary churn. This page explains Revenue Recovery's boundaries, how it
  activates, and how data flows across systems.
---

# How Revenue Recovery Works

### What systems are involved?

Revenue Recovery works alongside two systems that most subscription businesses already have in place: a billing engine and one or more payment processors.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','lineColor':'#4B5B76','primaryTextColor':'#0B2A5B','edgeLabelBackground':'#FFFFFF'},'flowchart':{'padding':16,'nodeSpacing':70,'rankSpacing':130}}}%%
flowchart LR
    BE["#160;#160;#160;Billing engine#160;#160;#160;"] -- "#160;#160;#160;Payment trigger#160;#160;#160;" --> PP["#160;#160;#160;#160;Payment processors#160;#160;#160;#160;"]
    PP -- "#160;#160;#160;Payment response#160;#160;#160;" --> BE

    classDef ext fill:#F1F5F9,stroke:#64748B,stroke-width:1.5px,color:#0F172A
    class BE,PP ext
```

**Billing engine**

The billing engine manages the scheduling, invoice generation and payment collection for all recurring plans created by the merchant. It can be a SaaS subscription platform such as Chargebee, Stripe Billing etc., or an in-house billing engine built by the merchant.

**Payment processors**

Payment processors are the systems that actually charge the customer. They are usually integrated with the billing engine, which uses them to automatically charge a customer when an invoice is due. These can be any PSP, such as Stripe, Adyen, PayPal etc., or a payment orchestrator like Hyperswitch.

### How does Revenue Recovery fit into this setup?

Revenue Recovery acts as a third-party plugin between the merchant's billing engine and payment processors.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','lineColor':'#4B5B76','primaryTextColor':'#0B2A5B','edgeLabelBackground':'#FFFFFF'},'flowchart':{'padding':16,'nodeSpacing':70,'rankSpacing':150}}}%%
flowchart LR
    BE["#160;#160;#160;Billing engine#160;#160;#160;"] -- "#160;#160;#160;Failed invoices#160;#160;#160;" --> RR["#160;#160;#160;Revenue Recovery#160;#160;#160;"]
    RR -- "#160;#160;#160;Recovery responses#160;#160;#160;" --> BE
    RR -- "#160;#160;#160;Retry payment trigger#160;#160;#160;" --> PP["#160;#160;#160;#160;Payment processor#160;#160;#160;#160;"]
    PP -- "#160;#160;#160;Payment response#160;#160;#160;" --> RR

    classDef ext fill:#F1F5F9,stroke:#64748B,stroke-width:1.5px,color:#0F172A
    classDef rr fill:#006DF9,stroke:#0050B3,stroke-width:1.5px,color:#FFFFFF
    class BE,PP ext
    class RR rr
```

It gets activated when a recurring payment fails. Revenue Recovery then retries the failed payment with the payment processor on behalf of the billing engine, and once the payment is captured, records the result back into the billing engine.

### How is Revenue Recovery activated?

Revenue Recovery is activated automatically based on the recovery start criteria set by the merchant. Until they are reached, your recurring payments work exactly as they do today.

In all the flows below, Revenue Recovery receives a stream of every transaction made by the billing engine. Every transaction made by Revenue Recovery is also streamed back to the billing engine.

**One-time setup**

The merchant connects the billing engine and the payment processor to Revenue Recovery once, and provides two sets of criteria that control the recovery cycle.

**Recovery start criteria** decide when Revenue Recovery starts retrying. Once they are reached, the recovery cycle begins automatically.

* **Start of recovery:** After how many external retries (retries done by the billing engine) should the recovery process start?

**Recovery end criteria** decide when Revenue Recovery stops retrying. Once they are met, the recovery cycle ends and the invoice is closed.

* **Grace period:** What is the grace period from the first payment failure within which retries can be performed?
* **Total retries:** What is the total number of retries, including external retries, that should be done within the grace period?

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','actorBkg':'#F1F5F9','actorBorder':'#64748B','actorTextColor':'#0F172A','actorLineColor':'#9DB2D3','signalColor':'#33425E','signalTextColor':'#0B2A5B','labelBoxBkgColor':'#006DF9','labelBoxBorderColor':'#0050B3','labelTextColor':'#FFFFFF','loopTextColor':'#0B2A5B','noteBkgColor':'#EAF2FF','noteBorderColor':'#99C2FF','noteTextColor':'#0B2A5B'},'themeCSS':'rect[name=RR]{fill:#006DF9} rect[name=RR] ~ text tspan{fill:#FFFFFF} rect[name=M],.actor-man rect,g[name=M] rect{fill:#F1F5F9 !important;stroke:#64748B !important} rect[name=M] ~ path,.actor-man path,g[name=M] path{fill:#64748B !important;stroke:none !important} .actor-man circle,g[name=M] circle{fill:#F1F5F9 !important;stroke:#64748B !important} .actor-man line,g[name=M] line{stroke:#64748B !important} .actor-man tspan,g[name=M] tspan{fill:#64748B !important} rect.actor-top[name=M] ~ text{display:none} .actor-top.actor-man text{display:none} line[name=M],line#actor0{transform-box:fill-box;transform-origin:center 127px;transform:scaleY(1.237)}'}}%%
sequenceDiagram
    actor M as Merchant
    participant RR as Revenue Recovery

    M->>RR: Connect billing engine
    M->>RR: Connect payment processor
    M->>RR: Provide retry criteria
```

#### When is Revenue Recovery not involved?

When an invoice is due, the billing engine makes the payment directly with the payment processor, as it does today. Revenue Recovery is not involved at this stage. What happens next depends on the outcome of the payment.

**Scenario 1: Payment is successful**

The recurring payment is successful. The invoice is closed and does not enter the recovery cycle.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','actorBkg':'#F1F5F9','actorBorder':'#64748B','actorTextColor':'#0F172A','actorLineColor':'#9DB2D3','signalColor':'#33425E','signalTextColor':'#0B2A5B','labelBoxBkgColor':'#006DF9','labelBoxBorderColor':'#0050B3','labelTextColor':'#FFFFFF','loopTextColor':'#0B2A5B','noteBkgColor':'#EAF2FF','noteBorderColor':'#99C2FF','noteTextColor':'#0B2A5B'},'themeCSS':'rect[name=RR]{fill:#006DF9} rect[name=RR] ~ text tspan{fill:#FFFFFF}'}}%%
sequenceDiagram
    participant BE as Billing engine
    participant RR as Revenue Recovery
    participant PP as Payment processor

    BE->>PP: Trigger payment for the due invoice
    PP-->>BE: Success
    BE--)RR: Stream transaction
    Note over BE: Invoice is closed
```

**Scenario 2: Payment fails but the invoice is recovered within the retry criteria**

The recurring payment fails but the invoice is recovered by the billing engine's retries before the recovery start criteria are reached. The invoice is closed and does not enter the recovery cycle.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','actorBkg':'#F1F5F9','actorBorder':'#64748B','actorTextColor':'#0F172A','actorLineColor':'#9DB2D3','signalColor':'#33425E','signalTextColor':'#0B2A5B','labelBoxBkgColor':'#006DF9','labelBoxBorderColor':'#0050B3','labelTextColor':'#FFFFFF','loopTextColor':'#0B2A5B','noteBkgColor':'#EAF2FF','noteBorderColor':'#99C2FF','noteTextColor':'#0B2A5B'},'themeCSS':'rect[name=RR]{fill:#006DF9} rect[name=RR] ~ text tspan{fill:#FFFFFF}'}}%%
sequenceDiagram
    participant BE as Billing engine
    participant RR as Revenue Recovery
    participant PP as Payment processor

    BE->>PP: Trigger payment for the due invoice
    PP-->>BE: Failed
    BE--)RR: Stream transaction

    loop External retries before the recovery start criteria are reached
        BE->>PP: Retry payment
        PP-->>BE: Success or failed response
        BE--)RR: Stream transaction
    end

    Note over BE: A retry succeeds, invoice is closed
```

**Scenario 3: Payment fails and invoice is cancelled by the merchant**

The recurring payment fails and invoice is cancelled by the merchant before the recovery start criteria are reached. The invoice is closed and does not enter the recovery cycle.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','actorBkg':'#F1F5F9','actorBorder':'#64748B','actorTextColor':'#0F172A','actorLineColor':'#9DB2D3','signalColor':'#33425E','signalTextColor':'#0B2A5B','labelBoxBkgColor':'#006DF9','labelBoxBorderColor':'#0050B3','labelTextColor':'#FFFFFF','loopTextColor':'#0B2A5B','noteBkgColor':'#EAF2FF','noteBorderColor':'#99C2FF','noteTextColor':'#0B2A5B'},'themeCSS':'rect[name=RR]{fill:#006DF9} rect[name=RR] ~ text tspan{fill:#FFFFFF} rect[name=M],.actor-man rect,g[name=M] rect{fill:#F1F5F9 !important;stroke:#64748B !important} rect[name=M] ~ path,.actor-man path,g[name=M] path{fill:#64748B !important;stroke:none !important} .actor-man circle,g[name=M] circle{fill:#F1F5F9 !important;stroke:#64748B !important} .actor-man line,g[name=M] line{stroke:#64748B !important} .actor-man tspan,g[name=M] tspan{fill:#64748B !important} rect.actor-top[name=M] ~ text{display:none} .actor-top.actor-man text{display:none} line[name=M],line#actor0{transform-box:fill-box;transform-origin:center 275px;transform:scaleY(1.109)}'}}%%
sequenceDiagram
    actor M as Merchant
    participant BE as Billing engine
    participant RR as Revenue Recovery
    participant PP as Payment processor

    BE->>PP: Trigger payment for the due invoice
    PP-->>BE: Failed
    BE--)RR: Stream transaction

    loop External retries before the recovery start criteria are reached
        BE->>PP: Retry payment
        PP-->>BE: Failed
        BE--)RR: Stream transaction

        break Cancel request received from the merchant
            M->>BE: Cancel request
            Note over BE: Invoice is closed
        end
    end
```

#### When is Revenue Recovery involved?

The recurring payment fails and is not recovered before the recovery start criteria are reached. The invoice enters the recovery cycle, where it is retried until the recovery end criteria are met. The recovery cycle ends in one of the three ways described below.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','actorBkg':'#F1F5F9','actorBorder':'#64748B','actorTextColor':'#0F172A','actorLineColor':'#9DB2D3','signalColor':'#33425E','signalTextColor':'#0B2A5B','labelBoxBkgColor':'#006DF9','labelBoxBorderColor':'#0050B3','labelTextColor':'#FFFFFF','loopTextColor':'#0B2A5B','noteBkgColor':'#EAF2FF','noteBorderColor':'#99C2FF','noteTextColor':'#0B2A5B'},'themeCSS':'rect[name=RR]{fill:#006DF9} rect[name=RR] ~ text tspan{fill:#FFFFFF}'}}%%
sequenceDiagram
    participant BE as Billing engine
    participant RR as Revenue Recovery
    participant PP as Payment processor

    BE->>PP: Trigger payment for the due invoice
    PP-->>BE: Failed
    BE--)RR: Stream transaction

    loop External retries before the recovery start criteria are reached
        BE->>PP: Retry payment
        PP-->>BE: Failed
        BE--)RR: Stream transaction
    end

    Note over RR: Recovery start criteria reached, recovery starts automatically
```

**Scenario 1: Payment is recovered**

A retry succeeds before the recovery end criteria are met. The process is stopped and the invoice is closed.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','actorBkg':'#F1F5F9','actorBorder':'#64748B','actorTextColor':'#0F172A','actorLineColor':'#9DB2D3','signalColor':'#33425E','signalTextColor':'#0B2A5B','labelBoxBkgColor':'#006DF9','labelBoxBorderColor':'#0050B3','labelTextColor':'#FFFFFF','loopTextColor':'#0B2A5B','noteBkgColor':'#EAF2FF','noteBorderColor':'#99C2FF','noteTextColor':'#0B2A5B'},'themeCSS':'rect[name=RR]{fill:#006DF9} rect[name=RR] ~ text tspan{fill:#FFFFFF}'}}%%
sequenceDiagram
    participant BE as Billing engine
    participant RR as Revenue Recovery
    participant PP as Payment processor

    loop Until the payment succeeds or the recovery end criteria are met
        RR->>PP: Retry payment
        PP-->>RR: Success or failed response
        RR--)BE: Stream transaction
    end

    Note over RR: Payment recovered, retries stop
```

**Scenario 2: Merchant cancels the recovery**

A cancel request is received from the merchant before the recovery end criteria are met. The process is stopped and the invoice is closed.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','actorBkg':'#F1F5F9','actorBorder':'#64748B','actorTextColor':'#0F172A','actorLineColor':'#9DB2D3','signalColor':'#33425E','signalTextColor':'#0B2A5B','labelBoxBkgColor':'#006DF9','labelBoxBorderColor':'#0050B3','labelTextColor':'#FFFFFF','loopTextColor':'#0B2A5B','noteBkgColor':'#EAF2FF','noteBorderColor':'#99C2FF','noteTextColor':'#0B2A5B'},'themeCSS':'rect[name=RR]{fill:#006DF9} rect[name=RR] ~ text tspan{fill:#FFFFFF} rect[name=M],.actor-man rect,g[name=M] rect{fill:#F1F5F9 !important;stroke:#64748B !important} rect[name=M] ~ path,.actor-man path,g[name=M] path{fill:#64748B !important;stroke:none !important} .actor-man circle,g[name=M] circle{fill:#F1F5F9 !important;stroke:#64748B !important} .actor-man line,g[name=M] line{stroke:#64748B !important} .actor-man tspan,g[name=M] tspan{fill:#64748B !important} rect.actor-top[name=M] ~ text{display:none} .actor-top.actor-man text{display:none} line[name=M],line#actor0{transform-box:fill-box;transform-origin:center 275px;transform:scaleY(1.109)}'}}%%
sequenceDiagram
    actor M as Merchant
    participant BE as Billing engine
    participant RR as Revenue Recovery
    participant PP as Payment processor

    loop Until the recovery end criteria are met
        RR->>PP: Retry payment
        PP-->>RR: Failed
        RR--)BE: Stream transaction

        break Cancel request received from the merchant
            M->>RR: Cancel request
            Note over RR: Retries stop
        end
    end
```

**Scenario 3: Payment is not recovered**

No successful payment is received before the recovery end criteria are met. The process is stopped and the invoice is closed.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Arial, sans-serif','actorBkg':'#F1F5F9','actorBorder':'#64748B','actorTextColor':'#0F172A','actorLineColor':'#9DB2D3','signalColor':'#33425E','signalTextColor':'#0B2A5B','labelBoxBkgColor':'#006DF9','labelBoxBorderColor':'#0050B3','labelTextColor':'#FFFFFF','loopTextColor':'#0B2A5B','noteBkgColor':'#EAF2FF','noteBorderColor':'#99C2FF','noteTextColor':'#0B2A5B'},'themeCSS':'rect[name=RR]{fill:#006DF9} rect[name=RR] ~ text tspan{fill:#FFFFFF}'}}%%
sequenceDiagram
    participant BE as Billing engine
    participant RR as Revenue Recovery
    participant PP as Payment processor

    loop Until the recovery end criteria are met
        RR->>PP: Retry payment
        PP-->>RR: Failed
        RR--)BE: Stream transaction
    end

    Note over RR: Recovery end criteria met, retries stop
```

**Note:** When Start of recovery is set to 0, the invoice will be picked up for retry right after the first failed transaction.
