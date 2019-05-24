import os
import argparse
from datetime import datetime

import datareader
import report_calculations
import report_generator


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('-path', type=dir_path)
    parser.add_argument('-e', '--yearly', nargs = '*', help='yearly report', type=date_year)
    parser.add_argument('-a', '--monthly', nargs = '*',help='monthly report', type=date_month)
    parser.add_argument('-c', '--bar_chart', nargs = '*', help='bar chart report', type=date_month)

    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def date_year(date):
    if not date:
        return

    try:
        return datetime.strptime(date, '%Y')
    except ValueError:
        raise argparse.ArgumentTypeError(f"Given Date({date}) not valid")


def date_month(date):
    if not date:
        return

    try:
        return datetime.strptime(date, '%Y/%m')
    except ValueError:
        raise argparse.ArgumentTypeError(f"Given Date({date}) not valid")


def main():
    parsed_args = parse_arguments()
    weather_records = datareader.prepare_weather_records(parsed_args.path)

    if parsed_args.yearly:

        for year in parsed_args.yearly:
            year_records = report_calculations.calculate_yearly_report(weather_records, year)
            report_generator.generate_yearly_report(year_records)

    if parsed_args.monthly:

        for month in parsed_args.monthly:
            month_records = report_calculations.calculate_monthly_report(weather_records, month)
            report_generator.generate_monthly_report(month_records)

    if parsed_args.bar_chart:

        for chart in parsed_args.bar_chart:
            bar_chart_records = report_calculations.calculate_bar_chart_report(weather_records, chart)
            report_generator.generate_bar_chart(bar_chart_records)


if __name__ == "__main__":
    main()
