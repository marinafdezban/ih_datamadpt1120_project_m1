def adding_columns(raw_data) -> object:
    print('Adding some new columns to dataframe')
    rows_counts = dict(raw_data['Job Title'].value_counts())
    percentage_calculate = raw_data['Job Title'].count()

    for i in raw_data.index:
        if raw_data.loc[i, 'Job Title'] is not None and raw_data.loc[i, 'Job Title'] != 'No job':
            raw_data.loc[i, 'Quantity'] = rows_counts[raw_data.loc[i, 'Job Title']]
            raw_data.loc[i, 'Percentage'] = rows_counts[raw_data.loc[i, 'Job Title']] / percentage_calculate

    print('Columns added!')
    raw_data.dropna(subset=['Job Title', 'Quantity'])

    print('Getting data sorted...')
    raw_data['Quantity'] = raw_data['Quantity'].astype('int64')
    raw_data['Percentage'] = raw_data['Percentage'].astype(float).map(lambda x: '{:.2%}'.format(x))
    raw_data = raw_data.sort_values(['Quantity', 'Percentage'])

    print('Data sorted!')

    return raw_data[['Country', 'Job Title', 'Rural', 'Quantity', 'Percentage']]
