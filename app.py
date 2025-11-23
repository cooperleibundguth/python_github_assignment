print("Welcome to my Python program!")

# Task 2 — Ask the user for input
hours = input("How many hours did you study today? ")

# Task 3 — Perform a calculation
weekly_hours = hours * 7

# Task 4 — Display the result clearly
print(f"You are on track to study {weekly_hours} hours this week!")

# Task 5 — Add simple error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number next time.")
    exit()
