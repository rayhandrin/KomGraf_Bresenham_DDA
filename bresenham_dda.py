"""
21IF2015 Komputer Grafik (Teori)
Aldrin Rayhan Putra (211511003)
D3-2A

REFERENSI
- https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)
- https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
- https://www.geeksforgeeks.org/dda-line-generation-algorithm-computer-graphics/
- https://www.geeksforgeeks.org/bresenhams-line-generation-algorithm/
- https://medium.com/geekculture/dda-line-drawing-algorithm-be9f069921cf
- https://medium.com/geekculture/bresenhams-line-drawing-algorithm-2e0e953901b3
- Tugas Komputer Grafik (Praktikum)
"""

# DDA Algorithm
def dda(x0, y0, x1, y1):
    """
    DAFTAR VARIABEL
    dx         = selisih dari x1 dengan x0
    dy         = selisih dari y1 dengan y0
    steps      = banyaknya titik yang akan ditampilkan
    xIncrement = penambahan nilai x untuk setiap titik baru
    yIncrement = penambahan nilai y untuk setiap titik baru
    x          = koordinat x yang akan ditampilkan
    x          = koordinat y yang akan ditampilkan
    xEnd       = koordinat x akhir
    m          = gradien garis
    """

    # VERSI 1
    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0

    if (dx != 0):
        m = dy / dx

        print("DDA:")
        print('+--------------+')
        print('|%4s|%4s|%4s|' % ('x', 'y', 'm'))
        print('+----+----+----+')
        print('|%4d|%4d|%4d|' % (x, y, m))

        while (x <= x1):
            if m < 1:
                y += m
                x += 1
            elif m > 1:
                y += 1
                x += 1 / m
            elif m == 1:
                y += 1
                x += 1
            print('|%4d|%4d|%4d|' % (x, y, m))
        print('+----+----+----+')
    else:
        print("DDA:")
        print("Gradien tidak terdefinisi!")

    # VERSI 2
    # steps = max(abs(dx), abs(dy))

    # xIncrement = dx / float(steps)
    # yIncrement = dy / float(steps)

    # print("DDA:")
    # print('+------------------------+')
    # print('|%4s|%4s|%4s|%4s|%4s|' % ('x', 'y', 'st', 'xIn', 'yIn'))
    # print('+----+----+----+----+----+')
    # print('|%4d|%4d|%4d|%4d|%4d|' % (x, y, steps, xIncrement, yIncrement))

    # for k in range(steps + 1):
    #     x += xIncrement
    #     y += yIncrement
    #     print('|%4d|%4d|%4d|%4d|%4d|' % (x, y, steps, xIncrement, yIncrement))
    # print('+------------------------+')

# Breseham Algorithm
def bresenham(x0, y0, x1, y1):
    """
    DAFTAR VARIABEL
    dx      = selisih dari x1 dengan x0
    dy      = selisih dari y1 dengan y0
    d       = variabel penentu titik selanjutnya
    nextPt1 = titik selanjutnya, apabila d <= 0
    nextPt2 = titik selanjutnya, apabila d > 0
    x       = koordinat x yang akan ditampilkan
    x       = koordinat y yang akan ditampilkan
    xEnd    = koordinat x akhir
    """

    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    nextPt1 = 2 * dy
    nextPt2 = 2 * (dy - dx)

    if x0 > x1:
        x = x1
        y = y1
        xEnd = x0
    else:
        x = x0
        y = y0
        xEnd = x1

    print("Bresenham:")
    print('+------------------------+')
    print('|%4s|%4s|%4s|%4s|%4s|' % ('x', 'y', 'd', 'd1', 'd2'))
    print('+----+----+----+----+----+')
    print('|%4d|%4d|%4d|%4d|%4d|' % (x, y, d, nextPt1, nextPt2))

    for x in range(x + 1, xEnd + 2):
        if d <= 0:
            d += nextPt1
        elif d > 0:
            d += nextPt2
            y += 1
        print('|%4d|%4d|%4d|%4d|%4d|' % (x, y, d, nextPt1, nextPt2))
    print('+----+----+----+----+----+')

# Gradien Positif
print("GRADIEN MIRING KE KANAN")
print("x1 > x0, y1 > y0")
print("p1 = (2, 3); p2 = (10, 5)")
dda(2, 3, 10, 5)
print()
bresenham(2, 3, 10, 5)
print()

# Gradien Negatif
print("GRADIEN MIRING KE KIRI")
print("x1 < x0, y1 > y0")
print("p1 = (0, 0); p2 = (-10, 15)")
dda(0, 0, -10, 15)
print()
bresenham(20, 10, 10, 20)
print()

# Gradien Tidak Terdefinisi (vertikal)
# karena x1 - x0 = 0
print("GRADIEN LURUS VERTIKAL")
print("x1 = x0, y1 > y0")
print("p1 = (1, 0); p2 = (1, 15)")
dda(1, 0, 1, 15)
print()
bresenham(1, 0, 1, 15)
print()

# Gradien 0 (horizontal)
print("GRADIEN LURUS HORIZONTAL")
print("x1 < x0, y1 = y0")
print("p1 = (1, 5); p2 = (-5, 5)")
dda(1, 5, -5, 5)
print()
bresenham(1, 5, -5, 5)
print()
