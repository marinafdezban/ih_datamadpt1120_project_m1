import pandas as pd
import re

def cleaning_rural(data_cleaned):

    data_cleaned['rural'] = data_cleaned['rural'].replace('countryside', 'Rural')
    data_cleaned['rural'] = data_cleaned['rural'].replace('urban', 'Urban')
    data_cleaned['rural'] = data_cleaned['rural'].replace('city', 'Urban')
    data_cleaned['rural'] = data_cleaned['rural'].replace('Country', 'Rural')
    data_cleaned['rural'] = data_cleaned['rural'].replace('rural', 'Rural')
    data_cleaned['rural'] = data_cleaned['rural'].replace('Non-Rural', 'Rural')

    return data_cleaned


def adding_columns(raw_data):
    rows_counts = dict(raw_data['Job Title'].value_counts())
    percentage_calculate = raw_data['Job Title'].count()

    for i in raw_data.index:
        if raw_data.loc[i, 'Job Title'] == None:
            pass
        else:
            raw_data.loc[i, 'Quantity'] = rows_counts[raw_data.loc[i, 'Job Title']]
            raw_data.loc[i, 'Percentage'] = rows_counts[raw_data.loc[i, 'Job Title']] * 100 / percentage_calculate

    raw_data.dropna(subset=['Job Title', 'Quantity'])

    raw_data['Quantity'] = raw_data['Quantity'].astype('int64')
    raw_data['Percentage'] = raw_data['Percentage'].astype(float).map(lambda x: '{:.2%}'.format(x))

    adding_columns(raw_data)

    return raw_data[['Country','Job Title','Age','Quantity','Percentage']]

