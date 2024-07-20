from dataclasses import dataclass
from typing import List, Optional


@dataclass
class UnittestGeneratorConfig:
    model: str
    api_base: str
    test_command: str
    code_coverage_report_path: Optional[str]
    mutation_coverage_report_path: Optional[str]
    coverage_type: str
    source_file_path: str
    test_file_path: str
    target_line_coverage_rate: float
