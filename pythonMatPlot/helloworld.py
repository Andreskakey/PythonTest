from matplotlib import pyplot as plt
from matplotlib import style 


style.use ('ggplot')

y = [2,4,5,7]
x = [6,3,10,5]

x2= [2,6,4,1]
y2= [7,1,9,7]

plt.bar(x,y,color='c', align= 'center')
plt.bar(x2,y2,color='g', align= 'center')

plt.title('test chart')
plt.ylabel ('y axis')
plt.xlabel ('x axis')
plt.show()
