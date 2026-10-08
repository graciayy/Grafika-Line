import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


# ==========================================
# VARIABEL GLOBAL
# ==========================================

line = 10
line_awal = 10
pilihan = 1


# ==========================================
# FUNGSI KUBUS
# ==========================================

def gambar_kubus(ax, line):

    vertices = [
        (-1, -1, -1),
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, 1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, 1, 1)
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    # Garis utama kubus
    for edge in edges:

        p1 = vertices[edge[0]]
        p2 = vertices[edge[1]]

        ax.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            color="black"
        )

    # Grid tambahan
    if line > 1:

        nilai = np.linspace(-1, 1, line + 1)

        for v in nilai:

            # Depan
            ax.plot(
                v * np.ones_like(nilai),
                nilai,
                np.ones_like(nilai),
                color="black",
                linewidth=0.5
            )

            # Belakang
            ax.plot(
                v * np.ones_like(nilai),
                nilai,
                -np.ones_like(nilai),
                color="black",
                linewidth=0.5
            )

            # Kiri
            ax.plot(
                -np.ones_like(nilai),
                v * np.ones_like(nilai),
                nilai,
                color="black",
                linewidth=0.5
            )

            # Kanan
            ax.plot(
                np.ones_like(nilai),
                v * np.ones_like(nilai),
                nilai,
                color="black",
                linewidth=0.5
            )

            # Atas
            ax.plot(
                nilai,
                np.ones_like(nilai),
                v * np.ones_like(nilai),
                color="black",
                linewidth=0.5
            )

            # Bawah
            ax.plot(
                nilai,
                -np.ones_like(nilai),
                v * np.ones_like(nilai),
                color="black",
                linewidth=0.5
            )

    ax.set_title("KUBUS")


# ==========================================
# FUNGSI BALOK
# ==========================================

def gambar_balok(ax, line):

    panjang = 3
    lebar = 2
    tinggi = 1.5

    x = [-panjang / 2, panjang / 2]
    y = [-lebar / 2, lebar / 2]
    z = [-tinggi / 2, tinggi / 2]

    vertices = [
        (x[0], y[0], z[0]),
        (x[1], y[0], z[0]),
        (x[1], y[1], z[0]),
        (x[0], y[1], z[0]),
        (x[0], y[0], z[1]),
        (x[1], y[0], z[1]),
        (x[1], y[1], z[1]),
        (x[0], y[1], z[1])
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    # Garis utama
    for edge in edges:

        p1 = vertices[edge[0]]
        p2 = vertices[edge[1]]

        ax.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            color="black"
        )

    # Grid tambahan
    if line > 1:

        nilai_x = np.linspace(x[0], x[1], line + 1)
        nilai_y = np.linspace(y[0], y[1], line + 1)
        nilai_z = np.linspace(z[0], z[1], line + 1)

        # Depan dan belakang
        for xx in nilai_x:

            ax.plot(
                [xx] * len(nilai_z),
                [y[0]] * len(nilai_z),
                nilai_z,
                color="black",
                linewidth=0.5
            )

            ax.plot(
                [xx] * len(nilai_z),
                [y[1]] * len(nilai_z),
                nilai_z,
                color="black",
                linewidth=0.5
            )

        # Kiri dan kanan
        for yy in nilai_y:

            ax.plot(
                [x[0]] * len(nilai_z),
                [yy] * len(nilai_z),
                nilai_z,
                color="black",
                linewidth=0.5
            )

            ax.plot(
                [x[1]] * len(nilai_z),
                [yy] * len(nilai_z),
                nilai_z,
                color="black",
                linewidth=0.5
            )

        # Atas dan bawah
        for zz in nilai_z:

            ax.plot(
                nilai_x,
                [y[0]] * len(nilai_x),
                [zz] * len(nilai_x),
                color="black",
                linewidth=0.5
            )

            ax.plot(
                nilai_x,
                [y[1]] * len(nilai_x),
                [zz] * len(nilai_x),
                color="black",
                linewidth=0.5
            )

    ax.set_title("BALOK")


# ==========================================
# FUNGSI TABUNG
# ==========================================

def gambar_tabung(ax, line):

    radius = 1
    tinggi = 2

    theta = np.linspace(
        0,
        2 * np.pi,
        line
    )

    z = np.linspace(
        -tinggi / 2,
        tinggi / 2,
        2
    )

    theta_grid, z_grid = np.meshgrid(theta, z)

    x = radius * np.cos(theta_grid)
    y = radius * np.sin(theta_grid)

    ax.plot_wireframe(
        x,
        y,
        z_grid,
        rstride=1,
        cstride=1,
        color="black"
    )

    # Atas
    ax.plot(
        radius * np.cos(theta),
        radius * np.sin(theta),
        tinggi / 2,
        color="black"
    )

    # Bawah
    ax.plot(
        radius * np.cos(theta),
        radius * np.sin(theta),
        -tinggi / 2,
        color="black"
    )

    ax.set_title("TABUNG")


# ==========================================
# FUNGSI KERUCUT
# ==========================================

def gambar_kerucut(ax, line):

    radius = 1
    tinggi = 2

    theta = np.linspace(
        0,
        2 * np.pi,
        line
    )

    z = np.linspace(
        0,
        tinggi,
        2
    )

    theta_grid, z_grid = np.meshgrid(
        theta,
        z
    )

    radius_grid = radius * (
        1 - z_grid / tinggi
    )

    x = radius_grid * np.cos(theta_grid)
    y = radius_grid * np.sin(theta_grid)

    ax.plot_wireframe(
        x,
        y,
        z_grid,
        rstride=1,
        cstride=1,
        color="black"
    )

    # Alas
    ax.plot(
        radius * np.cos(theta),
        radius * np.sin(theta),
        0,
        color="black"
    )

    ax.set_title("KERUCUT")


# ==========================================
# FUNGSI BOLA
# ==========================================

def gambar_bola(ax, line):

    radius = 1

    u = np.linspace(
        0,
        2 * np.pi,
        line
    )

    v = np.linspace(
        0,
        np.pi,
        line
    )

    x = radius * np.outer(
        np.cos(u),
        np.sin(v)
    )

    y = radius * np.outer(
        np.sin(u),
        np.sin(v)
    )

    z = radius * np.outer(
        np.ones(np.size(u)),
        np.cos(v)
    )

    ax.plot_wireframe(
        x,
        y,
        z,
        color="black"
    )

    ax.set_title("BOLA")


# ==========================================
# GENERATE ULANG OBJEK
# ==========================================

def generate():

    ax.clear()

    if pilihan == 1:

        gambar_kubus(
            ax,
            line
        )

    elif pilihan == 2:

        gambar_balok(
            ax,
            line
        )

    elif pilihan == 3:

        gambar_tabung(
            ax,
            line
        )

    elif pilihan == 4:

        gambar_kerucut(
            ax,
            line
        )

    elif pilihan == 5:

        gambar_bola(
            ax,
            line
        )

    # Pengaturan tampilan
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_box_aspect(
        [1, 1, 1]
    )

    ax.grid(True)

    # Update tulisan line
    teks_line.set_text(
        f"Jumlah Line : {line}"
    )

    # Refresh window
    fig.canvas.draw_idle()


# ==========================================
# TOMBOL +
# ==========================================

def tambah_line(event):

    global line

    line += 1

    generate()


# ==========================================
# TOMBOL -
# ==========================================

def kurang_line(event):

    global line

    if line > 2:

        line -= 1

        generate()


# ==========================================
# TOMBOL RESET
# ==========================================

def reset_line(event):

    global line

    line = line_awal

    generate()


# ==========================================
# INPUT
# ==========================================

print("=" * 40)
print("       PROGRAM BANGUN RUANG 3D")
print("=" * 40)

print("\nPilih Bangun Ruang:")
print("1. Kubus")
print("2. Balok")
print("3. Tabung")
print("4. Kerucut")
print("5. Bola")

pilihan = int(
    input("\nMasukkan pilihan (1-5): ")
)

line = int(
    input("Masukkan jumlah line awal: ")
)

if pilihan not in range(1, 6):

    print("Pilihan tidak valid!")
    exit()

if line < 2:

    print("Jumlah line minimal adalah 2!")
    exit()

line_awal = line


# ==========================================
# WINDOW
# ==========================================

fig = plt.figure(
    figsize=(8, 8)
)

ax = fig.add_axes(
    [0.08, 0.18, 0.84, 0.70],
    projection="3d"
)

fig.patch.set_facecolor("white")
ax.set_facecolor("white")


# ==========================================
# INFORMASI LINE
# ==========================================

teks_line = fig.text(
    0.5,
    0.105,
    f"Jumlah Line : {line}",
    ha="center",
    fontsize=13
)


# ==========================================
# MEMBUAT TOMBOL
# ==========================================

area_minus = fig.add_axes(
    [0.28, 0.02, 0.12, 0.06]
)

area_reset = fig.add_axes(
    [0.44, 0.02, 0.12, 0.06]
)

area_plus = fig.add_axes(
    [0.60, 0.02, 0.12, 0.06]
)


tombol_minus = Button(
    area_minus,
    "−"
)

tombol_reset = Button(
    area_reset,
    "RESET"
)

tombol_plus = Button(
    area_plus,
    "+"
)


# ==========================================
# EVENT BUTTON
# ==========================================

tombol_minus.on_clicked(
    kurang_line
)

tombol_plus.on_clicked(
    tambah_line
)

tombol_reset.on_clicked(
    reset_line
)


# ==========================================
# GENERATE AWAL
# ==========================================

generate()

plt.show()