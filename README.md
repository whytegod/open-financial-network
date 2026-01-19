## Project Structure

This repository is organized into clear layers to preserve the neutrality
and long-term integrity of the OFN protocol.

- Core concepts and principles are defined in documentation.
- Reference materials explain how OFN may be implemented.
- Source code represents experimental or optional implementations
  and does not redefine the OFN Core.
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



# Open Financial Network (OFN)

Open Financial Network (OFN) is an open, modular financial protocol focused on
access, interoperability, and security-first design.

This repository contains the **core documentation, design decisions, and RFCs**
that define the network before full implementation.

---

## 📄 Documentation

All core documents are located in the `docs/` directory.

### Core Papers
- **Whitepaper**: `docs/rfc/WHITEPAPER.md`  
  High-level vision, purpose, and economic intent.

- **Techpaper**: `docs/rfc/TECHPAPER.md`  
  Technical architecture and system design.

- **Threat Model**: `docs/rfc/THREAT-MODEL.md`  
  Security assumptions, risks, and mitigations.

---

## 📘 RFCs (Request for Comments)

RFCs describe proposed standards and decisions for the network.

Located in: `docs/rfc/`

- **RFC-0001** – Initial Architecture & Principles  
- **RFC-0002** – Network Roles & Responsibilities  

RFCs are immutable once accepted.

---

## 🧱 Project Status

- Documentation-first ✅  
- Architecture defined ✅  
- Security model defined ✅  
- Reference implementation: **pending**

This project intentionally freezes design before scaling or deployment.

---

## ⚖️ License

This project is released under the included `LICENSE` file.

---

## 🤝 Contributing

At this stage, contributions are limited to:
- RFC discussion
- Documentation review
- Security feedback

Implementation contributions will open later.

---

## 📌 Disclaimer

This repository does **not** contain production-ready financial software.
It is a design and research project.
