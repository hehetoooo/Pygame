import pygame
import math
import os
from settings import PATH_1 ,PATH_2

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))

# color (RGB)
RED = (255, 0, 0)
GREEN =(0, 255, 0)


class Enemy:
    def __init__(self,wave):                    #to control the wave

        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10                    #step count
        self.path = [PATH_1, PATH_2]            #list the path
        self.path_index = 0
        self.move_count = 0
        self.stride = 1                         #step size
        self.idx = wave  # to index path
        self.x, self.y = self.path[self.idx][0] #to determine path 1 and path 2

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        # Define the position of the health bar according to the position of the enemy .
        pygame.draw.rect(win, (RED), [(self.x - 20), (self.y - 30), 50, 5])
        pygame.draw.rect(win, (GREEN), [(self.x - 20), (self.y - 30), 25, 5])


    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
        #Calculate the number of steps required for the next point (根號A^2 + B^2)
        stride = 1
        ax, ay = self.path[self.idx][self.path_index]
        bx, by = self.path[self.idx][self.path_index + 1]
        distance_A_B = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
        max_count = int(distance_A_B / stride)

        #Calculate the number of steps required for the next point ,Otherwise count to zero
        unit_vector_x = (bx - ax) / distance_A_B
        unit_vector_y = (by - ay) / distance_A_B
        delta_x = unit_vector_x * stride
        delta_y = unit_vector_y * stride

        if self.move_count < max_count:
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1

        else:
            self.move_count = 0
            self.path_index += 1



class EnemyGroup:
    def __init__(self):
        self.campaign_count = 0         # self.reserved_members location
        self.campaign_max_count = 120   # (unit: frame)
        self.reserved_members = []      # the list to save Enemy
        self.expedition = []            # don't change this line until you do the EX.3
        self.period = 0                 # Passing unit (frame)
        self.wave_num = 0             # to calculate the wave of enemies


    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """
        if len(self.reserved_members) > 0 :
            if self.campaign_count > self.campaign_max_count :
                self.expedition.append(self.reserved_members.pop()) # Put Enemy() into self.expedition
                self.campaign_count = 0 # When the condition is greater than 120, return to zero when satisfied
            else:
                self.campaign_count += 1 # When the condition is not met +1


    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        for i in range(num):
            self.reserved_members.append(Enemy(self.wave_num))      #Put the resulting Enemy() into members
        if self.wave_num == 0:
            self.wave_num = 1
            print("This way is PATH 1 .")                           # when wave_num = 1, self.path select PATH_1 from the left
        else:
            self.wave_num = 0
            print("This way is PATH 2 .")                           # when wave_num = 0, self.path select PATH_ from the right
        self.period = 0
        self.campaign_count = 0

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)