import sys
from src.cleaner import clean_csv

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    if clean_csv(input_file):
        print("CSV cleaned successfully!")
