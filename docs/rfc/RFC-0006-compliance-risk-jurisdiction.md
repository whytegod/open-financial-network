# RFC-0006: Compliance, Risk & Jurisdiction Layer

- **RFC ID:** 0006
- **Title:** Compliance, Risk, and Jurisdiction Abstraction
- **Status:** Draft
- **Author:** Whytegod
- **Created:** 2026-01-19

---

## Summary

This RFC defines how regulatory compliance, risk controls, and jurisdictional constraints are handled within the Open Financial Network (OFN) without compromising protocol neutrality.

---

## Design Philosophy

OFN remains:
- Permissionless at the core
- Neutral by default
- Adaptable at the edges

Compliance is **layered**, not enforced globally.

---

## Compliance Abstraction

Compliance logic MAY be implemented via:
- Optional modules
- Asset-level constraints
- Identity-attached credentials
- Transaction-level rules

The core protocol does not mandate compliance behavior.

---

## Jurisdiction Mapping

Jurisdictional rules MAY define:
- Geographic constraints
- Asset eligibility
- Transaction limits
- Reporting requirements

Jurisdictions are represented as **policy sets**, not hardcoded logic.

---

## Risk Management

Risk controls MAY include:
- Transaction caps
- Velocity limits
- Exposure thresholds
- Circuit breakers

Risk logic is configurable and auditable.

---

## Selective Disclosure

Participants MAY:
- Prove compliance without revealing identity
- Use zero-knowledge or attestations
- Reveal information only when required

Privacy is preserved wherever possible.

---

## Institutional Participation

Institutions MAY:
- Attach compliance modules
- Operate within constrained environments
- Interact with permissionless participants via bridges

Institutional rules do not affect global users.

---

## Enforcement Boundaries

OFN does NOT:
- Enforce global KYC
- Police participants
- Act as a regulator

Responsibility lies with integrators and issuers.

---

## Security Considerations

- Policy bypass risks
- Credential forgery
- Misconfiguration

Mitigations MUST be documented per implementation.

---

## Future Work

- Reporting standards RFC
- Audit interface RFC
- Regulator node RFC (optional)

---

## Conclusion

This RFC enables OFN to operate across jurisdictions and regulatory environments while preserving openness, neutrality, and user choice.
