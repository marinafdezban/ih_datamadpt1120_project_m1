import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def export_table(raw_data_df, country) -> object:
    # country = input('Choose your fighter! Do you want to see data for all countries or just for one of them? ')

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


def visual_matplotlib(raw_data_df):
    print('Creating a chart...')
    quantity_mean = raw_data_df['Quantity'].mean()
    list_countries = raw_data_df['Country'].tolist()
    quantity = raw_data_df['Quantity'].tolist()
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.barh(list_countries, quantity, color='#644A84')
    plt.style.use('ggplot')
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    # Add a vertical line which indicates quantity mean
    ax.axvline(quantity_mean, ls='--', color='#B21ACD')

    # Customizing our fig
    ax.title.set(y=1.05)
    ax.set(xlabel='Quantity', ylabel='Countries', title='Project 1')
    ax.set_xticks([-5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
    fig.subplots_adjust(left=.1)

    print('Chart created!')

    return fig


def save_chart(fig, title):
    fig.savefig(f'results/{title}.png')
    print('Chart saved!')
