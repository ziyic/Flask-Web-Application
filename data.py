#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/4
# @Function:
# import sqlite3
import pandas as pd


def preprocess_csv(file):
    print('start preprocess data')
    data_sets = pd.read_csv(file)
    data_sets = data_sets.sort_values(by=['Members'], ascending=False)
    data_sets = data_sets.loc[(data_sets['Type'] == 'TV') & (data_sets['Genre'] != 'nan')
                              & (data_sets['Producer'].notnull())
                              & (data_sets['Studio'].notnull())]
    new_data_sets = []
    for i in range(2000):
        new_data_sets.append(data_sets.iloc[i, :])
    pd.DataFrame(new_data_sets).to_csv('simplified_data.csv', index=False)
    print('Simplified data prepared')
    return new_data_sets


def parse_genre(li_data):
    li_genre = []
    for row in li_data:
        str_genre = row[2]
        str_li_genre = str_genre.split(",")
        for i in str_li_genre:
            i = i.lstrip("[|'| ")
            i = i.rstrip("]|'| ")
            if i not in li_genre and i != 'Genre':
                li_genre.append(i)
    li_genre.sort()
    return li_genre


def parse_producer(li_data):
    li_producer = []
    for row in li_data:
        str_producer = row[5] + "," + row[6]
        str_li_producer = str_producer.split(",")
        for i in str_li_producer:
            i = i.lstrip("[|'| ")
            i = i.rstrip("]|'| ")
            if i not in li_producer:
                li_producer.append(i)
    li_producer.sort()
    return li_producer


def parse_source(li_data):
    li_source = []
    for row in li_data:
        source = row[12]
        source = source.lstrip("[|'| ")
        source = source.rstrip("]|'| ")
        if source not in li_source:
            li_source.append(source)
    return li_source


def db_insert(table, rows):
    if str(type(rows)) == "list":
        for row in rows:

            pass

    pass
