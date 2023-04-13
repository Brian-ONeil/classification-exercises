def get_titanic_data(SQL_query, directory, filename="titanic.csv"):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output titanic df
"""
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename) 
        return df
    
    else:
        df = new_titanic_data(SQL_query)
        
        #want to save to csv
        df.to_csv(filename)
        return df