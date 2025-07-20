import pandas as pd 
file=pd.read_csv('tackoverflow_qa.csv')
file


# # Find all questions that were created before 2014

# file['creationdate']=pd.to_datetime(file['creationdate'])

# filt=file['creationdate'].dt.year <=2014
# file[filt]


# # Find all questions with a score more than 50
# score_fi=file['score']>=50
# file[score_fi]


# # Find all questions with a score between 50 and 100
# score_fi=file['score'].between(50,100)
# file[score_fi]


# # Find all questions answered by Scott Boston
# scott_boston=file['ans_name']=='Scott Boston'
# file[scott_boston]


# # Find all questions answered by the following 5 users,Gardner,DarkAnt,David Underhill,Jason Strimpel,Dr. Dave
# names=['Gardner','DarkAnt','David Underhill','Jason Strimpel','Dr. Dave']
# five=file['ans_name'].isin(names)
# file[five]


# # Find all questions that were created between March, 2014 and October 2014 
# # # that were answered by Unutbu and have score less than 5.

# filt1=file['creationdate'].dt.month.between(3,10)
# filt2=file['creationdate'].dt.year==2014
# filt3=file['ans_name']=='unutbu'
# filt4=file['score']<=5
# filt_res=filt1&filt2&filt3&filt4
# file[filt_res]



# # Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
# filt_score=file['score'].between(5,10)
# filt_view=file['viewcount']>=10000
# filt_umumiy=filt_score|filt_view
# file[filt_umumiy]




# # Find all questions that are not answered by Scott Boston
# scott_boston=file['ans_name']=='Scott Boston'
# file[~scott_boston]


# Homework 3:

# Titanic data set, stored as CSV. The data consists of the following data columns:
# PassengerId: Id of every passenger.
# Survived: Indication whether passenger survived. 0 for yes and 1 for no.
# Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
# Name: Name of passenger.
# Sex: Gender of passenger.
# Age: Age of passenger in years.
# SibSp: Number of siblings or spouses aboard.
# Parch: Number of parents or children aboard.
# Ticket: Ticket number of passenger.
# Fare: Indicating the fare.
# Cabin: Cabin number of passenger.
# Embarked: Port of embarkation.

import pandas as pd 
read=pd.read_csv('titanic.csv')
read


# # Select Female Passengers in Class 1 with Ages between 20 and 30:
# #  Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

# filt_sex=read['Sex']=='female'
# filt_age=read['Age'].between(20,30)
# filt_res=filt_sex&filt_age
# read[filt_res]




# # Filter Passengers Who Paid More than $100:
# # Create a DataFrame with passengers who paid a fare greater than $100.

# filt_fare=read['Fare']>=100
# read[filt_fare]




# # Select Passengers Who Survived and Were Alone:
# #  Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

# filt_sur=read['Survived']==1
# filt_age=read['SibSp']==0
# filt_age1=read['Parch']==0
# filt_res=filt_sur&filt_age&filt_age1
# read[filt_res]




# # Filter Passengers Embarked from 'C' and Paid More Than $50:
# #  Create a DataFrame with passengers who embarked from 'C' and paid more than $50.


# filt_sur=read['Embarked']=='C'
# filt_fare=read['Fare']>=50
# filt_um=filt_sur&filt_fare
# read[filt_um]




# # Select Passengers with Siblings or Spouses and Parents or Children:
# #  Extract passengers who had both siblings or spouses aboard and parents or children aboard.

# filt_sbp=read['SibSp']==1
# filt_pch=read['Parch']==1
# filt_um=filt_sbp&filt_pch
# read[filt_um]



# # Filter Passengers Aged 15 or Younger Who Didn't Survive:
# #  Create a DataFrame with passengers aged 15 or younger who did not survive.

# filt_age=read['Age']<=15
# filt_surv=read['Survived']=0
# filt_um=filt_age|filt_surv
# read[filt_um]




# # Select Passengers with Cabins and Fare Greater Than $200:
# #  Extract passengers with known cabin numbers and a fare greater than $200.

# filt_age=read['Age']>=200
# filt_cbn=read['Cabin'].notna()

# filt_um=filt_age&filt_cbn
# read[filt_um]



# # Filter Passengers with Odd-Numbered Passenger IDs: 
# # Create a DataFrame with passengers whose PassengerId is an odd number.

# filt_pid=read['PassengerId']%2==0
# read[filt_pid]





# # Select Passengers with Unique Ticket Numbers:
# #  Extract a DataFrame with passengers having unique ticket numbers.

# un_ticket=read['Ticket'].value_counts()
# tickets=un_ticket[un_ticket==1]
# tickets





# Filter Passengers with 'Miss' in Their Name and Were in Class 1:
#  Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.




miss=read['Name'].str.contains('Miss')
read[miss]
