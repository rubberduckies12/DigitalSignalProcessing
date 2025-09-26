# Variables
principal = 10_000_000  # $20 million
rate = 0.08  # 8% annual interest
years = 20

# Calculate compound interest for each year
compound_values = []
for year in range(1, years + 1):
    amount = principal * (1 + rate) ** year
    compound_values.append((year, round(amount, 2)))

# Print results
for year, amount in compound_values:
    print(f"Year {year}: ${amount:,.2f}")