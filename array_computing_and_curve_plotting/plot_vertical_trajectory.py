import sys
import matplotlib.pyplot as plt


def vertical_trajectory(g, initial_velocities):
    times = []
    heights = []
    for v0 in initial_velocities:
        time = [(2 * v0) / g]
        height = [v0 * time[0] - 0.5 * g * time[0] ** 2]
        times.extend(time)
        heights.extend(height)
    return times, heights


def main():
    if len(sys.argv) < 3:
        print("Usage: python plot_vertical_trajectory.py <g> <initial_velocity1> <initial_velocity2> ...")
        return

    g = float(sys.argv[1])
    initial_velocities = [float(v) for v in sys.argv[2:]]

    times, heights = vertical_trajectory(g, initial_velocities)

    plt.plot(times, heights, marker='o')
    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.title('Vertical Trajectory')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
