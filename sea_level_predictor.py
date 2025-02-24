import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def create_line_best_fit(df, color):
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = pd.Series([i for i in range(df["Year"].min(), 2051)])
    regression_line = slope * x_values + intercept
    plt.plot(x_values, regression_line, color=color, label='Regression line')

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data points", color="darkblue")

    # Create first line of best fit
    df_first_line = df.copy()
    create_line_best_fit(df_first_line, "red")
    
    # Create second line of best fit
    df_second_line = df_first_line[df_first_line["Year"] >= 2000]
    create_line_best_fit(df_second_line, "cyan")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
