import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
from scipy.stats import linregress
import statsmodels.api as sm

svalvard_met = pd.read_csv("C:/Users/stian/OneDrive/Documents/Skule/ADA501/Øvinger/Øving 2/svalbard_met.csv", sep=";", decimal=",") # "Homogenisert middeltemperatur (mnd)":np.float64 , "Homogenisert middeltemperatur (mnd)":str}


svalvard_met['Tid(norsk normaltid)'] = pd.to_datetime(svalvard_met['Tid(norsk normaltid)'],format="%m.%Y")
svalvard_met['Tid(norsk normaltid)']=svalvard_met['Tid(norsk normaltid)'].map(dt.datetime.toordinal)


dates = svalvard_met["Tid(norsk normaltid)"]
temp = svalvard_met["Homogenisert middeltemperatur (mnd)"] 


# for i in range(1,len(temp)) :
#     #print(temp.loc[i])
#     tempvar = (temp.loc[i])
#     print(tempvar,"hi am her")
#     if tempvar == "NAN":
#         counter +=1




# print(svalvard_met)
# testVar = (temp.loc[[10]])
# print(testVar)
# print(type(temp.loc[[10]]))
# for i in range(len(temp)):
#     print(temp.loc[[i]])


plt.scatter(dates,temp)
plt.show()

slope, intercept, r, p, se = linregress(dates, temp)
result = linregress(dates, temp)
print(result)
print(result.slope, result.intercept_stderr)






# coeff = np.polyfit(dates,temp,deg=1) 
# print(coeff)
# functionA = np.poly1d(coeff)
# print(functionA)


# xx=np.linspace(10,20,1000)
# yy=functionA(xx)



# plt.scatter(dates,temp,color="black",s=100,label="datapoints")
# plt.plot(xx,yy,color="blue",label="fitted line")
# plt.legend()
# plt.title("A simple graph2")
# plt.grid(True)
# plt.show()








# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m.%Y'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=12))
# #plt.grid(True)
# plt.ylabel("Temperature")
# plt.xlabel('year')
# plt.scatter(datesString,temp)
# plt.gcf().autofmt_xdate()
# plt.show()








# dateString = []
# print(type(dates))
# for i in dates:
#     dateString.append(str(i))

# for j in range(len(dateString)):
#     dateString[j] = dateString[j].replace(".","-")

# dateString = pd.to_datetime(dateString)
# lastPoint = dateString.map(dt.datetime.toordinal)

# #replacedString[0] = dateString[1].replace(".","-")
# print(lastPoint)













# #svalvard_met['Tid(norsk normaltid)'] = pd.to_datetime(svalvard_met['Tid(norsk normaltid)'])

# index = svalvard_met.set_index('Homogenisert middeltemperatur (mnd)', inplace=False)

# print(index)
# #X = sm.add_constant(svalvard_met.index.to_julian_date())
# #print(X)
# datesString = []
# for i in dates:
#     datesString.append(str(i))

# # plt.plot(svalvard_met.index, svalvard_met['Homogenisert middeltemperatur (mnd)'], label='Value')
# # plt.show()
# #x= np.array(pd.to_datetime(svalvard_met['Tid(norsk normaltid)']).index.values, dtype=float)

# #result = linregress(temp, dates)

