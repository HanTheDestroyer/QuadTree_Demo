from settings import *
from particle import Particle


class Node:
    def __init__(self, data, x_range, y_range, screen, level):
        self.level = level
        self.data = data
        self.x_range = x_range
        self.y_range = y_range
        self.screen = screen
        self.children = []
        self.divided_data = []
        self.new_x_range = []
        self.new_y_range = []
        self.half_x = (x_range[0] + x_range[1]) / 2
        self.half_y = (y_range[0] + y_range[1]) / 2
        self.is_populated = False
        self.center, self.total_mass = center_of_mass(self.data)
        self.size = abs(self.x_range[1] - self.x_range[0]) / 2

        self.mass = 0
        for k in range(len(self.data)):
            self.mass += self.data[k].mass

        for k in range(children_amount):
            self.divided_data.append([])
            self.new_x_range.append([])
            self.new_y_range.append([])

        self.draw_lines()
        self.create_new_ranges()
        self.place_data()
        self.clean_data()

        # Check for nodes with multiple elements in them. If so, populate them.
        # Populating have conditions. Elements should not coincide for cells with few number of particles in them.
        for k in range(len(self.divided_data)):
            if len(self.divided_data[k]) > max_cell_size and self.level < max_depth:
                self.populate(self.divided_data[k], k)
                self.is_populated = True

    def place_data(self):
        """Places data to their respective quadrants(divided_data)"""
        if len(self.data) > 1 and type(self.data[0]) == Particle:
            for k in range(len(self.data)):
                if self.data[k].position[1] > self.half_y:
                    if self.data[k].position[0] <= self.half_x:
                        self.divided_data[3].append(self.data[k])
                    else:
                        self.divided_data[2].append(self.data[k])
                else:
                    if self.data[k].position[0] >= self.half_x:
                        self.divided_data[1].append(self.data[k])
                    else:
                        self.divided_data[0].append(self.data[k])

    def clean_data(self):
        """Removes empty arrays from divided data"""
        target = []
        for k in range(len(self.divided_data)):
            if len(self.divided_data[k]) == 0:
                target.append(k)
        target.reverse()

        for k in target:
            self.divided_data.pop(k)
            self.new_x_range.pop(k)
            self.new_y_range.pop(k)

    def create_new_ranges(self):
        """Creates new ranges for children nodes"""

        width = self.x_range
        width.append(self.half_x)
        height = self.y_range
        height.append(self.half_y)

        for k in range(children_amount):
            if k == 0:
                self.new_x_range[k] = [width[0], width[2]]
                self.new_y_range[k] = [height[0], height[2]]
            if k == 1:
                self.new_x_range[k] = [width[2], width[1]]
                self.new_y_range[k] = [height[0], height[2]]
            if k == 2:
                self.new_x_range[k] = [width[2], width[1]]
                self.new_y_range[k] = [height[2], height[1]]
            if k == 3:
                self.new_x_range[k] = [width[0], width[2]]
                self.new_y_range[k] = [height[2], height[1]]

    def draw_lines(self):
        if len(self.data) > max_cell_size:
            pygame.draw.line(self.screen, pygame.Color("White"),
                             [self.x_range[0], self.half_y], [self.x_range[1], self.half_y])
            pygame.draw.line(self.screen, pygame.Color("White"),
                             [self.half_x, self.y_range[0]], [self.half_x, self.y_range[1]])

    def populate(self, data, index):
        new_node = Node(self.divided_data[index],
                        self.new_x_range[index], self.new_y_range[index], self.screen, self.level + 1)
        self.children.append(new_node)

    def __getitem__(self, index):
        return self.data[index]


def center_of_mass(planets):
    total_moment_x = 0
    total_moment_y = 0
    total_mass = 0
    moments = []
    for k in range(len(planets)):
        moment_x = planets[k].position[0] * planets[k].mass
        total_moment_x += moment_x
        moment_y = planets[k].position[1] * planets[k].mass
        total_moment_y += moment_y
        total_mass += planets[k].mass
        moments.append(moment_x + moment_y)

    x_center = total_moment_x / total_mass
    y_center = total_moment_y / total_mass
    center = [x_center, y_center]

    return center, total_mass
