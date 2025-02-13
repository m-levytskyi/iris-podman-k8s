import sqlite3
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

print('\n\n Running train_model.py \n\n')

# Connect to the SQLite database
conn = sqlite3.connect('data/iris.db')
print('Successfully connected to the Database')

# Load data from the Iris table
df = pd.read_sql('SELECT * FROM iris', conn)
conn.close()
print('Data from DB loaded')

# Separate features and target
X = df.drop('target', axis=1)
y = df['target']

# Train a simple model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the model to a file
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model trained and saved successfully.")
