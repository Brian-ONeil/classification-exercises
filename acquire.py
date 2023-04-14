#######IMPORTS

import pandas as pd
import os
import env



#######FUNCTIONS





def new_titanic_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a db_url to mySQL
    - return a df of the given query from the titanic_db
    """
    url = env.get_db_url('titanic_db')
    
    return pd.read_sql(SQL_query, url)




def get_titanic_data(SQL_query, filename = 'titanic.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv
    - outputs titanic df
    """
    if os.path.exists(filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_titanic_data(SQL_query)

        df.to_csv(filename)
        return df
    
    
    
    
    
def new_iris_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a db_url to mySQL
    - return a df of the given query from the iris_db
    """
    url = env.get_db_url('iris_db')
    
    return pd.read_sql(SQL_query, url)



def get_iris_data(SQL_query, filename = 'iris.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv: defaulted to iris.csv
    - outputs iris df
    """
    if os.path.exists(filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_iris_data(SQL_query)

        df.to_csv(filename)
        return df
    
    

    
    
def new_telco_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a db_url to mySQL
    - return a df of the given query from the telco_db
    """
    url = env.get_db_url('telco_churn')
    
    return pd.read_sql(SQL_query, url)




def get_telco_data(SQL_query, filename = 'telco.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv: defaulted to telco.csv
    - outputs iris df
    """
    if os.path.exists(filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_telco_data(SQL_query)

        df.to_csv(filename)
        return df
    