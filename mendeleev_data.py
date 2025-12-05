import pandas as pd
from mendeleev import element

all_elements = []

for i in range(1, 119):
    el = element(i)
    
    # 1. Basic Info
    row_data = {
        "Symbol": el.symbol,
        "Name": el.name,
        "AtomicNumber": el.atomic_number,
        "Category": el.series,
        "Description": el.description
    }

    # 2. DEFAULT POSITION
    row = el.period
    col = el.group_id

    # 3. SPECIAL CASES (The Anchor Strategy)
    
    # Lanthanum (57) - Stays in Main Grid
    if el.atomic_number == 57:
        row = 6
        col = 3
        
    # Actinium (89) - Stays in Main Grid
    elif el.atomic_number == 89:
        row = 7
        col = 3

    # Lanthanides (58-71) - Move to Row 8
    elif 58 <= el.atomic_number <= 71:
        row = 8
        # Ce(58) needs to be Col 4. So: 58 - 54 = 4
        col = el.atomic_number - 54 

    # Actinides (90-103) - Move to Row 9
    elif 90 <= el.atomic_number <= 103:
        row = 9
        # Th(90) needs to be Col 4. So: 90 - 86 = 4
        col = el.atomic_number - 86

    row_data["Row"] = row
    row_data["Column"] = col
    
    all_elements.append(row_data)

# Save with semicolon separator
df = pd.DataFrame(all_elements)
df.to_csv("elements.csv", sep=";", index=False)
print("elements.csv has been regenerated with Anchor layout!")