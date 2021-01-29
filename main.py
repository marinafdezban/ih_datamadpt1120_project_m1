import argparse
from p_acquisition import m_acquisition as acq
from p_wrangling import m_wrangling as wra
from p_analysis import m_analysis as ana
from p_reporting import m_reporting as rep


def argument_parser():
    """
    parse arguments to script
    """
    parser = argparse.ArgumentParser(description='getting data from a survey')
    parser.add_argument("-p", "--path", help="specify path of the database", type=str, required=True)
    parser.add_argument("-c", "--country", help="specify country for the results", default="all countries", type=str)
    args = parser.parse_args()
    return args


def main(arguments):
    data_table = acq.sql_connection(arguments.path)
    add_jobs = acq.get_jobs_api(data_table)
    rename_col = wra.clean_rural(add_jobs)
    add_countries = acq.get_country_data(rename_col)
    results = ana.adding_columns(add_countries)

    # exporting table and visuals

    rep.export_table(results, arguments.country)
    fig = rep.visual_matplotlib(results)
    rep.save_chart(fig, title)
    print('You may find your results in the folder ./results ')


if __name__ == '__main__':
    print('Starting Project 1...')

    title = 'Project 1'
    my_arguments = argument_parser()
    main(my_arguments)

    print('Project 1 complete')
