import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString


plt.title("График")
plt.xlabel("t(ч)")
plt.ylabel("S(км)")
# plt.xticks([9, 10, 11, 12])
# ax = plt.gca()
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))

x1 = np.array([9, 12])
y1 = np.array([0, 87])

plt.plot(x1, y1, linewidth=2, markersize=20,  label="Арамис")


x2 = np.array([9, 12])
y2 = np.array([124, 25.55])

plt.plot(x2, y2, linewidth=2, markersize=20,  label="Атос")

plt.grid(color='green', linestyle='--', linewidth=1)

first_line = LineString(np.column_stack((x1, y1)))
second_line = LineString(np.column_stack((x2, y2)))
intersection = first_line.intersection(second_line)

if intersection.geom_type == 'MultiPoint':
    plt.plot(*LineString(intersection).xy, 'o')
elif intersection.geom_type == 'Point':
    plt.plot(*intersection.xy, 'o', color='grey')
    plt.plot([intersection.x, intersection.x], [intersection.y, 0], linestyle='--', color='grey', lw=2)
    plt.plot([9, intersection.x], [intersection.y, intersection.y], linestyle='--', color='grey', lw=2)
    plt.annotate('('+str(int(intersection.x))+','+str(int(intersection.y))+')', [intersection.x - 0.1, intersection.y + 9])

plt.legend()
plt.savefig("plots/myplot.png")
plt.show()
