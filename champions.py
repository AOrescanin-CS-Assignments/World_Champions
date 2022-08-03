#****************************************************************************************************
#
#       Name:         Alex Orescanin
#       Course:        COSC 2110 Computer Languages: Python
#       Assignment:   champions.py
#       Due Date:     10/09/2020
#       Description:
#               This program reads a file of world series winners and put them in a dictionary
#
#****************************************************************************************************

VIEW = 1
VIEW_ALL = 2
DELETE = 3
CHANGE = 4
QUIT = 5
LINE = 50
FILENAME = 'WorldSeriesWinners.txt'

def main():
    keep_going = 0
    teams_list = loadTeams()
    team_dict = get_dict(teams_list)

    while keep_going != QUIT:
        keep_going = get_user_choice()

        if keep_going == VIEW:
            team_name = input("Enter a team's name: ")
            print(team_dict.get(team_name, 'That team has not won the world series'))

        elif keep_going == VIEW_ALL:
            display(team_dict)

        elif keep_going == DELETE:
            team_name = input("Enter a team's name: ")
            if team_name in team_dict:
                del team_dict[team_name]
                print(team_name, 'were deleted')
            else:
                print(team_name, 'is not in list')

        elif keep_going == CHANGE:
            team_name = input("Enter a team's name: ")
            if team_name in team_dict:
                new_set = set([input('Enter new winning year(s): ')])
                del team_dict[team_name]
                team_dict[team_name] = new_set
                print(team_name, 'changed')
            else:
                print(team_name, 'is not in list')

    print('Goodbye')

#****************************************************************************************************

def loadTeams():
    teams_list = []

    try:
        team_file = open(FILENAME, 'r')
        teams = team_file.readline()

        while teams != '':
            teams = teams.rstrip('\n')
            teams_list.append(teams)
            teams = team_file.readline()

        team_file.close()
    except IOError:
        print('File not found')

    return teams_list

#****************************************************************************************************

def get_user_choice():
    print('\nMenu')
    print('-' * LINE)
    print("1. View a team's info\n2. View all team's info\n"
          "3. Delete a team's info\n4. Change a team's info\n5. Quit")

    choice = int(input('Please select an option: '))

    while choice < VIEW or choice > QUIT:
        choice = int(input('Invalid option, please re-enter: '))

    return choice

#****************************************************************************************************

def get_dict(teams_list):
    year = 1903
    team_dict = {}

    for team in teams_list:
        if team in team_dict:
            team_dict[team].add(year)
        else:
            team_dict[team] = set([year])

        year += 1

    return team_dict

#****************************************************************************************************

def display(team_dict):
    for key, value in team_dict.items():
        count = 0

        if key != 'none':
            print(key, ':')

            for year in team_dict[key]:
                print(year, end=' ')

                if (count + 1) % 8 == 0:
                    print('\n')

                count += 1

        print('\n')

#****************************************************************************************************

if __name__ == '__main__':
    main()

#****************************************************************************************************
# Sample Output:
# --------------------------------------------------
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Please select an option: 1
# Enter a team's name: Chicago Cubs
# {1907, 1908}
# --------------------------------------------------
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Please select an option: 4
# Enter a team's name: Chicago Cubs
# Enter new winning year(s): 1909 1910
# Chicago Cubs changed
# --------------------------------------------------
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Please select an option: 2
# Boston Americans :
# 1903
#
#
#
# New York Giants :
# 1921 1954 1922 1933 1905
#
# Chicago White Sox :
# 2005 1906 1917
#
# Pittsburgh Pirates :
# 1925 1960 1971 1909 1979
#
# Philadelphia Athletics :
# 1929 1930 1910 1911 1913
#
# Boston Red Sox :
# 2004 2007 1912 1915 1916 1918
#
# Boston Braves :
# 1914
#
# Cincinnati Reds :
# 1990 1940 1975 1976 1919
#
# Cleveland Indians :
# 1920 1948
#
# New York Yankees :
# 1923 1927 1928 1932 1936 1937 1938 1939
#
# 1941 1943 1947 1949 1950 1951 1952 1953
#
# 1956 1958 1961 1962 1977 1978 1996 1998
#
# 1999 2000
#
# Washington Senators :
# 1924
#
# St. Louis Cardinals :
# 1926 1931 1964 1934 1967 1942 2006 1944
#
# 1946 1982
#
# Detroit Tigers :
# 1968 1945 1984 1935
#
# Brooklyn Dodgers :
# 1955
#
# Milwaukee Braves :
# 1957
#
# Los Angeles Dodgers :
# 1988 1959 1963 1965 1981
#
# Baltimore Orioles :
# 1970 1966 1983
#
# New York Mets :
# 1969 1986
#
# Oakland Athletics :
# 1989 1972 1973 1974
#
# Philadelphia Phillies :
# 2008 1980
#
# Kansas City Royals :
# 1985
#
# Minnesota Twins :
# 1987 1991
#
# Toronto Blue Jays :
# 1992 1993
#
# Atlanta Braves :
# 1995
#
# Florida Marlins :
# 2003 1997
#
# Arizona Diamondbacks :
# 2001
#
# Anaheim Angels :
# 2002
#
# Chicago Cubs :
# 1909 1910
#
# --------------------------------------------------
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Please select an option: 3
# Enter a team's name: Chicago Cubs
# Chicago Cubs were deleted
# --------------------------------------------------
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Please select an option: 2
# Boston Americans :
# 1903
#
#
#
# New York Giants :
# 1921 1954 1922 1933 1905
#
# Chicago White Sox :
# 2005 1906 1917
#
# Pittsburgh Pirates :
# 1925 1960 1971 1909 1979
#
# Philadelphia Athletics :
# 1929 1930 1910 1911 1913
#
# Boston Red Sox :
# 2004 2007 1912 1915 1916 1918
#
# Boston Braves :
# 1914
#
# Cincinnati Reds :
# 1990 1940 1975 1976 1919
#
# Cleveland Indians :
# 1920 1948
#
# New York Yankees :
# 1923 1927 1928 1932 1936 1937 1938 1939
#
# 1941 1943 1947 1949 1950 1951 1952 1953
#
# 1956 1958 1961 1962 1977 1978 1996 1998
#
# 1999 2000
#
# Washington Senators :
# 1924
#
# St. Louis Cardinals :
# 1926 1931 1964 1934 1967 1942 2006 1944
#
# 1946 1982
#
# Detroit Tigers :
# 1968 1945 1984 1935
#
# Brooklyn Dodgers :
# 1955
#
# Milwaukee Braves :
# 1957
#
# Los Angeles Dodgers :
# 1988 1959 1963 1965 1981
#
# Baltimore Orioles :
# 1970 1966 1983
#
# New York Mets :
# 1969 1986
#
# Oakland Athletics :
# 1989 1972 1973 1974
#
# Philadelphia Phillies :
# 2008 1980
#
# Kansas City Royals :
# 1985
#
# Minnesota Twins :
# 1987 1991
#
# Toronto Blue Jays :
# 1992 1993
#
# Atlanta Braves :
# 1995
#
# Florida Marlins :
# 2003 1997
#
# Arizona Diamondbacks :
# 2001
#
# Anaheim Angels :
# 2002
#
# --------------------------------------------------
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Please select an option: 5
# Goodbye
#****************************************************************************************************