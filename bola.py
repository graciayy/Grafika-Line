import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

line_awal = int(input("Masukkan jumlah line awal: "))

if line_awal < 2:
    line_awal = 2

line = line_awal


def gambar_bola(ax, line):
    radius = 1

    u = np.linspace(0, 2 * np.pi, line)
    v = np.linspace(0, np.pi, line)

    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_wireframe(
        x, y, z,
        color="black",
        linewidth=0.7
    )


def generate():
    ax.clear()

    gambar_bola(ax, line)

    ax.set_title("BOLA")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_zlim(-1.3, 1.3)

    ax.set_box_aspect((1, 1, 1))
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