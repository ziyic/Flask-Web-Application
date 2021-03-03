#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/4
# @Function:
#import sqlite3
import csv

def read_csv(file):
    li_data = []
    with open(file)as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for row in f_csv:
            print(row)
            li_data.append(row)

    return li_data

def parse_genre(li_data):
    li_genre = []
    for row in li_data:
        str_genre = row[2]
        str_li_genre=str_genre.split(",")
        for i in str_li_genre:
            if i.startswith('['):
                i = i.lstrip()
            elif i.endswith(']'):
                i = i.rstrip()
            if i not in li_genre:
                li_genre.append(i)

    return li_genre

def parse_producer(li_data):
    li_producer = []
    for row in li_data:
        str_producer = row[5]+","+row[6]
        str_li_producer = str_producer.split(",")
        for i in str_li_producer:
            if i.startswith('['):
                i = i.lstrip()
            elif i.endswith(']'):
                i = i.rstrip()
            if i not in li_producer:
                li_producer.append(i)

    return li_producer

def parse_source(li_data):
    li_source = []
    for row in li_data:
        source = row[12]
        li_source.append(source)

    return li_source