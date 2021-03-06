import warnings
warnings.filterwarnings('ignore')

from math import sqrt
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split
import sklearn.metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

import numpy as np
import pandas as pd
import seaborn as sns




############################# Function File for Acquiring Data ############################


def get_player_data():
    '''
    This function is designed to pull our CS GO player stats data from the csv file into 
    a pandas dataframe then return the dataframe.
    
    It will also print out the shape of the dataframe after removing an unneccasry column
    '''
    df = pd.read_csv('player_stats.csv', index_col=0) ## reading our csv into a pandas dataframe

    return df 

    print("Shape of Dataframe (rows, columns):\n")
    print(df.shape)  ## look at shape
    

def acquire_stats(df):
    '''
    This function is designed to take in our dataframe and display the numerical statistics and 
    goes the extra step to add a range column for the numerical columns
    '''
    
    ## taking one step further and adding a range column

    stats_df = df.describe().T

    stats_df['range'] = stats_df['max'] - stats_df['min'] 

    return stats_df

def summarize_df(df):
    '''
    this function is designed to look at our dataframe and print out a short summary of the
    dataframe.
    
    This will include things like:
    info on the columns and data types
    value counts of categorical columns
    '''
    
    print('Info on Columns and Datatypes:\n')
    print(df.info()) ## <-- looking at our columns and datatypes
    print('------------------------------------------------\n')
    
    ## creating a list of columns I want value counts for
    list = ['country', 'teams']
    
    ## using list comprehension to look through our custom list of columns and print
    ## out their value counts
    for x in list:
        print(f'Value Counts for {x}:\n')
        print(df[x].value_counts())
        print('--------------------')
        
    
def univariate_distributions(df):
    '''
    This function is designed to take in the player stats dataframe and 
    look at univariate distributions using .hist()
    '''
    
    ## looking at our continuous variable distributions
    stats = ['total_maps', 'total_rounds', 'kd_diff', 'kd', 'rating']
    
    ## using list comprehension to look through our custom list of columns and print
    ## out their histograms viewing their distributions
    for x in stats:
        print(f'Distribution of {x}\n')
        df[x].hist()
        plt.show()
        print('--------------------')   
    