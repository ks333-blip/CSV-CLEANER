import csv
import os
def clean_csv(input_path, output_path):
    # Open the input CSV file and read all rows into memory
    with open(input_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Normalize column names (remove spaces, lowercase, replace hyphens)
    cleaned_columns = [
        col.strip().lower().replace(" ", "_").replace("-", "_")
        for col in reader.fieldnames
    ]

    cleaned_rows = []
    seen = set()   # Store rows we've already seen (used to remove duplicates)

    for row in rows:
        # Clean each value in the row (trim spaces, normalize column keys)
        cleaned_row = {
            col.strip().lower().replace(" ", "_").replace("-", "_"): value.strip()
            for col, value in row.items()
        }

        # Skip row if all fields are empty (example: ",,,")
        if all(value == "" for value in cleaned_row.values()):
            continue

        # Convert row dict into tuple so it can be stored in a set (for duplicate removal)
        tuple_row = tuple(cleaned_row.items())

        # Only add row if not seen before (removes duplicates)
        if tuple_row not in seen:
            seen.add(tuple_row)
            cleaned_rows.append(cleaned_row)

    # Write the final cleaned rows into the output CSV file
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cleaned_columns)
        writer.writeheader()        # Write column headers
        writer.writerows(cleaned_rows)   # Write all cleaned rows
