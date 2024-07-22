# Python code to generate the string-integer ID mapping for June 2024
import calendar

month = 6  # June
year = 2024

# Get the number of days in the month
num_days = calendar.monthrange(year, month)[1]

# Generate the mapping
string_integer_mapping = {f"{year}-{month:02d}-{day:02d}": str(day) for day in range(1, num_days + 1)}

# Print the generated mapping
print(string_integer_mapping)
