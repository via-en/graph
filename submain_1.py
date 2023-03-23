import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

plt.title("График")
plt.xlabel("t(ч)")
plt.ylabel("S(км)")

x1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y1 = np.array([0, 24, 48, 72, 96, 120, 144, 168, 192, 216])

plt.plot(x1, y1, linewidth=2, markersize=20,  label="Графиня Винтер")

x2 = np.array([2, 3, 4, 5, 6, 7, 8])
y2 = np.array([0, 36, 72, 108, 140, 176, 212])

plt.plot(x2, y2, linewidth=2, markersize=20,  label="Мушкетеры")

plt.grid(color='green', linestyle='--', linewidth=1)

first_line = LineString(np.column_stack((x1, y1)))
second_line = LineString(np.column_stack((x2, y2)))
intersection = first_line.intersection(second_line)

if intersection.geom_type == 'MultiPoint':
    plt.plot(*LineString(intersection).xy, 'o')
elif intersection.geom_type == 'Point':
    plt.plot(*intersection.xy, 'o', color='grey')
    plt.plot([intersection.x, intersection.x], [intersection.y, 0], linestyle='--', color='grey', lw=2)
    plt.plot([0, intersection.x], [intersection.y, intersection.y], linestyle='--', color='grey', lw=2)
    plt.annotate('('+str(intersection.x)[0:4]+','+str(int(intersection.y))+')', [intersection.x + 0.3, intersection.y - 5])

plt.legend()
plt.savefig("plots/myplot_1.png")
plt.show()
