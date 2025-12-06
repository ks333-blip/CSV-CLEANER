from src.cleaner import clean_csv
import sys

input_path = sys.argv[1]
output_path = "data/cleaned.csv"

clean_csv(input_path, output_path)
print("CSV cleaned successfully!")
