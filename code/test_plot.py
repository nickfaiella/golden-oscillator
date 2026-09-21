"""Test plot: sin(t) for 0-10 s. Confirms numpy + matplotlib work
and that figures save into the repository's figures/ folder."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # save to file without opening a window
import matplotlib.pyplot as plt
import numpy as np

# Repository root = the folder above code/, so this works from any directory
ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

t = np.linspace(0, 10, 1000)  # time in seconds
x = np.sin(t)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(t, x, color="#A8740F", linewidth=2)
ax.axhline(0, color="gray", linewidth=0.8)
ax.set_xlabel("Time t (s)")
ax.set_ylabel("sin(t)")
ax.set_title("Test plot: sin(t), 0-10 s")
ax.set_xlim(0, 10)
ax.grid(alpha=0.3)
fig.tight_layout()

out = FIGURES / "test.png"
fig.savefig(out, dpi=150)
print(f"Saved {out}")