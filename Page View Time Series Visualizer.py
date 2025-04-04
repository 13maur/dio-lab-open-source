import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data
def load_data():
    # Import the data and set the 'date' column as the index
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    
    # Step 2: Clean the data by filtering out the top and bottom 2.5% page views
    lower_bound = df['page_views'].quantile(0.025)
    upper_bound = df['page_views'].quantile(0.975)
    df = df[(df['page_views'] >= lower_bound) & (df['page_views'] <= upper_bound)]
    
    return df

# Step 3: Draw Line Plot
def draw_line_plot(df):
    # Create a copy of the data for manipulation
    df_copy = df.copy()
    
    # Set up the figure
    plt.figure(figsize=(12, 6))
    
    # Plot the line plot
    plt.plot(df_copy.index, df_copy['page_views'], color='blue', linewidth=1)
    
    # Set the title and labels
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Show the plot
    plt.grid(True)
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('line_plot.png')
    
    # Display the plot
    plt.show()

# Step 4: Draw Bar Plot
def draw_bar_plot(df):
    # Create a copy of the data for manipulation
    df_copy = df.copy()
    
    # Add year and month columns for grouping
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month
    
    # Calculate average page views by month and year
    monthly_avg = df_copy.groupby(['year', 'month'])['page_views'].mean().unstack()
    
    # Plot the bar plot
    monthly_avg.plot(kind='bar', figsize=(12, 6), stacked=False)
    
    # Set the title and labels
    plt.title('Average Daily Page Views for Each Month Grouped by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # Show the plot
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('bar_plot.png')
    
    # Display the plot
    plt.show()

# Step 5: Draw Box Plot
def draw_box_plot(df):
    # Create a copy of the data for manipulation
    df_copy = df.copy()
    
    # Add year and month columns for plotting
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month
    
    # Set up the figure
    plt.figure(figsize=(12, 6))
    
    # Create two subplots: Year-wise and Month-wise box plots
    # Year-wise Box Plot (Trend)
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='page_views', data=df_copy)
    plt.title('Year-wise Box Plot (Trend)')
    
    # Month-wise Box Plot (Seasonality)
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='page_views', data=df_copy)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # Show the plot
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('box_plot.png')
    
    # Display the plot
    plt.show()

# Main function to execute all steps
def time_series_visualizer():
    # Load and clean the data
    df = load_data()
    
    # Draw all the plots
    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plot(df)

# Run the visualizer
if __name__ == '__main__':
    time_series_visualizer()
