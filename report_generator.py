BLUE = '\033[34m'
RED = '\033[31m'


def generate_yearly_report(record):
    print(
        f"Yearly Analysis Report Generated :\n\n"
        f" Highest: {record['max_temp'].max_temp}C on {record['max_temp'].date.strftime('%B %d')}\n"
        f" Lowest: {record['low_temp'].low_temp}C on {record['low_temp'].date.strftime('%B %d')} \n "
        f"Humidity: {record['humidity'].max_humid}% on {record['humidity'].date.strftime('%B %d')}"
    )


def generate_monthly_report(record):
    print(
        f"\nMonthly Analysis Report Generated : \n\n"
        f"Highest Average: {record['avg_max_temp']}C \n"
        f"Lowest Average: {record['avg_low_temp']}C \n"
        f"Average Mean Humidity: {record['avg_mean_humid']}%\n"
    )


def generate_bar_chart(records):
    print('\nBar Chart Report Generated : \n')

    for record in records:
        day = record.date.day
        max_tmp_bar = '+' * record.max_temp
        low_tmp_bar = '+' * record.low_temp
        print(
            f"{day} {RED}{max_tmp_bar} {record.max_temp}C \n"
            f"{day} {BLUE}{low_tmp_bar} {record.low_temp}C"
        )


def generate_single_bar_chart(records):
    print('\nBonus implementation single bar chart : \n')

    for record in records:
        day = record.date.day
        low_tmp_bar = '+' * record.low_temp
        remain_tmp = '+' * (record.max_temp - record.low_temp)
        print(f"{day} {BLUE}{low_tmp_bar}{RED}{remain_tmp} {BLUE}{record.low_temp}C - {RED}{record.max_temp}C")
