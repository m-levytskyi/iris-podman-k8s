import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data(database_path):
    conn = sqlite3.connect(database_path)
    query = "SELECT * FROM iris"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def train_model(df):
    """
    Trains a RandomForestClassifier model on the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the features and target variable. 
                           It is expected to have a column named 'species' which is the target variable.

    Returns:
    RandomForestClassifier: The trained RandomForestClassifier model.
    """
    X = df.drop(columns=['species'])
    y = df['species']
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    return rf_model

if __name__ == "__main__":
    db_path = '/app/iris.db'
    data = load_data(db_path)
    model = train_model(data)
    joblib.dump(model, '/app/model.pkl')
    print("Model trained and saved.")
