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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input = ""
    while city_input.lower() not in CITY_DATA:
        city_input = input('\nWhich City You Would like To See Data for?(e.g. chicago, new york city, washington)\n')
        if city_input.lower() in CITY_DATA:
            city = CITY_DATA[city_input.lower()]
        else:
            print('\nPlease Enter city From (chicago, new york city, washington)\n')


    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month_input = ''
    while month_input.lower() not in months:
        month_input = input('\nWhich Month You Want To Filter By?(e.g. all or january, february, ... , june)\n')
        if month_input.lower() in months:
            month = month_input.lower()
        else:
            print('\nPlease Enter Month From january, february, ... , june Or all\n')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday','saturday', 'sunday']
    day_input = ''
    while day_input.lower() not in days:
        day_input = input('\nWhich Day You Want To Filter By?(e.g. all or monday, tuesday, ... sunday)\n')
        if day_input.lower() in days:
            day = day_input.lower()
        else:
            print('\nPlease Enter Day From monday, tuesday, ... sunday Or all')


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
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The Most Frequent Month Used By Bikeshare Users is:', most_common_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The Most Frequent Day Of Week Used By Bikeshare Users is:', most_common_day)

    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The Most Frequent Hour Used By Bikeshare Users is:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    print('The Most Popular Start Station Used By Bikeshare Users is:', top_start_station)

    # display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    print('The Most Popular End Used Station By Bikeshare Users is:', top_end_station)

    # display most frequent combination of start station and end station trip
    df['Start Station & End Station'] = df['Start Station'] + " And " + df['End Station']
    top_combination = df['Start Station & End Station'].mode()[0]
    print('The Most Popular Combination of Start And End Stations Used By Bikeshare Users is:', top_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('The Total Travel Time Spent By Bikeshare Users is:', total_time, 'seconds')

    # display mean travel time
    average_time = df['Trip Duration'].mean()
    print('The Average Travel Time Spent By Bikeshare Users is:', average_time, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_types_count = df['User Type'].value_counts()
    print('The Count Of User Types is:', dict(users_types_count))

    # Display counts of gender
    if city == 'new_york_city.csv' or city == 'chicago.csv':
        gender_count = df['Gender'].value_counts()
        print('The Count Of Gender is:', dict(gender_count))

        # Display earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('The Earliest Year Of Birth is:', int(earliest_birth_year))

        # Display most recent year of birth
        latest_birth_year = df['Birth Year'].max()
        print('The Most Recent Year Of Birth is:', int(latest_birth_year))

        # Display most common year of birth
        most_common_birth = df['Birth Year'].mode()[0]
        print('The Most Common Year Of Birth is:', int(most_common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    # Display 5 lines of raw data
    lines = 0
    while True:
        user_input = input('\nDo you Want To See 5 Lines Of Raw Data? Enter yes or no.\n')
        if user_input.lower() == 'yes':
            print(df[lines:lines + 5])
            lines += 5
        elif user_input.lower() not in ['yes', 'no']:
            print('\nPlease Respond With yes or no')
        else:
            break

    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
