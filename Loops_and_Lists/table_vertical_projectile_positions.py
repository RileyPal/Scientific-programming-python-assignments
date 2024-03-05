# Constants
v = 10.0  # initial velocity
g_earth = 9.8  # acceleration due to gravity on Earth (m/s^2)
g_mars = 3.7  # acceleration due to gravity on Mars (m/s^2)
max_t_upper_limit = 6
t = 0


def y_earth(t):
    return max(0, v * t - .5 * g_earth * t ** 2)


def y_mars(t):
    return max(0, v * t - .5 * g_mars * t ** 2)


def main():
    print("for initial velocity of 10 m/s opposing gravity")
    print("t\ty Earth \ty Mars")
    print("----------------------------------------------")
    print("using while loop")
    t = 0
    while t <= 6:
        t += 0.2
        print(f"{t:.2f}\t\t{y_earth(t):.2f}\t\t{y_mars(t):.2f}")
    print("--------------------------------------------")
    print("using for loop")
    print("t\ty Earth \ty Mars")
    print("----------------------------------------------")

    for t in range(0, 7):
        t += 0.2
        print(f"{t:.2f}\t\t{y_earth(t):.2f}\t\t{y_mars(t):.2f}")
    print("-------------------------")


if __name__ == "__main__":
    main()
