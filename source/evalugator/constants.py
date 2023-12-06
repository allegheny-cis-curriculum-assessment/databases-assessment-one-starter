"""Define constants with dataclasses for use in evalugator."""

from dataclasses import dataclass


# evalugator constant
@dataclass(frozen=True)
class Evalugator:
    """Define the Evalugator dataclass for constant(s)."""

    Run_Module: str
    Run_Filter: str
    Test_Module: str
    Test_Filter: str


evalugator = Evalugator(
    Run_Module="evalugator.run",
    Run_Filter="run_",
    Test_Module="evalugator.test",
    Test_Filter="test_",
)


# Columns constant
@dataclass(frozen=True)
class Columns:
    """Define the Columns dataclass for constant(s)."""

    Email_Address: int
    Occupation: int
    Synthetic_Index: int


columns = Columns(
    Email_Address=4,
    Occupation=3,
    Synthetic_Index=1,
)


# files constant
@dataclass(frozen=True)
class Files:
    """Define the Files dataclass for constant(s)."""

    DB_File_Name: str


files = Files(
    DB_File_Name="db/news_data.db",
)


# markers constant
@dataclass(frozen=True)
class Markers:
    """Define the Markers dataclass for constant(s)."""

    Separator: str


markers = Markers(
    Separator=" / ",
)
