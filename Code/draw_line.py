def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx == 0 or dy == 0:
        raise ValueError("Cannot draw a line with undefined slope.")

    m = dy / dx

    if 0 < m < 1:
        d = 2 * dy - dx
    else:
        d = 2 * dx - dy

    x, y = x1, y1

    points = [(x, y)]

    if 0 < m < 1:
        for _ in range(x1, x2):
            x += 1
            if d < 0:
                d += 2 * dy
            else:
                y += 1
                d += 2 * (dy - dx)
            points.append((x, y))
    else:
        for _ in range(y1, y2):
            y += 1
            if d < 0:
                d += 2 * dx
            else:
                x += 1
                d += 2 * (dx - dy)
            points.append((x, y))

    return points
