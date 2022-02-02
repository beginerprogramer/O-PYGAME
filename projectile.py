import pygame


# definir la classe qui va gerer notre projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    # definir la constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (59, 59))  # taille de projectile
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 100
        self.origin_image = self.image
        self.angle = 2

    def rotate(self):
        # tourner le projectile
        self.angle += 7  # vitesse d'animation du projectile
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectilme entre dans collision avec un monstre
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            # suprimer le projectile
            self.remove()

        # verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > 1000:
            # suprimer le projectile(en dehors de l'ecran)
            self.remove()
