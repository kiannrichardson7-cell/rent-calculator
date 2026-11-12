# Simple rent calculator
# Works out what rent costs per week, fortnight, month and year.

weekly_rent = float(input("What is the weekly rent? $"))

fortnightly = weekly_rent * 2
monthly = weekly_rent * 52 / 12
yearly = weekly_rent * 52

print(f"Per week:      ${weekly_rent:.2f}")
print(f"Per fortnight: ${fortnightly:.2f}")
print(f"Per month:     ${monthly:.2f}")
print(f"Per year:      ${yearly:.2f}")

budget = 400
if weekly_rent <= budget:
    print("That's within the $400 a week budget.")
else:
    print("That's over the $400 a week budget.")
