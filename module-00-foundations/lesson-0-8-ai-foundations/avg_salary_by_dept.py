"""
Average Salary by Department
-----------------------------
Calculates the average salary per department from a list of employee records.
Mirrors what you'd write in SQL as:
    SELECT department, AVG(salary) FROM employees GROUP BY department;
"""

employees = [
    {"name": "Alice",   "department": "Engineering", "salary": 95000},
    {"name": "Bob",     "department": "Engineering", "salary": 105000},
    {"name": "Carol",   "department": "Marketing",   "salary": 72000},
    {"name": "David",   "department": "Marketing",   "salary": 68000},
    {"name": "Eva",     "department": "HR",          "salary": 61000},
    {"name": "Frank",   "department": "HR",          "salary": 65000},
    {"name": "Grace",   "department": "Engineering", "salary": 112000},
    {"name": "Hank",    "department": "Marketing",   "salary": 75000},
]

# --- Step 1: Group salaries by department ---
dept_salaries = {}

for emp in employees:
    dept = emp["department"]
    salary = emp["salary"]

    if dept not in dept_salaries:
        dept_salaries[dept] = []          # start a new list for this department
    dept_salaries[dept].append(salary)   # add this employee's salary to the list

# --- Step 2: Calculate the average for each department ---
print(f"{'Department':<15} {'Avg Salary':>12} {'# Employees':>13}")
print("-" * 42)

for dept, salaries in sorted(dept_salaries.items()):
    avg = sum(salaries) / len(salaries)
    print(f"{dept:<15} ${avg:>11,.2f} {len(salaries):>13}")
