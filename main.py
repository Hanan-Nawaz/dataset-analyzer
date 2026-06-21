from src.load_data import load_data
from src.analyze_dataset import (
    show_basic_info,
    show_columns_types,
    show_missing_values,
    show_duplicate_values,
    show_stats,
)
import sys

def print_analysis(name, df):
    """Print the dataset analysis results."""

    rows, columns = show_basic_info(df)

    print("=" * 65)
    print(f"{name} - Dataset Analysis Report")
    print("=" * 65)

    # Basic Info
    print("\nBasic Information")
    print(f"Rows    : {rows}")
    print(f"Columns : {columns}")

    # Column Types
    print("\nColumn Types")
    print("-" * 35)
    print(f"{'Column':<20} {'Type':<15}")
    print("-" * 35)

    for col, dtype in show_columns_types(df):
        print(f"{col:<20} {dtype:<15}")

    # Missing Values
    print("\nMissing Values")
    print("-" * 45)
    print(f"{'Column':<20} {'Null':<10} {'Zero':<10}")
    print("-" * 45)

    for col, values in show_missing_values(df).items():
        null_count, zero_count = values
        print(f"{col:<20} {null_count:<10} {zero_count:<10}")

    # Duplicate Values
    print(f"\nDuplicate Rows : {show_duplicate_values(df)}")

    # Statistics
    stats = show_stats(df)

    print("\nDataset Statistics")
    print("-" * 65)
    print(f"{'Column':<20} {'Data Type':<15} {'Non-Null Count':<15}")
    print("-" * 65)

    for col in stats["columns"]:
        print(
            f"{col:<20}"
            f"{stats['dtypes'][col]:<15}"
            f"{stats['non_null_count'][col]:<15}"
        )

    print("-" * 65)
    print(f"Memory Usage : {stats['memory_usage']} bytes")
    print(f"Shape        : {stats['shape']}")
    print("=" * 65)

def main():
    file_path = sys.argv[1]

    df = load_data(file_path)
    print_analysis(file_path.split("/")[1], df)

if __name__ == "__main__":
    main()