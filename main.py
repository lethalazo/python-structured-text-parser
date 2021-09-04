"""
Author: Arsalan Azmi
Description: Structured Text Parser.
Package: python-structured-text-parser
Python Version: 3.9
Year: 2021
Version: 1
"""
# ---- IMPORTS ----
from structured_text_parser import StructuredTextParser

# -----------------
# Class Definitions
# -----------------
class Main:
    """
    Main runner class.
    """
    def __init__(self):
        filename       = 'doc.txt'
        fieldSeparator = ':'
        lineSeparator = '-----------------------------------------'

        self.__parser = StructuredTextParser(fieldSeparator, filename, lineSeparator)

    # Public API
    def run(self):
        outputFilename = 'output.xlsx'
        self.__parser.writeToExcel(outputFilename)
        self.__parser.queryData()

# =============
# Main
# =============
runner = Main()
runner.run()