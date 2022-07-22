import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { "chicago": "chicago.csv",
              "new york city": "new_york_city.csv",
              "washington": "washington.csv" }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print("Hello there and good day to you! Let's explore some US bikeshare data!")
	
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    try:
        city = input ("For which city would you like to see data: Chicago, New York City or Washington?").lower()
        while (city not in cities):
            print("You entered:",city,". Please enter one of the available cities.")
            city = input("Please choose one of the following: Chicago, New York City or Washington?").lower()
        print("You entered:",city,", thank you.")
    except KeyError:
            print("Error occurred")
	
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april" , "may", "june", "all"]
    try:
        month = input("Which month would you like to look at: January, February, March, April, May, June or 'all'?").lower()
        while (month not in months):
            print('You entered',month,'. Please enter one of the available options.')
            month = input("Please choose one of the following: January, February, March, April, May, June or 'all' ").lower()
        print("You entered: ",month,", thank you.")
    except KeyError:
            print ('Error occurred')
	
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)	
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    try:
        day = input ("Which weekday would you like to look at: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or 'all'? ").lower()
        while (day not in days):
            print("You entered",day,". Please enter one of the available options.")
            day = input("Please choose one of the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or 'all' ").lower()
        print("You selected",day,", thank you.")
    except KeyError:
        print('Error occurred')
    print('-'*40)
    return city, month, day  
   
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
	
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"]= pd.to_datetime(df["Start Time"])
    df["year"]= df["Start Time"].dt.year
    df["month"]= df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df=df[df['month'] == month]
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel for a selected city."""
    print("\n Calculating The most frequent times of travel...\n")
    start_time = time.time()
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    common_month = df["month"].mode()[0]
    print("The most common month of travel:", common_month)
    
    # TO DO: display the most common day of week
    df["day_of_week"] = df["Start Time"].dt.day_name()
    common_day_of_week = df["day_of_week"].mode()[0]
    print("The most common day of week of travel:",common_day_of_week)
    
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("The most common hour of travel:",common_hour)
    print("\nThis took %s seconds." %round((time.time() - start_time),3))
    print("-"*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\nCalculating the most popular Stations and Trip...\n")
    start_time = time.time()
    common_start = df["Start Station"].mode()[0]
    print(common_start)
	
    # TO DO: display most commonly used end station
    common_end = df["End Station"].mode()[0]
    print(common_end)
	
    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"] + df["End Station"]
    common_combination = df ["combination"].mode()[0]
    print(common_combination)
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print("-"*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("\nTotal travel time: %s."%str(datetime.timedelta(seconds = int(total_travel_time))))
	
    # TO DO: display mean travel time 
    average_travel_time = df["Trip Duration"].mean()
    print('\nAverage travel time: %s.'%str(datetime.timedelta(seconds = average_travel_time)))
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print("-"*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\nCalculating User statistics...\n")
    start_time = time.time()
    # TO DO: Display counts of user types
    count_user_types = df["User Type"].value_counts()
    print("Number of users by type:\n",count_user_types)
    
    # TO DO: Display counts of gender
    try:
        count_gender = df["Gender"].value_counts()
        print()
        print("Count of genders:\n", count_gender)
    except KeyError:
        print("No data is available for this selection.")    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = df["Birth Year"].min()
        earliest_year = int(earliest_birthyear)
        print()
        print("The earliest year of birth:", earliest_year)
        most_recent_year = df["Birth Year"].max()
        recent_year = int(most_recent_year)
        print()
        print("The most recent year of birth:", recent_year)
        most_common_birth = df["Birth Year"].mode()[0]
        common_birth = int(most_common_birth)
        print()
        print("The most common year of birth:", common_birth)
    except KeyError:
        print('No data is available for this selection')
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print("-"*40)
	
def view_chosen_data(df):
    viewer_choice = input("\nWould you like to see 5 rows of trip data? Type yes or no: \n").lower()
    choices = ["yes"]
    view_steps = 0
    while (viewer_choice in choices):
        print(df.iloc[view_steps:view_steps+5])
        view_steps += 5
        viewer_choice = input("Do you want to continue?:").lower()
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_chosen_data(df)
        restart = input("\n Do you want to restart the script? Type yes or no.\n")
        if restart.lower() != "yes":
            break
if __name__ == "__main__":
	main()