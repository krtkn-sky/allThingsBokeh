import pandas as pd
import random

# Function to generate a data entry with natural variations
def generate_data_entry():
    year = random.randint(2010, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    
    # Generate temperature and pressure with natural variations
    temperature = random.uniform(-20, 35)  # Temperature in Celsius
    pressure = random.uniform(980, 1020)  # Pressure in hPa
    
    return [year, month, day, hour, temperature, pressure]

# Generate and store 33,000 data entries in an Excel file (weather.xlsx)
data = []
for _ in range(33000):
    data_entry = generate_data_entry()
    data.append(data_entry)

df = pd.DataFrame(data, columns=["Year", "Month", "Day", "Hour", "Temperature", "Pressure"])
df.to_excel("weather.xlsx", index=False)

