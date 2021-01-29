import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def export_table(raw_data_df, country) -> object:

    country = input('Choose your fighter! Do you want to see data for all countries or just for one of them? ')

    print('Exporting the Data Frame...')

    # exporting the table for all countries.
    df_result = raw_data_df[['Country', 'Job Title', 'Rural', 'Quantity', 'Percentage']]
    df_result = df_result.sort_values(['Quantity', 'Percentage'])

    if country == 'all countries':
        print('Exporting all countries data...')
        df_result.to_csv('results/all_countries_data.csv')
        return print('Here you have your file exported!')

    else:
        if country in raw_data_df['Country'].unique().tolist():
            raw_data_df[raw_data_df['Country'] == country].to_csv(f'results/{country} results.csv')
            print('Exporting country data...')
        else:
            raise ValueError("Input is not in database")
        return print('File exported!')

