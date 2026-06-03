# %% [markdown]
# # My lesson 4 practice work
# 
# Hello! This page shows my practice work for lesson 04 to show weekly sales.

# %%
sales_by_week = {
    "Week 1": 12000,
    "Week 2": 8500,
    "Week 3": 14700,
    "Week 4": 9800,
    "Week 5": 11200,
    "Week 6": 12000,
}

print("Weekly Sales Report")
print("-------------------")

for week, revenue in sales_by_week.items():
    print(week, ":", revenue)






# %%
def calculate_total(sales_dict):
    total = 0
    for revenue in sales_dict.values():
        total = total + revenue
    return total


# %%
def calculate_average(sales_dict):
    total = calculate_total(sales_dict)
    count = len(sales_dict)
    return total / count

# %%
print("Weekly Sales Report")
print("---------------------")

for week, revenue in sales_by_week.items():
    print(week, ":", revenue)

print()
print("Summary")
print("-------")
print("Total:", calculate_total(sales_by_week))
print("Average:", calculate_average(sales_by_week))
print("Number of week:", len(sales_by_week))


