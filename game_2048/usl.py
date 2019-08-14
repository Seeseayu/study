import os

from bll import GameController, MoveDirection


class GameConsoleView:
    def __init__(self):
        self.__controller= GameController()

    def start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def __print_map(self):
        os.system("clear")
        for line in self.__controller.list_map:
            for item in line:
                print(item,end=" ")
            print( )

    def update(self):
        while True:
            str_input=input("请输入wasd:")
            self.__move_map(str_input)
            if not self.__controller.is_change:continue
            self.__controller.generate_new_number()
            self.__print_map()
            if self.__controller.is_game_over():
                print("游戏结束喽")
                break


    def __move_map(self,str_input):
        if str_input == "w":
            self.__controller.move(MoveDirection.UP)
        elif str_input == "s":
            self.__controller.move(MoveDirection.DOWN)
        elif str_input == "a":
            self.__controller.move(MoveDirection.LEFT)
        elif str_input == "d":
            self.__controller.move(MoveDirection.RIGHT)