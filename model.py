"""
Sales forecasting logic (NO pickle, NO model loading)
"""

import numpy as np

def predict_sales(days: int):
    """
    Generate mock sales forecast data
    """

    base_value = 1000
    trend = 5
    predictions = []

    for i in range(days):
        seasonal_factor = 1 + 0.1 * np.sin(2 * np.pi * i / 7)
        random_factor = np.random.normal(1, 0.1)

        forecast = base_value + (i * trend)
        forecast = forecast * seasonal_factor * random_factor

        predictions.append(round(max(0, forecast), 2))

    return predictions
