import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # print(df.head())
    # Create scatter plot
    plt.figure(figsize= (10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data',s=10)
    # Create first line of best fit
   
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = range(1880,2051)
    sea_leves1 = [slope1 * year + intercept1 for year in years1]
    plt.plot(years1, sea_leves1, color='red', label='Best Fit Line (1880-2050)')
    
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years2 = range(1880, 2051)
    sea_levels2 = [slope2 * year + intercept2 for year in years2]
    plt.plot(years2, sea_levels2, color='green', label='Best Fit Line (2000-2050)')
    
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()