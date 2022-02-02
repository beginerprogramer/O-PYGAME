# creer une premiere classe qi va representer notre joueur
import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.game = game
        self.health = 50
        self.max_health = 50
        self.attack = 15
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()  # bach mitirich projectile wa7d
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec le monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity  # velocity pour definir vitesse de joueur + pour la droite et - pour la gauche

    def move_left(self):
        self.rect.x -= self.velocity
