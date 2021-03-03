#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/3
# @Function:

from flask import Blueprint
r_anime = Blueprint('anime', __name__)


@r_anime.route('/')
def index():
    return 'Hello, anime!'