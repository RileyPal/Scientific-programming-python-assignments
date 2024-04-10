import vpython as vp

# Constants for different celestial bodies
earth_gravity = 9.81  # m/s^2
mars_gravity = 3.71  # m/s^2
moon_gravity = 1.62  # m/s^2


# Function to calculate the range and time of flight
def calculate_range_time_of_flight(initial_velocity, angle, gravity):
    v0_x = initial_velocity * vp.cos(angle)
    v0_y = initial_velocity * vp.sin(angle)
    t_flight = (2 * v0_y) / gravity
    range_x = v0_x * t_flight
    return range_x, t_flight


# Create fields for Earth, Mars, and Moon
earth_field = vp.box(pos=vp.vector(0, 0, 0), size=vp.vector(20, 0.1, 20), color=vp.color.green)
mars_field = vp.box(pos=vp.vector(25, 0, 0), size=vp.vector(20, 0.1, 20), color=vp.color.red)
moon_field = vp.box(pos=vp.vector(-25, 0, 0), size=vp.vector(20, 0.1, 20), color=vp.color.gray(0.7))

# Create labels for celestial bodies
vp.label(pos=vp.vector(0, -5, 0), text="EARTH", color=vp.color.green)
vp.label(pos=vp.vector(25, -5, 0), text="MARS", color=vp.color.red)
vp.label(pos=vp.vector(-25, -5, 0), text="MOON", color=vp.color.gray(0.7))

# Create balls for different scenarios
initial_position = vp.vector(-10, 0.5, -10)
initial_velocity = 20
angle = vp.radians(30)  # 30 degrees
radius = 0.5

# Earth ball
earth_range, earth_t_flight = calculate_range_time_of_flight(initial_velocity, angle, earth_gravity)
earth_ball = vp.sphere(pos=initial_position, radius=radius, color=vp.color.blue)
earth_velocity = vp.vector(initial_velocity * vp.cos(angle), initial_velocity * vp.sin(angle), 0)
earth_ball.trail = vp.curve(color=vp.color.blue)

# Mars ball
mars_range, mars_t_flight = calculate_range_time_of_flight(initial_velocity, angle, mars_gravity)
mars_ball = vp.sphere(pos=initial_position + vp.vector(25, 0, 0), radius=radius,
                      color=vp.vector(1, 0.4, 0.6))  # Use a combination of red and blue for pink color
mars_velocity = vp.vector(initial_velocity * vp.cos(angle), initial_velocity * vp.sin(angle), 0)
mars_ball.trail = vp.curve(color=vp.vector(1, 0.4, 0.6))  # Use the same color for the trail
# Moon ball
moon_range, moon_t_flight = calculate_range_time_of_flight(initial_velocity, angle, moon_gravity)
moon_ball = vp.sphere(pos=initial_position + vp.vector(-25, 0, 0), radius=radius, color=vp.color.white)
moon_velocity = vp.vector(initial_velocity * vp.cos(angle), initial_velocity * vp.sin(angle), 0)
moon_ball.trail = vp.curve(color=vp.color.white)


# Function to update ball position
def update_position(ball, velocity, t_flight, gravity):
    dt = t_flight / 1000
    t = 0
    while t < t_flight:
        vp.rate(1000)
        velocity.z -= gravity * dt
        ball.pos += velocity * dt
        ball.trail.append(pos=ball.pos)
        t += dt


# Update positions for all balls
update_position(earth_ball, earth_velocity, earth_t_flight, earth_gravity)
update_position(mars_ball, mars_velocity, mars_t_flight, mars_gravity)
update_position(moon_ball, moon_velocity, moon_t_flight, moon_gravity)
