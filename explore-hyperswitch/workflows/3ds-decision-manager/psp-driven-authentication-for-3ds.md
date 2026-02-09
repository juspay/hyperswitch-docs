---
icon: rotate-exclamation
---

# PSP driven Authentication for 3DS

The simplest form on invoking a 3DS is via the PSP through which the transaction is being processed. This tries the transaction to that PSP and any retry of transaction would need to re-invoke the 3DS

#### Invoking 3DS via payments through the underlying PSP

```javascript
// Set authentication type in the Payments call
 "authentication_type": "three_ds"
```

Note - Certain PSPs do not support 3DS and require the merchant to perform authentication independently before sedning the transction&#x20;

