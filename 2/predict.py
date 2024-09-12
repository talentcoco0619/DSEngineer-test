import pandas as pd
import joblib

# Load the test dataset
test_df = pd.read_csv('hidden_test.csv')

# Load the trained model
model = joblib.load('model.joblib')

# Make predictions
predictions = model.predict(test_df)

# Save the predictions
output = pd.DataFrame({'Id': test_df.index, 'Prediction': predictions})
output.to_csv('predictions.csv', index=False)