import pygame


# creer une classe qui va gerer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 20
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 2

    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie (rouge )
        bar_color = (111, 210, 46)
        # definir une couleur pour l'arriere plan de la jauge (gris fonce)
        back_bar_color = (60, 63, 60)

        # definir la position de notre jauge de vie et ainsi sa largeur et soon epaiseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]  # x y w h
        # definir la position de notre arriere plan de notre jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner notre barre de vie
        pygame.draw.rect(surface, bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
