"""
Planetary Gravity Calculator

Given the dimensions of several planets and an object's mass,
calculate the amount of force exerted on an object's surface
using Newton's Law of Universal Gravitation:

F = G * ((M1 * M2) / D)

Example:

Input:
    Object mass = 100 kg
    Number of planets = 4
    List of planets (name, radius (m), and avg density (kg/m^3)) =
        Tantalus, 3104500, 5009
        Reach, 7636500, 4966
        Circumstance, 4127000, 4132
        Tribute, 2818000, 4358

Output:
    Weight of object on each planet (in Newtons) =
        Tantalus:       434.467 N
        Reach:          1059.536 N
        Circumstance:   476.441 N
        Tribute:        343.117 N
"""
import argparse
import math

# Gravitational constant
G = float("6.67e-11")


class Planet(object):

    def __init__(self, name, radius, density):
        self.name = name
        self.radius = radius
        self.density = density
        self.volume = (4 * math.pi * math.pow(self.radius, 3)) / 3
        self.mass = self.volume * self.density

    def calc_force(self, obj_mass):
        return float(G * ((obj_mass * self.mass) / math.pow(self.radius, 2)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program that calculates the gravitational'
                                                 'pull on an object of mass M on a number N'
                                                 'of given planets.')
    parser.add_argument('-f', '--file', action='store', default=None, dest='input',
                        help='Optional text file containing data for each planet.')
    args = parser.parse_args()
    planet_objects = []
    object_mass = 0

    if args.input is None:
        object_mass = int(raw_input('Object mass (in kg): '))
        num_planets = int(raw_input('Number of planets: '))

        for i in range(0, num_planets):
            planet_name = raw_input('Planet name ({}/{}): '.format(i+1, num_planets))
            planet_radius = int(raw_input('Planet radius ({}/{}): '.format(i+1, num_planets)))
            planet_density = int(raw_input('Planet density ({}/{}): '.format(i+1, num_planets)))
            planet_objects.append(Planet(planet_name, planet_radius, planet_density))

        print "\n"
        print "=====Weight of object of mass M on each given planet====="
        for p in planet_objects:
            print "{}:\t{} N".format(p.name, p.calc_force(object_mass))
    else:
        object_mass = int(raw_input('Object mass (in kg): '))
        with open(args.input, 'r') as f:
            for line in f:
                try:
                    planet_name, planet_radius, planet_density = line.split(',')
                    planet_objects.append(Planet(planet_name, float(planet_radius), float(planet_density)))
                except ValueError:
                    pass

        print "\n"
        print "=====Weight of object of mass M on each given planet====="
        for p in planet_objects:
            print "{0}:\t{1:.3f} N".format(p.name, p.calc_force(object_mass))