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


############################# Function File for Modeling the Data ############################


def get_metrics(df, model_name,rmse_validate,r2_validate):
    df = df.append({
        'model': model_name,
        'rmse_outofsample':rmse_validate, 
        'r^2_outofsample':r2_validate}, ignore_index=True)
    return df