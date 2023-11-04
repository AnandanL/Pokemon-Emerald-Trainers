import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/anandanlakshminarayanan/Downloads/Copy of Pokemon Gen 3 Trainers DataSheet - Emerald Swampert.csv')

# Fill NaN values in 'Name' and 'Location' with the previous valid value
df['Name'].fillna(method='ffill', inplace=True)
df['Location'].fillna(method='ffill', inplace=True)

def format_data(row):
    output = ""

    # Format the Pokémon details
    if pd.notna(row['Pokemon']):
        output += f"{row['Pokemon']}"
        output += f"\nLevel: {row['Level']}\n"
        output += f"Adamant Nature\n"
        output += f"Ability: Pickup\n"
        
        # Add the attacks
        for i in range(1, 5):
            attack_col = f"Attack {i}"
            if pd.notna(row[attack_col]):
                output += f"- {row[attack_col]}\n"

    return output.strip()

# Apply the function to each row and collect the results
formatted_data = df.apply(format_data, axis=1)

# Export the formatted data to a .txt file
with open('formatted_data.txt', 'w') as file:
    for entry in formatted_data:
        file.write(entry)
        file.write("\n\n")  # Double spacing



