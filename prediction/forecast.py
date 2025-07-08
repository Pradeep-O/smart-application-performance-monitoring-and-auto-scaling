from prophet import Prophet
import pandas as pd

def predict_traffic_prophet(csv_path="data/metrics.csv"):
    df = pd.read_csv(csv_path)
    df = df.rename(columns={"timestamp": "ds", "request_rate": "y"})
    df['ds'] = pd.to_datetime(df['ds'])
    
    model = Prophet(daily_seasonality=True, weekly_seasonality=True)
    model.fit(df[['ds', 'y']])
    
    future = model.make_future_dataframe(periods=60, freq='min')  # Predict next 60 mins
    forecast = model.predict(future)
    
    predicted_traffic = forecast[['ds', 'yhat']].tail(60)['yhat'].mean()
    return predicted_traffic

if __name__ == "__main__":
    pred = predict_traffic_prophet()
    print(f"Prophet predicted average traffic next hour: {pred:.2f}")
