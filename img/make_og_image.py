from jutility import plotting

dark_blue = [0, 0, 0x50]
black = [0, 0, 0]

mp = plotting.MultiPlot(
    plotting.Subplot(
        plotting.ImShow(
            [[black, black], [dark_blue, dark_blue]],
            interpolation="bicubic",
            aspect="auto",
            extent=[-1, 1, -1, 1],
        ),
        plotting.Text(
            *[0, -0.15],
            "J",
            fs=200,
            fontfamily="monospace",
            c="#fefae0",
        ),
    ),
    pad=0,
    figsize=[6, 4],
    dpi=160,
)
mp.save("og_image", "img")
