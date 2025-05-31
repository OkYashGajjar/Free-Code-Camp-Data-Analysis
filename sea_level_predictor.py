import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Line of best fit for all data
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_extended = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels_extended, 'r', label='Fit: All Data')

    # Line of best fit for data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = intercept_recent + slope_recent * years_recent
    plt.plot(years_recent, sea_levels_recent, 'green', label='Fit: Since 2000')

    # Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and return figure
    plt.savefig('sea_level_plot.png')
    return plt.gca().figure
