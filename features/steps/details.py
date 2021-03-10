#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/10
# @Function:

from behave import *

use_step_matcher("re")


@given("I navigate to the Anime details page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.get('http://127.0.0.1:5000/anime/details/20')


@when("I click on the Back link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_element_by_partial_link_text('back').click()


@then("I should be navigated to Anime list page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.current_url == 'http://127.0.0.1:5000/anime/'


@when("I click on the Home link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_element_by_partial_link_text('home').click()


@then("I should be navigated to the index page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.current_url == 'http://127.0.0.1:5000/'
