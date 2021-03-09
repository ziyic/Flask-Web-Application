#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/10
# @Function:

from urllib.parse import urlencode
import copy


class Pager:
    def __init__(self, current, total, url_prefix, params, per_page, max_page):
        try:
            current = int(current)
        except TypeError:
            current = 1
        if current <= 0:
            current = 1
        self.current = current

        self.total = total

        self.per_page = per_page

        max_page_num, div = divmod(total, per_page)
        if div:
            max_page_num += 1
        self.max_page_num = max_page_num

        self.max_page = max_page
        self.half_max_pager_count = int((max_page - 1) / 2)

        self.url_prefix = url_prefix
        params = copy.deepcopy(params)
        get_dict = params.to_dict()

        self.params = get_dict

    @property
    def start(self):
        return (self.current - 1) * self.per_page

    @property
    def end(self):
        return self.current * self.per_page

    def page_html(self):
        if self.max_page_num <= self.max_page:
            start = 1
            end = self.max_page_num
        else:
            if self.current <= self.half_max_pager_count:
                start = 1
                end = self.max_page
            elif (self.current + self.half_max_pager_count) > self.max_page_num:
                end = self.max_page_num
                start = self.max_page_num - self.max_page + 1
            else:
                start = self.current - self.half_max_pager_count
                end = self.current + self.half_max_pager_count

        page_html_list = []

        self.params['page'] = 1
        first_page = f'<li><a href="{self.url_prefix}?{urlencode(self.params)}">First &nbsp;&nbsp;</a></li>'
        page_html_list.append(first_page)

        self.params["page"] = self.current - 1
        if self.params["page"] < 1:
            previous_page = f'<li class="disabled"><a href="{self.url_prefix}?{urlencode(self.params)}"' \
                            f' aria-label="Previous">Previous</span></a></li>'
        else:
            previous_page = f'<li><a href = "{self.url_prefix}?{urlencode(self.params)}"' \
                            f' aria-label = "Previous" >Previous</span></a></li>'
        page_html_list.append(previous_page)

        for i in range(start, end + 1):
            self.params['page'] = i
            if i == self.current:
                temp = f'<li class="active"><a href="{self.url_prefix}?{urlencode(self.params)}" ' \
                       f'style="font-weight: bolder;font-size: larger">{i}</a></li>'
            else:
                temp = f'<li><a href="{self.url_prefix}?{urlencode(self.params)}">{i}</a></li>'
            page_html_list.append(temp)

        self.params["page"] = self.current + 1
        if self.params["page"] > self.max_page_num:
            self.params["page"] = self.current
            next_page = f'<li class="disabled"><a href = "{self.url_prefix}?{urlencode(self.params)}"' \
                        f' aria-label = "Next">Next</span></a></li >'
        else:
            next_page = f'<li><a href = "{self.url_prefix}?{urlencode(self.params)}"' \
                        f' aria-label = "Next">Next</span></a></li>'
        page_html_list.append(next_page)

        self.params['page'] = self.max_page_num
        last_page = f'<li><a href="{self.url_prefix}?{urlencode(self.params)}">Last</a></li>'
        page_html_list.append(last_page)

        return ''.join(page_html_list)
