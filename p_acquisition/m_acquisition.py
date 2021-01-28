import re
import sqlite3
import requests
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup


# connect to database
from pandas import DataFrame


def sql_connection(path) -> object:
    """"
       :return: connect to the database and return a pandas dataframe, united by a primary key 'uuid'.
    """
    path: str = 'data/raw_data_project_m1.db'
    conn = sqlite3.connect(path)
    print('Connecting to database')
    sql_code = ('''
          SELECT personal_info.uuid,country_info.country_code, country_info.rural, career_info.normalized_job_code
          FROM personal_info
          JOIN career_info ON personal_info.uuid=career_info.uuid
          JOIN country_info ON personal_info.uuid=country_info.uuid
          JOIN poll_info ON personal_info.uuid=poll_info.uuid
          ''')

    print(f'Loading data from {path}')
    raw_data_df: DataFrame = pd.DataFrame(pd.read_sql_query(sql_code, conn))
    print('Connected to database!')
    return raw_data_df


# connect to API
def get_jobs_api(data_to_api) -> object:
    print('Waiting for API...')
    jobs_unique_values = data_to_api['normalized_job_code'].unique()
    job_title_requests = []
    url = 'http://api.dataatwork.org/v1/jobs/'

    # creating a list with api jobs
    for value in jobs_unique_values:
        response_data = requests.get(f'{url}{value}').json()
        if list(response_data.keys())[0] == 'error':
            pass
        else:
            job_title_requests.append(response_data)

    # create two lists: one with keys and other with values
    # uuid values
    job_uuid_list = []
    for uuid_item in job_title_requests:
        try:
            job_uuid_list.append(uuid_item['uuid'])
        except:
            pass

    # title values
    job_titles_job_list = []

    for title_item in job_title_requests:
        try:
            job_titles_job_list.append(title_item['title'])
        except:
            pass

    dict_job_id_titles_value = dict(zip(job_uuid_list, job_titles_job_list))

    # adding the data from the api to the df
    data_to_api['Job Title'] = data_to_api['normalized_job_code']

    for uuid, title in dict_job_id_titles_value.items():
        data_to_api.loc[data_to_api['normalized_job_code'] == uuid, 'Job Title'] = title

        # changing null values in Job Title column.
    data_to_api['Job Title'] = data_to_api['Job Title'].fillna('No job')

    print('Jobs data from API added!')

    return data_to_api


# Getting countries data from Web Scraping
def get_country_data(raw_data_df):
    print('Getting countries info by Web Scraping...')

    # connecting to Eurostat web
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    # getting the data
    table = soup.find_all('div', {'class': 'mw-content-ltr'})[0]
    countries_data = table.find_all('table')
    countries_names = [info.text for info in countries_data]

    # using regular expressions in order to clean countries data
    cleaning_spaces = [re.sub(r'\s', '', i) for i in countries_names]
    cleaning_special_characters = [re.sub(r'\*', '', i) for i in cleaning_spaces]
    cleaning_brackets = [re.sub(r'\[\d\]', '', i) for i in cleaning_special_characters]
    countries_scrapping_data = ''.join(cleaning_brackets)

    # separating keys and values in order to convert it in a dictionary
    countries_values = re.split(r'\(\w{0,7}\)', countries_scrapping_data)
    countries_keys = re.findall(r'\(\w{0,7}\)', countries_scrapping_data)
    countries_keys = [re.sub(r'\(|\)', '', i) for i in countries_keys]
    dict_keys_values_countries = dict(zip(countries_keys, countries_values))

    # adding missing countries
    dict_keys_values_countries['GB'] = 'Great Britain'
    dict_keys_values_countries['GR'] = 'Greece'

    # adding countries to the dataframe
    raw_data_df['Country'] = raw_data_df['country_code']
    for keys, values in dict_keys_values_countries.items():
        raw_data_df.loc[raw_data_df['country_code'] == keys, 'Country'] = values

    print('Countries data from Web Scraping added!')

    return raw_data_df
