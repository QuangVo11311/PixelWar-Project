import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
		pygame.display.set_caption('7Phu Impact')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def run(self):
		game_over = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)

			if not game_over:
				self.level.run()
			else:
				self.show_game_over()

			pygame.display.update()
			self.clock.tick(FPS)

			if self.level.check_game_over():
				game_over = True

if __name__ == '__main__':
	game = Game()
	game.run()