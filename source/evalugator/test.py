"""Test the functions that are a part of an assessment."""

# ruff: noqa: PLR2004

from typing import Any, List

import assessment
import sqlite3
from evalugator import constants, execute

FILE_NAME = constants.files.DB_File_Name

def do_tests() -> List[Any]:
    """Test all of the sub-parts of the assessment."""
    # execute all of the test cases defined in this module
    # and then return their output in a list of strings,
    # with each entry in the list the output of one test
    test_output: List[str] = []
    test_output = execute.execute_by_name_filter(
        constants.evalugator.Test_Module, constants.evalugator.Test_Filter
    )
    return test_output

def test_part_one():
    part_one_output = assessment.create_or_connect_db(FILE_NAME)
    try:
        assert isinstance(part_one_output, sqlite3.Connection)
        return True
    except AssertionError:
        return False

def test_part_two():
    part_one_connection = assessment.create_or_connect_db(FILE_NAME)
    part_two_output = assessment.query_prolific_author(part_one_connection.cursor())
    try:
        assert part_two_output == 46
        return True
    except AssertionError:
        return False

def test_part_three():
    part_one_connection = assessment.create_or_connect_db(FILE_NAME)
    part_two_output = assessment.query_prolific_author(part_one_connection.cursor())
    part_three_output = assessment.query_stories_by_author(part_one_connection.cursor(), part_two_output)
    try:
        assert len(part_three_output) == 13
        return True
    except AssertionError:
        return False

def test_part_four():
    part_one_connection = assessment.create_or_connect_db(FILE_NAME)
    part_two_output = assessment.query_prolific_author(part_one_connection.cursor())
    part_four_output = assessment.query_author_by_id(part_one_connection.cursor(), part_two_output)
    try:
        assert part_four_output == "Isaiah Foster"
        return True
    except AssertionError:
        return False

def test_part_five():
    part_one_connection = assessment.create_or_connect_db(FILE_NAME)
    part_two_output = assessment.query_prolific_author(part_one_connection.cursor())
    part_five_output = assessment.update_author_status(
        part_one_connection,
        part_one_connection.cursor(),
        part_two_output,
        "ACTIVE"
    )
    try:
        assert part_five_output == {'author': 46, 'status': 'ACTIVE', 'updated': True}
        return True
    except AssertionError:
        return False
