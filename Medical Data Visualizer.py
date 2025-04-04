import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def medical_data_visualizer(df):
    # Step 1: Import the data from medical_examination.csv and assign it to the df variable.
    df = pd.read_csv('medical_examination.csv')

    # Step 2: Add an overweight column to the data based on BMI calculation
    # BMI = weight(kg) / (height(m))^2
    df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
    df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)

    # Step 3: Normalize cholesterol and gluc columns
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    # Step 4: Draw the Categorical Plot
    # Prepare the data for the categorical plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group by 'cardio' and show the counts of each feature
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')

    # Create the categorical plot
    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count", height=5, aspect=1.2)
    fig.fig.tight_layout()

    # Step 5: Draw the Heat Map
    # Clean the data: filter out the incorrect data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = corr.where(pd.np.triu(pd.np.ones(corr.shape), k=1).astype(bool))

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', cbar_kws={'shrink': .8})

    # Display the plot
    plt.show()

    # Return the figure object for the categorical plot (from step 4)
    return fig
