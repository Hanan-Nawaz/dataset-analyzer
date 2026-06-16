import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Convert file into the Dataframe

    Parameters
    ----------
    file_path : str
        path of the dataset file

    Returns
    -------
    pd.DataFrame
        Dataframe of the dataset 
    """        

    try:

        if "csv" in file_path or ".xlsx" in file_path:
            df = pd.read_csv(file_path, index_col=0)
            return df
        else:
            print("The file must be csv or excel file")
    except Exception as e:
        print(f"The error is {e}")