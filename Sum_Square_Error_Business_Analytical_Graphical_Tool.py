# y=mx+c is the general equation of line
# formulation of sse is sse= summation of [(y(i)-x(i)]^2
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
from sympy import *
import point_predictor_calculus_excluding_complex_numbers as cp
#taking coordinates
n=int(input("Enter the number of total data points:"))
x=[]
y=[]
for i in range(1,n+1):
    print("Enter the value of X of data point ",i,end="")
    xe=float(input(":"))
    x.append(xe)
    print("Enter the value of Y of data point ",i,end="")
    ye=float(input(":"))
    y.append(ye)
print("Given coordinates dataset:")
for i in range(0,n):
    print("Point,",i+1,"= [",x[i],",",y[i],"]")

#graphing the given coordinates (initial coordinates)

plt.plot(x,y,'o',label="Initial Coordinates")
plt.title("Given Data coordinates")
plt.xlabel("x axis coordinates")
plt.ylabel("y axis coordinates")
plt.scatter(x,y)
plt.legend()
plt.show()

#taking the values of m and c (y= mx+c)
print("Enter the equation of the line for which to find the SSE of:")
print("Enter in y = m.x + c format")
m=float(input("Enter the value of M [slope] *to keep it by default enter 1: "))
c=float(input("Enter the value of C *to keep it by default enter 0 :"))
print("Given equation of line is: y = ",m,".x + ",c)

#ploting the given equation: ( line with initial coordinates)

px=np.linspace(min(x)-5, max(x)+5)
yp=m*px+c
plt.plot(x,y,'o')
taglinehead=m,"x + ",c
plt.plot(px,yp,color='r',linestyle='-',linewidth=0.8,label=taglinehead)
plt.legend(loc="upper left")
titles=("Initial coordinates with actual error with respect to line (mx+c)")
plt.xlabel("Coded by Om Podey")
plt.ylabel("Coded by Om Podey")
plt.title(titles)
plt.show()

#SSE
#creating error x coordinates
newtempx=[]
for temp in range(0,n):
    tempx=m*x[temp]+c
    newtempx.append(tempx)
print("Errored x asis coordinates",(newtempx))
#creating summations
ssesummations=[]
for mod in range(0,n):
    error_coordinate=(newtempx[mod]-y[mod])**2
    ssesummations.append(error_coordinate)
#Showing the errors with respect to line on graph: (line and initial coordinates)
print("Sum of Squared error for the given coordinates is = ",sum(ssesummations)," units.")

#Predicting the points over the lines which can minimize the error
#from predicting points file.
predicted_x,predicted_y=cp.find_points_over_equation(n,x,y,m,c)

#graping the error points and the predicted datapoints: (line, (intial, final) coordinates)
#converting the roots to float datatype:
plt.style.use('dark_background')
leftend=float(min(predicted_x))
rightend=float(max(predicted_x))
px=np.linspace((leftend) ,((rightend)))
yp=m*px+c
plt.plot(x,y,'o')
taglinehead=m,"x + ",c
plt.plot(px,yp,color='r',linestyle='-',linewidth=0.8)
plt.legend(loc="upper left")
titles=("Finall Predicted error distances from actuall data coordinates.")
plt.title(titles)
plt.plot(predicted_x, predicted_y,'o',color='r',label="predicted Coordinates")
plt.xlabel("Coded by Om Podey")
plt.ylabel("Coded by Om Podey")
plt.legend()
plt.show()
#joining the points with referece to predicted points and actuall points
plt.style.use('dark_background')
leftend=float(min(predicted_x))
rightend=float(max(predicted_x))
px=np.linspace((leftend) ,((rightend)))
yp=m*px+c
plt.plot(x,y,'o')
taglinehead=m,"x + ",c
plt.plot(px,yp,color='r',linestyle='-',linewidth=0.8)
plt.legend(loc="upper left")
titles=("Finall predicted error=",sum(ssesummations)," units")
plt.title(titles)
plt.plot(predicted_x, predicted_y,'o',color='r')
#prediction data-coordinates= predicted_x , predicted_y
#oringnial data-coordinates=x,y
plt.plot((x,predicted_x),(y,predicted_y),linestyle='--',label="Predicted Distance",color='w')
plt.xlabel("Coded by Om Podey")
plt.ylabel("Coded by Om Podey")
plt.legend()
plt.show()
















