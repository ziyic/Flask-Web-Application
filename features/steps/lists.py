#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/10
# @Function:
from behave import *

use_step_matcher("re")


@given("The Anime list page is successfully accessed and the list on the Anime list page are being used correctly")
def step_impl(context):
    """
    Navigate to the Anime list page

    :type context: behave.runner.Context
    """
    context.browser.get('http://localhost:5000/anime')


@when("I click on the link to the Anime details")
def step_impl(context):
    """
    Click on the link

    :type context: behave.runner.Context
    """
    context.browser.find_element_by_partial_link_text('One Piece').click()


@then("I should be navigated to the Anime details page")
def step_impl(context):
    """
    we should be directed to the anime detail page

    :type context: behave.runner.Context
    """
    assert context.browser.current_url == 'http://127.0.0.1:5000/anime/details/21'


@given("I navigate to the Anime list page")
def step_impl(context):
    """
    Navigate to the Anime list page

    :type context: behave.runner.Context
    """
    context.browser.get('http://127.0.0.1:5000/anime/?page=2')


@when("I click on the link to the Next page")
def step_impl(context):
    """
    Click on the 'Next' link

    :type context: behave.runner.Context
    """
    context.browser.find_element_by_partial_link_text('Next').click()


@then("I should be navigated to the next Anime list page")
def step_impl(context):
    """
    we should be directed to the next anime list page

    :type context: behave.runner.Context
    """
    assert context.browser.current_url == 'http://127.0.0.1:5000/anime/?page=3'


@when("I click on the link to a page number")
def step_impl(context):
    """
    Click on the a page number link

    :type context: behave.runner.Context
    """
    context.browser.find_element_by_partial_link_text('4').click()


@then("I should be navigated to the page number of Anime list page")
def step_impl(context):
    """
    we should be directed to the anime list page with Specific page number

    :type context: behave.runner.Context
    """
    assert context.browser.current_url == 'http://127.0.0.1:5000/anime/?page=4'
