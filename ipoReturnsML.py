############################################################################
#
# ipoReturnsML 
#
############################################################################

import re
import tweepy
import pandas as pd
import openpyxl
import statistics
from tweepy import OAuthHandler
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from xCredentials import * # Credentials for logging into Twitter dev console

from ipoReturnsMLFunctions import * # Needs avgPolarity function which is defined in the ipoReturnsMLFunctions file

############################################################################
############################################################################

# Possible sectors in the excel document would include for instance Technology, Energy, Real Estate, Financials, IT, Healthcare, Utilities, Consumer Staples, Industrial, Consumer Discretionary

ipoDataPATH = excelPATH # This needs to be filled in based on where the excel file is saved
ipoDataDocument = openpyxl.load_workbook(ipoDataPATH)
ipoSheet = ipoDataDocument.active

# Pulls data for companies from the excel document

companies = ipoSheet['A']
companiesList = [companies[x].value for x in range(len(companies)]
                 
sectors = ipoSheet['C']
sectorList = [sectors[x].value for x in range(len(sectors)]

timeToIPO = ipoSheet['D']                 
timeToIPOList = [timeToIPO[x].value for x in range(len(timeTOIPO)]           

oneDayReturns = ipoSheet['E']                 
oneDayReturnsList = [oneDayReturns[x].value for x in range(len(oneDayReturns)]

# Scrapes Twitter using functions from ipoReturnsMLFunctions to determine the average polarity of 20 tweets for each company. 

companyAvgPolarityList = []

for company in companiesList:
    avgPolarityValue = avgPolarity(company, 20) # Set number of tweets to 20 for each company
    companyAvgPolarityList.append(avgPolarityValue)

# Now save the average polarity data to the excel document for good measure

for i in range(len(companyAvgPolarityList)): 
    j=str(i+2) 
    ipoSheet['B'+j].value = companyAvgPolarityList[i]

ipoSheet.save(filename=ipoDataPATH)

# Now put all data into a pandas dataframe to manipulate for supervised machine learning

ipoReturnDictionary = {'Companies' : companiesList, 'Sentiment' : companyAvgPolarityList, 'Sectors' : sectorsList, 'Time to IPO' : timeTOIPOList, 'Returns' : oneDayReturnsList}

ipoReturnDataFrame = pd.DataFrame(ipoReturnDictionary)

# Below isolate categorical variables by one-hot encoding. The only categorical variable is the sector in this case

ipoReturnDataFrameEncoded = pd.get_dummies(ipoReturnDataFrame)

# Now extract predictor and target variables into numpy array for supervised machine learning analysis

features = ipoReturnDataFrameEncoded.loc[:, 'time to ipo' : timeTOIPOLIST] # This includes all of the headings for the features, not the target
X = features.values
Y = ipoReturnDataFrameEncoded[returns].values # This is the heading for the target which is the one day returns

# Now carry out linear regression on test data and see how accurate the results are on the training data. At this stage it is straightforward to also introduce alternatives to linear regression

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
linReg = LinearRegression().fit(X_train, Y_train)

print("Training score: {:.2f}".format(linReg.score(X_train, Y_train)))                     
print("Test score: {:.2f}".format(linReg.score(X_test, Y_test)))













    
    

