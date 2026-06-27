import pandas as pd

def load_data(file) -> pd.DataFrame:
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
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
            return df
        elif file.name.endswith(".xlsx"):
            df = pd.read_excel(file)
            return df
        else:
            print("The file must be csv or excel file")
    except Exception as e:
        print(f"The error is {e}")