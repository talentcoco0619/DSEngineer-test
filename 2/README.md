# Regression Model for Tabular Data

## Project Structure
- `eda.ipynb`: Jupyter notebook for exploratory data analysis.
- `train.py`: Script for training the regression model.
- `predict.py`: Script for making predictions on the test data.
- `requirements.txt`: List of required Python packages.
- `predictions.csv`: File containing the prediction results.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the EDA notebook:
    Open `eda.ipynb` in Jupyter Notebook and run all cells.

4. Train the model:
    ```bash
    python train.py
    ```

5. Make predictions on the test data:
    ```bash
    python predict.py
    ```

## General Guidance
- Ensure that `train.csv` and `hidden_test.csv` are in the same directory as the scripts.
- The model is saved as `model.joblib` after training.
- Predictions are saved in `predictions.csv`.