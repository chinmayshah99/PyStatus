"""Main module."""

from typing import Tuple
from .status import Status
from pprint import pprint

import functools
import logging
def chcker(function):
    print(function)
    ret = Status(function.__name__)
    print(ret)
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            ret_val = function(*args, **kwargs)
            print(ret_val)
            ret.vvalue = ret_val
        except Exception as e:
            _error_args = None
            if e.args is not None:
                if isinstance(e.args, Tuple):
                    arg = list(e.args)
                    if len(arg)  == 1:
                        _error_args = arg[0]
                    else:
                        _error_args = e.args
                else:
                    _error_args = e.args
            else:
                _error_args = e.__class__[1]
            _class_name = e.__class__.__name__
            ret.werror = (_class_name, _error_args)
            logging.info("some error occured")
        finally:
            return ret
    return wrapper
