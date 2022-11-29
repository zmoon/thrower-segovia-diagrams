"""
Created on Mon Nov 28 18:56:27 2022

@author: zmoon
"""
# from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.close("all")

# Matplotlib settings
plt.rcParams.update(
    {
        "figure.autolayout": True,
        "axes.formatter.limits": (-3, 4),  # scilimits
        "axes.formatter.use_mathtext": True,
    }
)


# %% Data

data = {
    "C-a": [
        # string, fret, finger
        (5, 3, 2),
        (5, 5, 4),
        (4, 2, 1),
        (4, 3, 2),
        (4, 5, 4),
        (3, 2, 1),
        (3, 4, 3),
        (3, 5, 1),
        (3, 7, 3),
        (2, 5, 1),
        (2, 6, 2),
        (2, 8, 4),
        (1, 5, 1),
        (1, 7, 3),
        (1, 8, 4),
    ]
}


# %% Plot

fig, ax = plt.subplots(figsize=(8, 3.2))


# Frets
fret_lims = (0, 13)
for x in range(*fret_lims):
    ax.axvline(x, color="0.7", zorder=0)

# Markers
kwargs = dict(radius=0.2, color="0.8")
for x in range(*fret_lims):
    if x in {3, 5, 7, 9, 15, 17, 19}:
        p = mpl.patches.Circle((x - 0.5, 3.5), **kwargs)
        ax.add_patch(p)
    elif x == 12:
        for y in [2.5, 4.5]:
            p = mpl.patches.Circle((x - 0.5, y), **kwargs)
            ax.add_patch(p)
    else:
        pass

# Strings
for y in range(1, 7):
    ax.axhline(y, c="silver", lw=1 + 0.4 * y, zorder=1)

# Segovia
for string, fret, finger in data["C-a"]:
    x, y = fret - 0.5, string
    p = mpl.patches.Circle((x, y), radius=0.4, color="0.2", zorder=10, clip_on=False)
    ax.add_patch(p)

    ax.text(x, y, finger, ha="center", va="center", color="w", size=16, zorder=20)


ax.axis("scaled")

ax.set_xlim(fret_lims)
d = 0.23
ax.set_ylim((6 + d, 1 - d))


# %% Save figs?

# from savefigs import savefigs; savefigs(formats=["svg"])
