import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Initialize positions and directions
def initialize_particles(N, L):
    x = np.random.rand(N) * L
    y = np.random.rand(N) * L
    theta = 2 * np.pi * np.random.rand(N)
    return x, y, theta


# Find neighbors within radius R
def find_neighbors(x, y, i, R):
    dx = x - x[i]
    dy = y - y[i]
    distance_squared = dx**2 + dy**2
    neighbors = distance_squared < R**2
    return neighbors


# Update particle directions
def update_directions(x, y, theta, R, eta):
    N = len(theta)
    new_theta = np.zeros(N)
    for i in range(N):
        neighbors = find_neighbors(x, y, i, R)
        S = np.sum(np.sin(theta[neighbors]))
        C = np.sum(np.cos(theta[neighbors]))
        theta_avg = np.arctan2(S, C)
        noise = eta * (np.random.rand() - 0.5)  # angular noise
        new_theta[i] = theta_avg + noise
    return new_theta


# Update particle positions
def update_positions(x, y, theta, v0, dt, L):
    x_new = (x + v0 * np.cos(theta) * dt) % L
    y_new = (y + v0 * np.sin(theta) * dt) % L
    return x_new, y_new


# Compute global order parameter
def compute_order_parameter(theta):
    N = len(theta)
    sum_cos = np.sum(np.cos(theta))
    sum_sin = np.sum(np.sin(theta))
    phi = np.sqrt(sum_cos**2 + sum_sin**2) / N
    return phi


# Simulation function
def simulate_vicsek(N, L, v0, R, eta, dt, Nt):
    x, y, theta = initialize_particles(N, L)
    phi_list = []
    x_history, y_history, theta_history = [], [], []

    for t in range(Nt):
        theta = update_directions(x, y, theta, R, eta)
        x, y = update_positions(x, y, theta, v0, dt, L)

        phi_list.append(compute_order_parameter(theta))
        x_history.append(x.copy())
        y_history.append(y.copy())
        theta_history.append(theta.copy())

    return phi_list, x_history, y_history, theta_history


# Animation function
def animate_vicsek(x_history, y_history, theta_history, L):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)

    # Initial frame
    x = x_history[0]
    y = y_history[0]
    theta = theta_history[0]
    quiver = ax.quiver(x, y, np.cos(theta), np.sin(theta), angles='xy', scale_units='xy', scale=1)
    title = ax.set_title(f"Time step: 0")  # create title artist

    # Update function
    def update(frame):
        x = x_history[frame]
        y = y_history[frame]
        theta = theta_history[frame]
        quiver.set_offsets(np.c_[x, y])
        quiver.set_UVC(np.cos(theta), np.sin(theta))
        title.set_text(f"Time step: {frame}")
        return quiver, title

    anim = FuncAnimation(fig, update, frames=len(x_history), blit=True, interval=50)
    plt.show()


# Main function
def main():
    # Parameters
    N = 100     # number of particles
    L = 10      # box size
    v0 = 1.0    # particle speed
    R = 1.0     # interaction radius
    eta = 0.1   # noise amplitude
    dt = 0.1    # time step
    Nt = 100    # number of time steps

    phi_list, x_history, y_history, theta_history = simulate_vicsek(N, L, v0, R, eta, dt, Nt)

    print("Final order parameter:", phi_list[-1])

    # Plot order parameter over time
    plt.figure()
    plt.plot(phi_list)
    plt.xlabel("Time step")
    plt.ylabel("Order parameter φ")
    plt.title("Global Order Parameter Over Time")
    plt.show()

    # Animate the swarm
    animate_vicsek(x_history, y_history, theta_history, L)


if __name__ == "__main__":
    main()
