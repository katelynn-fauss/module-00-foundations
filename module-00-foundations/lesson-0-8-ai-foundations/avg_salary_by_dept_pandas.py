import pandas as pd

# Sample data — replace with your actual DataFrame source
employees = pd.DataFrame({
    "name":       ["Alice", "Bob", "Carol", "David", "Eva", "Frank", "Grace", "Hank"],
    "department": ["Engineering", "Engineering", "Marketing", "Marketing", "HR", "HR", "Engineering", "Marketing"],
    "salary":     [95000, 105000, 72000, 68000, 61000, 65000, 112000, 75000],
})

avg_salary_by_dept = (
    employees
    .groupby("department", sort=False)          # group rows by department; sort=False defers ordering to us
    .agg(
        avg_salary=("salary", "mean"),          # named aggregation: new col "avg_salary" = mean of "salary"
        employee_count=("name", "count"),       # bonus: headcount per department
    )
    .round({"avg_salary": 2})                   # round only the avg_salary column to 2 decimal places
    .sort_values("avg_salary", ascending=False) # highest average salary first
    .reset_index()                              # promote "department" from index back to a regular column
)

print(avg_salary_by_dept)
