import pandas as pd
from functools import reduce


def cleaning_rural_column(column_rural):
    if column_rural.startswith('C' or 'c'):
        return 'Rural'
    else:
        return 'Urban'


def clean_rural(table) -> object:
    """
    :type table: object
    """
    table['Rural'] = table.apply(lambda x: cleaning_rural_column(x['rural']), axis=1)
    return table
