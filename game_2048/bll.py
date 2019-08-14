import copy
import random

from model import MoveDirection, Location


class GameController:

    def __init__(self):
        self.__list_merge = [0, 0, 0, 0]
        self.__list_map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location=[]
        self.__is_change=False

    @property
    def is_change(self):
        return self.__is_change

    @property
    def list_map(self):
        return self.__list_map

    def __zero_to_end(self):
        for i in range(len(self.__list_merge)-1,-1,-1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] *= 2
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        for line in self.__list_map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        for line in self.__list_map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __move_up(self):
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    def __move_down(self):
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        for c in range(1,len(self.__list_map)):
            for r in range(c,len(self.__list_map)):
                self.__list_map[r][c-1],self.__list_map[c-1][r]=self.__list_map[c-1][r],self.__list_map[r][c-1]

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for c in range(len(self.__list_map)):
            for r in range(len(self.__list_map[c])):
                if self.__list_map[c][r]==0:
                    self.__list_empty_location.append(Location(c,r))

    def generate_new_number(self):
        self.__calculate_empty_location()
        if len(self.__list_empty_location)==0:return
        loc=random.choice(self.__list_empty_location)
        self.__list_map[loc.c][loc.r]=self.__create_random_number()

    def __create_random_number(self):
        return 4 if random.randint(1,10)==1 else 2

    def move(self,dir=MoveDirection.UP):
        riginal_map = copy.deepcopy(self.__list_map)
        if dir==MoveDirection.UP:
            self.__move_up()
        elif dir==MoveDirection.DOWN:
            self.__move_down()
        elif dir == MoveDirection.LEFT:
            self.__move_left()
        elif dir == MoveDirection.RIGHT:
            self.__move_right()
        self.__is_change=self.__list_map!=riginal_map

    def is_game_over(self):
        if len(self.__list_empty_location):
            return False
        for r in range(len(self.__list_map)):
            for c in range(len(self.__list_map)-1):
                if self.__list_map[r][c]==self.__list_map[r][c+1] or self.__list_map[r][c]==self.__list_map[r+1][c]:
                    return False
                return True


