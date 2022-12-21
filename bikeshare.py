import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    print( '================== Hello! ================== ' )
    print('==================Bike Share data analysis project==================')
    print( '=' * 100 )


    print( '==================Do you want To see the Data set ?==================' )



    print( '==================We are going to explore the reasults of analysing US bikeshare data==================' )
    print( '=' * 100 )


    city = ''
    while (True):
        if (city == 'chicago' or city == 'new york city' or city == 'washington'):
            break
        else:
            city = input( 'Would you like to see data for Chicago, New york city, Washington' ).lower()

    choice = ''
    while (True):
        if (choice == 'month' or choice == 'day' or choice == 'both' or choice == 'none'):
            break
        else:
            choice = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.' ).lower()

    month = 'none'
    day = 0


    if (choice == 'both' or choice == 'month'):
        while (True):
            if (
                    month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june'):
                break
            else:
                month = input( 'Which month? January, February, March, April, May or June?' ).lower()
    if (choice == 'both' or choice == 'day'):
        while (True):
            if (day >= 1 and day <= 7):
                break
            else:
                day = int( input( 'Which day? Please type your response as an integer e.g: 1 = sunday.' ) )

    print( '=' * 100 )
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv( CITY_DATA[city.lower()] )


    df['Start Time'] = pd.to_datetime( df['Start Time'] )
    df['End Time'] = pd.to_datetime( df['End Time'] )

    df['Hour'] = df['Start Time'].dt.hour

    df['Month'] = df['Start Time'].dt.month

    df['Day of week'] = df['Start Time'].dt.day_name()

    if (month != 'none'):
        months_of_year = ['january', 'february', 'march', 'april', 'may', 'june']
        index_of_month = months_of_year.index( month ) + 1
        df = df[df['Month'] == index_of_month]


    if (day != 0):
        day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        index_of_day = day_of_week[day - 1]
        df = df[df['Day of week'] == index_of_day]

    return df


def time_stats(df):
    print( '=' * 100 )
    print('=============================1- Popular times of travel=============================')
    print( '=====================Displays statistics on the most frequent times of travel.====================' )
    print( '=' * 100 )
    print( '\nCalculating The Most Frequent Times of Travel...\n' )
    start_time = time.time()


    print( '=' * 100 )
    print( 'Most common month:            :', df['Month'].value_counts().index[0] )
    print( 'Most common day of week:      :', df['Day of week'].value_counts().index[0] )
    print( 'Most common start hour:       :', df['Hour'].value_counts().index[0] )

    print( "\nThis took %s seconds." % (time.time() - start_time) )
    print( '=' * 100 )


def station_stats(df):
    print( '=============================2- Popular stations and trip=============================' )
    print( '=====================Displays statistics on the most popular stations and trip.====================' )
    print( '=' * 100 )
    print( '\nCalculating The Most Popular Stations and Trip...\n' )

    start_time = time.time()
    print( 'Most common start station:              :', df['Start Station'].value_counts().index[0] )
    print( 'Most common end station:                :', df['End Station'].value_counts().index[0] )

    print(
        pd.DataFrame( df.groupby( ['Start Station', 'End Station'] ).size().sort_values( ascending=False ) ).iloc[0] )

    print( "\nThis took %s seconds." % (time.time() - start_time) )
    print( '=' * 100 )

def printName():
    print("Sarah Alqahtani")
    
def word():
    print("i love Udacity Programm")


def trip_duration_stats(df):
    print( '=============================3-  Trip duration=============================' )
    print( '=====================Displays statistics on the total and average trip duration.====================' )
    print( '=' * 100 )
    print( '\nCalculating Trip Duration...\n' )
    start_time = time.time()

    print( 'Total travel time: ', df['Trip Duration'].sum() )
    print( 'Mean travel time: ', df['Trip Duration'].mean() )
    print( "\nThis took %s seconds." % (time.time() - start_time) )
    print( '=' * 100 )



def user_stats(df, city):
    print( '=============================4-  User info=============================' )
    print( '=========================Displays statistics on bikeshare users.====================================' )
    print( '=' * 100 )
    print( '\nCalculating User Stats...\n' )
    start_time = time.time()

    print( 'Counts of user types: ', df['User Type'].value_counts() )

    if (city == 'Chicago' or city == 'New york city'):

        print( 'Counts of gender: ', df['Gender'].value_counts() )
        print( 'Most earliest year of birth: ', df['Birth Year'].sort_values().iloc[0] )
        print( 'Most recent year of birth: ', df['Birth Year'].sort_values( ascending=False ).iloc[0] )
        print( 'Most common year of birth', df['Birth Year'].value_counts().index[0] )

    print( "\nThis took %s seconds." % (time.time() - start_time) )
    print( '=' * 100 )


def main():
    while True:
        city, month, day = get_filters()
        df = load_data( city, month, day )

        #print( df.columns.values )
        #print(df.iloc[0, 0:3])

        Display_data = input( '\nWould you like To see 5 Rws of the Data set ? Enter yes or no.\n' )

        if Display_data.lower() != 'no':
            start_loc = 0
            keep_asking = True
            while (keep_asking):
                print( df.iloc[start_loc:start_loc + 5] )
                start_loc += 5
                view_display = input( "Do you wish to continue?: " ).lower()
                if view_display == "no":
                    keep_asking = False

        print( '=' * 100 )
        Display_data = input( '\nWould you like To see Analysis reasult of the data ? Enter yes or no.\n' )
        if Display_data.lower() != 'no':
            time_stats( df )
            station_stats( df )
            trip_duration_stats( df )
            user_stats( df, city )



        restart = input( '\nWould you like to restart? Enter yes or no.\n' )
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
