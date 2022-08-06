#!/usr/bin/env python3
# The MIT License (MIT).
# Copyright (c) 2022 ALIF-FUSOBAR.

from instapy import util

def test_default_values_returned():
    assert util.get_action_delay("like") == 2
    assert util.get_action_delay("comment") == 2
    assert util.get_action_delay("follow") == 2
    assert util.get_action_delay("unfollow") == 2
