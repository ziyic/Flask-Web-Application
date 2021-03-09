#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/3
# @Function:

from flask import Flask, Blueprint, request, render_template
import sqlite3

from pager import *

anime = Blueprint('anime', __name__, url_prefix='/anime')
db = 'anime_data.db'


def get_dict_genre():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from table_genre")
    dicts = {}
    li_data = cur.fetchall()
    for row in li_data:
        dicts[row["id"]] = row["genre_name"]
    conn.close()
    return dicts


def get_dict_producer():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from table_producer")
    dicts = {}
    li_data = cur.fetchall()
    for row in li_data:
        dicts[row["id"]] = row["producer_name"]
    conn.close()
    return dicts


def get_dict_source():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from table_source")
    dicts = {}
    li_data = cur.fetchall()
    for row in li_data:
        dicts[row["id"]] = row["source"]
    conn.close()
    return dicts


dict_genre = get_dict_genre()
dict_producer = get_dict_producer()
dict_source = get_dict_source()


@anime.route('/')
def index():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from table_anime")
    li_data = cur.fetchall()

    pager = Pager(request.args.get('page', 1), len(li_data), request.path, request.args, 20, 5)
    index_list = li_data[pager.start:pager.end]
    pages = pager.page_html()
    conn.close()
    return render_template("list.html", index_list=index_list, pages=pages)


@anime.route('/details/<anime_id>')
def details(anime_id):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f'select * from table_anime WHERE id= {anime_id}')
    i_anime = cur.fetchall()[0]
    cur.execute(f'select * from r_table_anime_genre WHERE anime_ID= {anime_id}')
    g_anime = cur.fetchall()
    genres = []
    for i in g_anime:
        genres.append(dict_genre[i["genre_ID"]])
    cur.execute(f'select * from r_table_anime_producer WHERE anime_ID= {anime_id}')
    p_anime = cur.fetchall()
    producers = []
    for i in p_anime:
        producers.append(dict_producer[i["producer_ID"]])
    source = dict_source[i_anime["anime_source"]]
    conn.close()
    return render_template("detail.html",
                           anime=i_anime,
                           genres=str(genres).lstrip("[| ").rstrip("]| "),
                           producers=str(producers).lstrip("[| ").rstrip("]| "),
                           source=source.lstrip("[|'| ").rstrip("]|'| "))
