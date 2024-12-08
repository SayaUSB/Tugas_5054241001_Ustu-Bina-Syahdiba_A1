import pandas as pd

def read_csv_file(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Display basic information about the dataframe
        print("Basic information about the dataframe:")
        print(df.info())
        
        # Display the first few rows of the dataframe
        print("\nFirst few rows of the dataframe:")
        print(df.head())
        
        # Display basic statistics of numerical columns
        print("\nBasic statistics of numerical columns:")
        print(df.describe())
        
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: Unable to parse '{file_path}'. Please check if it's a valid CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    df = read_csv_file('chocolate.csv')