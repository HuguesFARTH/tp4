import tkinter as tk
import math
import Monster
import Player
import Heart

class Projectile:
    """

    """
    def __init__(self, app, canvas, dir: list, pos: list, isplayer):
        self.app = app
        self.canvas = canvas
        self.dir = dir
        self.pos = pos
        self.rayon = 5
        self.isplayer = isplayer
        self.speed = 20 * self.app.config['bulletSpeed']


    def draw(self):
        """
        Affichage du projectile
        :return:
        """
        self.canvas.create_oval(self.pos[0]-self.rayon, self.pos[1]-self.rayon ,self.pos[0]+self.rayon , self.pos[1]+self.rayon, fill = "green" if self.isplayer else "red" )

    def update(self):
        """
        update du projectile
        :return:
        """
        self.pos[0] += self.dir[0] * self.speed
        self.pos[1] += self.dir[1] * self.speed
        self.collide()
        if self.pos[0] < 0:
            self.remove()
        if self.pos[0] > int(self.canvas.cget('width')):
            self.remove()
        if self.pos[1] < 0:
            self.remove()
        if self.pos[1] > int(self.canvas.cget('height')):
            self.remove()


    def remove(self):
        """

        :return:
        """
        if self in self.app.gameFrame.entities:
            self.app.gameFrame.entities.remove(self)

    def collide(self):
        """
        Verifie la collision entre un projectile et un block/player/monster
        :return:
        """
        for ent in self.app.gameFrame.entities:
            if isinstance(ent, Projectile):
                continue
            if isinstance(ent, Heart.Heart):
                continue
            elif not self.isplayer and isinstance(ent,Monster.Monster):
                continue
            elif self.isplayer and isinstance(ent,Player.Player):
                continue
            elif math.pow(self.pos[0]-ent.pos[0],2) + math.pow(self.pos[1]-ent.pos[1],2)< math.pow(self.rayon + ent.size/2,2):
                self.remove()
                ent.hit()
                return
