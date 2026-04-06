---
description: Review complete connector flow coverage across 100+ payment processors with detailed payment method support matrices for authorize, capture, refund, and dispute operations
---

# Connector Flow Coverage

<!--
This file is auto-generated. Do not edit by hand.
Source: data/field_probe/
Regenerate: python3 scripts/generators/docs/generate.py --all-connectors-doc
-->

This document provides a comprehensive overview of payment method support
across all connectors for each payment flow. Flow names follow the gRPC
service definitions from `crates/types-traits/grpc-api-types/proto/services.proto`.

## Flow Coverage

Flow names follow the gRPC service definitions. Each flow is prefixed with
its service name (e.g., `PaymentService.Authorize`, `RefundService.Get`).

### PaymentService.Authorize

Authorize a payment amount on a payment method. This reserves funds without capturing them, essential for verifying availability before finalizing.

**Legend:** ✓ Supported | x Not Supported | ⚠ Not Implemented | ? Error / Missing required fields

| Connector | CARD / Card | CARD / Bancontact | WALLET / Apple Pay | WALLET / Apple Pay Dec | WALLET / Apple Pay SDK | WALLET / Google Pay | WALLET / Google Pay Dec | WALLET / Google Pay SDK | WALLET / PayPal SDK | WALLET / Amazon Pay | WALLET / Cash App | WALLET / PayPal | WALLET / WeChat Pay | WALLET / Alipay | WALLET / Revolut Pay | WALLET / MiFinity | WALLET / Bluecode | WALLET / Paze | WALLET / Samsung Pay | WALLET / MB Way | WALLET / Satispay | WALLET / Wero | BNPL / Affirm | BNPL / Afterpay | BNPL / Klarna | UPI / UPI Collect | UPI / UPI Intent | UPI / UPI QR | Online Banking / Thailand | Online Banking / Czech | Online Banking / Finland | Online Banking / FPX | Online Banking / Poland | Online Banking / Slovakia | Open Banking / UK | Open Banking / PIS | Open Banking / Generic | Bank Redirect / Local | Bank Redirect / iDEAL | Bank Redirect / Sofort | Bank Redirect / Trustly | Bank Redirect / Giropay | Bank Redirect / EPS | Bank Redirect / Przelewy24 | Bank Redirect / PSE | Bank Redirect / BLIK | Bank Redirect / Interac | Bank Redirect / Bizum | Bank Redirect / EFT | Bank Redirect / DuitNow | Bank Transfer / ACH | Bank Transfer / SEPA | Bank Transfer / BACS | Bank Transfer / Multibanco | Bank Transfer / Instant | Bank Transfer / Instant FI | Bank Transfer / Instant PL | Bank Transfer / Pix | Bank Transfer / Permata | Bank Transfer / BCA | Bank Transfer / BNI VA | Bank Transfer / BRI VA | Bank Transfer / CIMB VA | Bank Transfer / Danamon VA | Bank Transfer / Mandiri VA | Bank Transfer / Local | Bank Transfer / Indonesian | Bank Debit / ACH | Bank Debit / SEPA | Bank Debit / BACS | Bank Debit / BECS | Bank Debit / SEPA Guaranteed | Alternate PMs  / Crypto | Alternate PMs  / Reward | Alternate PMs  / Givex | Alternate PMs  / PaySafeCard | Alternate PMs  / E-Voucher | Alternate PMs  / Boleto | Alternate PMs  / Efecty | Alternate PMs  / Pago Efectivo | Alternate PMs  / Red Compra | Alternate PMs  / Red Pagos | Alternate PMs  / Alfamart | Alternate PMs  / Indomaret...