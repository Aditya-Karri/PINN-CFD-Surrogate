import csv
import numpy as np
import os

# Define path
file_path = r"D:\cfd-ml-project\cases_to_run.csv"

# Define range: -4 to +18 degrees
angles = np.concatenate([
    np.arange(-4, 0, 2.0),    # -4, -2 (2.0 deg steps)
    np.arange(0, 10.5, 1.0),   # 0, 1... 10 (1.0 deg steps)
    np.arange(10.5, 16.5, 0.5), # 10.5, 11,...16(0.5 deg step for detail)
    np.arange(17,18.5,1)    # likely post stall 1 deg step
])

# Sort and remove duplicates
angles = np.unique(angles)

print(f"Generating {len(angles)} cases...")

with open(file_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["case_id", "aoa", "re"])  # Header
    
    for ang in angles:
        # Create clean case ID names (e.g., "minus2deg" or "8.5deg")
        if ang < 0:
            label = f"minus{abs(ang):g}deg"
        else:
            label = f"{ang:g}deg"
            
        writer.writerow([label, ang, "6e6"])

print(f" 'cases_to_run.csv' generated at {file_path}")