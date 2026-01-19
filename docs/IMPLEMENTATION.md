# Open Financial Network (OFN)
## Implementation Guide (Non-Normative)

### Status
This document is **informational and non-normative**.

It does **not** define protocol rules, governance authority, economic guarantees, or compliance obligations.

The authoritative documents for OFN are:
- Whitepaper
- Techpaper
- RFCs
- Governance Framework
- Threat Model

This guide exists solely to assist implementers in building compatible systems.

---

## 1. Purpose

The Open Financial Network (OFN) is designed as a **protocol framework**, not a single reference implementation.

This document provides:
- Guidance for building OFN-compatible systems
- Clarification of expected behaviors
- Examples of implementation boundaries

This document **does not override or amend** any RFC or specification.

---

## 2. Design Principles for Implementers

Implementations SHOULD adhere to the following principles:

### 2.1 Protocol Fidelity
- Implementations MUST follow RFC specifications exactly
- Undefined behavior MUST NOT be assumed
- Extensions MUST be proposed via the RFC process

### 2.2 Modularity
- Components SHOULD be loosely coupled
- Identity, transaction processing, asset issuance, and governance logic SHOULD be separable
- No component SHOULD assume privileged access

### 2.3 Determinism
- State transitions MUST be deterministic
- Identical inputs MUST produce identical outputs
- External dependencies MUST NOT affect protocol logic

---

## 3. Reference Architecture (Conceptual)

An OFN-compatible system typically consists of:

- **Identity Layer**
  - Verifiable identity primitives
  - Credential validation
  - Revocation handling

- **Transaction Layer**
  - Transaction validation
  - Fee calculation
  - Settlement ordering

- **Asset Layer**
  - Asset definitions
  - Issuance and redemption logic
  - Supply constraints

- **Governance Interface**
  - RFC awareness
  - Version signaling
  - Upgrade compatibility

Implementers MAY combine or separate components as needed, provided protocol behavior remains intact.

---

## 4. Minimal Viable Implementation (MVI)

A minimal implementation MAY include:
- Static identity verification
- Single-asset transaction processing
- Deterministic fee model
- Manual governance updates

This is sufficient for:
- Testing
- Auditing
- Third-party review
- Academic or institutional evaluation

---

## 5. Versioning and Compatibility

- Implementations MUST clearly signal supported RFC versions
- Backward-incompatible changes REQUIRE governance approval
- Experimental features MUST be isolated and disabled by default

---

## 6. Security Considerations

Implementers are responsible for:
- Secure key management
- Defense against replay attacks
- Validation of all external inputs

Refer to `THREAT-MODEL.md` for detailed risk assumptions.

---

## 7. Compliance Considerations

OFN is protocol-level infrastructure.

Compliance obligations:
- Are jurisdiction-specific
- Exist at the implementation layer
- Are outside the scope of the protocol itself

Implementers MUST ensure compliance with applicable laws.

---

## 8. Governance Interaction

Implementations:
- MUST respect governance decisions
- MUST not bypass RFC processes
- MUST support orderly upgrades

Governance authority is defined exclusively in `GOVERNANCE.md`.

---

## 9. Non-Goals

This document intentionally does NOT define:
- Token economics
- Business models
- Deployment timelines
- Validator incentives
- Regulatory classifications

---

## 10. Final Note

OFN is designed to be:
- Stable
- Auditable
- Institution-grade

Implementers are encouraged to prioritize correctness over speed.
