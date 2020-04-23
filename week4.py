import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# df_city = pd.read_csv("City_Zhvi_AllHomes.csv")

# df_gdp = pd.read_excel("gdplev.xls")

# print(df_uni_town.head())

# dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada',
          'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland',
          'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois',
          'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho',
          'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii',
          'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey',
          'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico',
          'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands',
          'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia',
          'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York',
          'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California',
          'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico',
          'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands',
          'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    df_uni_town = pd.read_csv('university_towns.txt', header=None, error_bad_lines=False)
    df = pd.DataFrame({'State': [], 'RegionName': []} )
    # print(df)
    # i = 0

    x = ""
    val = ""
    for row in df_uni_town.itertuples(index= False):
        # print("row._0: ", row._0)         #print(getattr(row, '_0'))

        if "[edit]" in (row._0):
            # print((row._0).index('['))
            x = row._0[:row._0.index('[')]
            # df = df.append({'State': x}, ignore_index=True)
            # df.insert(df.__len__()+1, ,x,  allow_duplicates=False)
            # print(df.head(-1))
            # continue
            # print("x: ", x)
        if "[edit]" not in (row._0):
            if ":" not in (row._0):
                val = (row._0)[: (row._0).index('(')]
                # print("df.__len__(): ", df.__len__())
                df = df.append({'State': x, 'RegionName': val}, ignore_index=True)
                # print(df.iloc[[-1]])
            else:
                if "(" not in (row._0):
                    continue
                else:
                    val = (row._0)[: (row._0).index('(')]
                    # print("df.__len__(): ", df.__len__())
                    df = df.append({'State': x, 'RegionName': val}, ignore_index=True)
                    # print(df.iloc[[-1]])
            # continue
            # df.insert(df.__len__()+1, 'RegionName', val,  allow_duplicates=False)
    print(df.head())



    return df
# get_list_of_university_towns()

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''

    df_gdp = pd.read_excel("gdplev.xls")

    df_gdp = df_gdp[7:]
    # print(df_gdp.head())

    gdp = pd.DataFrame({'Quarter': [], 'ChainedValue': []})

    for row in df_gdp.itertuples(index= False):
        # print("row: ", row)
        # print("row._4: ", int(row._4[:4]))
        if int(row._4[:4]) >= 2000:
            gdp = gdp.append({'Quarter': row._4, 'ChainedValue': row._6}, ignore_index=True)
    # print(gdp['ChainedValue'][0])

    x = -1
    for i in range( len(gdp.index) - 2):
        if gdp['ChainedValue'][i] - gdp['ChainedValue'][i+1] > 0:
            if gdp['ChainedValue'][i+1] - gdp['ChainedValue'][i+2] > 0:
                x = i
                break
    # print(gdp['ChainedValue'][x-1], gdp['ChainedValue'][x] , " , ",  gdp['ChainedValue'][x+1], gdp['ChainedValue'][x+2])
    # print(gdp['Quarter'][x], gdp['ChainedValue'][x])

    return gdp['Quarter'][x]
# print(get_recession_start())

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''

    df_gdp = pd.read_excel("gdplev.xls")

    df_gdp = df_gdp[7:]
    # print(df_gdp.head())

    gdp = pd.DataFrame({'Quarter': [], 'ChainedValue': []})

    for row in df_gdp.itertuples(index=False):
        # print("row: ", row)
        # print("row._4: ", int(row._4[:4]))
        if int(row._4[:4]) >= 2000:
            gdp = gdp.append({'Quarter': row._4, 'ChainedValue': row._6}, ignore_index=True)
    # print(gdp['ChainedValue'][0])

    x = -1
    for i in range(len(gdp.index) - 2):
        if gdp['ChainedValue'][i] - gdp['ChainedValue'][i + 1] > 0:
            if gdp['ChainedValue'][i + 1] - gdp['ChainedValue'][i + 2] > 0:
                x = i
                break
    # print(x)

    y = -1
    for i in range(len(gdp.index) - 2):
        if i > x:
            if gdp['ChainedValue'][i] - gdp['ChainedValue'][i + 1] < 0:
                if gdp['ChainedValue'][i + 1] - gdp['ChainedValue'][i + 2] < 0:
                    y = i
                    break

    return gdp['Quarter'][y]
# print(get_recession_end())

def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''
    df_gdp = pd.read_excel("gdplev.xls")

    df_gdp = df_gdp[7:]
    # print(df_gdp.head())

    gdp = pd.DataFrame({'Quarter': [], 'ChainedValue': []})

    for row in df_gdp.itertuples(index=False):
        # print("row: ", row)
        # print("row._4: ", int(row._4[:4]))
        if int(row._4[:4]) >= 2000:
            gdp = gdp.append({'Quarter': row._4, 'ChainedValue': row._6}, ignore_index=True)
    # print(gdp['ChainedValue'][0])

    x = -1
    for i in range(len(gdp.index) - 2):
        if gdp['ChainedValue'][i] - gdp['ChainedValue'][i + 1] > 0:
            if gdp['ChainedValue'][i + 1] - gdp['ChainedValue'][i + 2] > 0:
                x = i
                break
    # print(x)

    y = -1
    for i in range(x, len(gdp.index) - 2):
        if gdp['ChainedValue'][i] - gdp['ChainedValue'][i + 1] < 0:
            if gdp['ChainedValue'][i + 1] - gdp['ChainedValue'][i + 2] < 0:
                y = i + 2
                break
        # if i > x:
        #     if gdp['ChainedValue'][i] - gdp['ChainedValue'][i + 1] < 0:
        #         if gdp['ChainedValue'][i + 1] - gdp['ChainedValue'][i + 2] < 0:
        #             y = i+1
        #             break
    # print(gdp['ChainedValue'][y-2], gdp['ChainedValue'][y-1] , " , ",  gdp['ChainedValue'][y], gdp['ChainedValue'][y+1])
    # print(gdp['Quarter'][y], gdp['ChainedValue'][y])

    z = 1000000000
    index = -1
    for i in range(x,y+1,1):
        # print(gdp['ChainedValue'][i])
        if gdp['ChainedValue'][i] < z:
            z = gdp['ChainedValue'][i]
            index = i

    # print(gdp['ChainedValue'][index])

    return gdp['Quarter'][index]
print(get_recession_bottom())

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''

    return "ANSWER"