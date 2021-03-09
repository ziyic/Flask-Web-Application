#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/4
# @Function:
import sqlite3
import pandas as pd

conn = sqlite3.connect('anime_data.db')
cur = conn.cursor()
dict_genre: dict[str, int] = {}
dict_producer: dict[str, int] = {}
dict_source: dict[str, int] = {}


def parse_genre(li_data):
    li_genre = []
    count = 0
    for row in li_data:
        str_genre = row[2]
        try:
            str_li_genre = str_genre.split(",")
        except AttributeError:
            str_li_genre = []
        for i in str_li_genre:
            i = i.lstrip("[|'| ").rstrip("]|'| ")
            if i not in li_genre and i != 'Genre':
                count += 1
                li_genre.append(i)
    li_genre.sort()
    for i in range(len(li_genre)):
        dict_genre[li_genre[i]] = i + 1
    return li_genre


def parse_producer(li_data):
    li_producer = []
    for row in li_data:
        try:
            str_producer = row[5] + "," + row[6]
        except TypeError:
            str_producer = str(row[5]) + "," + str(row[6])
        str_li_producer = str_producer.split(",")
        for i in str_li_producer:
            i = i.lstrip("[|'| ").rstrip("]|'| ")
            if i not in li_producer and (i != 'Producer' or 'Studio'):
                li_producer.append(i)
    li_producer.sort()
    for i in range(len(li_producer)):
        dict_producer[li_producer[i]] = i + 1
    return li_producer


def parse_source(li_data):
    li_source = []
    for row in li_data:
        source = row[12]
        try:
            source = source.lstrip("[|'| ").rstrip("]|'| ")
        except AttributeError:
            source = None
        if (source is not None) and (source not in li_source):
            li_source.append(source)
    li_source.sort()
    for i in range(len(li_source)):
        dict_source[li_source[i]] = i + 1
    return li_source


def parse_anime(li_data):
    li_anime = []
    for row in li_data:
        name = row[1].replace('"', "'")
        try:
            li_anime_genre = row[2].split(",")
        except AttributeError:
            li_anime_genre = []
        for i in range(len(li_anime_genre)):
            li_anime_genre[i] = li_anime_genre[i].lstrip("[|'| ").rstrip("]|'| ")
        try:
            synopsis = row[3].replace('"', "'")
        except AttributeError:
            synopsis = 'NULL'
        try:
            li_anime_producer = (row[5] + "," + row[6]).split(",")
        except (TypeError, AttributeError):
            li_anime_producer = (str(row[5]) + "," + str(row[6])).split(",")
        for i in range(len(li_anime_producer)):
            li_anime_producer[i] = li_anime_producer[i].lstrip("[|'| ").rstrip("]|'| ")
        u_li_anime_producer = []
        for i in li_anime_producer:
            if i not in u_li_anime_producer:
                u_li_anime_producer.append(i)
        aired = row[13]
        try:
            aired = aired.split("to")
        except AttributeError:
            aired = ["NULL"]
        try:
            source = dict_source[row[12]]
        except KeyError:
            source = "NULL"
        db_anime = f'{row[0]},"{name}","{synopsis}",' \
                   f'{"NULL" if str(row[7]) == "nan" else row[7]},{row[8]},' \
                   f'{"NULL" if str(row[9]) == "nan" else row[9]},{row[10]},' \
                   f'{"NULL" if str(row[11]) == "nan" else row[11]},{source},"{aired[0]}",' \
                   f'"{"NULL" if str(row[14]) == "nan" else row[14]}" '
        insert_db("table_anime", db_anime)
        if db_anime not in li_anime:
            li_anime.append(db_anime)
        parse_r_anime_genre(row[0], li_anime_genre)
        parse_r_anime_producer(row[0], u_li_anime_producer)

    return li_anime


def parse_r_anime_genre(anime_id, li_anime_genre):
    li_anime_genre_id = []
    for i in li_anime_genre:
        li_anime_genre_id.append(f"{anime_id},{dict_genre[i]}")
    insert_db("r_table_anime_genre", li_anime_genre_id)


def parse_r_anime_producer(anime_id, li_anime_producer):
    li_anime_producer_id = []
    if len(li_anime_producer) != 0:
        for i in li_anime_producer:
            li_anime_producer_id.append(f"{anime_id},{dict_producer[i]}")
        insert_db("r_table_anime_producer", li_anime_producer_id)


def preprocess_csv(file):
    print('start preprocess data')
    data_sets = pd.read_csv(file).sort_values(by=['ScoredBy', 'Members'], ascending=False).drop_duplicates(['Anime_id'])
    data_sets = data_sets.loc[(data_sets['Type'] == 'TV')]
    new_data_sets = []
    for i in range(2000):
        new_data_sets.append(data_sets.iloc[i, :])
    pd.DataFrame(new_data_sets).to_csv('simplified_data.csv', index=False)
    print('Simplified data prepared')
    return new_data_sets


def init_database():
    f = open('./db/create_sqlite_tables.sql', 'r')
    with f:
        data = f.read()
    cur.executescript(data)
    li = preprocess_csv('Anime_data.csv')
    li_data = []
    for row in li:
        li_data.append(row)

    insert_db("table_genre", parse_genre(li_data), autoincrement=True)
    insert_db("table_producer", parse_producer(li_data), autoincrement=True)
    insert_db("table_source", parse_source(li_data), autoincrement=True)
    insert_db("table_anime", parse_anime(li_data), autoincrement=False)


def insert_db(table, values, autoincrement=False):
    if str(type(values)) == "<class 'list'>" and not autoincrement:
        for v in values:
            sql = f"INSERT INTO {table} VALUES ({v})"
            if table == 'table_anime':
                print(sql)
            cur.execute(sql)
            conn.commit()
    elif str(type(values)) == "<class 'list'>" and autoincrement:
        for v in values:
            v = f"NULL, '{v}'"
            sql = f"INSERT INTO {table} VALUES ({v})"
            if table == 'table_anime':
                print(sql)
            cur.execute(sql)
            conn.commit()


if __name__ == '__main__':
    init_database()
