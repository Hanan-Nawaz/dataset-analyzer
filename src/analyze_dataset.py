import pandas as pd

def show_basic_info(df: pd.DataFrame) -> list:
    """Gives us number of columns and rows

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe, created by the load_data

    Returns
    -------
    list
        Returns a list that contains the [No. of Cols, No. of Rows]
    """

    return [df.columns.value_counts().sum(), df[df.columns[0]].size]

def show_columns_types(df: pd.DataFrame) -> list:
    """Gives us the data types of columns

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe, created by the load_data

    Returns
    -------
    list
        Gives us a list, [(column_name, data_type)]
    """
    return list(zip(df.columns, df.dtypes.astype(str)))

def show_missing_values(df: pd.DataFrame) -> dict:
    """Gives us a count of Null and Zero values per column

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe, created by the load_data

    Returns
    -------
    dict
        Gives us a dict

    Note
    ----

    {
        col_name: [nan_vales, zero_values]
    }
    """
    missing_values_dict = {}

    for col in df.columns:
        missing_values_dict[col] = [int(df[col].isna().sum()), int((df[col] == 0).sum())]

    return missing_values_dict
        
def show_duplicate_values(df: pd.DataFrame) -> int:
    """Gives us the number of Duplicate values in the Dataset

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe, created by the dataset

    Returns
    -------
    int
        gives us the number of duplicated rows
    """

    return df.duplicated().sum()

def show_stats(df: pd.DataFrame) -> dict:
    """Gives us the Stats about the dataset

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe, created from the dataset

    Returns
    -------
    dict
        dict of the df.info()
    """

    info = {
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "non_null_count": df.count().to_dict(),
        "memory_usage": int(df.memory_usage(deep=True).sum()),
        "shape": df.shape,
    }

    return info
