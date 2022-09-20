# CSV-Analyser

![Build test](https://img.shields.io/github/workflow/status/yzhu27/CSVAnalyser/Update%20Coverage%20on%20Readme)
![MIT license](https://img.shields.io/github/license/yzhu27/CSVAnalyser)
![GitHub top language](https://img.shields.io/github/languages/top/yzhu27/CSVAnalyser)
![GitHub contributors](https://img.shields.io/github/contributors/yzhu27/CSVAnalyser)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7093577.svg)](https://doi.org/10.5281/zenodo.7093577)

Welcome to Group 7's repository for 22 fall Software Engineering homework 2 & 3!

This project is intended to read and analyze CSV files. Based on the example source code written in LUA, we implemented multiple functions in Python as listed below.


## Functions

**Read CSV**

- Import the input file to a dictionary line by line, separated by given separator.


**CLI**

- Update information through command line. Help string would be printed if run "-h".


**Generate Statistical Summaries**

- This function is for column data. For each column, the data is either numeric (which denoted with a leading upper case letter) or symbolic (which denoted with a leading lower case letter). Employ different statistical variebles to describe both types of data.


To suppot these functions, we defined 5 classes.

## Class

**Cols**

- Record column names and variables, differentiating dependent variables and independent variables by leading letters of column names.


**Rows**

- Record data by row.


**Num**

- Num class is for calculating features of numeric data. Methods of add, mid and div are included, among which mid is stand for the middle value of the sorted data, while div means standard deviation of this column of numbers.


**Sym**

- Sym class is for calculating features of symbolic data. Methods of add, mid and div are included, among which mid represents the most common symbol in the set; div is the entropy of these symbols.


**Data**


Test coverage is as below:

<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-90%25-brightgreen.svg" /></a><br/><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/Cols.py">Cols.py</a></td><td>20</td><td>1</td><td>1</td><td><a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/Cols.py#L 95%"> 95%</a></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/Data.py">Data.py</a></td><td>30</td><td>2</td><td>2</td><td><a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/Data.py#L 93%"> 93%</a></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/Num.py">Num.py</a></td><td>53</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/Row.py">Row.py</a></td><td>6</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/Sym.py">Sym.py</a></td><td>27</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/__init__.py">__init__.py</a></td><td>0</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/csv.py">csv.py</a></td><td>12</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/the.py">the.py</a></td><td>13</td><td>0</td><td>100%</td><td>&nbsp;</td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/utils.py">utils.py</a></td><td>53</td><td>19</td><td>19</td><td><a href="https://github.com/yzhu27/CSVAnalyser/blob/main/src/utils.py#L 64%"> 64%</a></td></tr><tr><td><b>TOTAL</b></td><td><b>214</b></td><td><b>22</b></td><td><b>90%</b></td><td>&nbsp;</td></tr></tbody></table></details>

<!-- Pytest Coverage Comment:End -->
