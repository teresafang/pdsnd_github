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
    while True:
        city = input('Enter the city (chicago, new york city, washington) you\'d like the bikeshare data for: ').lower().strip()
        if city == "stop":
            import sys
            sys.exit(0)
        elif city not in CITY_DATA.keys():
            print('Please enter a valid US city. To quit, enter stop.')
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the month you\'d like the bikeshare data for: ').lower().strip()
        if month == "stop":
            import sys
            sys.exit(0)
        elif month not in ["january", "february", "march", "april", "may", "june", "all"]:
            print('Please enter a valid month. To quit, enter stop.')
            continue
        else: 
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day of week you\'d like the bikeshare data for: ').lower().strip()
        if day == "stop":
            import sys
            sys.exit(0)
        elif day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            print('Please enter a valid day of week. To quit, enter stop.')
            continue
        else: 
            break

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

    df = pd.read_csv(city.replace(' ', '_') + ".csv")
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week' ] = df['Start Time'].dt.weekday_name
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

    # TO DO: display the most common month
    df['Start Time Month'] = pd.to_datetime(df['Start Time']).dt.month
    common_month = df['Start Time Month'].value_counts().idxmax()
    
    if common_month == 1:
        print('The most frequent month of travel is: January \n')
    elif common_month == 2:
        print('The most frequent month of travel is: February \n')
    elif common_month == 3:
        print('The most frequent month of travel is: March \n')
    elif common_month == 4:
        print('The most frequent month of travel is: April \n')
    elif common_month == 5:
        print('The most frequent month of travel is: May \n')
    elif common_month == 6:
        print('The most frequent month of travel is: June \n')


    # TO DO: display the most common day of week
    df['Start Time Day'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    common_day = df['Start Time Day'].value_counts().idxmax()
    if common_day == 0:
        print('The most frequent day of travel is: Monday \n')
    elif common_day == 1:
        print('The most frequent day of travel is: Tuesday \n')
    elif common_day == 2:
        print('The most frequent day of travel is: Wednesday \n')
    elif common_day  == 3:
        print('The most frequent day of travel is: Thursday \n')
    elif common_day  == 4:
        print('The most frequent day of travel is: Friday \n')
    elif common_day  == 5:
        print('The most frequent day of travel is: Saturday \n')
    elif common_day  == 6:
        print('The most frequent day of travel is: Sunday \n')


    # TO DO: display the most common start hour
    df['Start Time Hour'] = pd.to_datetime(df['Start Time']).dt.hour
    common_hour = df['Start Time Hour'].value_counts().idxmax()
    if common_hour < 12:
        print('The most frequent hour of travel is: {} AM \n'.format(common_hour))
    elif common_hour >=12:
        print('The most frequent hour of travel is: {} PM \n'.format(common_hour % 12))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: {}\n'.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: {}\n'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combo'] = df['Start Station'] + ' & ' + df['End Station']
    station_combo = df['Station Combo'].value_counts().idxmax()
    print('The most frequent combination of start station and end station is: {}\n'.format(station_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('The total travel time is: {} seconds'.format(total_duration))

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('The mean travel time is: {} seconds'.format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
  
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df.groupby(['User Type']).size().reset_index(name='Count'), '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print(df.groupby(['Gender']).size().reset_index(name='Count'))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('The earliest year of birth is: {} \n'.format(df['Birth Year'].min().astype(int)))
        print('The most recent year of birth is: {} \n'.format(df['Birth Year'].max().astype(int)))
        print('The most common year of birth is: {} \n'.format(df['Birth Year'].value_counts().idxmax().astype(int)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
        
        start_row = 0
        end_row = 5
        
        if raw_data.lower() == 'yes':
            print(df.iloc[start_row:end_row])
            see_more = input('\n Would you like to see more raw data? Enter yes or no.\n')
            while see_more.lower() == 'yes':
                start_row += 5
                end_row += 5
                print(df.iloc[start_row:end_row])
                see_more = input('\n Would you like to see more raw data? Enter yes or no.\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
