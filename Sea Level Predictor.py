import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Step 1: Load the dataset
def load_data():
    # Load the dataset from the CSV file
    df = pd.read_csv('epa-sea-level.csv')
    return df

# Step 2: Create a scatter plot and line of best fit
def draw_scatter_and_fit_lines(df):
    # Create a scatter plot of the Year vs. Sea Level
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # First Line of Best Fit: Using all data points
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope_all * df['Year'] + intercept_all, color='red', label='Best Fit Line (1880-2014)')

    # Second Line of Best Fit: Using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(df_recent['Year'], slope_recent * df_recent['Year'] + intercept_recent, color='green', label='Best Fit Line (2000-2014)')

    # Predict sea level in 2050 for both lines
    plt.plot(2050, slope_all * 2050 + intercept_all, 'ro')  # 2050 prediction for all data
    plt.plot(2050, slope_recent * 2050 + intercept_recent, 'go')  # 2050 prediction for 2000 onward

    # Add titles and labels
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Display legend
    plt.legend()

    # Save the figure
    plt.savefig('sea_level_predictor.png')

    # Show the plot
    plt.show()

# Main function to load the data and draw the plots
def sea_level_predictor():
    # Load the data
    df = load_data()

    # Draw the scatter plot and fit lines
    draw_scatter_and_fit_lines(df)

# Run the function to generate the plot
if __name__ == '__main__':
    sea_level_predictor()
