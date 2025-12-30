
"""
Training script for Sales Forecasting project
This script simulates training using historical sales data
(No pickle, no model saving – logic handled directly in model.py)
"""

import pandas as pd

def train_model(csv_path: str):
    """
    Simulate training process using sales data
    """

    print("Starting training process...")

    # Load dataset
    df = pd.read_csv(csv_path)

    # Basic validation
    if "sales" not in df.columns:
        raise ValueError("Dataset must contain a 'sales' column")

    # Convert date column if present
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")

    # Simple training logic (statistics)
    avg_sales = df["sales"].mean()
    max_sales = df["sales"].max()
    min_sales = df["sales"].min()

    print("Training completed successfully ✅")
    print(f"Average Sales : {round(avg_sales, 2)}")
    print(f"Max Sales     : {round(max_sales, 2)}")
    print(f"Min Sales     : {round(min_sales, 2)}")

    return {
        "average_sales": avg_sales,
        "max_sales": max_sales,
        "min_sales": min_sales
    }

# Run training directly
if __name__ == "__main__":
    train_model("../9. Sales-Data-Analysis.csv")
