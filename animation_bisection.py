# generate mid points list using bisection
# plot the function graph using given function
# plot red dot on each frame based on x, y of mid points[frame]

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return x**2 - 4

epsilon=1e-10

def bisection_all(left, right):
    midpoints = []
    while True:
        mid = (left + right) / 2
        midpoints.append(mid)
        if abs(f(mid)) < epsilon:
            return mid, midpoints  # root + all mids
        if f(mid) * f(left) < 0:
            right = mid
        else:
            left = mid

root, mids = bisection_all(1, 4)
print(root)

x_vals = [i*0.01 for i in range(0, 501)]  # 0 <= x <= 5 in steps of 0.01
y_vals = [f(x) for x in x_vals]

fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(min(y_vals), max(y_vals))
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Bisection Convergence")

ax.plot(x_vals, y_vals, color="blue", label="f(x)")

midpoint_dot, = ax.plot([], [], "ro", markersize=8) # Empty x and y lists, r = "red", o = "circle"

iteration_label = ax.text(0.05, 0.9, "")

def init():
    midpoint_dot.set_data([], [])
    iteration_label.set_text("")

def update(frame):
    x_mid = mids[frame]
    y_mid = f(x_mid)
    midpoint_dot.set_data([x_mid], [y_mid])
    iteration_label.set_text(f"Iteration {frame+1}: x = {x_mid}")

ani = animation.FuncAnimation(
    fig,       # figure object
    update,    # function to call at each frame
    frames=len(mids),  # number of frames
    init_func=init,    # function to draw on first frame
    interval=800       # milliseconds between frames
)

plt.legend()
plt.show()
