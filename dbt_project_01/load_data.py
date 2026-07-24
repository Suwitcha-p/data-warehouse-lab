import duckdb
import os
from pathlib import Path

# Connect to DuckDB
conn = duckdb.connect('dev.duckdb')

# Create the northwind schema if it doesn't exist
conn.execute("CREATE SCHEMA IF NOT EXISTS northwind")

# Get all CSV files from the dataset folder
dataset_path = Path('../dataset')
csv_files = list(dataset_path.glob('*.csv'))

print(f"Found {len(csv_files)} CSV files")
print("-" * 50)

# Load each CSV into the northwind schema
for csv_file in sorted(csv_files):
    table_name = csv_file.stem
    print(f"Loading {table_name}...", end=" ")
    
    try:
        # Read CSV and create table in northwind schema
        conn.execute(f"""
            CREATE TABLE northwind.{table_name} AS
            SELECT * FROM read_csv_auto('{csv_file}')
        """)
        
        # Get row count
        result = conn.execute(f"SELECT COUNT(*) FROM northwind.{table_name}").fetchone()
        print(f"✓ ({result[0]} rows)")
    except Exception as e:
        print(f"✗ Error: {e}")

print("-" * 50)

# Show all tables
tables = conn.execute(
    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'northwind' ORDER BY table_name"
).fetchall()

print(f"✅ Successfully created {len(tables)} tables in 'northwind' schema:")
for i, table in enumerate(tables, 1):
    print(f"   {i:2d}. {table[0]}")

conn.close()
