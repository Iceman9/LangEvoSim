import random


class Realm:

    """Class Realm initializes an object that represents a population's living
    ground.
    Attributes:
        map (list): A matrix of the realms map.
    """

    def __init__(self):
        self.map = []
        self.size = None

    def __repr__(self):
        map = self.get_map()
        string_map = ''
        for row in map:
            row = ' '.join([str(el) if el else ' ' for el in row]) + '\n'
            string_map += row
        return string_map


    def construct_basic_map(self, size_in_x=20, size_in_y=20):
        """
        Constructs a map of the entire world for populations to populate.
        Alternatively, constructs a map for one population.

        Parameters:
            size_in_x (int): default=20; an input argument size_in_x represents
                the Realm's length on x axis.
        """
        temp_map = [None for i in range(11, size_in_x * size_in_y + 11)]
        self.map = []
        for i in range(size_in_x):
            self.map.append(temp_map[size_in_y * i: size_in_y * (i + 1)])
        self.size = (size_in_x, size_in_y)

    def get_map(self):
        """Returns the map (lists) of a Realm object.
        """
        return self.map

    def check_if_pos_is_taken(self, pos):
        """Returns the name of **Agent** object on ``position`` or ``None``. If
        position is out of map's bounds, returns True.

        Parameters:
            pos (touple): an input argument pos is a position to check if
                taken.
        """
        x = pos[0]
        y = pos[1]
        try:
            return self.map[x][y]
        except IndexError:
            return True

    def move_agent_to_pos(self, agent, new_pos):
        """Moves **Agent** object from ``current position`` to
        ``new position``.

        Parameters:
            agent (Agent): an input argument agent denotes the Agent object to
                move
            new_pos (touple): an input argument new_pos denotes new position to
                which Agent object moves
        """
        map = self.get_map()
        new_x, new_y = new_pos
        map[new_x][new_y] = agent
        agent.set_position(new_pos)

    def plant_agent(self, agent):
        """Plants an **Agent** on the map.

        Parameters:
            agent (Agent): Agent object to be put on map.
        """
        map = self.get_map()
        # Draw random  indexes
        while 1:
            x = random.randint(0, self.size[0] - 1)
            y = random.randint(0, self.size[1] - 1)
            if self.check_if_pos_is_taken((x, y)):
                continue

            else:
                map[x][y] = agent
                agent.set_position((x, y))
                agent.set_land(self)
                break

    def get_possible_moves(self, pos):
        """ This function gives us the ``possible moves`` from the position
        **pos** in the current **land**.

        Parameters:
            pos (touple): Position (x,y).
        """

        x, y = pos

        up = x + 1, y
        down = x - 1, y
        left = x, y - 1
        right = x, y + 1

        moves = []

        status = self.check_if_pos_is_taken(up)
        if status is not True:
            moves.append((up, status, 'up'))

        status = self.check_if_pos_is_taken(down)
        if status is not True:
            moves.append((down, status, 'down'))

        status = self.check_if_pos_is_taken(left)
        if status is not True:
            moves.append((left, status, 'left'))

        status = self.check_if_pos_is_taken(right)
        if status is not True:
            moves.append((right, status, 'right'))

        return moves




if __name__ == '__main__':
    realm = Realm()
    realm.construct_basic_map()
    [print(i) for i in realm.get_map()]


    x = 5
    y = 5
    position_is_taken = realm.check_if_pos_is_taken((x, y))
    print(position_is_taken)

    x = 599999
    y = 509000
    position_is_taken = realm.check_if_pos_is_taken((x, y))
    print(position_is_taken)

    from agent import Agent
    map = realm.get_map()
    map[10][10] = Agent()
    x = 10
    y = 10
    position_is_taken = realm.check_if_pos_is_taken((x, y))
    print(position_is_taken)
