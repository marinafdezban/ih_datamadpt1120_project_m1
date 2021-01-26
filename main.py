import argparse
from p_acquisition import m_acquisition as acq
from p_wrangling import m_wrangling as wra
from p_reporting import m_reporting as rep

def argument_parser():
    """
    parse arguments to script
    """
    parser = argparse.ArgumentParser(description='getting data from a survey')
    parser.add_argument("-p", "--path", help="specify path of the database", type=str, required=True)
    parser.add_argument("-c", "--country", help="specify country for the results", default="all countries", type=str)
    args=parser.parse_args()
    return args

def main(arguments):
    print("starting process")

    data_table = acq.sql_connection(arguments.path)
    data_clean = wra.cleaning_rural(data_table)
    add_jobs = acq.get_jobs_api(data_clean)
    add_countries = acq.get_country_data(add_jobs)
    add_new_columns = wra.adding_columns(add_countries)

    # exporting table

    rep.export_table(add_new_columns, arguments.country)


if __name__ == '__main__':
    print('starting project 1...')

    my_arguments = argument_parser()
    main(my_arguments)

    print('project 1 complete')