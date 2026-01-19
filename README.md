## Scope and Non-Goals

### In Scope
- Core financial infrastructure
- Peer-to-peer value transfer
- Protocol-level design
- Open participation and validation
- Long-term sustainability

### Out of Scope (For Now)
- Marketing campaigns
- Social media hype
- Influencer promotion
- Speculative token behavior
- Short-term profit narratives

OFN is designed as foundational financial infrastructure, not a consumer-facing or hype-driven product.
# Open Financial Network (OFN)

Open Financial Network (OFN) is an open, neutral financial protocol designed to support
digital value exchange without centralized control.

This repository contains the core documentation and specifications for OFN.

---

## Purpose

OFN exists to:
- Enable open financial infrastructure
- Reduce dependency on centralized intermediaries
- Support transparent, verifiable transactions
- Remain neutral, open, and extensible

---

## Repository Structure




/docs ├── WHITEPAPER.md   # Vision, goals, economics ├── TECHPAPER.md    # Technical architecture README.md             # Project overview LICENSE               # Open-source license



---

## Current Status

- Documentation phase
- No production code yet
- Open for review and discussion

---

## Principles

- Open by default
- Security-first design
- Minimal assumptions
- Long-term sustainability

---

## Roadmap (High-Level)

1. Specification freeze
2. Peer review
3. Reference implementation
4. Test network
5. Main network

---

## License

This project is released under the terms of the included LICENSE file.

## Threat Model (High-Level)

The OFN protocol assumes a partially adversarial environment.

### Considered Threats
- Malicious peers attempting double-spend or replay attacks
- Sybil attacks through fake node identities
- Network partition or temporary censorship
- Data integrity corruption

### Non-Goals in Threat Handling
- State-level adversaries
- Physical attacks on infrastructure
- Guaranteed anonymity at all layers

The protocol prioritizes resilience, graceful degradation, and recoverability over absolute guarantees.
