---
hidden: true
---

# Services

### Data Management

#### Data Ingestion Service

Our ingestion service connects to merchant and processor data sources using secure, flexible channels so you get timely, reliable inputs without manual work

**Supported connection types**

* **Direct processor integrations (API / webhooks)**
  * Real-time ingestion via processor APIs or webhook events.
  * Eliminates polling and manual downloads for low-latency, continuous reconciliation
* **SFTP / Scheduled file pulls**
  * Secure SFTP connectors that poll data on a configurable schedule
  * Supports directory monitoring and incremental retrieval to avoid duplicate processing
* **Manual file uploads / UI drag-and-drop**
  * Upload files through the dashboard for ad-hoc imports or backfills

#### Data Transformation Service

The transformation service is the intelligent data processing engine that bridges the gap between diverse payment processor formats and your reconciliation requirements. It automatically converts raw financial data from any source into a standardized, reconciliation-ready format.

The transformation service handles virtually any data format your payment processors provide. Structured Data Formats:

* CSV Files: Delimiter-separated values with configurable column mappings
* JSON: Nested data structures with complex field extraction
* Fixed-Width: Legacy formats like COBOL with position-based field extraction

**Flexible Configuration**

* Custom transformation rules per connection
* Support for multiple file formats from the same source
* Configurable field mappings and business logic
* Version control for transformation configurations

**Error Management**

* Detailed error categorization and resolution guidance
* Automatic alerts for systematic data issues

<figure><img src="../../../.gitbook/assets/image (1) (2).png" alt=""><figcaption></figcaption></figure>
