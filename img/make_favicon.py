from jutility import plotting

def make_icon(
    dpi: float,
    name: str,
):
    mp = plotting.MultiPlot(
        plotting.Subplot(
            plotting.Circle(
                [0, 0],
                1,
                ec=None,
                fc="#000050",
            ),
            plotting.Text(
                *[0, -0.15],
                "J",
                fs=200,
                fontfamily="monospace",
                c="#fefae0",
            ),
            xlim=[-1, 1],
            ylim=[-1, 1],
            axis_square=True,
            axis_off=True,
        ),
        colour="#00000000",
        pad=0,
        figsize=[4, 4],
        dpi=dpi,
    )
    mp.save(name, "img")

make_icon(32/4, "favicon")
make_icon(144/4, "icon_144")
make_icon(160, "icon_large")
