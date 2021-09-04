"""
Author: Arsalan Azmi
Description: Structured Text Parser.
Package: python-structured-text-parser
Python Version: 3.9
Year: 2021
Version: 1
"""
# ---- IMPORTS ----
import os as _os
import pandas as _pd

# -----------------
# Class Definitions
# -----------------      
class StructuredTextParser:
    """
    Class for Structured Text Parser.
    """
    def __init__(self, fieldSeparator, filename, lineSeparator):
        """
        Parameters
        ----------
        fieldSeparator : str
            Separator used to seperate fields and their value in the provided file. (eg: 'Key: Value' -> ':')
        filename : str
            File name.
        lineSeparator : str
            Separator used to separate data entries in the provided file. (eg: 'Key1: Value1/nKey2: Value2' -> '/n')
        """
        self.__data           = _pd.DataFrame()
        self.__fieldSeperator  = fieldSeparator
        self.__filename        = filename
        self.__lineSeparator  = lineSeparator
        self.__parseFile()

    # Public API
    def queryData(self):
        """
        Query data by field/column.
        """
        df = self.__data

        cols = list(df.columns)
        for idx, col in enumerate(cols):
            print(idx, ": ", col)

        try:
            idx = ''
            while idx.lower != 'q':
                print("Please input the index (0 - {}) of the column to read or 'q' to exit:".format(len(cols) - 1))
                idx = input()
                print(df[cols[int(idx)]])
        except ValueError:
            exit()

    def writeToExcel(self, outputFilename):
        """
        Write data to excel.

        Parameters
        ----------
        outputFilename : str
            Output file name.
        """
        df = self.__data
        df.to_excel(outputFilename)
        print("Excel file written to '{}'!".format(outputFilename))

        print('Open excel file? (y/n)')
        choice = input().lower() == 'y'
        if choice:
            if _os.name == 'posix':
                cmd = 'open '
            else:
                cmd = 'start '
            _os.system(cmd + outputFilename)

    # Private API
    def __parseFile(self):
        try:
            f = open(self.__filename, "r")
            with f:
                lines = f.readlines()

                parsedData = []
                currData   = {}
                currField  = ''
                currValue  = '' 
                for line in lines:
                    line = line.replace('\n', '')
                    seperator = line.find(self.__lineSeparator)
                    if not line:
                        if currData:
                            parsedData.append(currData.copy())
                        currData = {}
                    elif seperator < 0:
                        splitIdx = line.find(self.__fieldSeperator)
                        if not currField:
                            currField = line[0:splitIdx-1]
                        currValue += line[splitIdx+2:]
                    else:
                        currData[currField] = currValue
                        currValue, currField = '', ''
                df = _pd.DataFrame()
                parsedData.append(currData.copy())
                self.__data = df.from_dict(parsedData)
        except FileNotFoundError:
            exit("ERROR: File not found. Please copy data as {} file in the script's folder!".format(self.__filename))