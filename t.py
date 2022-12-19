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
    #
    # Pattern 1
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
    ],
    #
    # Pattern 2
    "Amm-a": [  # "mm" for melodic minor
        (6, 5, 1),
        (6, 7, 3),
        (6, 8, 4),
        (5, 5, 1),
        (5, 7, 3),
        (5, 9, 1),
        (5, 11, 3),
        (5, 12, 4),
        (4, 9, 1),
        (4, 10, 2),
        (4, 12, 4),
        (3, 9, 1),
        (3, 11, 3),
        (2, 9, 1),
        (2, 10, 1),
        (2, 12, 3),
        (2, 13, 4),
        (1, 10, 1),
        (1, 12, 3),
        (1, 14, 1),
        (1, 16, 3),
        (1, 17, 4),
    ],
    "Am-d": [
        (1, 17, 4),
        (1, 15, 2),
        (1, 13, 4),
        (1, 12, 3),
        (1, 10, 1),
        (2, 13, 4),
        (2, 12, 3),
        (2, 10, 1),
        (3, 12, 3),
        (3, 10, 1),
        (3, 9, 3),
        (3, 7, 1),
        (4, 10, 4),
        (4, 9, 3),
        (4, 7, 1),
        (5, 10, 4),
        (5, 8, 2),
        (5, 7, 1),
        (6, 10, 4),
        (6, 8, 4),
        (6, 7, 3),
        (6, 5, 1),
    ],
    #
    # Pattern 3
    "G-a": [
        (6, 3, 2),
        (6, 5, 4),
        (5, 2, 1),
        (5, 3, 2),
        (5, 5, 4),
        (4, 2, 1),
        (4, 4, 3),
        (4, 5, 4),
        (3, 2, 1),
        (3, 4, 3),
        (3, 5, 1),
        (3, 7, 3),
        (2, 5, 1),
        (2, 7, 3),
        (2, 8, 4),
        (1, 5, 1),
        (1, 7, 3),
        (1, 8, 1),
        (1, 10, 3),
        (1, 12, 1),
        (1, 14, 3),
        (1, 15, 4),
    ],
    "G-d": [
        (1, 15, 4),
        (1, 14, 3),
        (1, 12, 1),
        (1, 10, 4),
        (1, 8, 2),
        (1, 7, 1),
        (2, 10, 4),
        (2, 8, 2),
        (2, 7, 1),
        (3, 9, 3),
        (3, 7, 1),
        (4, 10, 4),
        (4, 9, 3),
        (4, 7, 1),
        (5, 10, 4),
        (5, 9, 3),
        (5, 7, 1),
        (5, 5, 4),
        (5, 3, 2),
        (5, 2, 1),
        (6, 5, 4),
        (6, 3, 2),
    ],
}

# Pattern 1 is also used for D, Db, Eb
for tonic, delta in [("D", 2), ("Db", 1), ("Eb", 3)]:
    data[f"{tonic}-a"] = [(string, fret + delta, finger) for string, fret, finger in data["C-a"]]

# For Pattern 1, desc is just asc in reverse
for tonic in ["C", "D", "Db", "Eb"]:
    data[f"{tonic}-d"] = data[f"{tonic}-a"][::-1]

# Pattern 2 is also used for F#, G#, F, G
for tonic, delta in [("F#", -3), ("G#", -1), ("F", -4), ("G", -2)]:
    data[f"{tonic}mm-a"] = [
        (string, fret + delta, finger) for string, fret, finger in data["Amm-a"]
    ]
    data[f"{tonic}m-d"] = [(string, fret + delta, finger) for string, fret, finger in data["Am-d"]]

# Pattern 3 is also used for A, B, F#, Ab, Bb
for tonic, delta in [("A", 2), ("B", 4), ("F#", -1), ("Ab", 1), ("Bb", 3)]:
    data[f"{tonic}-a"] = [(string, fret + delta, finger) for string, fret, finger in data["G-a"]]
    data[f"{tonic}-d"] = [(string, fret + delta, finger) for string, fret, finger in data["G-d"]]


# %% Plot

which = "Bb-a"

assert which[-2:] in {"-a", "-d"}, "ascending or descending"
ascending = which.endswith("-a")

fig, ax = plt.subplots(figsize=(10, 3.2))

# Frets
fret_lims = (0, 19)
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
nstrings = 6
for y in range(1, nstrings + 1):
    ax.axhline(y, c="silver", lw=1 + 0.4 * y, zorder=1)

# Segovia
vals = [4, 11, 7, 2, 9, 4]
radius = 0.4
kwargs = dict(zorder=10, clip_on=False)
prev_string = prev_finger = None
v0 = None
n = None  # scale degree
for string, fret, finger in data[which]:
    x, y = fret - 0.5, string

    v = vals[string - 1] + fret

    if v0 is None:
        v0 = v

    if v % 12 == v0 % 12:  # reset
        n = 1

    color = "0.65" if v % 12 == v0 % 12 else "0.2"
    if (
        prev_string is not None
        and prev_finger is not None
        and string == prev_string
        and (finger <= prev_finger if ascending else finger >= prev_finger)
    ):
        # Must have shifted
        s = 2 / math.sqrt(3) * radius * 2 * 0.9
        sgn = -1  # +1 for pointing down
        p = mpl.patches.Polygon(
            [(x - s / 2, y - sgn * radius), (x, y + sgn * radius), (x + s / 2, y - sgn * radius)],
            closed=True,
            color=color,
            **kwargs,
        )
    else:
        p = mpl.patches.Circle((x, y), radius=radius, color=color, **kwargs)
    ax.add_patch(p)

    ax.text(x, y, finger, ha="center", va="center", color="w", size=16, zorder=20)
    ax.text(x, y + 0.3, n, ha="center", va="center", color="w", size=8, zorder=20)

    prev_string = string
    prev_finger = finger
    n += 1

edge_space = 0.23
d = 0.01
ax.text(
    fret_lims[-1] - d - edge_space,
    nstrings - d,
    which,
    va="bottom",
    ha="right",
    size=18,
    bbox=dict(facecolor="0.7", alpha=0.7),
)

ax.axis("scaled")

ax.set_xlim(fret_lims)
ax.set_ylim((6 + edge_space, 1 - edge_space))

# Remove ax labels
ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())

plt.show()


# %% Save figs?

# from savefigs import savefigs; savefigs(formats=["svg", "png"])
