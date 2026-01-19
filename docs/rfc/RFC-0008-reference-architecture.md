# RFC-0008: Reference Architecture & Node Types

- **RFC ID:** 0008
- **Title:** Reference Architecture and Node Classification
- **Status:** Draft
- **Author:** Whytegod
- **Created:** 2026-01-19

---

## Summary

This RFC defines the reference architecture of the Open Financial Network (OFN) and categorizes the node types that participate in the network.

---

## Architectural Overview

OFN is a modular, layered financial protocol composed of interoperable components rather than a monolithic system.

Core layers include:
- Networking layer
- Identity layer
- Transaction execution layer
- Asset registry layer
- Governance layer
- Compliance interface layer

Each layer MAY be implemented independently.

---

## Node Types

### Validator Nodes
- Maintain protocol state
- Validate transactions
- Enforce consensus rules
- Participate in governance execution

Validator nodes MUST meet minimum performance and security requirements.

---

### Gateway Nodes
- Interface with external systems
- Handle API access
- Translate off-chain events to on-chain messages

Gateway nodes SHOULD be rate-limited and auditable.

---

### Observer Nodes
- Read-only access
- State indexing
- Analytics and monitoring

Observer nodes do not participate in consensus.

---

### Issuer Nodes
- Authorized to create assets
- Maintain issuance policies
- Subject to compliance constraints

Issuer nodes MAY also act as gateway nodes.

---

### Client Nodes
- End-user wallets
- Application clients
- Smart device integrations

Client nodes do not hold global state.

---

## Communication Model

Nodes communicate via:
- Signed messages
- Deterministic serialization
- Versioned protocol schemas

All messages MUST be verifiable.

---

## Deployment Models

OFN supports:
- Public networks
- Consortium networks
- Private deployments
- Hybrid configurations

---

## Scalability Considerations

Architecture supports:
- Horizontal scaling
- Sharded execution
- Layered settlement
- Off-chain computation

---

## Upgrade Strategy

Protocol upgrades MUST:
- Be backward-aware
- Use version negotiation
- Avoid silent breaking changes

---

## Security Considerations

Each node type has:
- Defined trust assumptions
- Explicit permissions
- Limited authority scope

---

## Conclusion

This reference architecture provides a flexible yet disciplined framework for implementing OFN across diverse environments.
