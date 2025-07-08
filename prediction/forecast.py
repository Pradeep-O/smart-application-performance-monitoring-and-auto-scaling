import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_traffic(csv_path="data/metrics.csv"):
    df = pd.read_csv(csv_path)
    df['time_index'] = np.arange(len(df))
    
    model = LinearRegression()
    model.fit(df[['time_index']], df[['request_rate']])
    
    future_index = pd.DataFrame({'time_index': np.arange(len(df), len(df) + 5)})
    prediction = model.predict(future_index)

    
    return prediction.mean()  # average of next 5 predictions

if __name__ == "__main__":
    print(f"Predicted average traffic: {predict_traffic()}")
