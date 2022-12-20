import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def plot_receipt_count_predictions(all_data, x, y):
    plt.scatter(all_data['timestamp'], all_data["Receipt_Count"], label='Data')
    plt.plot(x, y, color='k', label='Predictions')
    plt.xlabel('Timestamp')
    plt.ylabel('Receipt_Count')
    plt.legend()
    return plt

def print_eval_results(evaluation_results):
    for key, value in evaluation_results.items():
        print(f"Metric Name: {key:30} | Value: {value}")

def convert_column_to_datetime(column):
    return pd.to_datetime(column)

def prepare_data(dataframe):
    
    # Convert the "# Date" column into a datetime object
    dataframe["# Date"] = convert_column_to_datetime(dataframe["# Date"])
    
    dataframe['timestamp'] = dataframe["# Date"].astype(int)/ 10**9
    return dataframe

def train_valid_split(df,percent_split=0.2,random_state=5):
    train,test = train_test_split(df,test_size=percent_split,random_state=random_state)
    X_train =  train["timestamp"]
    X_test = test["timestamp"]
    y_train = train["Receipt_Count"]
    y_test = test["Receipt_Count"]
    return X_train, X_test, y_train, y_test 

def run_evaluation_calculations(y_test, y_predictions):
    mse = mean_squared_error(y_test, y_predictions)
    rmse = mean_squared_error(y_test, y_predictions, squared=False)
    r2_score_ = r2_score(y_test, y_predictions)
    mae = mean_absolute_error(y_test, y_predictions)
    return {
        "Mean Squared Error":mse,
        "Root Mean Squared Error":rmse,
        "R-squared":r2_score_,
        "Mean Absolute Error":mae
    }

def train_test_beginning_end(all_data):
    TOTAL_PERCENT_VALIDATION_DATA = .16
    TOTAL_PERCENT_TRAINING_DATA = 1-TOTAL_PERCENT_VALIDATION_DATA

    NUM_ROWS_OF_TOTAL_DATA = all_data.shape[0]

    FIRST_SPLIT_INDEX = int((TOTAL_PERCENT_VALIDATION_DATA / 2) * NUM_ROWS_OF_TOTAL_DATA)
    SECOND_SPLIT_INDEX = int((1-(TOTAL_PERCENT_VALIDATION_DATA / 2)) * NUM_ROWS_OF_TOTAL_DATA)
    training_data = all_data.iloc[FIRST_SPLIT_INDEX:SECOND_SPLIT_INDEX]
    validation_data = all_data.iloc[np.r_[0:FIRST_SPLIT_INDEX, SECOND_SPLIT_INDEX:NUM_ROWS_OF_TOTAL_DATA]]
    X_train = training_data["timestamp"]
    X_train = np.asarray(X_train).astype(np.float32)

    y_train = training_data["Receipt_Count"]
    y_train = np.asarray(y_train).astype(np.float32)
    X_validation = validation_data["timestamp"]
    X_validation = np.asarray(X_validation).astype(np.float32)

    y_validation = validation_data["Receipt_Count"]
    y_validation = np.asarray(y_validation).astype(np.float32)
    return X_train, X_validation, y_train, y_validation

