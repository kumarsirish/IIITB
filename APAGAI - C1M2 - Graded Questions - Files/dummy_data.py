import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of rows and columns
num_rows = 640
num_cols = 119

# Example lists of states and districts
states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Generate random states and district names
state_col = np.random.choice(states, size=num_rows)
district_col = [f"District_{i}" for i in range(num_rows)]

# Generate population and literate counts
population_col = np.random.randint(50_000, 10_000_000, size=num_rows)
literate_col = (population_col * np.random.uniform(0.5, 0.95, size=num_rows)).astype(int)

# Create 115 additional dummy columns
extra_cols = {
    f"Feature_{i}": np.random.randint(0, 1000, size=num_rows)
    for i in range(num_cols - 4)
}

# Build DataFrame
df = pd.DataFrame({
    "State": state_col,
    "District": district_col,
    "Population": population_col,
    "Literate": literate_col,
    **extra_cols
})

# Save to CSV
df.to_csv("dummy_district_data.csv", index=True)

df.head()
