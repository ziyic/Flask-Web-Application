#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/10
# @Function:

from behave import *

use_step_matcher("re")


@given("I navigate to the index page and I can see the navigation link")
def navigate(context):
    """
    Navigate to the index page

    :type context: behave.runner.Context
    """
    context.browser.get('http://localhost:5000/')


@when("I click on the navigation link")
def click(context):
    """
    Click on the link

    :type context: behave.runner.Context
    """
    context.browser.find_element_by_partial_link_text('click to start').click()


@then("I should be navigated to the anime list page")
def anime_list(context):
    """
    we should be directed to the anime list page

    :type context: behave.runner.Context
    """
    assert context.browser.current_url == 'http://localhost:5000/anime'
