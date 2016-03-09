import pygame #This imports all the pygame methods

pygame.init() #This initialize the methods

gameDisplay = pygame.display.set_mode((600,480))
	#Display setmode sets the screen size
pygame.display.set_caption('Snake Me')
	#Display set caption give the name to the window
	
#Defining colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#Defining frame
clock = pygame.time.Clock()


#Defining the snake head
lead_x = 200
lead_y = 200
lead_x_change = 0
lead_y_change = 0

gameExit = False

while not gameExit:# This is the main loop
	for event in pygame.event.get():# This fetches all the events like keyup, mousemove
		if event.type == pygame.QUIT:# For all other types of events refer to pygameEvent.txt
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -2
				lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = 2
				lead_y_change = 0
			elif event.key == pygame.K_UP:
				lead_y_change = -2
				lead_x_change = 0
			elif event.key == pygame.K_DOWN:
				lead_y_change = 2
				lead_x_change = 0
	
	lead_x += lead_x_change	# Usign while loop for continuous movement
	lead_y += lead_y_change	# Usign while loop for continuous movement		
	gameDisplay.fill(white) # this puts the background color
	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, 10, 10])
	pygame.display.update();
	
	clock.tick(30)# This sets the frames per second

pygame.quit()
quit()
