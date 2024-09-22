import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    df.plot(x="Year", y="CSIRO Adjusted Sea Level", kind="scatter", ax=ax)

    # Create first line of best fit (using all data)
    x1 = range(df["Year"].min(), 2051, 1)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.plot(x1, intercept + slope * x1, 'r', label='Best Fit Line 1')

    # Create second line of best fit (for years >= 2000)
    df_recent = df[df['Year'] >= 2000]
    x2 = range(2000, 2051, 1)
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    plt.plot(x2, intercept2 + slope2 * x2, 'g', label='Best Fit Line 2')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
