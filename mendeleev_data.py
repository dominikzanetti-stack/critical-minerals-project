import pandas as pd
from mendeleev import element

# 1. Define our specific categories
# Rare Earth Elements (Chemical definition)
rare_earths = [
    "Sc", "Y", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", 
    "Dy", "Ho", "Er", "Tm", "Yb", "Lu"
]

# US Critical Minerals (USGS 2022 Final List)
# Note: The USGS lists "Rare Earth Elements group" as one entry, 
# so technically all REEs are Critical.
critical_minerals = [
    "Al", "Sb", "As", "Ba", "Be", "Bi", "B", "C", "Cd", "Ce", "Cs", "Cr", "Co", 
    "Cu", "Dy", "Er", "Eu", "F", "Gd", "Ga", "Ge", "Hf", "Ho", "In", "Ir", 
    "K", "La", "Pb", "Li", "Lu", "Mg", "Mn", "Nd", "Ni", "Nb", "Pd", "P", 
    "Pt", "Pr", "Pm", "Re", "Rh", "Rb", "Ru", "Sm", "Sc", "Si", "Ag", "Ta", 
    "Te", "Tb", "Tm", "Sn", "Ti", "W", "U", "V", "Yb", "Y", "Zn", "Zr"
]

all_elements = []

for i in range(1, 119):
    el = element(i)
    
    # 1. Basic Info
    row_data = {
        "Symbol": el.symbol,
        "Name": el.name,
        "AtomicNumber": el.atomic_number,
        "Category": el.series,
        "Description": el.description,
        "Rare": 0,
        "Critical": 0            
    }

    if row_data["Symbol"] in rare_earths:
        row_data["Rare"] = 1
    if row_data["Symbol"] in critical_minerals:
        row_data["Critical"] = 1

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

    # Lanthanides (58-71) - Move to Row 9
    elif 58 <= el.atomic_number <= 71:
        row = 9
        # Ce(58) needs to be Col 4. So: 58 - 54 = 4
        col = el.atomic_number - 54 

    # Actinides (90-103) - Move to Row 10
    elif 90 <= el.atomic_number <= 103:
        row = 10
        # Th(90) needs to be Col 4. So: 90 - 86 = 4
        col = el.atomic_number - 86

    row_data["Row"] = row
    row_data["Column"] = col
    
    all_elements.append(row_data)

# Save with semicolon separator
df = pd.DataFrame(all_elements)
df.to_csv("elements.csv", sep=";", index=False)
print("elements.csv has been regenerated with Anchor layout!")