<!--
---
title: Best Practices
description: Apply testing best practices to write maintainable, reliable connector validation scenarios
last_updated: 2026-03-12
generated_from: backend/ucs-connector-tests/
auto_generated: false
reviewed_by: engineering
reviewed_at: 2026-03-12
approved: true
---
-->

# Best Practices

## Overview

Following these best practices ensures your tests are maintainable, reliable, and effective at catching issues.

## Writing Test Scenarios

### Use Auto-Generate for Dynamic Values

Always use `auto_generate` for values that should be unique per test run:

**Good**:
```json
{
  "merchant_transaction_id": {"id": "auto_generate"},
  "customer": {
    "name": "auto_generate",
    "email": {"value": "auto_generate"},
    "id": "auto_generate"
  }
}
```

### Never Commit Credentials

Keep credentials in environment variables or secret stores:

**Good**:
```bash
export CONNECTOR_AUTH_FILE_PATH=~/.ucs-creds.json
# File is in .gitignore
```

**Avoid**:
```bash
# Do not do this
creds.json  # Committed to git
```

### Use Test Environments

Always test against sandbox/test endpoints:

```json
{
  "stripe": {
    "connector_account_details": {
      "api_key": "sk_test_..."
    }
  }
}
```

### Rotate Regularly

Update API keys periodically:

- Set calendar reminders
- Use short-lived tokens where possible
- Audit key usage regularly
- Revoke unused keys

## Test Organization

### Group Related Scenarios

Keep similar scenarios together:

```json
{
  "no3ds_auto_capture_credit_card": { },
  "no3ds_auto_capture_debit_card": { },
  "no3ds_manual_capture_credit_card": { },
  "no3ds_declined_card": { }
}
```

### Separate Happy Path and Edge Cases

Mark primary scenarios as default:

```json
{
  "no3ds_auto_capture_credit_card": {
    "is_default": true
  },
  "no3ds_declined_card": {
    "is_default": false
  }
}
```

### Document Connector Limitations

Use connector specs to document supported features:

```json
{
  "connector": "mynewconnector",
  "supported_suites": [
    "authorize",
    "capture",
    "void"
  ]
}
```

## Debugging

### Enable Debug Mode

When tests fail, enable debug output:

```bash
export UCS_DEBUG_EFFECTIVE_REQ=1
cargo run --bin run_test -- --connector stripe --suite authorize
```

### Print grpcurl Command

Test the exact request manually:

```bash
cargo run --bin run_test ... --print-grpcurl
# Copy and modify the grpcurl command
```

### Check Test Reports

Always check the generated report:

```bash
cat backend/ucs-connector-tests/test_report.md
```

### Isolate Failures

Run a single scenario to isolate issues:

```bash
cargo run --bin run_test \
  --connector stripe \
  --suite authorize \
  --scenario failing_scenario
```

## Performance

### Minimize Dependencies

Only depend on what you actually need:

**Good**:
```json
{
  "suite": "get",
  "depends_on": ["authorize"]
}
```

**Avoid**:
```json
{
  "suite": "get",
  "depends_on": ["create_access_token", "create_customer", "authorize"]
}
```

**Why**: Get only needs the transaction ID from authorize.

### Use Efficient Assertions

Prefer simple assertions over complex ones:

**Good**:
```json
{
  "status": {"one_of": ["CHARGED", "AUTHORIZED"]}
}
```

**Avoid**:
```json
{
  "status": {"equals": "CHARGED"},
  "alternative_status": {"equals": "AUTHORIZED"},
  "tertiary_status": {"equals": "PENDING"}
}
```

## Review Checklist

Before submitting new tests:

- [ ] Uses `auto_generate` for dynamic values
- [ ] Has one `is_default: true` scenario
- [ ] Assertions are focused and minimal
- [ ] Uses realistic test card numbers
- [ ] Follows naming conventions
- [ ] Dependencies are correct
- [ ] Credentials are not committed
- [ ] Test runs locally
- [ ] Report is generated correctly

## Next Steps

- [Configuration](./configuration.md) - Environment and credentials setup
- [Usage](./usage.md) - Running tests
- [CI/CD Integration](./ci-cd.md) - Continuous integration
