import pandas as pd

def export_table(df_final, country):

    print('Time to export the Data Frame...')

    # exporting the table for all countries.
    df_result = df_final[['Country', 'Job Title', 'Age', 'Quantity', 'Percentage']]
    df_result = df_result.sort_values(['Quantity', 'Percentage'])

    if country == 'all countries':
        print('exporting all_countries_data.csv file...')
        df_result.to_csv('../data/all_countries_data.csv')
        return 'Here you have your file exported!'

    else:
        if country in df_final['Country'].values():
            df_final[df_final['Country'] == country].to_csv(f'../data/{country} results.csv')
        else:
            raise ValueError("Input is not in database")
        return 'file exported!'

