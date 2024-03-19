import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

x=np.array([7,5,2])
y=np.array([4,3,7])
z=np.array([9,2,1])
w=np.array([6,8,3])
points={'x':x,'y':y,'z':z,'w':w}
for i in points:
    for j in points:
        if i!=j:
            print(f'r({i},{j})={np.linalg.norm(points[i]-points[j])} - расстояние Евклида')
            print(f'r({i},{j})={np.linalg.norm(points[i] - points[j])**2} - квадрат Евклидова расстояния')
            print(f'r({i},{j})={np.linalg.norm(points[i] - points[j],ord=np.inf)} - расстояние Чебышева')
            print(f'r({i},{j})={np.linalg.norm(points[i] - points[j],ord=1)} - расстояние Хемминга')
ax.scatter(*x)
ax.scatter(*y)
ax.scatter(*z)
ax.scatter(*w)
plt.show()