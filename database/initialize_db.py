import sqlite3
import pandas as pd
from sklearn.datasets import load_iris

print('\n\n Running initialize_db.py \n\n')

# Load Iris dataset
iris = load_iris()
iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_data['target'] = iris.target
print('Dataset loaded')

# Create SQLite database
conn = sqlite3.connect('iris.db')
iris_data.to_sql('iris', conn, if_exists='replace', index=False)
print('DB created')

conn.close()
