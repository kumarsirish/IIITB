import pandas as pd
df = pd.read_csv('dummy_district_data.csv', index_col=0)
input_state = input().strip().upper()

# Load your dataset

# Compute literacy rate

df["LiteracyRate"] = df["Literate"] / df["Population"]

# Convert State column to uppercase for comparison
df["State_upper"] = df["State name"].str.upper()

# Filter for the given state
state_df = df[df["State_upper"] == input_state]

# Identify district with highest literacy rate
ser_out = state_df.loc[state_df["LiteracyRate"].idxmax()]

# Print only the district name
print(ser_out["District name"])



