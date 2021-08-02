import pygame
import os

# load image
UPGRAGE_MENU = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade_menu.png")),(200,200))
UPGRAGE_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade.png")), (70, 45))
SELL_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "sell.png")), (45, 45))

class UpgradeMenu:
    def __init__(self, x, y):
        #Create upgrade button and sell button
        self.__buttons = [Button(UPGRAGE_BUTTON, "upgrade", x, y - 70),Button(SELL_BUTTON, "sell", x, y + 75)]
        self.image = UPGRAGE_MENU
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image, self.rect)

        # draw button
        # (Q2) Draw buttons here
        for but in self.__buttons:
            win.blit(but.image, but.rect)


    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons

class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image  # image of the button
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the menu image

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        # If the mouse clicks within the image range of the button, return True
        return True if self.rect.collidepoint(x, y) else False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name





