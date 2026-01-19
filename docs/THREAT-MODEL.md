# Open Financial Network (OFN) – Threat Model

## Purpose

This document outlines the high-level threat assumptions and security boundaries of the Open Financial Network (OFN).

It is not an exhaustive security audit.  
It exists to clarify what the protocol defends against and what it explicitly does not.

---

## Threat Assumptions

OFN assumes an open and adversarial network environment.

- Any node may behave maliciously
- Network traffic may be observed or delayed
- Peers cannot be trusted by default
- Messages may be replayed or reordered

---

## Considered Threats

### Network-Level Threats
- Sybil attacks using fake identities
- Eclipse attacks isolating nodes
- Message flooding and denial-of-service
- Network partitioning

### State-Level Threats
- Double-spend attempts
- Invalid state transitions
- Transaction replay attacks
- State divergence between peers

---

## Mitigation Principles

OFN mitigates threats through:
- Deterministic validation rules
- Cryptographic signatures
- Peer diversity
- Rate limiting
- Conservative protocol defaults

Security favors correctness and recoverability over speed.

---

## Explicit Non-Goals

OFN does NOT attempt to defend against:
- State-level adversaries
- Physical attacks on infrastructure
- Guaranteed anonymity
- Social engineering attacks

These risks are considered outside protocol scope.

---

## Security Philosophy

OFN assumes no single component is trusted.

Security emerges from:
- Verifiability
- Transparency
- Redundancy
- Simplicity