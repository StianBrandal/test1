
import numpy as np
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt

luftTemp = pd.read_excel(r"C:/Users/stian/OneDrive/Documents/Skule/ADA501/Øvinger/Øving 2/LuftTemperature.xlsx")
tempOverF = pd.read_excel(r"C:/Users/stian/OneDrive/Documents/Skule/ADA501/Øvinger/Øving 2/temperatur.xlsx")


luftTempA = luftTemp["Lufttemperatur"]
tempOverFA = tempOverF["Temperatur: 0.5m"]
timeA = tempOverF["Tid"]
n = luftTemp["Nr"]

# 2 A
# plt.xlabel("Time")
# plt.ylabel("temperature")

# plt.plot(timeA,luftTempA,color="b",
#          marker='o', markerfacecolor='blue', markersize=12)
# plt.plot(timeA,tempOverFA,color="r",
#          marker='o', markerfacecolor='red', markersize=12)

# plt.grid(True)
# plt.show()


#2 B

plt.xlabel("Temperature 0.5m")
plt.ylabel("Air temperature")


plt.scatter(luftTempA,tempOverFA)
plt.show()
# plt.plot(timeA,tempOverFA,label="surface Temp",
#          marker='o', markerfacecolor='blue', markersize=12)


#m, b = np.polyfit(luftTempA,tempOverFA,1)
#plt.plot(luftTempA,m*luftTempA+b)

coeff = np.polyfit(luftTempA,tempOverFA,deg=3) 
print(coeff)
functionA = np.poly1d(coeff)
print(functionA)


xx=np.linspace(10,20,1000)
yy=functionA(xx)



plt.scatter(luftTempA,tempOverFA,color="black",s=100,label="datapoints")
plt.plot(xx,yy,color="blue",label="fitted line")

plt.legend()

plt.title("A simple graph2")




plt.grid(True)
plt.show()




# 2  C
# plt.plot(luftTempA,tempOverFA,"o")
# m, b = np.polyfit(tempOverFA,luftTempA,1)
# plt.plot(luftTempA,m*tempOverFA+b)

# plt.grid(True)
# plt.show()