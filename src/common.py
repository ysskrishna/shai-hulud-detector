from dataclasses import dataclass, field
from typing import List, Optional
from enum import StrEnum

class ScanStatus(StrEnum):
    OKAY = "OKAY"
    FLAG = "FLAG"
    ERROR = "ERROR"

@dataclass
class SuspiciousRepo:
    name: str
    html_url: str
    reason: str
    file_path: Optional[str] = None

@dataclass
class ScanStats:
    search_description_hits: int = 0
    suspicious_files_found: int = 0

@dataclass
class ScanResult:
    username: str
    status: ScanStatus = field(default=ScanStatus.OKAY)
    suspicious_repos: List[SuspiciousRepo] = field(default_factory=list)
    stats: ScanStats = field(default_factory=ScanStats)
    error: Optional[str] = None