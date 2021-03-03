#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/3
# @Function:
class Anime:
    def __init__(self, anime_id, name, synopsis, rating, scored_by,popularity,members,episodes,aired,link,source,genre=[],producer=[], ):
        self.link = link
        self.aired = aired
        self.source = source
        self.episodes = episodes
        self.members = members
        self.popularity = popularity
        self.scored_by = scored_by
        self.rating = rating
        self.producer = producer
        self.synopsis = synopsis
        self.genre = genre
        self.name = name
        self.anime_id = anime_id

    def __str__(self):
        return f"{self.anime_id},{self.name},{self.genre},{self.synopsis},{self.rating},{self.scored_by},{self.popularity},{self.members},{self.episodes},{self.source},{self.aired},{self.link}"