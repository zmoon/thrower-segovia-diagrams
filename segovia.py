"""
Fretboard diagrams for the Segovia Scales
"""
from functools import lru_cache


@lru_cache(1)
def load_data():
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
        #
        # Pattern 4
        "Emm-a": [
            (6, 0, None),
            (6, 2, 1),
            (6, 3, 2),
            (6, 5, 4),
            (5, 2, 1),
            (5, 4, 3),
            (5, 6, 3),
            (5, 7, 4),
            (4, 4, 1),
            (4, 5, 2),
            (4, 7, 4),
            (4, 9, 2),
            (4, 11, 4),
            (3, 8, 1),
            (3, 9, 2),
            (3, 11, 4),
            (2, 8, 1),
            (2, 10, 3),
            (2, 12, 2),
            (2, 14, 4),
            (1, 11, 1),
            (1, 12, 2),
        ],
        "Em-d": [
            (1, 12, 2),
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
            (6, 2, 1),
            (6, 0, None),
        ],
        #
        # Pattern 5
        "Bmm-a": [
            (5, 2, 1),
            (5, 4, 3),
            (5, 5, 4),
            (4, 2, 1),
            (4, 4, 3),
            (4, 6, 1),
            (4, 8, 3),
            (4, 9, 1),
            (4, 11, 3),
            (4, 12, 4),
            (3, 9, 1),
            (3, 11, 3),
            (2, 9, 1),
            (2, 11, 3),
            (2, 12, 1),
            (2, 14, 3),
            (2, 15, 4),
            (1, 12, 1),
            (1, 14, 3),
            (1, 16, 1),
            (1, 18, 3),
            (1, 19, 4),
        ],
        "Bm-d": [
            (1, 19, 4),
            (1, 17, 2),
            (1, 15, 4),
            (1, 14, 3),
            (1, 12, 1),
            (2, 15, 4),
            (2, 14, 3),
            (2, 12, 1),
            (2, 10, 4),
            (2, 8, 2),
            (2, 7, 1),
            (2, 5, 4),
            (2, 3, 2),
            (2, 2, 1),
            (3, 4, 3),
            (3, 2, 1),
            (4, 5, 4),
            (4, 4, 3),
            (4, 2, 1),
            (5, 5, 4),
            (5, 4, 3),
            (5, 2, 1),
        ],
        #
        # Pattern 6
        "E-a": [
            (6, 0, None),
            (6, 2, 1),
            (6, 4, 3),
            (6, 5, 4),
            (5, 2, 1),
            (5, 4, 1),
            (5, 6, 3),
            (5, 7, 4),
            (4, 4, 1),
            (4, 6, 3),
            (4, 7, 4),
            (3, 4, 1),
            (3, 6, 3),
            (2, 4, 1),
            (2, 5, 2),
            (2, 7, 4),
            (1, 4, 1),
            (1, 5, 2),
            (1, 7, 4),
            (1, 9, 1),
            (1, 11, 3),
            (1, 12, 4),
        ],
        "E-d": [
            (1, 12, 4),
            (1, 11, 3),
            (1, 9, 1),
            (1, 7, 4),
            (1, 5, 2),
            (1, 4, 1),
            (2, 7, 4),
            (2, 5, 2),
            (2, 4, 1),
            (3, 6, 3),
            (3, 4, 1),
            (4, 7, 4),
            (4, 6, 3),
            (4, 4, 1),
            (5, 7, 4),
            (5, 6, 3),
            (5, 4, 1),
            (5, 2, 1),
            (6, 5, 4),
            (6, 4, 3),
            (6, 2, 1),
            (6, 0, None),
        ],
        #
        # Pattern 7
        "C#mm-a": [
            (5, 4, 1),
            (5, 6, 3),
            (5, 7, 4),
            (4, 4, 1),
            (4, 6, 3),
            (4, 8, 1),
            (4, 10, 3),
            (4, 11, 4),
            (3, 8, 1),
            (3, 9, 2),
            (3, 11, 4),
            (2, 9, 2),
            (2, 11, 4),
            (1, 8, 1),
            (1, 9, 2),
        ],
        "C#m-d": [
            (1, 9, 2),
            (1, 7, 4),
            (1, 5, 2),
            (1, 4, 1),
            (2, 7, 4),
            (2, 5, 2),
            (2, 4, 1),
            (3, 6, 3),
            (3, 4, 1),
            (4, 7, 4),
            (4, 6, 3),
            (4, 4, 1),
            (5, 7, 4),
            (5, 6, 3),
            (5, 4, 1),
        ],
        #
        # Pattern 8
        "F-a": [
            (6, 1, 1),
            (6, 3, 3),
            (5, 0, None),
            (5, 1, 1),
            (5, 3, 3),
            (5, 5, 1),
            (5, 7, 3),
            (5, 8, 4),
            (4, 5, 1),
            (4, 7, 3),
            (4, 8, 4),
            (3, 5, 1),
            (3, 7, 3),
            (2, 5, 1),
            (2, 6, 2),
            (2, 8, 4),
            (1, 5, 1),
            (1, 6, 2),
            (1, 8, 4),
            (1, 10, 1),
            (1, 12, 3),
            (1, 13, 4),
        ],
    }

    # Pattern 1 is also used for D, Db, Eb
    for tonic, delta in [("D", 2), ("Db", 1), ("Eb", 3)]:
        data[f"{tonic}-a"] = [
            (string, fret + delta, finger) for string, fret, finger in data["C-a"]
        ]

    # For Pattern 1, desc is just asc in reverse
    for tonic in ["C", "D", "Db", "Eb"]:
        data[f"{tonic}-d"] = data[f"{tonic}-a"][::-1]

    # Pattern 2 is also used for F#, G#, F, G
    for tonic, delta in [("F#", -3), ("G#", -1), ("F", -4), ("G", -2)]:
        data[f"{tonic}mm-a"] = [
            (string, fret + delta, finger) for string, fret, finger in data["Amm-a"]
        ]
        data[f"{tonic}m-d"] = [
            (string, fret + delta, finger) for string, fret, finger in data["Am-d"]
        ]

    # Pattern 3 is also used for A, B, F#, Ab, Bb
    for tonic, delta in [("A", 2), ("B", 4), ("F#", -1), ("Ab", 1), ("Bb", 3)]:
        data[f"{tonic}-a"] = [
            (string, fret + delta, finger) for string, fret, finger in data["G-a"]
        ]
        data[f"{tonic}-d"] = [
            (string, fret + delta, finger) for string, fret, finger in data["G-d"]
        ]

    # Pattern 5 is also used for Bb
    for tonic, delta in [("Bb", -1)]:
        data[f"{tonic}mm-a"] = [
            (string, fret + delta, finger) for string, fret, finger in data["Bmm-a"]
        ]
        data[f"{tonic}m-d"] = [
            (string, fret + delta, finger) for string, fret, finger in data["Bm-d"]
        ]

    # Pattern 7 is also used for D#, C, D
    for tonic, delta in [("D#", 2), ("C", -1), ("D", 1)]:
        data[f"{tonic}mm-a"] = [
            (string, fret + delta, finger) for string, fret, finger in data["C#mm-a"]
        ]
        data[f"{tonic}m-d"] = [
            (string, fret + delta, finger) for string, fret, finger in data["C#m-d"]
        ]

    # Pattern 8 desc is just asc in reverse
    for tonic in ["F"]:
        data[f"{tonic}-d"] = data[f"{tonic}-a"][::-1]

    assert len(data) == 48, "major/minor, asc/dec (12 * 2 * 2 = 48)"

    return data


def _sort_scale_key_key(s):
    import re

    m = re.fullmatch(r"([A-G])([#b]?)(m{,2}?)\-([ad])", s)
    if m is None:
        raise ValueError(f"Bad scale key: {s!r}")

    nat, acc, minor, asc_desc = m.groups()

    iacc = 0
    if acc:
        iacc = "#b".index(acc) + 1

    return (
        "CDEFGAB".index(nat),
        iacc,
        1 if minor else 0,
        1 if asc_desc == "d" else 0,
    )


def plot_scale(
    which,
    *,
    ax=None,
    finger_label_size=16,
    cell_aspect=1.0,
    edge_space=0.23,
    show_which=True,
):
    import math

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    data = load_data()
    if which not in data:
        raise ValueError(
            f"Unrecognized scale: {which}. "
            f"Valid options are: {', '.join(sorted(data, key=_sort_scale_key_key))}. "
            "That is, -a for ascending, -d for descending, "
            "m for minor (only descending), mm for melodies minor (only ascending)."
        )

    if cell_aspect > 1:
        raise ValueError("cell_aspect (y/x for fretboard grid cells) > 1 not supported")

    assert which[-2:] in {"-a", "-d"}, "[a]scending or [d]escending"
    ascending = which.endswith("-a")

    if ax is None:
        _, ax = plt.subplots(figsize=(10 / cell_aspect, 3.2))

    # Frets
    fret_lims = (0, 19)
    for x in range(*fret_lims):
        ax.axvline(x, color="0.7", zorder=0)

    # Markers
    kwargs = dict(width=0.4 * cell_aspect, height=0.4, color="0.8")
    for x in range(*fret_lims):
        if x in {3, 5, 7, 9, 15, 17, 19}:
            p = mpl.patches.Ellipse((x - 0.5, 3.5), **kwargs)
            ax.add_patch(p)
        elif x == 12:
            for y in [2.5, 4.5]:
                p = mpl.patches.Ellipse((x - 0.5, y), **kwargs)
                ax.add_patch(p)
        else:
            pass

    # Strings
    nstrings = 6
    for y in range(1, nstrings + 1):
        ax.axhline(y, c="silver", lw=1 + 0.4 * y, zorder=1)

    # Segovia
    vals = [4, 11, 7, 2, 9, 4]  # pitch class value wrt. C, string 1 (high E) to string 6 (low E)
    standard_radius = 0.4
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

        radius = standard_radius
        if fret == 0:  # Open string
            radius = standard_radius * 0.6
            x = fret
        color = "0.65" if v % 12 == v0 % 12 else "0.2"
        if (
            prev_string is not None
            and prev_finger is not None
            and string == prev_string
            and finger is not None
            and (finger <= prev_finger if ascending else finger >= prev_finger)
        ):
            # Must have shifted
            s = 2 / math.sqrt(3) * radius * 2 * 0.9 * cell_aspect
            sgn = -1  # +1 for pointing down
            p = mpl.patches.Polygon(
                [
                    (x - s / 2, y - sgn * radius),
                    (x, y + sgn * radius),
                    (x + s / 2, y - sgn * radius),
                ],
                closed=True,
                color=color,
                **kwargs,
            )
        else:
            p = mpl.patches.Ellipse(
                (x, y),
                width=2 * radius * cell_aspect,
                height=2 * radius,
                color=color,
                **kwargs,
            )
        ax.add_patch(p)

        ax.text(
            x,
            y,
            finger,
            ha="center",
            va="center",
            color="w",
            size=finger_label_size,
            zorder=20,
        )
        ax.text(
            x,
            y + 0.3 * radius / standard_radius,
            n,
            ha="center",
            va="center",
            color="w",
            size=finger_label_size // 2,
            zorder=20,
        )

        prev_string = string
        prev_finger = finger
        n += 1

    d = 0.01
    if show_which:
        ax.text(
            fret_lims[-1] - d - edge_space,
            nstrings - d,
            which,
            va="bottom",
            ha="right",
            size=int(1.125 * finger_label_size),
            bbox=dict(facecolor="0.7", alpha=0.7),
        )

    ax.axis("scaled")
    ax.set_aspect(cell_aspect)

    ax.set_xlim(fret_lims)
    ax.set_ylim((6 + edge_space, 1 - edge_space))

    # Remove ax labels
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.close("all")

    # Matplotlib settings
    plt.rcParams.update(
        {
            "figure.autolayout": True,
            "axes.formatter.limits": (-3, 4),  # scilimits
            "axes.formatter.use_mathtext": True,
            "axes.titlesize": 8,
        }
    )

    cases = [
        # scale key, ax title
        ("C-a", "Pattern 1 -- C, D, Db, Eb\nAscending"),
        ("Amm-a", "Pattern 2 -- Am, F#m, G#m, Fm, Gm\nAscending"),
        ("C-d", "Descending"),
        ("Am-d", "Descending"),
        ("G-a", "\nPattern 3 -- G, A, B, F#, Ab, Bb\nAscending"),
        ("Emm-a", "\nPattern 4 -- Em\nAscending"),
        ("G-d", "Descending"),
        ("Em-d", "Descending"),
        ("Bmm-a", "\nPattern 5 -- Bm, Bbm\nAscending"),
        ("E-a", "\nPattern 6 -- E\nAscending"),
        ("Bm-d", "Descending"),
        ("E-d", "Descending"),
        ("C#mm-a", "\nPattern 7 -- C#m, D#m, Cm, Dm\nAscending"),
        ("F-a", "\nPattern 8 -- F\nAscending"),
        ("C#m-d", "Descending"),
        ("F-d", "Descending"),
    ]

    assert len(cases) == 16
    assert len(cases) % 2 == 0
    fig, axs = plt.subplots(len(cases) // 2, 2, figsize=(6.8, 8.85), constrained_layout=True)

    for (which, title), ax in zip(cases, axs.flat):
        plot_scale(
            which,
            ax=ax,
            finger_label_size=8,
            cell_aspect=0.88,
            edge_space=0,
            show_which=False,
        )
        title_ = title.replace("--", "\u2013").replace("#", "\u266f").replace("b", "\u266d")
        ax.set_title(title_)

    fig.get_layout_engine().set(w_pad=4 / 72, wspace=0.2)

    fig.savefig("all-patterns.svg", bbox_inches="tight", pad_inches=0, transparent=True)

    plt.show()
