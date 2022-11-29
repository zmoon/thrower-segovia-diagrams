"""
Created on Mon Nov 28 18:56:27 2022

@author: zmoon
"""
import math

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
vals = [4, 11, 7, 2, 9, 4]
radius = 0.4
kwargs = dict(zorder=10, clip_on=False)
prev_string = prev_finger = None
v0 = None
for string, fret, finger in data["C-a"]:
    x, y = fret - 0.5, string

    v = vals[string - 1] + fret

    if v0 is None:
        v0 = v

    color = "0.65" if v % 12 == v0 % 12 else "0.2"
    if (
        prev_string is not None
        and prev_finger is not None
        and string == prev_string
        and finger <= prev_finger
    ):
        # Must have shifted
        s = 2 / math.sqrt(3) * radius * 2 * 0.9
        sgn = -1  # +1 for pointing down
        p = mpl.patches.Polygon(
            [(x - s / 2, y - sgn * radius), (x, y + sgn * radius), (x + s / 2, y - sgn * radius)],
            closed=True,
            color=color,
            **kwargs
        )
    else:
        p = mpl.patches.Circle((x, y), radius=radius, color=color, **kwargs)
    ax.add_patch(p)

    ax.text(x, y, finger, ha="center", va="center", color="w", size=16, zorder=20)

    prev_string = string
    prev_finger = finger

ax.axis("scaled")

ax.set_xlim(fret_lims)
d = 0.23
ax.set_ylim((6 + d, 1 - d))

# Remove ax labels
ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())


# %% Save figs?

# from savefigs import savefigs; savefigs(formats=["svg"])
