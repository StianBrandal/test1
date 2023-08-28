
import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt

#https://www.kaggle.com/code/hamelg/python-for-data-21-descriptive-statistics/notebook         https://www.youtube.com/watch?v=3mELSEnGBvA&ab_channel=DataDaft

spring = pd.read_excel(r"C:/Users/stian/OneDrive/Documents/Skule/ADA501/Øvinger/Øving 2/spring.xlsx")

svalbard_met = pd.read_csv(r"C:/Users/stian/OneDrive/Documents/Skule/ADA501/Øvinger/Øving 2/svalbard_met.csv")



print(spring)
print(spring["x"])


meanX = spring["x"].mean()
meanY = spring["y"].mean()
print("Mean of X ", meanX)
print("Mean of X ", meanY)


standard_devX = statistics.stdev(spring["x"])
standard_devY = statistics.stdev(spring["y"])
print("Standard deviation of X  ",standard_devX)
print("Standard deviation of Y  ",standard_devY)


covMat = np.stack((spring["x"],spring["y"]),axis=0) # getting the x and y row from the excel file because if not when using np.cov on spring you get the first colum as well.
print("Cov = ",np.cov(covMat))



corr = np.corrcoef(covMat)
print("Cor =",  corr)



print("\n\n\n\n\n")

print(covMat[0])

xAxis =covMat[0] # [1,3,5,7] 
yAxis = covMat[1] #[2,4,6,1] #
# plt.plot(xAxis,yAxis)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# plt.title("A simple graph")
# #plt.show()

# #  Regression Lines,
# plt.plot(xAxis,yAxis,"o")
# plt.xlabel("X-axis2")
# plt.ylabel("Y-axis2")

# m, b = np.polyfit(xAxis,yAxis,1)
# plt.plot(xAxis,m*xAxis+b)
# plt.title("A simple graph2")
#plt.show()

# scatterplots 
# plt.scatter(xAxis,yAxis)
# plt.show()



# plt.hist()


#print(svalbard_met)