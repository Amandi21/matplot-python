import matplotlib.pyplot as plt
import pandas as np


b = [1,0,0,1] 
a = np.array(b)
a = a.reshape(2,2)
print(a) 
c = [2,0]
a = np.array(c)

print(a)
x = [1,2,3,4,5]
y = [6,7,8,9,10]

xp = np.array(x)
yp = np.array(y)



plt.plot(xp,yp)
plt.show()