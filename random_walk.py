from random import choice


class RandomWalk:
    """ A class to generate random walks. """

    def_init__(self, num_points=5000):
        """ attributes for the walk """
        self.num_points = num_points

        #all walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ all the points in the walk."""

        #walk until reaching this length.
        while len(self.x_values) < self_num.points:
            
            #lay out direction and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_distance = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #moves that go nowhere are skipped
            if x_step == 0 and y_step == 0:
                continue

            #calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)