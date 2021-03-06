#!/usr/bin/env python

import sys
import logging

import pandas as pd

logging.basicConfig(format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    stream=sys.stdout,
    level=logging.INFO)
log = logging.getLogger(__name__)


###################
# CSV import config


def main():
    file_path = "/opt/app/data/core/Batting.csv"
    table_name = 'batting'

    df = pd.read_csv(file_path)
    df = df[df['yearID'] > 1980]
    df['1B'] = (df['H'] - (df['2B'] + df['3B'] + df['HR']))

    grouped_df = df.groupby("yearID")[["AB", "H", "1B", "2B", "3B", "HR", "SO"]].sum()

    grouped_df['1B_per'] = (grouped_df['1B'] / grouped_df['AB'])
    grouped_df['2B_per'] = (grouped_df['2B'] / grouped_df['AB'])
    grouped_df['3B_per'] = (grouped_df['3B'] / grouped_df['AB'])
    grouped_df['HR_per'] = (grouped_df['HR'] / grouped_df['AB'])
    grouped_df['SO_per'] = (grouped_df['SO'] / grouped_df['AB'])

    print grouped_df.to_csv()

if __name__ == '__main__':
    main()
