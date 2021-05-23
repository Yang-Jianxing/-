import numpy as np
import matplotlib.pyplot as plt

x_coords = np.linspace(-100, 100, 500)
y_coords = np.linspace(-100, 100, 500)
points = []
for y in y_coords:
    for x in x_coords:
        if ((x*0.03)**2+(y*0.03)**2-1)**3-(x*0.03)**2*(y*0.03)**3 <= 0:
            points.append({"x": x, "y": y})
heart_x = list(map(lambda point: point["x"], points))
heart_y = list(map(lambda point: point["y"], points))

plt.scatter(heart_x, heart_y, s=10, alpha=0.5,c=range(len(heart_x)),cmap="Blues")
plt.show()
#改变颜色，cmap="颜色")
#<cmap="autumn"> 橙色的爱心送给热情洋溢的她
#<cmap="cool"> 紫色的爱心送给优雅宁静的她
#<cmap="magma"> 晚霞般的爱心送给醇厚脱俗的她
#<cmap="rainbow"> 彩虹般的爱心送给充满绚丽幻想的她
#<cmap="Reds"> 炽热的爱心送给热烈奔放的她
#<cmap="spring"> 青春的爱心送给充满朝气的她
#<cmap="viridis"> 翡翠色的爱心送给平静柔和的她
#<cmap="gist_rainbow"> 五彩缤纷的爱心送给多姿多彩的她
