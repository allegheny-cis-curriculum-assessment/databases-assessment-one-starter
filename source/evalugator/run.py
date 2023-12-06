"""Run the functions that are a part of an assessment."""

from typing import Any, List

import sqlite3
import assessment
from evalugator import constants, execute

FILE_NAME = constants.files.DB_File_Name

def do_runs() -> List[Any]:
    """Run all of the sub-parts of the assessment."""
    # execute all of the run functions defined in this module
    # and then return their output in a list of strings,
    # with each entry in the list the output of one run
    run_output: List[str] = []
    run_output = execute.execute_by_name_filter(
        constants.evalugator.Run_Module, constants.evalugator.Run_Filter
    )
    return run_output

def run_part_one():
    """Run the function defined by part-one of the assessment."""
    separator = constants.markers.Separator
    part_one_output = assessment.create_or_connect_db(FILE_NAME)
    try:
        assert type(part_one_output) == sqlite3.Connection
        return "Connected"
    except AssertionError:
        return ""

def run_part_two():
    part_one_connection = assessment.create_or_connect_db(FILE_NAME)
    part_two_output = assessment.query_prolific_author(part_one_connection.cursor())
    return part_two_output

def run_part_three():
    part_one_connection = assessment.create_or_connect_db(FILE_NAME)
    part_two_output = assessment.query_prolific_author(part_one_connection.cursor())
    part_three_output = assessment.query_stories_by_author(part_one_connection.cursor(), part_two_output)
    return part_three_output

def run_part_four():
    part_one_connection = assessment.create_or_connect_db(FILE_NAME)
    part_two_output = assessment.query_prolific_author(part_one_connection.cursor())
    part_four_output = assessment.query_author_by_id(part_one_connection.cursor(), part_two_output)
    return part_four_output

def run_part_five():
    part_one_connection = assessment.create_or_connect_db(FILE_NAME)
    part_two_output = assessment.query_prolific_author(part_one_connection.cursor())
    part_five_output = assessment.update_author_status(
        part_one_connection,
        part_one_connection.cursor(),
        part_two_output,
        status = "ACTIVE"
    )
    return part_five_output
