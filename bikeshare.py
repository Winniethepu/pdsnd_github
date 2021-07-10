import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data from Chicago,New York City or Washington?')
    city=input()
    while city.lower() not in CITY_DATA.keys():
        print('Please choose a city in the following list: chicago,new york city and washington.')
        city=input()

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Would you like to filter the data by month or not at all? Pleaset type \'all\' for no time filter.')
    month=input()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Would you like to filter the data by weekday or not at all? Pleaset type \'all\' for no time filter.')
    day=input()
    """
    Input Augments must be Roman Number.

    """
    print('-'*40)
    return city, month, day

    if city=='Washintong' and month=='7':
        print('We currently don\'t have this data, would you like to choose another city or a different time?' )


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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    if month!='all':
        months=['January','Febrauary','March','April','May','June','July','August','September','Octber','November','December']
        month=months.index(month.title())+1
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print('Most common month is:',most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week=df['day_of_week'].mode()[0]
    print('Most common day of week is:',most_common_day_of_week)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_popular_hour=df['hour'].mode()[0]
    print('Most popular hour is:',most_popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('Most commonly used start station is:',start_station)

    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('Most commonly used end station is:',end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_popular_station_combination=df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most frequent combination of stations is:',most_popular_station_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total trave time is:',total_travel_time)
    # TO DO: display mean travel time
    average_travel_time=df['Trip Duration'].mean()
    print('The average trave time is:',average_travel_time)

    print("\nThis took %s seconds.\n '_'*40" % (time.time() - start_time))



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts=df['User Type'].value_counts()
    print('Subscriber:',user_type_counts['Subscriber'])
    print('Customer:',user_type_counts['Customer'])
    print('\n')

    # TO DO: Display counts of gender
    gender_counts=df['Gender'].value_counts()
    print('Male:',gender_counts['Male'])
    print('Female:',gender_counts['Female'])

 # TO DO: Display earliest, most recent, and most common year of birth

    earlist_year_of_birth=df['Birth Year'].min()
    most_recent_year_of_birth=df['Birth Year'].max()
    most_common_year_of_birth=df['Birth Year'].mode()[0]
    print('Earliest year of birth:',earlist_year_of_birth)
    print('Most recent year of birth:',most_recent_year_of_birth)
    print('Most common year of birth:',most_common_year_of_birth)



    print("\nThis took %s seconds.\n '_'*40" % (time.time() - start_time))



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
