import csv
import os

def clean_csv(input_file, output_file="data/cleaned_output.csv"):
    # ---- STEP 1: Read the CSV ----
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    raw_columns = data[0]
    rows = data[1:]

    # ---- STEP 2: Clean column names ----
    clean_columns = []
    col_count = {}

    for col in raw_columns:
        new_col = col.strip().lower().replace(" ", "_").replace("-", "_")

        if new_col in col_count:
            col_count[new_col] += 1
            new_col = f"{new_col}_{col_count[new_col]}"
        else:
            col_count[new_col] = 1

        clean_columns.append(new_col)

    # ---- STEP 3: Clean rows ----
    cleaned_rows = []
    seen = set()

    for row in rows:
        cleaned = [v.strip() for v in row]

        if all(v == "" for v in cleaned):
            continue

        row_tuple = tuple(cleaned)

        if row_tuple not in seen:
            seen.add(row_tuple)
            cleaned_rows.append(cleaned)

    # ---- STEP 4: Write output ----
    os.makedirs("data", exist_ok=True)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(clean_columns)
        writer.writerows(cleaned_rows)

    return True
