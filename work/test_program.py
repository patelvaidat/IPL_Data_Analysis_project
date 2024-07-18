import os

import warnings

# import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

warnings.filterwarnings('ignore')
sns.set_style('darkgrid')

clear = lambda: os.system('cls')

global del_df
del_df=pd.read_csv("./input/deliveries.csv")

global match_df
match_df = pd.read_csv("./input/matches.csv")


def menu_1():
        #Menu 1
        print('\t[1-1] What is IPL?')
        print('\t[1-2] Contents of this Project\n')
        global option_1
        option_1=(input('Enter your option: '))
        option_1 = option_1

def menu_1_options():
        if option_1 == '1-1':
            option_1_1()
            # break
        elif option_1 == '1-2':
            option_1_2()
            # break

#Option 1.1 of Option 1
def option_1_1():
    #Option 1>>1.1
    print('\nThe Indian Premier League (IPL) is a professional Twenty20 cricket league, contested by eight teams based out of eight different Indian cities. The league was founded by the Board of Control for Cricket in India (BCCI) in 2007. It is usually held between March and May of every year and has an exclusive window in the ICC Future Tours Programme.\n\nThe IPL is the most-attended cricket league in the world and in 2014 was ranked sixth by average attendance among all sports leagues. In 2010, the IPL became the first sporting eventin the world to be broadcast live on YouTube. The brand value of the IPL in 2019 was 475 billion (US$6.7 billion), according to Duff & Phelps. According to BCCI, the 2015 IPL seasoncontributed 11.5 billion (US$160 million) to the GDP of the Indian economy.')
#option_1_1()

#Option 1.2 of Option 1
def option_1_2():
    #Option 1>>1.2
    print('\nThis is an IPL Data Analysis Program. Using this program, you can:\n\n\t1.View the source files of the program.\n\t2.View specific enteries of the program via specific constraints.\n\t3.Analyse the data by teams and matches played.\n\t4.View the visual Representations of specific aspects of the matches')
# option_1_2()

def menu_2():
    #Menu 2
    print('\n\t[2-1] Read file containing all data regarding matches (2008-2019)\n')
    print('\t[2-2] Read file containing all data regarding specific match deliveries (2008-2019)\n')
    global option_2
    option_2 = (input('Enter the option: '))
    option_2 = option_2

def menu_2_options():
        if option_2 == '2-1':
            option_2_1()
        elif option_2 == '2-2':
            option_2_2()
        elif option!= '2-1' or '2-2':
            clear()
            print('Input entered is invalid. Enter valid input.')
            menu_2()
            menu_2_options()

#Option 2.1 of Option 2
def option_2_1():
    #Option 2>>2.1
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print('\n',match_df)
# option_2_1()

#Option 2.2 of Option 2
def option_2_2():
    #Option 2>>2.2
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print('\n',del_df)
# option_2_2()


def menu_3():
    #Menu 3
    print('\n[3] Data Manipulation\n')
    print('\t[3-1] Display specific column')
    print('\t[3-2] Display specific row')
    print('\t[3-3] Display desired range of columns')
    print('\t[3-4] Display desired range of rows\n')
    global option_3
    option_3 = input('Enter the option: ')
    option_3 = option_3

global list_3
list_3=['3-1','3-2','3-3','3-4'] 

def menu_3_options():
        if option_3 == '3-1':
            option_3_1()
        elif option_3 == '3-2':
            option_3_2()
        elif option_3 == '3-3':
            option_3_3()
        elif option_3 == '3-4':
            option_3_4()
        elif option_3 not in list_3:
            clear()
            print('Input entered is invalid. Enter valid input.')
            menu_3()
            menu_3_options()

global x
x = match_df.columns.unique()
global y
y = match_df.index

#Option 3.1 of Option 3
def option_3_1():
    print ('\n',x,'\n')
    column_name=input('\nEnter the column name: ')
    if column_name in x:
        print(match_df[x])

    else:
        clear()
        print('Invalid column name. Please  enter valid column name again\n')
        option_3_1()
# option_3_1()

#Option 3.2 of Option 3
def option_3_2():
    print ('[',y.min(),',',y.max(),']')
    row_name=int(input('Enter any row number between these 2 numbers:'))
    if row_name in y:
        print('All details regarding the row number',row_name,':\n',match_df.loc[row_name])
    elif row_name not in y:
        clear()
        print('Invalid row number. Please  enter valid column name again\n')
        option_3_2()
# option_3_2()

#Option 3.3 of Option 3
def option_3_3():
    print(x)
    column_name_start=input('Enter the starting column range name:')
    column_name_end=input('Enter the ending column range name:')
    if column_name_start and column_name_end in x:
        print('All details regarding the range of columns from',column_name_start,'to',column_name_end,'are:\n',match_df.loc[:,column_name_start:column_name_end])
    elif column_name_start or column_name_end not in x:
        clear()
        print('\nInvalid input entered. Please enter valid input\n')
        option_3_3()
    elif column_name_start and column_name_end not in x:
        clear()
        print('\nInvalid input entered. Please enter valid input\n')
        option_3_3()
# option_3_3()

#Option 3.4 of Option 3
def option_3_4():
    print ('[',y.min(),',',y.max(),']')
    row_range_start = int(input('Enter the starting row range number:'))
    row_range_end = int(input('Enter the ending row range number:'))
    if row_range_start  and row_range_end in y:
        print('All details regarding the range of rows from',row_range_start,'to',row_range_end,'are:\n',match_df.loc[row_range_start:row_range_end])
    elif row_range_start or row_range_end not in x:
        clear()
        print('\nInvalid input entered. Please enter valid input\n')
        option_3_4()
    elif row_range_start and row_range_end not in x:
        clear()
        print('\nInvalid input entered. Please enter valid input\n')
        option_3_4()
# option_3_4()


def menu_4():
    #Menu 4
    print('\n\t[4-1] Top 10 winning teams based on runs')
    print('\t[4-2] Top 15 winning teams based on wickets')
    print('\t[4-3] Teams won by highest number of runs')
    print('\t[4-4] Teams won by highest number of wickets')
    print('\t[4-5] Man of the match winners & the number of times title won in IPL (2008-2019)')
    print('\t[4-6] Top 15 man of the match winners & the number of times title won in (IPL 2008-2019)\n')

    global option_4
    option_4 = input('Enter the option: ')
    option_4 = option_4

global list_4
list_4=['4-1','4-2','4-3','4-4','4-5','4-6']

def menu_4_options():
        if option_4 == '4-1':
            option_4_1()
        elif option_4 == '4-2':
            option_4_2()
        elif option_4 == '4-3':
            option_4_3()
        elif option_4 == '4-4':
            option_4_4()
        elif option_4 == '4-5':
            option_4_5()
        elif option_4 == '4-6':
            option_4_6()
        elif option_4 not in list_4:
            clear()
            print('Input entered is invalid. Enter valid input.')
            menu_4()
            menu_4_options()


#Option 4.1 of Option 4
def option_4_1():
    match_df_=match_df.sort_values('win_by_runs',ascending=False)
    top_10 = match_df_[['winner','win_by_runs']].head(10)
    print ('\nTop 10 winning teams based on win by runs\n')
    print (top_10)
# option_4_1()

#Option 4.2 in Option 4
def option_4_2():
    global top_15
    global match_df__
    match_df__=match_df.sort_values('win_by_wickets',ascending=False)
    top_15 = match_df__[['winner','win_by_wickets']].head(15)
    print ('\nTop 15 winning teams based on win by wickets\n')
    print (top_15,'\n')
# option_4_2()

#Option 4.3 in Option 4
def option_4_3():
    highest_runs=match_df['win_by_runs'].max()
    print ('\nHighest win_by-runs score and the winning team\n')
    print ('Highest number of runs: ',highest_runs)
    highest = match_df[match_df['win_by_runs']==highest_runs]
    print ('Name of team: ',(highest['winner']).to_string(index=False))
    print('\n',highest)
    # print(match_df.loc[highest])
# option_4_3()

#Option 4.4 of Option 4 (Modified under sequence)
def option_4_4():
    match_df_=match_df.sort_values('win_by_wickets',ascending=False)
    top_10_ = match_df_[['winner','win_by_wickets']].head(10)
    print ('\nTop 10 winning teams based on win by wickets\n')
    print (top_10_,'\n')
# option_4_4()

#Option 4.5 of Option 4 (Modified under sequence)
def option_4_5():
    print ('\nMan of the match winners & the number of times title won in IPL (2008-2019)')
    print ('\n===========================================================================\n')
    # print ('===========================================================================================================================================')
    freq={}
    man_of_match=list(match_df['player_of_match'])
    for items in man_of_match:
        freq[items]=man_of_match.count(items)
    player=[]
    times=[]
    dict={'Name':player,'title':times}
    # print (dict)
    for key,value in freq.items():
        player.append(key)
        times.append(int(value))
    player_of_match = pd.DataFrame(dict,index=player)
    player_of_match = player_of_match.sort_values('title',ascending=False).reset_index()
    del player_of_match['index']
    # print (dict)
    print(player_of_match,'\n')
# option_4_5()

#Option 4.6 of Option 4 (Modified under sequence)
def option_4_6():
    print ('\nTop 15 "Man of the Match" winners & the number of times title won in IPL (2008-2019)')
    print ('====================================================================================')
    # print ('===========================================================================================================================================')
    freq={}
    man_of_match=list(match_df['player_of_match'])
    for items in man_of_match:
        freq[items]=man_of_match.count(items)
    player=[]
    times=[]
    dict={'Name':player,'title':times}
    # print (dict)
    for key,value in freq.items():
        player.append(key)
        times.append(int(value))
    player_of_match = pd.DataFrame(dict,index=player)
    player_of_match = player_of_match.sort_values('title',ascending=False).head(15).reset_index()
    del player_of_match['index']
    # print (dict)
    print(player_of_match,'\n')
# option_4_6()


def menu_5():
    #Menu 5
    print('\t[5-1] Matches by number of wickets; user defined')
    print('\t[5-2] Matches by number of runs; user defined')
    print('\t[5-3] Matches declared as tie')
    print('\t\t[5-4-1] Matches won by the team entered; user defined (Please enter the correct team name from the numpy array.\n\t\t\tOtherwise there will be no proper record-wise utput)')
    print('\t\t[5-4-2] Matches won by selected team with win by wickets')
    print('\t\t[5-4-3] Matches won by selected team with win by runs')


    global option_5
    option_5 = (input('\nEnter the option: '))
    option_5 = option_5

global list_5
list_5=['5-1','5-2','5-3','5-3-1','5-3-2','5-3-3']

def menu_5_options():
        if option_5 == '5-1':
            option_5_1()
        elif option_5 == '5-2':
            option_5_2()
        elif option_5 == '5-3':
            option_5_3()
        elif option_5 == '5-4-1':
            option_5_4_1()
        elif option_5 == '5-4-2':
            option_5_4_2()
        elif option_5 == '5-4-3':
            option_5_4_3()
        elif option_5 not in list_5:
            clear()
            print('Input entered is invalid. Enter valid input.')
            menu_5()
            menu_5_options()


global mi
global mi_toset_runs
global match_df_win_by_runs_reset_index_win_by_runs
global num_runs
match_df_win_by_runs_reset_index = match_df['win_by_runs'].reset_index()
ni = match_df['win_by_wickets'].reset_index()
match_df_win_by_wickets = ni['win_by_wickets']
match_df_win_by_runs_reset_index_win_by_runs = match_df_win_by_runs_reset_index['win_by_runs']
mi_toset_runs = set(match_df_win_by_runs_reset_index_win_by_runs)
mi_toset_wickets = set(match_df_win_by_wickets)

#Option 5.1 of Option 5
def option_5_1():
    try:
        print(mi_toset_wickets)
        # print('[',match_df['win_by_wickets'].min(),',',match_df['win_by_wickets'].max(),']')
        num_wickets = int(input("Enter any number of wickets from the above numbers by which winning team won: "))
        # print(num_wickets)
        # print(type(num_wickets))
        if type(num_wickets)==int and (num_wickets in mi_toset_wickets):
            custom_runs=match_df[match_df['win_by_wickets'] ==num_wickets]
            print(custom_runs[['team1','team2','winner','win_by_wickets']],'\n')

        elif type(num_wickets)==int and (num_wickets not in mi_toset_wickets):
            clear()
            print ('Value not in range.\nPlease input value between:')#,'[',match_df['win_by_wickets'].min(),',',match_df['win_by_wickets'].max()   ,']')
            option_5_1()
        else: #type(num_wickets)!=int
            clear()
            print ('Invalid Input.\nPlease enter integer input value')#,'[',match_df['win_by_wickets'].min(),',',match_df['win_by_wickets'].max(),']'#)
            option_5_1()
    except ValueError:
        clear()
        print ('Invalid Input.\nPlease enter integer input value')#,mi_toset_wickets)
        option_5_1()
# option_5_1()

#Option 5.2 of Option 5
def option_5_2():
    try:
        print(mi_toset_runs)
        # print('[',match_df['win_by_runs'].min(),',',match_df['win_by_runs'].max(),']')
        num_runs = int(input("Enter any number of runs from the above numbers by which winning team won: "))
        # print(num_runs)
        # print(type(num_runs))
        if type(num_runs)==int and (num_runs in mi_toset_runs):
            custom_runs=match_df[match_df['win_by_runs'] ==num_runs]
            print(custom_runs[['team1','team2','winner', 'win_by_runs']],'\n')

        elif type(num_runs)==int and (num_runs not in mi_toset_runs):
            print ('Value not in range.\nPlease input value between: ','[',match_df['win_by_runs'].min(),',',match_df['win_by_runs'].max(),']')
            option_5_2()
        else: #type(num_runs)!=int
            clear()
            print ('Invalid Input.\nPlease enter integer input value between: ','[',match_df['win_by_runs'].min(),',',match_df['win_by_runs'].max(),']')
            option_5_2()
    except ValueError:
        clear()
        # print ('dfsdfsdfsdfsdfsdfsdfsdfsd')
        print ('Invalid Input.\nPlease enter integer input value between: ',mi_toset_wickets)
# option_5_2()

#Option 5.3 of Option 5
def option_5_3():
    print('\nMatches declared as tie\n')
    tie_match=match_df[match_df['result']=='tie']
    tie_match
    tie_match.iloc[:,1:9]
    print(tie_match.iloc[:,1:9])
# option_5_3()

match_df_team1_unique=match_df['team1'].unique()

#Option 5.4.1 of Option 5
global team_df_1
def option_5_4_1():
    print (match_df_team1_unique,'\n')
    print('Matches won by the team entered; user defined\n')
    global team_input_1
    team_input_1=input('Enter a team name: ')
    print ('==================')
    try:
        if team_input_1 in match_df_team1_unique:
            team_df_1=match_df[(match_df['team1']==team_input_1) | ((match_df['team2'])==team_input_1)]
            print('Number of matches played by %s :%d'%(team_input_1,team_df_1.shape[0]))
            print ('Report for the matches won by the IPL team: ',team_input_1)
            print ('===========================================')
            team_win_1=team_df_1[team_df_1['winner']==team_input_1]
            print('\n',team_win_1[['season','team1','team2','winner','win_by_runs','win_by_wickets']],'\n')
            team_df_1
        elif team_input_1 not in match_df_team1_unique:
            clear()
            print('Input value doesnt belong to list above.\nPlease re-enter name from list.\n')
            # print (match_df_team1_unique)
            option_5_4_1()
    except ValueError:
        clear()
        # print ('dfsdfsdfsdfsdfsdfsdfsdfsd')
        print ('Invalid Input.\nPlease enter valid team name: ',mi_toset_wickets)
        option_5_4_1()
# option_5_4_1()

#Option 5.4.2 of Option 5
global team_df_2
def option_5_4_2():
    print (match_df_team1_unique,'\n')
    print('Matches won with win-by-wickets by the team entered; user defined\n')
    global team_input_2
    team_input_2=input('Enter a team name: ')
    print ('==================')
    try:
        if team_input_2 in match_df_team1_unique:
            team_df_3=match_df[(match_df['team1']==team_input_2) | ((match_df['team2'])==team_input_2)]
            team_win_2=team_df_3[team_df_3['winner']==team_input_2]
            win_2=team_win_2[team_win_2['win_by_wickets']>0]
            win_2=win_2[['win_by_wickets','team1','team2']]
            print ('\n',win_2,'\n')
        elif team_input_2 not in match_df_team1_unique:
            clear()
            print('Input value doesnt belong to list above.\nPlease re-enter name from list.\n')
            option_5_4_2()
            # print (match_df_team1_unique)
    except ValueError:
        clear()
        # print ('dfsdfsdfsdfsdfsdfsdfsdfsd')
        print ('Invalid Input.\nPlease enter valid team name: ',mi_toset_runs)
        option_5_4_2()
# option_5_4_2()

#Option 5.4.3 of Option 5
global team_df_3
def option_5_4_3():
    print (match_df_team1_unique,'\n')
    print('Matches won with win-by-runs by the team entered; user defined\n')
    global team_input_3
    team_input_3=input('Enter a team name: ')
    print ('==================')
    try:
        if team_input_3 in match_df_team1_unique:
            team_df_3=match_df[(match_df['team1']==team_input_3) | ((match_df['team2'])==team_input_3)]
            team_win_3=team_df_3[team_df_3['winner']==team_input_3]
            win_1=team_win_3[team_win_3['win_by_runs']>0]
            win_1=win_1[['win_by_runs','team1','team2']]
            win_1=win_1.sort_values('win_by_runs',ascending=False)
            print (win_1)
        elif team_input_3 not in match_df_team1_unique:
            clear()
            print('Input value doesnt belong to list above.\nPlease re-enter name from list.\n')
            option_5_4_3()
            # print (match_df_team1_unique)
    except ValueError:
        clear()
        # print ('dfsdfsdfsdfsdfsdfsdfsdfsd')
        print ('Invalid Input.\nPlease enter valid team name: ',mi_toset_runs)
        option_5_4_3()
# option_5_4_3()


def menu_6():
    #Menu 6
    #T
    print('\n\t[6-1] Toss win decision')
    print('\t[6-2] Number of matches vs season')
    print('\t[6-3] Favourite city for playing matches')
    print('\t[6-4] Number of matches won by each team')
    print('\t[6-5] Number of matches played vs Number of matches won')
    print('\t[6-6] Advantage of batting first/second in a stadium; user defined')
    print('\t[6-7] Advantage of batting first/second in Feroz Shah Kotla, Delhi')
    print('\t[6-8] Advantage  of batting first/second in MA Chidambaram Stadium, Chepauk')
    print('\t[6-9] Advantage  of batting first/second in Wankhede Stadium, Mumbai')
    print('\t[6-10] Top 10 man of match winners')
    print('\t[6-11] Top winnig teams; win by runs')
    print('\t[6-12] Top 15 winnig teams; win by wickets')
    print('\t[6-13-1] Teams defeated by win by wickets; user defined')
    print('\t[6-13-2] Frequency of Victory for team by number of wickets; user defined')
    print('\t[6-13-3] Number of matches won & lost by a team; user defined\n')
    # print('\t[6-14] Winning by Runs - Team Performance')
    # print('\t[6-15] Winning by Wickets - Team Performance\n')


    global option_6
    option_6 = (input('Enter the option: '))
    option_6 = option_6

global list_6
list_6=['6-1','6-2','6-3','6-4','6-5','6-6','6-7','6-9','6-10','6-11','6-12','6-13-1','6-13-2','6-13-2','6-14','6-15']

def menu_6_options():
        if option_6 == '6-1':
            option_6_1()
        elif option_6 == '6-2':
            option_6_2()
        elif option_6 == '6-3':
            option_6_3()
        elif option_6 == '6-4':
            option_6_4()
        elif option_6 == '6-5':
            option_6_5()
        elif option_6 == '6-6':
            option_6_6()
        elif option_6 == '6-7':
            option_6_7()
        elif option_6 == '6-8':
            option_6_8()
        elif option_6 == '6-9':
            option_6_9()
        elif option_6 == '6-10':
            option_6_10()
        elif option_6 == '6-11':
            option_6_11()
        elif option_6 == '6-12':
            option_6_12()
        elif option_6 == '6-13-1':
            option_6_13_1()
        elif option_6 == '6-13-2':
            option_6_13_2()
        elif option_6 == '6-13-3':
            option_6_13_3()
            clear()
            print('Input entered is invalid. Enter valid input.')
            menu_6()
            menu_6_options()



#Option 6.1 of Option 6
def option_6_1():
    #Plot of Field vs Bat
    print('Toss win decision')
    colour_pref=['#7952B3','#FFC107']
    y_data = match_df['toss_decision'].value_counts()
    x_data=['Field','Bat']
    plt.style.use('ggplot')
    # plt.style.use('dark_background')
    plt.bar(x_data,y_data,color=colour_pref)
    #match_df['toss_decision'].value_counts()
    # sns.countplot(x='toss_decision', data=match_df)
    plt.title('Toss win decision',fontsize=15)
    plt.xlabel('Toss Decision',fontsize=15)
    plt.ylabel('Frequency',fontsize=15)
    plt.show()
# option_6_1()

def option_6_2():
    print('Number of matches vs season')
    #Plot of Number of matches vs season
    number_matches_df = match_df.groupby('season')[['id']].count()
    # print (number_matches_df)
    # plt.plot(number_matches_df.index,number_matches_df.id,'ms',markersize=10,markeredgecolor='black',linestyle='dashed',color='',linewidth=5)
    plt.plot(number_matches_df.index,number_matches_df.id,'mD',markersize=7.5,markeredgecolor='black',markerfacecolor='#808080',linestyle='solid',color='#000000',linewidth=3)
    plt.title('Number of matches in each season',fontsize=15)
    plt.xlabel('Seasons',fontsize=15)
    plt.ylabel('Number of matches',fontsize=15)
    plt.xticks(number_matches_df.index)
    # plt.plot(number_matches_df.index,number_matches_df.id,'p--g',color='#de0000')

    # sns.lineplot(data=number_matches_df,x=number_matches_df.index,y=number_matches_df.id,color='#FF0000',markers=True,dashes=True)
    plt.show()
# option_6_2()

#Option 6.3 of Option 6
def option_6_3():
    print('Favourite city for playing matches')
    #Plot of Number of matches vs city played in
    number_matches_city_df = match_df.groupby('city')[['id']].count()
    number_matches_city_df=number_matches_city_df.sort_values('id', ascending=False).reset_index()
    number_matches_city_df.rename(columns = { 'id': 'matches_won','winner':'city'}, inplace = True)
    # print (number_matches_city_df)
    plt.figure(figsize=(10,7))
    plt.title('Favourite city for playing matches',size=15)
    # plt.barh(number_matches_city_df.city,number_matches_city_df.matches_won)
    # plt.style.use('dark_background')
    sns.set_style("dark")
    sns.barplot(x=number_matches_city_df.matches_won, y=number_matches_city_df.city, orient='h', palette='hsv_r')
    plt.xticks(rotation=0,fontsize=10)
    plt.ylabel('City',fontsize=15)
    plt.xlabel('Number of matches played',fontsize=15)
    plt.plot()
    plt.show()
# option_6_3()

#Option 6.4 of Option 6
def option_6_4():
    print('Number of matches won by each team')
    #Plot of Number of matches won by each team
    global matches_won_teams
    matches_won_teams = match_df.groupby('winner')[['id']].count()
    matches_won_teams=matches_won_teams.sort_values('id', ascending=False).reset_index()
    matches_won_teams.rename(columns = { 'id': 'matches_won','winner':'team'}, inplace = True)
    # print (matches_won_teams)
    plt.figure(figsize=(8,4))
    sns.barplot(x=matches_won_teams.matches_won, y=matches_won_teams.team, orient='h', palette='cool')
    plt.title('Number of matches won by each team')
    plt.ylabel('Teams')
    plt.xlabel('Total no. of matches won')
    # plt.xticks(rotation=90,fontsize=10)
    # sns.barplot(matches_won_teams.matches_won,matches_won_teams.team,orient='h',palette='brg')
    plt.plot()
    plt.show()
# option_6_4()

#Option 6.5 of Option 6
def option_6_5():
    print('Number of matches played vs Number of matches won')

    #Number of matches played vs Number of matches won
    matches_won_teams = match_df.groupby('winner')[['id']].count()
    matches_won_teams=matches_won_teams.sort_values('id', ascending=False).reset_index()
    matches_won_teams.rename(columns = { 'id': 'matches_won','winner':'team'}, inplace = True)
    matches_team_match_won = pd.concat([match_df['team1'],match_df['team2']])
    matches_team_match_won=matches_team_match_won.value_counts().reset_index()
    matches_team_match_won.columns=['team','total_matches']
    matches_team_match_won.set_index('team',inplace=True)
    merged_matches_team_match_won=matches_team_match_won.merge(matches_won_teams,on='team')
    merged_matches_team_match_won['winning_percent'] = (merged_matches_team_match_won.matches_won/merged_matches_team_match_won.total_matches)*100
    merged_matches_team_match_won
    plt.title('Number of matches played vs Number of matches won',fontweight=800)
    plt.xlabel('Teams')
    plt.ylabel('Total no. of matches/Winning Percent')
    plt.xticks(rotation=90,fontsize=9)
    # plt.bar(merged_matches_team_match_won.team,merged_matches_team_match_won.total_matches,alpha=0.4,color='#00ec51')
    # plt.bar(merged_matches_team_match_won.team,merged_matches_team_match_won.matches_won, alpha=0.4,color='255, 0, 0')
    plt.bar(merged_matches_team_match_won.team,merged_matches_team_match_won.total_matches,alpha=0.4,color='#FF0000')
    plt.bar(merged_matches_team_match_won.team,merged_matches_team_match_won.matches_won, alpha=0.4,color='#00FF21')
    # plt.bar(merged_matches_team_match_won.team,merged_matches_team_match_won.total_matches,alpha=0.4,color='#145BC5')
    # plt.bar(merged_matches_team_match_won.team,merged_matches_team_match_won.matches_won, alpha=0.4,color='#0600FF')
    plt.plot(merged_matches_team_match_won.team,merged_matches_team_match_won.winning_percent,'o-k')
    plt.legend(['Winning Percent','Matches Played','Matches Won'])
    plt.show()
# sns.barplot(merged_matches_team_match_won.team,merged_matches_team_match_won.total_matches,color='#FF7E00',hue='')
# sns.barplot(merged_matches_team_match_won.team,merged_matches_team_match_won.matches_won,color='#00137F',hue='')
#Graph is green
# option_6_5()

#Option 6.6 of Option 6
def option_6_6():
    print('Advantage of batting first/second in a stadium; user defined')
    print ('\n',match_df['venue'].unique())
    venue_input=input('Enter a venue name: ')
    print   ('=============================================================================================================================')
    stadium_name=match_df.loc[(match_df['venue']==venue_input) ]
    stadium_name_win_by_runs=stadium_name[stadium_name['win_by_runs']>0]
    slices=[len(stadium_name_win_by_runs),len(stadium_name)-len (stadium_name_win_by_runs)]
    labels=['Batting first','Batting Second']
    # b = np.random.random(3,)
    g = np.random.random(3,)
    r = np.random.random(3,)
    color = (r, g)
    a=len(stadium_name_win_by_runs)
    b=len(stadium_name)-len (stadium_name_win_by_runs)
    plt.pie(slices,labels=labels,colors=color,autopct='%4.2f%%', startangle=90,explode=(0,0.05),shadow=1,textprops={'fontsize':15})
    plt.title(venue_input,fontsize=20)
    plt.show()
# option_6_6()
                                                                                                      
#Option 6.7 of Option 6
def option_6_7():
    print('Advantage of batting first/second in Feroz Shah Kotla, Delhi')
    # Advantage  of batting first/second in a stadium
    Delhi_stadium=match_df.loc[(match_df['venue']=='Feroz Shah Kotla') ]
    Delhi_stadium_win_by_runs=Delhi_stadium[Delhi_stadium['win_by_runs']>0]
    slices=[len(Delhi_stadium_win_by_runs),len(Delhi_stadium)-len(Delhi_stadium_win_by_runs)]
    labels=['Batting first','Batting Second']
    plt.pie(slices,labels=labels,startangle=20,shadow=1,explode=(0,0.2),autopct='%2.2f%%',colors=['#1519ef','#fc4811'])
    plt.title('Feroz Shah Kotla',fontsize=20)
    plt.show()
    print(len(Delhi_stadium_win_by_runs))
    print(len(Delhi_stadium))
# option_6_7()

#Option 6.8 of Option 6
def option_6_8():
    print('Advantage of batting first/second in Wankhede Stadium, Mumbai')
    wankhede_stadium=match_df.loc[(match_df['venue']=='Wankhede Stadium')]
    wankhede_stadium_win_by_runs=wankhede_stadium[wankhede_stadium['win_by_runs']>0]
    slices=[len(wankhede_stadium_win_by_runs),len(wankhede_stadium)-len(wankhede_stadium_win_by_runs)]
    print (len(wankhede_stadium_win_by_runs))
    labels=['Batting first','Batting Second']
    plt.pie(slices,labels=labels,startangle=20,shadow=1,explode=(0,0.2),autopct='%2.2f%%',colors=['#F55C47','#4AA96C'])
    plt.title('Wankhede Stadium\nChances of winning with respect to the stadium\n')
    plt.show()
# option_6_8()

#Option 6.9 of Option 6
def option_6_9():
    print('Advantage of batting first/second in a stadium in MA Chidambaram Stadium, Chepauk')
    chennai_stadium=match_df.loc[(match_df['venue']=='MA Chidambaram Stadium, Chepauk') ]
    chennai_stadium_win_by_runs=chennai_stadium[chennai_stadium['win_by_runs']>0]
    slices=[len(chennai_stadium_win_by_runs),len(chennai_stadium)-len(chennai_stadium_win_by_runs)]
    labels=['Batting first','Batting Second']
    plt.pie(slices,labels=labels,textprops={'fontsize':15},colors=['#00BCD4','#DD2C00'],autopct='%4.2f%%',startangle=90,explode=(0,0.1),shadow=1)
    plt.title('MA Chidambaram Stadium, Chepauk',fontsize=15)
    plt.show()
# option_6_9()

#Option 6.10 of Option 6
def option_6_10():
    print('Top 10 man of match winners')
    match_man_of_match = match_df.groupby(['player_of_match'])[['id']].count().reset_index()
    match_man_of_match = match_man_of_match.rename(columns={'id':'num'})
    match_man_of_match_sort_desc = match_man_of_match.sort_values('num',ascending=False)
    match_man_of_match_head= match_man_of_match_sort_desc.head(10)
    sns.barplot(x=match_man_of_match_head.num, y=match_man_of_match_head.player_of_match, orient='h', palette='winter')
    plt.title('Top 10 man of match winners',fontsize=20)
    plt.xlabel('Number of wins',fontsize=15)
    plt.ylabel('Man of Match winner',fontsize=15)
    plt.show()
# option_6_10()

#Option 6.11 of Option 6
def option_6_11():
    freq={}
    man_of_match=list(match_df['player_of_match'])
    for items in man_of_match:
        freq[items]=man_of_match.count(items)
    player=[]
    times=[]
    dict={'Name':player,'title':times}
    for key,value in freq.items():
        player.append(key)
        times.append(int(value))
    player_of_match = pd.DataFrame(dict,index=player)
    player_of_match = player_of_match.sort_values('title',ascending=False).head(15)
    player_of_match.plot(kind='bar',color='r',edgecolor='k',)
    plt.title('TOP PLAYERS AS PLAYER OF THE MATCH')
    plt.legend(['Scores'])
    plt.xlabel("Player's Name")
    plt.ylabel("Number of times title won")
    print('TOP PLAYERS AS PLAYER OF THE MATCH')
    plt.show()
# option_6_11()


#Option 6.12 of Option 6
def option_6_12():
    match_df_new=match_df.sort_values('win_by_wickets',ascending=False)
    top_15 = match_df_new[['winner','win_by_wickets']].head(15)
    print('\nTop 10 winnig teams; win by runs\n')
    top_15[['winner','win_by_wickets']].plot(kind='bar',x='winner',color='blue')
    plt.title('TOP FIFTEEN WINNIG TEAMS BY WIN BY RUNS',fontsize=15)
    plt.xlabel('Teams')
    plt.ylabel('Win by Runs')
    plt.ylim(5,12)
    plt.show()
# option_6_12()


#Option 6_13_1 of Option 6
global team_win
global win_2
def option_6_13_1():
    print (match_df['team1'].unique())
    global team_input_custom
    team_input_custom=input('Enter a team name: ')
    team_win=match_df[match_df['winner']==team_input_custom]
    team_win[['season','team1','team2','winner','win_by_runs','win_by_wickets']]
    print('\n=============================================================================================================================\n')
    print('Teams defeated by win by wickets; user defined\n')
    win_2=team_win[team_win['win_by_wickets']>0]
    win_2=win_2[['win_by_wickets','team1','team2']]
    print (win_2)
    print('\n')
    plt.figure(figsize=(10,6))
    # plt.style.use('dark_background')
    plt.style.context('dark_background')
    plt.barh(win_2.head(6).team1,win_2.head(6).win_by_wickets,color=['red','#FFD700','#0000FF','#787878','#FF006E','#60FF00'])
    plt.title('Teams defeated by %s - win by wickets'%team_input_custom)
    plt.grid(True)

    plt.show()
# option_6_13_1()

#Option 6_13_2 of Option 6
def option_6_13_2():
    print ('\n',match_df['team1'].unique(),'\n')
    team_input_custom=input('Enter a team name: ')
    print   ('\n=============================================================================================================================\n')
    # team_input_custom_without_space=team_input_custom.replace(' ','_')
    team_df_custom=match_df[(match_df['team1']==team_input_custom) | ((match_df['team2'])   ==team_input_custom)]
    team_win_custom=team_df_custom[team_df_custom['winner']==team_input_custom]
    team_win_custom[['season','team1','team2','winner','win_by_runs','win_by_wickets']]
    # team_win.shape[0]
    win_2_custom=team_win_custom[team_win_custom['win_by_wickets']>0]
    win_2_custom=win_2_custom[['win_by_wickets','team1','team2']]
    bins=[1,2,3,4,5,6,7,8,9,10]
    plt.style.use('seaborn-bright')
    win_2_custom['win_by_wickets'].plot(kind='hist',rwidth=0.9,color=['#17B528','#00137F'],edgecolor='k')
    # win_2_custom['win_by_wickets'].plot(kind='hist',rwidth=0.9,color='pink',edgecolor='k')
    plt.xticks(bins)
    plt.title('Frequency of Victory for %s - win by wickets'%team_input_custom)
    plt.xlabel('Win by Wickets')
    plt.ylabel('Frequency')
    plt.plot()
    # plt.grid(True)

    plt.show()
    # print (win_2_custom)
# option_6_13_2()
#👍
# team_win_custom=match_df[match_df['winner']==team_input_custom]

#Option 6_13_3 of Option 6
def option_6_13_3():
    print (match_df['team1'].unique())
    team_input_custom=input('Enter a team name: ')
    print   ('=============================================================================================================================')

    if team_input_custom in (match_df['team1'].unique()):
        team_df=match_df[(match_df['team1']==team_input_custom) | ((match_df['team2'])==team_input_custom)]
        team_win_custom=match_df[match_df['winner']==team_input_custom]
        winlost=[]
        winlost.append(team_win_custom.shape[0])# NO OF MATCHES WON BY PUNE WARRIORS
        winlost.append(team_df.shape[0]-team_win_custom.shape[0])# NO OF MATCHES LOST BY PUNE WARRIORS
        xx=['Won','Lost']
        ex=(0.09,0)
        r = np.random.random(3,)
        # b = np.random.random(3,)
        g = np.random.random(3,)
        color = (r, g)
        # colours_1= ['#04deab','#911a65']
        # colours_2 = ['#03ddff','#f8fc24']
        # colours_3 = ['#0804ff','#e6ff00']
        plt.pie(winlost,labels=xx,explode=ex,autopct='%1.1f%%',textprops={'fontsize':14},shadow=True,startangle=90,colors=color)
        # plt.pie(winlost,labels=xx,explode=ex,autopct='%1.1f%%',shadow=True,startangle=60)
        plt.title('Matches played, won and lost by %s'%team_input_custom,fontsize=15)
        plt.show()


def main_menu():
    clear()
    # print('\n\t\t\t\t\t\t\t\tIPL Data Analysis\n')
    xyzabc=('\n|****************************************|     IPL Data Analysis     |*****************************************|\n')
    abc=xyzabc.center(0)
    print(abc)
    print('[1] Get description about the IPL\n')
    print('[2] Access the IPL data files\n')
    print('[3] Data Manipulation\n')
    print('[4] Team wise Analysis\n')
    print('[5] Match wise Analysis\n')
    print('[6] Visual Analysis\n')
    print('[0] Exit the program\n')
    print('|**************************************************************************************************************|')
    global option
    option=float(input('\nEnter your option from the above: '))
    list_options=[1,2,3,4,5,6,0]
    if option==1:
        menu_1()
        menu_1_options()
        anykey=input('\nEnter any key to return to menu: ')
        clear()
        main_menu()
    elif option==2:
        menu_2()
        menu_2_options()
        anykey=input('\nEnter any key to return to menu: ')
        main_menu()
        clear()
    elif option==3:
        menu_3()
        menu_3_options()
        anykey=input('\nEnter any key to return to menu: ')
        main_menu()
        clear()
    elif option==4:
        menu_4()
        menu_4_options()
        anykey=input('\nEnter any key to return to menu: ')
        main_menu()
        clear()
    elif option==5:
        menu_5()
        menu_5_options()
        anykey=input('\nEnter any key to return to menu: ')
        main_menu()
        clear()
    elif option==6:
        menu_6()
        menu_6_options()
        anykey=input('\nEnter any key to return to menu: ')
        main_menu()
        clear()
    elif option==0:
        clear()
        exit()
    if option not in list_options:
        clear()
        print('\nInvalid Input. Please enter valid input.\n')
        main_menu()

main_menu()