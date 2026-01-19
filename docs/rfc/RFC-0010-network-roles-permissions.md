# RFC-0010: Network Roles, Permissions & Accountability

- RFC ID: 0010
- Status: Draft
- Author: OFN Core Contributors
- Created: 2026-01-19

---

## 1. Overview

This RFC defines the formal roles, permissions, and accountability mechanisms within the Open Financial Network (OFN).

It establishes clear authority boundaries to prevent abuse, ambiguity, and centralized capture.

---

## 2. Design Principles

Role and permission design in OFN follows these principles:

- **Least Privilege**  
  Participants receive only the permissions required for their role.

- **Separation of Duties**  
  No single role should control issuance, validation, and governance simultaneously.

- **Explicit Accountability**  
  All privileged actions must be attributable to an identifiable role.

- **Revocability**  
  Permissions must be revocable through defined governance or protocol processes.

---

## 3. Role Definitions

### 3.1 Network Participants
General users and institutions interacting with OFN.

Permissions:
- Submit transactions
- Hold and transfer assets
- Interact with OFN-compatible services

Restrictions:
- No protocol modification authority

---

### 3.2 Validator / Operator Nodes
Entities responsible for transaction validation and network availability.

Permissions:
- Validate and order transactions
- Maintain protocol state
- Execute governance-approved upgrades

Restrictions:
- Cannot unilaterally modify protocol rules
- Subject to performance and security requirements

---

### 3.3 Asset Issuers
Entities authorized to issue and manage assets.

Permissions:
- Create and manage assets
- Define asset-specific rules

Restrictions:
- Bound by issuance and compliance constraints
- No control over core protocol behavior

---

### 3.4 Gateway Operators
Entities operating external integration gateways.

Permissions:
- Translate external events into OFN messages
- Apply integration-specific compliance checks

Restrictions:
- No authority over internal state transitions
- Subject to audit and revocation

---

### 3.5 Governance Actors
Participants involved in protocol decision-making.

Permissions:
- Propose RFCs
- Participate in review and approval processes
- Adjust protocol parameters within scope

Restrictions:
- Governance power limited by defined voting and approval mechanisms

---

## 4. Permission Enforcement

Permissions are enforced through:
- Protocol-level validation rules
- Cryptographic authorization
- Governance-approved role assignments

Implicit permissions are not allowed.

---

## 5. Accountability Mechanisms

Accountability MAY include:
- Action logging
- Public audit trails
- Performance monitoring
- Sanctions or removal

All privileged actions MUST be attributable.

---

## 6. Abuse & Misconduct

Abuse MAY include:
- Exceeding authorized permissions
- Protocol manipulation
- Security negligence
- Regulatory misrepresentation

Abuse responses MAY include:
- Permission revocation
- Economic penalties
- Governance intervention

---

## 7. Governance Interaction

Role definitions and permissions MAY be updated only through RFC-defined governance processes (RFC-0005).

Emergency actions are exceptional and time-limited.

---

## 8. Limitations

OFN does not guarantee:
- Perfect enforcement in all environments
- Immunity from coordinated abuse
- Elimination of human error

Participants assume responsibility for their actions.

---

## 9. Conclusion

This RFC establishes a disciplined authority and accountability framework that protects OFN from centralized control, ambiguity, and misuse.
