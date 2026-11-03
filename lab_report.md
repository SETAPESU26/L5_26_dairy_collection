# Lab 5: Static Code Analysis
## Dairy Milk Collection Ledger

### Objective
Improve the quality, security, and style of the assigned Python program using Pylint, Bandit, and Flake8.

### Work completed
- Preserved the original source as dairy_collection_before.py.
- Generated BEFORE and AFTER reports for all three tools.
- Replaced unsafe SQL string construction with parameterized queries.
- Removed shell command execution.
- Replaced MD5 with SHA-256.
- Improved naming, documentation, and formatting.
- Checked that the program continued to run.

### Results

| Check | Before | After |
|---|---|---|
| Pylint | 2.00/10 | 10.00/10 |
| Bandit | 3 findings | 0 findings |
| Flake8 | 7 reported violations | 0 reported violations |

### Functional verification
The demonstration returned a total of 32.5 litres and identified Lata as the top supplier in the sample data.

### Conclusion
The static analysis tools helped identify security risks, style violations, and code-quality problems. After the changes, the program ran successfully and the final reports met the target results.

### Evidence
Screenshots of the original run, BEFORE reports, AFTER reports, and Git commit history should be included in the screenshots folder.
