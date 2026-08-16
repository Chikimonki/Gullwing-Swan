# Gullwing-Swan — COBOL Modernisation to Python

The Swan glides above modern systems while paddling beneath the legacy COBOL code. YouTube Video Evidence: https://youtu.be/91wFxuTLjvM

## What It Does

Parses COBOL source code and extracts business logic for modernisation.

| Division | Purpose |
|----------|---------|
| IDENTIFICATION | Program metadata |
| DATA | Working storage, linkage, file sections |
| PROCEDURE | Business rules (IF/COMPUTE/MOVE) |
| ENVIRONMENT | System dependencies |

## Features

- **COBOL Parser** — Structured extraction of all divisions
- **Business Rule Extraction** — IF/COMPUTE/MOVE → hot-swappable rules
- **Python Translation** — Automated translation of business logic
- **DORA Compliance** — Audit trail for COBOL-dependent banks

## Quick Start

```python
from src.cobol_parser import COBOLParser

parser = COBOLParser()
divisions = parser.parse(cobol_source)
rules = parser.extract_business_rules()
python_code = parser.translate_to_python()
The Problem
220 billion lines of COBOL run global banking. 60% of COBOL programmers retire in 5 years. Nobody teaches it.

The Solution
Gullwing-Swan glides across the legacy surface, extracting the business logic that matters — ready for translation to modern languages.

License
MIT
