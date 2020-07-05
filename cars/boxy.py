class Boxy:
    def __init__(self, colors):
        c = colors[0]
        w = colors[1]
        b = colors[2]
        a = colors[3]

        self.picture = [
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, c, c, c, c, c, c, c, c, c, b, b, b, b, b, b],
            [b, b, b, b, b, b, c, a, a, a, c, a, a, a, c, b, b, b, b, b, b],
            [b, b, b, b, b, b, c, a, a, a, c, a, a, a, c, b, b, b, b, b, b],
            [b, b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, b],
            [b, b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, b],
            [b, b, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, b, b],
            [b, b, c, c, c, w, w, w, c, c, c, c, c, w, w, w, c, c, c, b, b],
            [b, b, b, b, b, w, c, w, b, b, b, b, b, w, c, w, b, b, b, b, b],
            [b, b, b, b, b, w, w, w, b, b, b, b, b, w, w, w, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
            [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        ]
