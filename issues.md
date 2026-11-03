# Lab 5: Static Code Analysis — Issue Report

File analyzed: dairy_collection.py

| Issue | Tool | Original Line | Description | Fix Applied |
|---|---|---:|---|---|
| SQL injection risk (B608) | Bandit | 11 | SQL values were inserted using string formatting. | Replaced string construction with parameterized SQL. |
| Weak MD5 hash (B324) | Bandit | 16 | MD5 is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256 for the farmer digest. |
| Shell execution (B605) | Bandit | 31 | os.system() executed a shell command using input text. | Removed shell execution and printed the slip message directly. |
| Unused import (F401) | Flake8 | 2 | The json module was imported but never used. | Removed the unused import. |
| Long lines (E501) | Flake8 | 7, 11, 20, 25 | Several lines exceeded the configured limit. | Wrapped long statements and queries. |
| Ambiguous variable (E741) | Flake8 | 26 | The variable name l was difficult to distinguish. | Used a descriptive variable name. |
| None comparison (E711) | Flake8 | 36 | Compared fat with None using ==. | Changed the condition to fat is None. |
| Missing documentation (C0114/C0116) | Pylint | Multiple | Module and functions lacked docstrings. | Added module and function docstrings. |
| Naming convention (C0103) | Pylint | Multiple | Function names used camelCase. | Changed names to snake_case. |
| Redefined outer name (W0621) | Pylint | Multiple | Function parameters reused the outer connection name. | Used explicit connection parameters and a local connection in main(). |
| String formatting (C0209) | Pylint | Multiple | Some formatting could use modern alternatives. | Used f-strings where appropriate. |

## Verification

- Original Pylint score: 2.00/10
- Final Pylint score: 10.00/10
- Original Bandit findings: 3 (2 High, 1 Medium)
- Final Bandit findings: 0
- Final Flake8 report: empty, indicating no reported violations.
- Functional check: the demonstration still reports a total of 32.5 litres.
