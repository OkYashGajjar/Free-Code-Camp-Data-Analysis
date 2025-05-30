import pandas as pd

def calculate_demographic_data():

    #Reads Data from csv
    df = pd.read_csv('data.csv')
    
    #How many people of each race are represented in this dataset? 
    #This should be a Pandas series with race names as the index labels. (race column)
    value_counts = df['race'].value_counts()
    print(value_counts)

    #What is the average age of men?
    avg_age_men = df[df['sex'] == 'Male']['age'].mean()
    print(avg_age_men)

    #What is the percentage of people who have a Bachelor's degree?
    total_count = len(df)
    bachelor_count = len(df[df['education'] == 'Bachelors'])
    percentage = round(bachelor_count/total_count * 100)
    print(percentage)

    #What percentage of people with advanced education 
    #(Bachelors, Masters, or Doctorate) make more than 50K?
    adv_edu = ['Bachelors', 'Masters', 'Doctorate']
    high_edu = df[df['education'].isin(adv_edu)]
    higher_edu = high_edu[high_edu['salary'] == '>50k']
    perc_higher_edu = round(len(higher_edu)/len(high_edu) * 100)
    print(perc_higher_edu)

    #What percentage of people without advanced education make more than 50K?
    lower_edu = df[~df['education'].isin(adv_edu)]
    lower_edu_rich = lower_edu[lower_edu['salary'] == '>50k']
    perc_lower_edu_rich = round(len(lower_edu_rich)/len(lower_edu) * 100)
    print(perc_lower_edu_rich)

    #What is the minimum number of hours a person works per week?
    min_work_hour_per_week = df['hours-per-week'].min()
    print(min_work_hour_per_week)

    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hour_worker = df[df['hours-per-week' == min_work_hour_per_week]]
    min_work_more_salary = min_hour_worker[min_hour_worker['salary'] == '>50k']
    perc_min_worker_with_high_salary = len(min_work_more_salary)/len(min_hour_worker) *100
    print(perc_min_worker_with_high_salary)

    #What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_percentage_by_country = (rich_by_country / country_counts * 100).fillna(0)
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_by_country.max())

    #Identify the most popular occupation for those who earn >50K in India.
    rich_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = rich_indians['occupation'].mode()[0]

    return {
        'race_count': value_counts,
        'average_age_men': avg_age_men,
        'percentage_bachelors': percentage,
        'percentage_higher_education_rich': perc_higher_edu,
        'percentage_lower_education_rich': perc_lower_edu_rich,
        'min_work_hours': min_work_hour_per_week,
        'rich_percentage': perc_min_worker_with_high_salary,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }