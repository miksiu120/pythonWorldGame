# I have to change the of the file to GameWindow.py, but I don't have any idea yet

from graphicFiles.Square import *
from graphicFiles.constValues import *
from World import *
from Logs import *
import os
from importsOrganisms import *

class DataSaver:
    def __init__(self, savingElement):
        self.savingElement = savingElement

    def save_game(self):
        try:
            with open("save01.txt", "w") as file:

                len_org = len(self.savingElement.getOrganisms())
                file.write(f"{len_org}\n")
                for organism in self.savingElement.getOrganisms():
                    ascii = organism.getAscii()
                    strength = organism.getStrength()
                    initiative = organism.getInitiative()
                    age = organism.getAge()
                    x = organism.getPosition().getX()
                    y = organism.getPosition().getY()
                    file.write(f"{ascii}\n")
                    file.write(f"{strength}\n")
                    file.write(f"{initiative}\n")
                    file.write(f"{age}\n")
                    file.write(f"{x} {y}\n")
                    if isinstance(organism, Human):
                        human = organism
                        alzur_status = human.getShieldStatus()
                        file.write(f"{alzur_status}\n")
                        cool_down = human.getShieldCooldown()
                        file.write(f"{cool_down}\n")


                kill_len = len(self.savingElement.getKillList())
                file.write(f"{kill_len}\n")
                for i in range(len(self.savingElement.getOrganisms())):
                    for j in range(len(self.savingElement.getKillList())):
                        if self.savingElement.getOrganisms()[i] == self.savingElement.getKillList()[j]:
                            file.write(f"{i}\n")
            print("Game saved to file: save01.txt")
        except IOError as e:
            print(f"Error while saving game to file: {e}")

    def load_game(self):
        self.savingElement.getOrganisms().clear()
        try:
            with open("save01.txt", "r") as file:

                len_org = int(file.readline())
                for i in range(len_org):
                    element = file.readline().strip()
                    if element == "":
                        i -= 1
                        continue
                    strength = int(file.readline())
                    initiative = int(file.readline())
                    age = int(file.readline())
                    pos_x, pos_y = map(int, file.readline().split())
                    if element == 'W':
                        self.savingElement.getOrganisms().append(Wolf(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'S':
                        self.savingElement.getOrganisms().append(Sheep(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'F':
                        self.savingElement.getOrganisms().append(Fox(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'T':
                        self.savingElement.getOrganisms().append(Turtle(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'A':
                        self.savingElement.getOrganisms().append(Antylope(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'B':
                        self.savingElement.getOrganisms().append(Belladonna(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'D':
                        self.savingElement.getOrganisms().append(Dandelion(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'G':
                        self.savingElement.getOrganisms().append(Grass(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'U':
                        self.savingElement.getOrganisms().append(Guarana(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == 'O':
                        self.savingElement.getOrganisms().append(SosnowskiBarszcz(self.savingElement, pos_x, pos_y, strength, initiative, age))
                    elif element == '7':
                        alzur_status = bool(file.readline())
                        alzur_cooldown = int(file.readline())
                        human = Human(self.savingElement, pos_x, pos_y, strength, initiative, age, alzur_cooldown)
                        human.setShieldStatus(alzur_status)
                        self.savingElement.getOrganisms().append(human)
                        self.savingElement.setMainCharacter(human)
                        self.savingElement.setHumanPosition(Coordinates(pos_x, pos_y))


        except FileNotFoundError:
            print("File not found.")