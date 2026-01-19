# RFC-0001: OFN Core Protocol

- **RFC ID:** 0001
- **Title:** Open Financial Network Core Protocol
- **Status:** Draft
- **Author:** Whytegod
- **Created:** 2026-01-19

---

## Summary

This RFC defines the core principles, structure, and responsibilities of the Open Financial Network (OFN).  
It establishes OFN as an open, modular, and trust-minimized financial coordination protocol.

---

## Motivation

Global financial systems are:
- Closed
- Permissioned
- Fragmented
- Biased by geography and institutions

OFN exists to create a **neutral financial coordination layer** that anyone can build on, verify, and participate in.

---

## Core Principles

1. **Openness**  
   OFN specifications are public and auditable.

2. **Modularity**  
   Components can evolve independently without breaking the network.

3. **Neutrality**  
   No geographic, political, or institutional bias.

4. **Security First**  
   Threat modeling and verification are mandatory, not optional.

5. **Interoperability**  
   OFN integrates with existing financial and blockchain systems.

---

## Protocol Scope

The OFN Core Protocol governs:
- Identity abstraction
- Transaction validation logic
- Network governance standards
- Security assumptions

It does NOT define:
- UI/UX
- Wallet design
- Business models

---

## Governance

- Changes to the core protocol require an RFC
- RFCs are discussed publicly
- Final acceptance is based on security, clarity, and alignment with OFN principles

---

## Backward Compatibility

Breaking changes MUST:
- Be clearly labeled
- Include migration paths
- Pass a security review

---

## Security Considerations

All protocol changes must reference:
- Threat vectors
- Attack surfaces
- Mitigation strategies

See `THREAT-MODEL.md`.

---

## Future Work

- Identity layer RFC
- Transaction routing RFC
- Compliance abstraction RFC

---

## Conclusion

This RFC establishes the foundation of the Open Financial Network.  
All future components MUST align with this core protocol.
