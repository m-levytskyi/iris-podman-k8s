import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data(db_path):
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM iris"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def train_model(df):
    X = df.drop(columns=['species'])
    y = df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    db_path = '/app/iris.db'
    data = load_data(db_path)
    model = train_model(data)
    joblib.dump(model, '/app/model.pkl')
    print("Model trained and saved.")
