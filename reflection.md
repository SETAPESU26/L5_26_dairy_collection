# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing it. It helps identify code quality issues, possible security vulnerabilities, and style violations before the program is delivered.

## 2. What did Pylint, Bandit, and Flake8 identify?

Pylint identified missing docstrings, naming convention problems, long lines, and other code-quality issues. Bandit identified a SQL injection risk, weak MD5 hashing, and shell execution. Flake8 identified an unused import, long lines, an ambiguous variable name, and an incorrect comparison with None.

## 3. What changes were made to improve the program?

I used parameterized SQL queries, replaced MD5 with SHA-256, removed shell execution, improved function names and documentation, corrected formatting issues, and handled an empty collection safely. I then reran the analysis tools to verify the changes.

## 4. How does static analysis help software development?

Static analysis helps find problems early, improves readability and maintainability, and reduces the risk of security vulnerabilities. Using multiple tools is useful because each tool checks different aspects of the source code.
