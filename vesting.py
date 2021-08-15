#!/usr/bin/env python
# vesting.py
__version__ = '0.1.0'

import sys
import datetime
import pandas as pd

def get_parameters():
    # get parameters from stdin
    filename = sys.argv[1]
    target_date = sys.argv[2]
    target_date = datetime.datetime.fromisoformat(target_date)

    return filename, target_date

def create_dataframe(filename):
    # create dataframe
    df = pd.read_csv(filename,
        header=None)
    df.columns = ['vestingType', 'employeeID', 'employeeName', 'awardID', 'date', 'quantity']
    df.date = pd.to_datetime(df.date)

    return df

def get_all_employees(df):
    # get employees list
    df_employees = df.drop_duplicates(subset='employeeID').copy()
    df_employees = df_employees.set_index('employeeID').to_dict()
    employees = df_employees['employeeName']

    return employees

def group_by_employee_and_award(df, target_date):
    # group events by employee id and award type given the date is before the target date
    df_group = df.copy()
    df_group.quantity = df_group.apply(lambda x: x.quantity if x.date <= target_date else 0, axis=1)
    df_group = df_group.groupby(by=['employeeID', 'awardID']).sum()
    df_group = df_group.reset_index()

    return df_group

def format_response(df, employees):
    # format response
    df = df.sort_values(by=['employeeID', 'awardID'])
    df['employeeName'] = df.apply(lambda x: employees[x.employeeID], axis=1)
    df = df[['employeeID', 'employeeName', 'awardID', 'quantity']]
    
    return df

def main():
    # calls others functions
    filename, target_date = get_parameters()
    df = create_dataframe(filename)
    employees = get_all_employees(df)
    df_group = group_by_employee_and_award(df, target_date)
    response = format_response(df_group, employees)

    print(response)
    return response

if __name__ == '__main__':
    main()
