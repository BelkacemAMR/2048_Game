import matplotlib
import numpy as np
import matplotlib.pyplot as plt

#Initialisation des données:
import numpy as np
import matplotlib.pyplot as plt
up = 10
down = 30
left = 60
right = 100

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

data = [up,
          down,
          left,
          right]

Bouton = "up", "down", "left", "right"

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} push)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, Bouton,
          title="Bouton",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("% de push sur les boutons directionelles lors d'une session de jeu 2048")

plt.show()

#########################################################################################################################################################
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(data[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("% de push sur les boutons directionelles lors d'une session de jeu 2048")

plt.show()

######################################################################################################################################
fig, ax = plt.subplots()

Directions = ['Up', 'Down', 'Left', 'Right']

bar_labels = ['Up', 'Down', 'Left', 'Right']
bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(Directions, data, label=bar_labels, color=bar_colors)

ax.set_ylabel('Nbre de push')
ax.set_title('Boutons ')
ax.legend(title='Nbre de Push sur les touches directionelles')

plt.show()

###########################################################################################################################"

data = {'Up': up, 'Down': down, 'Left': left, 'Right': right}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle("Nbre de pushs lors d'une cession de jeu de 2048")


###############################################################################
# Cela fonctionne sur les deux axes:
data1 = [up, down, left,  right]

activity = ["Up", "Down", "Left", "Right"]

fig, ax = plt.subplots()
ax.plot(activity,data1, label="Joueur1")
#ax.plot(activity, data, label="Joeurs2")
ax.legend (title="Nbre de pushs lors d'une cession de jeu de 2048")

plt.show()
