dataset={'library':[]}

import re
import pandas as pd

# # Sample dataset
# data = {
#     "gameid": [101, 102, 103],
#     "publishers": [
#         "['a inc.', 'b inc', 'c.,Inc.']",
#         "['x Ltd.', 'y,Inc.', 'z Studios']",
#         "['m corp', 'n, Inc.', 'o.,Inc.']"
#     ]
# }

# Create DataFrame
df = pd.DataFrame(dataset)

def split_publishers(text):
    # Remove brackets and extra spaces
    text = text.strip("[]").replace("'", "").strip()

    # Regular expression to split correctly while keeping variations of "Inc." intact
    # pattern = r'\s*(.*?)(?<!Inc)\s*,\s*'

    # Extract publishers while keeping "Inc." intact
    # matches = re.findall(pattern, text)

    # Remove empty strings and return cleaned list
    # return [pub.strip() for pub in matches if pub.strip()]
    text = text.replace(', Inc', ' Inc');
    text = text.replace(',Inc', ' Inc');
    text = text.replace(', Ltd', ' Ltd');
    text = text.replace(',Ltd', ' Ltd');
    text = text.replace(', LTD', ' LTD');
    text = text.replace(',LTD', ' LTD');
    
    
    return text

# Apply function to split publishers into lists
df["Cleaned_Publishers"] = df["publishers"].apply(split_publishers)

# Explode the DataFrame to create separate rows for each publisher
df_exploded = df.explode("Cleaned_Publishers").drop(columns=["publishers"]).rename(columns={"Cleaned_Publishers": "publisher"})

# Reset index
df_exploded = df_exploded.reset_index(drop=True)

# Print result
print(df_exploded)

