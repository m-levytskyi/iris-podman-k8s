import sqlite3
import pandas as pd
from sklearn.datasets import load_iris

def initialize_db(db_path):
    conn = sqlite3.connect(db_path)
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df.to_sql('iris', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    initialize_db('/app/iris.db')
    print("Database initialized.")
