import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
#from adjustText import adjust_text

plt.title("График")
plt.xlabel("t(ч)")
plt.ylabel("S(км)")

x1 = np.array([0, 1, 2])
y1 = np.array([0, 42, 84])
plt.plot(x1, y1, linewidth=2, markersize=20, label="Мушкетеры")

x2 = np.array([0.167, 1.167, 2])
y2 = np.array([0, 48, 88])

plt.plot(x2, y2, linewidth=2, markersize=20,  label="Гвардейцы")
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
    plt.annotate('('+str(intersection.x)[0:4]+','+str(int(intersection.y))+')', [intersection.x + 0.05, intersection.y - 5])

plt.legend()
plt.savefig("plots/myplot_2.png")

plt.show()
