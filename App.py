import tkinter as tk
from PIL import Image, ImageTk
import ILib
import random
import IFrame
import config

class App:
    """
    classe principale du jeu qui va appeler les autres méthodes et classes
    Initialise le menu et la configuration des touches
    """
    def __init__(self, main):
        print("init App")
        self.main = main

        self.alienCollision = False

        self.tk = tk.Tk()
        self.tk.geometry(str(main.xSize) + "x" + str(main.ySize))
        self.tk.minsize(main.xSize, main.ySize)
        self.tk.maxsize(main.xSize, main.ySize)

        # LOADING ASSETS
        self.assets = {}
        self.initAssets()

        self.configObject = config.Config('config.ini')    #classe config
        self.config = self.configObject.read_config()     #dictionnaire contenant la configuration

        self.menu = "menu"

        self.gameFrame = IFrame.GameFrame(self)
        self.gameFrame.unBind()

        self.settings = IFrame.SettingsFrame(self)
        self.settings.frame.grid_forget()

        self.menuFrame = IFrame.GameMenu(self)

    def update_config(self):
        """
        :return: update la config des objets du jeu
        """
        self.configObject.modify_config(self.config)

    def initAssets(self):
        """
        initialise les assets donc les textures des joueurs et des monstres et des blocks,les textures des blocs et des monstres une fois endommagés
        :return: rien
        """
        # BACKGROUND
        self.assets['background'] = []
        image = Image.open("assets/background.jpg")
        image = image.resize((self.main.xSize, self.main.ySize
        ))
        self.assets['background'].append(ImageTk.PhotoImage(image))

        # PLAYER
        self.assets['player'] = []
        image = Image.open("assets/player.png")
        image = image.resize((45, 45
        ))
        self.assets['player'].append(ImageTk.PhotoImage(image))

        # MONSTER
        self.assets['monster'] = []
        image = Image.open("assets/monster_yellow.png")
        image = image.resize((30, 30))
        self.assets['monster'].append(ImageTk.PhotoImage(image))
        image = Image.open("assets/monster_orange.png")
        image = image.resize((30, 30))
        self.assets['monster'].append(ImageTk.PhotoImage(image))
        image = Image.open("assets/monster_red.png")
        image = image.resize((30, 30))
        self.assets['monster'].append(ImageTk.PhotoImage(image))
        image = Image.open("assets/monster_black_red.png")
        image = image.resize((30, 30))
        self.assets['monster'].append(ImageTk.PhotoImage(image))

        # MONSTER DAMAGES
        self.assets['monster_damages'] = []
        for i in range(0,4):
            image = Image.open("assets/monster_hit_"+str(3 - i)+".png")
            image = image.resize((30, 30))
            self.assets['monster_damages'].append(ImageTk.PhotoImage(image))

        # BLOCKS
        self.assets['block'] = []
        image = Image.open("assets/stone.png")
        image = image.resize((30, 30))
        self.assets['block'].append(ImageTk.PhotoImage(image))

        # BLOCKS DAMAGES
        self.assets['block_damages'] = []
        for i in range(0,3):
            image = Image.open("assets/hit_"+str(2 - i)+".png")
            image = image.resize((30, 30))
            self.assets['block_damages'].append(ImageTk.PhotoImage(image))

        # HEALTH ENTITI
        self.assets['heart'] = []
        image = Image.open("assets/heart.png")
        image = image.resize((10, 10))
        self.assets['heart'].append(ImageTk.PhotoImage(image))


        self.assetsSize = {}
        for k,v in self.assets.items():
            self.assetsSize[k] = len(v)
        print(self.assetsSize)

    def update(self):
        """
        update les frames en fonction de la valeur de self.menu qui indique à quelle page on doit se situer.
        :return:
        """
        if self.menu == "play":
            self.gameFrame.update()
            self.tk.update_idletasks()
            self.tk.update()

        elif self.menu == "menu":
            self.tk.update_idletasks()
            self.tk.update()

        elif self.menu == "settings":
            self.tk.update_idletasks()
            self.tk.update()

    def draw(self):
        """
        affiche la bonne frame et le bon canvas.
        :return:
        """
        if self.menu == "play":
            self.gameFrame.draw()
