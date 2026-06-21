import pytest
from src.load_data import load_data
from src.analyze_dataset import (show_basic_info, show_columns_types, 
                                 show_missing_values, show_duplicate_values,
                                 show_stats)
import pandas as pd

@pytest.mark.parametrize (
    "case", 
    [
        {
            "input": {
                "file_path": "data/sample.csv"
            },
            "output": {
                "df_type": 'pandas.DataFrame',
                "basic_info": [4, 10],
                "columns_types": [('id', 'int64'), ('name', 'str'), ('age', 'int64'), ('city', 'str')],
                "missing_values": {'id': [0, 0], 'name': [1, 0], 'age': [0, 1], 'city': [0, 0]},
                "duplicate_values": 1,
                "stats": {'columns': ['id', 'name', 'age', 'city'], 'dtypes': {'id': 'int64', 'name': 'str', 'age': 'int64', 'city': 'str'}, 'non_null_count': {'id': 10, 'name': 9, 'age': 10, 'city': 10}, 'memory_usage': 1376, 'shape': (10, 4)}
            }
        },
        {
            "input": {
                "file_path": "data/sample.xlsx"
            },
            "output": {
                "df_type": 'pandas.DataFrame',
                "basic_info": [4, 10],
                "columns_types": [('id', 'int64'), ('name', 'str'), ('age', 'int64'), ('city', 'str')],
                "missing_values": {'id': [0, 0], 'name': [1, 0], 'age': [0, 1], 'city': [0, 0]},
                "duplicate_values": 1,
                "stats": {'columns': ['id', 'name', 'age', 'city'], 'dtypes': {'id': 'int64', 'name': 'str', 'age': 'int64', 'city': 'str'}, 'non_null_count': {'id': 10, 'name': 9, 'age': 10, 'city': 10}, 'memory_usage': 1376, 'shape': (10, 4)}
            }
        }
    ],
    ids=[
        "Dataset Analyzer test - Sample.csv",
        "Dataset Analyzer test - Sample.xlsx"
    ]
)
def test_analyze_dataset(case):
    """Method to test our Dataset Analzyer"""

    # input and outout
    input = case["input"]
    output = case["output"]

    # executing methods to be tested
    df = load_data(input["file_path"])
    basic_info = show_basic_info(df)
    col_types = show_columns_types(df)
    missing_values = show_missing_values(df)
    duplicate_values = show_duplicate_values(df)
    stats = show_stats(df)

    # checking the results
    assert isinstance(df, pd.DataFrame)
    assert basic_info == output["basic_info"]
    assert col_types == output["columns_types"]
    assert missing_values == output["missing_values"]
    assert duplicate_values == output["duplicate_values"]
    assert stats == output["stats"]

    