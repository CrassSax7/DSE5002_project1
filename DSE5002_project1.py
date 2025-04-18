#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 10:32:25 2025
Project Mission statement: Utilize rdataproject.csv and answer the following 
from the following assignment instructions - Your CEO has decided that the company 
needs a full-time data scientist, and possibly a team of them in the future. 
She thinks she needs someone who can help drive data science within then entire 
organization and could potentially lead a team in the future. She understands that 
data scientist salaries vary widely across the world and is unsure what to pay them. 
To complicate matters, salaries are going up due to the great recession and the 
market is highly competitive. Your CEO has asked you to prepare an analysis on 
data science salaries and provide them with a range to be competitive and 
get top talent. The position can work offshore, but the CEO would like to know 
what the difference is for a person working in the United States. Your company is 
currently a small company but is expanding rapidly. 

Prepare your analysis in an R file. Your final product should be a power point 
presentation giving your recommendation to the CEO. CEOs do not care about your 
code and don’t want to see it. They want to see visuals and a well 
thought out analysis. You will need to turn in the power point and the code
as a flat R file. (Updated instructions dictate that code analysis should be done in 
                   Python)

@author: caseybrookshier
"""

import pandas as pd
import numpy as np
import os

# chack on the current working directory
#change directory for use of relative paths 
os.chdir('/Users/caseybrookshier/Desktop/Merrimack/DSE5002/Project_1') 
os.getcwd()

#get the dataframe from the file sales.csv
# set the file path to the location you saved the file or make sure it is in␣
#↪your current working directory 

df = pd.read_csv("r project data-1.csv") 
df.head()