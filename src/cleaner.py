import csv
import os

def clean_csv(input_path, output_path):
    with open(input_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

   
    cleaned_columns = [
        col.strip().lower().replace(" ", "_").replace("-", "_")
        for col in reader.fieldnames
    ]

    cleaned_rows = []
    seen = set()   

    for row in rows:
        cleaned_row = {
            col.strip().lower().replace(" ", "_").replace("-", "_"): value.strip()
            for col, value in row.items()
        }


        if all(value == "" for value in cleaned_row.values()):
            continue

        # remove duplicates
        tuple_row = tuple(cleaned_row.items())
        if tuple_row not in seen:
            seen.add(tuple_row)
            cleaned_rows.append(cleaned_row)

    # write cleaned output
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cleaned_columns)
        writer.writeheader()
        writer.writerows(cleaned_rows)
