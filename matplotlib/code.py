# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)

loan_status = data['Loan_Status'].value_counts()

plt.figure(figsize=[14,8])
plt.xlabel('Status(Y/N)')
plt.ylabel('Counts')
plt.title("Plot of Status VS Counts")
plt.bar(loan_status.index,loan_status)


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()


property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
print(property_and_loan)


# --------------
#Code starts here


#Expensive Education
#Higher education has always been an expensive endeavour for people but it results in better career opportunities and stability in life. But does higher education result in a better guarantee in issuing loans?#

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))

plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here


#After seeing the loan status distribution, let's check whether being graduate or not also leads to different loan amount distribution by plotting an overlapping density plot of two values#

graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']

graduate.plot(kind='Density' , label ='Graduate')

not_graduate.plot(kind='Density' , label = 'Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
#For any finance institiution to be successful in it's loan lending system, there has to be a correlation between the borrower's income and loan amount he is lent. Let's see how our company fares in that respect:

#Creating 3 Subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Applicant Income')

ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')


data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_2.set_title('Total Income')




