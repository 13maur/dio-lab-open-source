import pandas as pd

def demographic_data_analyzer(df):
    # Question 1: How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # Question 2: What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # Question 3: What is the percentage of people who have a Bachelor's degree?
    bachelors_percentage = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

    # Question 4: What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education_high_income = advanced_education[advanced_education['salary'] == '>50K']
    advanced_education_percentage = (advanced_education_high_income.shape[0] / advanced_education.shape[0]) * 100

    # Question 5: What percentage of people without advanced education make more than 50K?
    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    no_advanced_education_high_income = no_advanced_education[no_advanced_education['salary'] == '>50K']
    no_advanced_education_percentage = (no_advanced_education_high_income.shape[0] / no_advanced_education.shape[0]) * 100

    # Question 6: What is the minimum number of hours a person works per week?
    min_hours_per_week = df['hours-per-week'].min()

    # Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_df = df[df['hours-per-week'] == min_hours_per_week]
    min_hours_high_income = min_hours_df[min_hours_df['salary'] == '>50K']
    min_hours_percentage_high_income = (min_hours_high_income.shape[0] / min_hours_df.shape[0]) * 100

    # Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary_data = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size()
    highest_percentage_country = country_salary_data.idxmax()
    highest_percentage = country_salary_data.max() * 100

    # Question 9: Identify the most popular occupation for those who earn >50K in India.
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular_occupation_india = india_high_income['occupation'].value_counts().idxmax()

    # Returning the results as a dictionary
    return {
        "race_count": race_count,
        "average_age_men": round(average_age_men, 1),
        "bachelors_percentage": round(bachelors_percentage, 1),
        "advanced_education_high_income_percentage": round(advanced_education_percentage, 1),
        "no_advanced_education_high_income_percentage": round(no_advanced_education_percentage, 1),
        "min_hours_per_week": min_hours_per_week,
        "min_hours_percentage_high_income": round(min_hours_percentage_high_income, 1),
        "highest_percentage_country": highest_percentage_country,
        "highest_percentage": round(highest_percentage, 1),
        "most_popular_occupation_india": most_popular_occupation_india
    }

