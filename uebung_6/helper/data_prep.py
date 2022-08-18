import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer


def outlier_detection(df, columns):

    i = 1
    
    for column in columns:
        if i == 1:
            outlier_df = df[(np.abs(stats.zscore(df[column])) > 3)]
            i += 1
        else:
            outlier_df = outlier_df.append(df[(np.abs(stats.zscore(df[column])) > 3)])
            
    # check if outlier unique
    if len(outlier_df.index) != len(set(outlier_df.index)):
        
        outlier_df = outlier_df[~outlier_df.index.duplicated(keep='first')]
        
    return outlier_df


def get_index_outlier(df, columns):
    
    i = 1
    
    for column in columns:
        if i == 1:
            outlier_list = df[(np.abs(stats.zscore(df[column])) > 3)].index.values
            i += 1
        else:
            outlier_list = np.append(outlier_list, df[(np.abs(stats.zscore(df[column])) > 3)].index.values)
            
        # check and remove unique items
        if len(outlier_list) != len(set(outlier_list)):
            outlier_list = np.unique(outlier_list)
        
    return outlier_list


def dataset_visualization(dataset):

    for x in dataset.columns:
        
        if (pd.api.types.is_string_dtype(dataset[x])) & (dataset[x].nunique() < 100):
            dataset[x].value_counts().plot(kind='bar', figsize=(20,10))
            plt.title('Barplot der Variable {}'.format(x))
            plt.ylabel('Count of Occurences')
            plt.xlabel('{} Categories'.format(x))
            
            plt.show()
            
        if  pd.api.types.is_numeric_dtype(dataset[x]):

            # Darstellung eines Histogrammes
            count, bin_edges = np.histogram(dataset[x], 15)

            dataset[x].plot.hist(alpha=0.5,
                                    figsize=(20,10),
                                    bins=15,
                                    xticks=bin_edges)
            plt.title('Histogramm der Variable {}'.format(x))
            plt.ylabel('Number of Datapoints')
            plt.xlabel('Number of {}'.format(x))

            plt.show()

            # Darstellung eines Boxplots
            dataset[x].plot(kind='box', color='blue', vert=True, figsize=(20, 6)) 
            plt.title('Boxplot der Variable {}'.format(x))

            plt.show()

def simple_computer_group_by_index(train_df, test_df, index_train, index_test, column_list, group_by_column):
    train_df.loc[index_train, column_list] = np.NaN
    test_df.loc[index_test, column_list] = np.NaN

    imp = SimpleImputer(strategy='mean')

    for district in train_df[group_by_column].unique():
        train_df.loc[train_df[group_by_column] == district, column_list] = imp.fit_transform(
            train_df.loc[train_df[group_by_column] == district, column_list])
        test_df.loc[test_df[group_by_column] == district, column_list] = imp.fit_transform(
            test_df.loc[test_df[group_by_column] == district, column_list])
        
    return train_df, test_df