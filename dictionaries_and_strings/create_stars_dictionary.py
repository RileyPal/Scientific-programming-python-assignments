def convert_list_of_tuples(data):
    stars = {}
    for star_data in data:
        star_name, distance_ly, apparent_brightness, luminosity = star_data
        stars[star_name] = {
            'distance': distance_ly,
            'apparent brightness': apparent_brightness,
            'luminosity': luminosity
        }
    return stars

def print_star_information(star_name, stars):
    star_info = stars.get(star_name)
    if star_info:
        print(f"Star: {star_name}")
        print(f"    Distance (ly):            {star_info['distance']}")
        print(f"    Apparent brightness (m):  {star_info['apparent brightness']}")
        print(f"    Luminosity (L_sun):       {star_info['luminosity']}")
    else:
        print(f"Star '{star_name}' not found in the data.")

# Nearby star data
nearby_star_data = [
    ('Alpha Centauri A',    4.3,  0.26,      1.56),
    ('Alpha Centauri B',    4.3,  0.077,     0.45),
    ('Alpha Centauri C',    4.2,  0.00001,   0.00006),
    ("Barnard's Star",      6.0,  0.00004,   0.0005),
    ('Wolf 359',            7.7,  0.000001,  0.00002),
    ('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
    ('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
    ('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
    ('Sirius A',            8.6,  1.00,      23.6),
    ('Sirius B',            8.6,  0.001,     0.003),
    ('Ross 154',            9.4,  0.00002,   0.0005),
]

# Convert data to nested dictionary
stars = convert_list_of_tuples(nearby_star_data)

# Print information for two different stars
print_star_information('Sirius A', stars)
print("\n")
print_star_information('Alpha Centauri B', stars)
