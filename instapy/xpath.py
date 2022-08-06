#!/usr/bin/env python3
# The MIT License (MIT).
# Copyright (c) 2022 ALIF-FUSOBAR.

from .xpath_compile import xpath

def read_xpath(function_name, xpath_name):
    return xpath[function_name][xpath_name]
