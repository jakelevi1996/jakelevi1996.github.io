from jutility import plotting

dark_blue = [0, 0, 0x50]
black = [0, 0, 0]

mp = plotting.MultiPlot(
    plotting.Subplot(
        plotting.Text(
            *[0, -0.15],
            "JL",
            fs=200,
            fontfamily="monospace",
            c="#fefae0",
        ),
        xlim=[-1, 1],
        ylim=[-1, 1],
        axis_off=True,
    ),
    colour="#001100",
    pad=0,
    figsize=[6, 4],
    dpi=160,
)
mp.save("og_image", "img")
