#!/usr/bin/env python
"""Tests for `pystatus` package."""
# pylint: disable=redefined-outer-name

import pytest

from pystatus.pystatus import chcker

@chcker
def add(a, b):
    return a + b

@chcker
def divide(a, b):
    return a / b


def test_pystatus():
    # x = chcker(add)(1,3)
    x = add(1,3)
    # print(x.value)
    assert x.vvalue == 4


def test_pystatus_error():
    # x = chcker(add)(1,3)
    x = divide(1,0)
    if x.status:
        assert x.vvalue == 4
    else:
        assert x.status == False
