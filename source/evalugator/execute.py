"""Reflectively access and run functions using inspection."""

import importlib
import inspect
from typing import List


def execute_by_name_filter(module_name: str, function_name_filter: str) -> List[str]:
    """Test all of the sub-parts of the assessment."""
    # define the list of the function output
    function_output: List[str] = []
    # extract all of the functions in this module
    module = importlib.import_module(module_name)
    functions = inspect.getmembers(module, inspect.isfunction)
    # sort the functions by their line number as they appear
    # inside of the module definition; this ensures that the
    # output will be in the same order as the functions
    # appear inside of the module definition
    functions.sort(key=lambda x: inspect.getsourcelines(x[1])[1])
    # filter for functions starting with the specified
    # function name filter; only these functions will be invoked
    # and then their output will be stored in the function output list
    for member in functions:
        # found a function that starts with the name filter
        if member[0].startswith(function_name_filter):
            # execute the test function and store
            # its output inside of the list of output
            function_output.append(member[1]())
    # return the list of the function output such
    # that each element in the list is a string
    # that contains the output of a function; note
    # that this approach is general-purpose and will
    # this work with either run or test functions
    return function_output
