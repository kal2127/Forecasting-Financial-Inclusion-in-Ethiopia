import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """Loads a CSV file with error handling."""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Could not find file at: {file_path}")
        df = pd.read_csv(file_path)
        print(f"✅ Successfully loaded data from {file_path}")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def plot_indicator_trend(df, indicator_name, title="Indicator Trend"):
    """Creates a consistent line plot for any indicator."""
    try:
        data = df[df['indicator'] == indicator_name].copy()
        if data.empty:
            print(f"⚠️ No data found for indicator: {indicator_name}")
            return
            
        plt.figure(figsize=(10, 5))
        plt.plot(pd.to_datetime(data['observation_date']), data['value_numeric'], marker='o')
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()
    except Exception as e:
        print(f"❌ Error during plotting: {e}")