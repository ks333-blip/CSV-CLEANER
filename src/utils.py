import os

def file_exists(path):
    return os.path.isfile(path)

def clean_column_name(col):
    return col.strip().lower().replace(" ", "_").replace("-", "_")
