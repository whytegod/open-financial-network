"""
OFN Core Definition

This file defines the immutable core identity
of the Open Financial Network (OFN).

No execution logic.
No networking.
No state mutation.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class OFNProtocol:
    name: str = "Open Financial Network"
    symbol: str = "OFN"
    version: str = "0.1.x"

    principles: Tuple[str, ...] = (
        "Open by default",
        "Infrastructure-first design",
        "Security over speed",
        "Explicit governance",
        "Transparency at all layers",
    )

    guarantees: Tuple[str, ...] = (
        "Deterministic protocol behavior",
        "Auditable design",
        "No hidden monetary policy",
        "Backward compatibility unless RFC-approved",
    )

    non_goals: Tuple[str, ...] = (
        "Speculation-first incentives",
        "Centralized control",
        "Undocumented changes",
        "Implicit governance",
    )


OFN = OFNProtocol()
