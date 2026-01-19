# RFC-0002: OFN Identity & Account Abstraction Layer

- **RFC ID:** 0002
- **Title:** Identity and Account Abstraction Layer
- **Status:** Draft
- **Author:** Whytegod
- **Created:** 2026-01-19

---

## Summary

This RFC defines the Identity and Account Abstraction Layer of the Open Financial Network (OFN).  
It enables users, entities, and systems to interact with OFN without relying on traditional bank accounts or centralized identity providers.

---

## Motivation

Current financial identity systems are:
- Fragmented
- Region-locked
- Surveillance-heavy
- Institution-controlled

OFN requires a **neutral identity layer** that:
- Preserves privacy
- Supports compliance where required
- Works across jurisdictions

---

## Design Goals

1. **Pseudonymity by Default**  
   Users interact using abstract identities, not real-world identifiers.

2. **Composable Identity**  
   Identity components (keys, credentials, permissions) are modular.

3. **Account Abstraction**  
   Accounts are logic-based, not key-based.

4. **Jurisdiction Flexibility**  
   Compliance rules can be layered without altering the core protocol.

---

## Identity Model

An OFN Identity consists of:
- A root identifier
- One or more cryptographic keys
- Optional credential attestations
- Permission scopes

Identities MAY represent:
- Individuals
- Organizations
- Smart contracts
- Devices

---

## Account Abstraction

Accounts are programmable entities that:
- Validate transactions
- Enforce rules and limits
- Support recovery mechanisms

Key loss does NOT equal identity loss.

---

## Compliance Layer (Optional)

Compliance modules MAY:
- Attach credentials
- Enforce transaction constraints
- Provide selective disclosure

Core OFN remains neutral and permissionless.

---

## Security Considerations

- Key rotation
- Identity recovery
- Sybil resistance
- Credential forgery

All implementations MUST document mitigations.

---

## Backward Compatibility

Identity upgrades MUST:
- Preserve existing identifiers
- Allow opt-in migration paths

---

## Future Work

- Credential standards RFC
- Identity recovery RFC
- Cross-chain identity mapping

---

## Conclusion

This RFC establishes identity as a flexible, privacy-preserving foundation for OFN without sacrificing interoperability or compliance.
