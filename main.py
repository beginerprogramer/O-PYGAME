import pygame
from game import Game
pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption('ezzir')
screen = pygame.display.set_mode((1080, 720))

# importer charger l'arriere plan²
background = pygame.image.load('assets/bg.jpg')

game = Game()

running = True

while running:

    # appliquer la background du jeu
    screen.blit(background, (0, -200))

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer le monstre de notre jeu

    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des image de mon monstre
    game.all_monsters.draw(screen)

    # verifier si le joueur souhaite aller a gauche ou a droite et ajuster les bordures
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()


    # mettre a jour l'ecran
    pygame.display.flip()
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("closing the game")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenche pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
