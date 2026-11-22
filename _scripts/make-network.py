"""
Draws the faint network (nodes and links) used as the page background.
It is dense and fully connected along one edge and thins out and fades away from it.
How far it reaches varies across the width (low on one side, high on the other),
and the fade follows that shape. The page shows the drawing flipped (see body::before
in assets/css/style.css), so the dense edge sits at the bottom of the page.

Run from the repo folder:   python3 _scripts/make-network.py
It writes assets/img/network-light.svg and assets/img/network-dark.svg.
Change SEED for a different random layout. No extra Python packages needed.
(Folders starting with "_" are not published, so this script stays private.)
"""
import math
import random

SEED = 9
W, H = 2400, 900          # size of the drawing in pixels (keep in sync with body::before in style.css)
Y_MAX = 880               # how far the network reaches at its tallest point
GAP_DENSE = 46            # spacing between nodes at the dense edge
GAP_SPARSE = 200          # spacing between nodes at the far end
LINKS_PER_NODE = 3        # each node links to this many nearest neighbours
LINE_WIDTH = 1.6
COLORS = {"light": "#c3cad1", "dark": "#353c44"}   # full-strength color, at the dense edge

random.seed(SEED)


def reach(x):
    """How far the network extends from the dense edge at horizontal position x.
    Strongly uneven on purpose: low on the left, rising steeply to the right, with a gentle wave."""
    u = min(max(x / W, 0), 1)
    return Y_MAX * (0.38 + 0.62 * u ** 1.8 + 0.06 * math.sin(2 * math.pi * (1.6 * u + 0.1)))


def height(x, y):
    """0 at the dense edge, 1 at the far end of the network at this x."""
    return min(max(y / reach(x), 0), 1)


def gap(x, y):
    """Minimum spacing between nodes, growing away from the dense edge."""
    return GAP_DENSE + (GAP_SPARSE - GAP_DENSE) * height(x, y) ** 0.9


def fade(x, y):
    """Opacity: full at the dense edge, fading to nothing at the far end (follows reach())."""
    return (1 - height(x, y)) ** 1.1


# Random nodes; spacing depends on height, so they thin out gradually.
nodes = []
for _ in range(60000):
    x, y = random.uniform(-20, W + 20), random.uniform(0, Y_MAX)
    if y > reach(x):
        continue
    if all(math.dist((x, y), n) >= min(gap(x, y), gap(*n)) for n in nodes):
        nodes.append((x, y))

# Link each node to its nearest neighbours (only reasonably close ones).
links = set()
for i, a in enumerate(nodes):
    near = sorted((math.dist(a, b), j) for j, b in enumerate(nodes) if j != i)
    k = LINKS_PER_NODE if random.random() < 0.6 else LINKS_PER_NODE - 1
    for d, j in near[:k]:
        if d <= 2.6 * gap(*a):
            links.add((min(i, j), max(i, j)))

degree = [0] * len(nodes)
for i, j in links:
    degree[i] += 1
    degree[j] += 1

for name, color in COLORS.items():
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
             f'<g stroke="{color}" stroke-width="{LINE_WIDTH}" stroke-linecap="round">']
    for i, j in sorted(links):
        (x1, y1), (x2, y2) = nodes[i], nodes[j]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        # Long links (relative to the local spacing) are drawn fainter than short ones.
        rel = math.dist(nodes[i], nodes[j]) / gap(mx, my)
        length_factor = min(1, max(0.35, 1.25 - 0.4 * rel))
        op = fade(mx, my) * length_factor
        if op > 0.03:
            parts.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke-opacity="{op:.2f}"/>')
    parts.append(f'</g><g fill="{color}">')
    for (x, y), deg in zip(nodes, degree):
        # Most nodes are tiny; well-connected "hubs" get a slightly larger dot.
        r = 4.6 if deg >= 5 else 3.4 if deg == 4 else 2.6
        op = fade(x, y)
        if op > 0.03:
            parts.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill-opacity="{op:.2f}"/>')
    parts.append("</g></svg>")
    path = f"assets/img/network-{name}.svg"
    with open(path, "w") as f:
        f.write("\n".join(parts) + "\n")
    hubs = sum(d >= 5 for d in degree)
    print(f"{path}: {len(nodes)} nodes ({hubs} hubs), {len(links)} links")
