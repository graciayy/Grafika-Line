import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

line_awal = int(input("Masukkan jumlah line awal: "))

if line_awal < 2:
    line_awal = 2

line = line_awal


def gambar_kerucut(ax, line):
    radius = 1
    tinggi = 2

    theta = np.linspace(0, 2 * np.pi, line)
    z = np.linspace(0, tinggi, line)

    theta_grid, z_grid = np.meshgrid(theta, z)

    radius_grid = radius * (1 - z_grid / tinggi)

    x = radius_grid * np.cos(theta_grid)
    y = radius_grid * np.sin(theta_grid)

    ax.plot_wireframe(
        x, y, z_grid,
        color="black",
        linewidth=0.7
    )

    # Lingkaran dasar
    ax.plot(
        radius * np.cos(theta),
        radius * np.sin(theta),
        0,
        color="black"
    )


def generate():
    ax.clear()

    gambar_kerucut(ax, line)

    ax.set_title("KERUCUT")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(0, 2.5)

    ax.set_box_aspect((1, 1, 1.5))
    ax.grid(True)

    teks_line.set_text(f"Jumlah Line : {line}")

    fig.canvas.draw_idle()


def tambah_line(event):
    global line

    line += 1
    generate()


def kurang_line(event):
    global line

    if line > 2:
        line -= 1
        generate()


def reset_line(event):
    global line

    line = line_awal
    generate()


fig = plt.figure(figsize=(8, 8))

ax = fig.add_axes(
    [0.08, 0.18, 0.84, 0.70],
    projection="3d"
)

fig.patch.set_facecolor("white")
ax.set_facecolor("white")

teks_line = fig.text(
    0.5,
    0.105,
    f"Jumlah Line : {line}",
    ha="center",
    fontsize=13
)

area_minus = fig.add_axes([0.28, 0.02, 0.12, 0.06])
area_reset = fig.add_axes([0.44, 0.02, 0.12, 0.06])
area_plus = fig.add_axes([0.60, 0.02, 0.12, 0.06])

tombol_minus = Button(area_minus, "−")
tombol_reset = Button(area_reset, "RESET")
tombol_plus = Button(area_plus, "+")

tombol_minus.on_clicked(kurang_line)
tombol_plus.on_clicked(tambah_line)
tombol_reset.on_clicked(reset_line)

generate()

plt.show()