import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], alpha=0.7)

    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    x_pred = pd.Series(range(1880, 2051))  # predict until 2050
    y_pred = intercept + slope * x_pred
    ax.plot(x_pred, y_pred, "r", label="Best fit (1880–2050)")

    # Create second line of best fit (from year 2000 onward)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = intercept2 + slope2 * x_pred_recent
    ax.plot(x_pred_recent, y_pred_recent, "g", label="Best fit (2000–2050)")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save plot and return figure
    fig.savefig("sea_level_plot.png")
    return fig
