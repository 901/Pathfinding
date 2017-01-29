import pygame
import random
import math
from random import randint
from ast import literal_eval as make_tuple

# Initialize Screen
pygame.init()
myfont = pygame.font.SysFont("monospace", 15)

blockwidth = 6				# Drawing dimensions of block
GridCols = 160
GridRows = 120
GameScreen = pygame.display.set_mode((GridCols*blockwidth+200,GridRows*blockwidth+34))

# Initialize Grid
grid = [['1' for y in range(GridRows)] for x in range(GridCols)]
start_x = 0
start_y = 0
goal_x = 1
goal_y = 1

cursor_x = 0
cursor_y = 0

# Make Random Grid
def makeGrid():
	# Make 8 hard to traverse areas
	areasmade = 0
	areacoordinates = []
	while areasmade < 8:
		area_x = randint(0,GridCols-1)
		area_y = randint(0,GridRows-1)
		
		if (area_x,area_y) not in areacoordinates:
			areacoordinates.append((area_x,area_y))
			for x in range(area_x-15,area_x+15):
				if x >= 0 and x < GridCols:
					for y in range(area_y-15,area_y+15):
						if y >= 0 and y < GridRows:
							# 20% chance of this being hard to traverse
							if randint(0,9) < 5:
								grid[x][y] = '2'
			
			#drawScreen()
			areasmade += 1
			

	# Make 4 rivers
	riversmade = 0
	
	while riversmade < 4:
		makeriver = True
		rivercells = []
		
		# Select a starting boundary
		x = randint(1,GridCols-2)
		y = randint(1,GridRows-2)
		
		startside = randint(0,3)	# 0 = North, 1 = East, 2 = South, 3 = West
		if startside == 0:
			y = 0
			direction = 2
			#direction = random.choice([1,2,3])
		elif startside == 1:
			x = GridCols-1
			direction = 3
			#direction = random.choice([0,2,3])
		elif startside == 2:
			y = GridRows-1
			direction = 0
			#direction = random.choice([0,1,3])
		else:
			x = 0
			direction = 1
			#direction = random.choice([0,1,2])
		
		travelled = 0
		totaltravelled = 0
		
		while True:
			# Quit if out of bounds
			if x<0 or x>=GridCols or y<0 or y>=GridRows:
				break
			
			# Quit if crossed a river, do not make river
			if grid[x][y] == 'a' or grid[x][y] == 'b':
				makeriver = False
				break
			if (x,y) in rivercells:
				makeriver = False
				break
				
			rivercells.append((x,y))
			travelled += 1
			totaltravelled += 1
			
			# Move to next cell
			if direction == 0:
				y -= 1
			elif direction == 1:
				x += 1
			elif direction == 2:
				y += 1
			else:
				x -= 1
				
			# Change directions if travelled 20 cells
			if travelled >= 20:
				travelled = 0
				if randint(0,9) > 6:		# 40% chance change directions
					if direction == 0:
						direction = random.choice([1,3])
					elif direction == 1:
						direction = random.choice([0,2])
					elif direction == 2:
						direction = random.choice([1,3])
					else:
						direction = random.choice([0,2])
		
		if totaltravelled < 100:
			makeriver = False
		
		if makeriver == True:
			for cell in rivercells:
				if grid[cell[0]][cell[1]] == '1':
					grid[cell[0]][cell[1]] = 'a'
				else:
					grid[cell[0]][cell[1]] = 'b'
				
			riversmade += 1
			
	# Blocked cells
	needtoblock = GridCols*GridRows*0.2
	blocked = 0
	
	while blocked < needtoblock:
		x = randint(0,GridCols-1)
		y = randint(0,GridRows-1)
		if grid[x][y]=='1' or grid[x][y]=='2':
			grid[x][y] = '0'
			blocked += 1
	
	# Return the coordinates of hard to traverse areas
	return areacoordinates
	
# Generate Start and Finish
def generateStartFinish():

	# Generate Start
	x = randint(0,39)
	y = randint(0,39)
	if x>20:
		x = GridCols-x
	if y>20:
		y = GridRows-y
		
	while grid[x][y]=='a' or grid[x][y]=='b':
		x = randint(0,GridCols-1)
		y = randint(0,GridRows-1)
		if x>20:
			x = GridCols-x
		if y>20:
			y = GridRows-y
		
	start_x = x
	start_y = y
	
	# Generate Finish
	while grid[x][y]=='a' or grid[x][y]=='b' or grid[x][y]=='0' or math.sqrt((x-start_x)**2+(y-start_y)**2)<100:
		x = randint(0,GridCols-1)
		y = randint(0,GridRows-1)
		if x>20:
			x = GridCols-x
		if y>20:
			y = GridRows-y

	goal_x = x
	goal_y = y
	
	return start_x,start_y,goal_x,goal_y

# Draw Grid
def drawGrid(myGridSurface):
	myGridSurface.fill((255,255,255))
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] == '0': 
				pygame.draw.rect(myGridSurface, (40,40,40), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(myGridSurface, (40,40,40), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
			elif grid[x][y] == '1': 
				pygame.draw.rect(myGridSurface, (255,255,255), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(myGridSurface, (100,100,100), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
			elif grid[x][y] == '2': 
				pygame.draw.rect(myGridSurface, (200,200,200), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(myGridSurface, (100,100,100), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
			elif grid[x][y] == 'a': 
				pygame.draw.rect(myGridSurface, (130,170,255), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(myGridSurface, (100,100,100), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
			elif grid[x][y] == 'b': 
				pygame.draw.rect(myGridSurface, (70,90,220), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(myGridSurface, (100,100,100), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
	
	myGridSurface = myGridSurface.convert()
	return myGridSurface
	
# Draw Screen
def drawScreen(GridSurface):
	'''GameScreen.fill((255,255,255))
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] == '0': 
				pygame.draw.rect(GameScreen, (40,40,40), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(GameScreen, (40,40,40), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
			elif grid[x][y] == '1': 
				pygame.draw.rect(GameScreen, (255,255,255), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(GameScreen, (100,100,100), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
			elif grid[x][y] == '2': 
				pygame.draw.rect(GameScreen, (200,200,200), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(GameScreen, (100,100,100), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
			elif grid[x][y] == 'a': 
				pygame.draw.rect(GameScreen, (130,170,255), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(GameScreen, (100,100,100), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)
			elif grid[x][y] == 'b': 
				pygame.draw.rect(GameScreen, (70,90,220), (x*blockwidth+10,y*blockwidth+10,blockwidth,blockwidth), 0)
				pygame.draw.rect(GameScreen, (100,100,100), (x*blockwidth+10,y*blockwidth+10,blockwidth+1,blockwidth+1), 1)'''
	
	GameScreen.blit(GridSurface,(0,0))
	
	pygame.draw.circle(GameScreen, (255,0,0), (start_x*blockwidth+blockwidth/2+10,start_y*blockwidth+blockwidth/2+10),blockwidth/2, 0)
	pygame.draw.circle(GameScreen, (0,255,0), (goal_x*blockwidth+blockwidth/2+10,goal_y*blockwidth+blockwidth/2+10),blockwidth/2, 0)
	
	pygame.draw.rect(GameScreen, (255,0,0), (cursor_x*blockwidth+9,cursor_y*blockwidth+9,blockwidth+2,blockwidth+2), 2)
	
	# Draw text
	label = myfont.render("G = Generate Grid     E = New Start (R) and Goal (G)     S = Save Map     L = Load Map     Esc = Quit", 1, (0,0,0))
	GameScreen.blit(label, (30, blockwidth*GridRows+14))
	
	label = myfont.render("("+str(cursor_x)+","+str(cursor_y)+")", 1, (0,0,0))
	GameScreen.blit(label, (10+blockwidth*GridCols+30, 30))
	
	label = myfont.render("Type: "+grid[cursor_x][cursor_y], 1, (0,0,0))
	GameScreen.blit(label, (10+blockwidth*GridCols+30, 50))
	
	
	label = myfont.render("Start: ("+str(start_x)+","+str(start_y)+")", 1, (0,0,0))
	GameScreen.blit(label, (10+blockwidth*GridCols+30, 80))
	label = myfont.render("Goal: ("+str(goal_x)+","+str(goal_y)+")", 1, (0,0,0))
	GameScreen.blit(label, (10+blockwidth*GridCols+30, 100))
	
	label = myfont.render("Neighbors:", 1, (0,0,0))
	GameScreen.blit(label, (10+blockwidth*GridCols+30, 130))
	
	draw_y = 150
	neighbors = getNeighbors(cursor_x,cursor_y)
	
	for neighbor in neighbors:
		label = myfont.render("("+str(neighbor[0])+","+str(neighbor[1])+")", 1, (0,0,0))
		GameScreen.blit(label, (10+blockwidth*GridCols+30, draw_y))
		draw_y += 20
	
	pygame.display.update()

# Get neighbors of a cell
def getNeighbors(x,y):
	myneighbors = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
	
	'''for neighbor in myneighbors:
		if neighbor[0] < 0:							# Out of bounds left
			myneighbors.remove(neighbor)
		elif neighbor[0] >= GridCols:				# Out of bounds right
			myneighbors.remove(neighbor)
		elif neighbor[1] < 0:						# Out of bounds up
			myneighbors.remove(neighbor)
		elif neighbor[1] >= GridRows:				# Out of bounds down
			myneighbors.remove(neighbor)
		elif grid[neighbor[0]][neighbor[1]] == '0':	# Wall
			myneighbors.remove(neighbor)'''
			
	myneighbors[:] = [neighbor for neighbor in myneighbors if neighbor[0]>=0 and neighbor[1]>=0 and neighbor[0]<GridCols and neighbor[1]<GridRows and grid[neighbor[0]][neighbor[1]] != '0']
	
	return myneighbors
	
# Main loop
running = True

GridSurface = pygame.Surface(GameScreen.get_size())

areacoordinates = makeGrid()
GridSurface = drawGrid(GridSurface)
start_x,start_y,goal_x,goal_y = generateStartFinish()

while(running):
	# Get Input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			elif event.key == pygame.K_g:
				grid = [['1' for y in range(GridRows)] for x in range(GridCols)]
				areacoordinates = makeGrid()
				GridSurface = drawGrid(GridSurface)
				start_x,start_y,goal_x,goal_y = generateStartFinish()
				print "Generated new map"
			elif event.key == pygame.K_e:
				start_x,start_y,goal_x,goal_y = generateStartFinish()
				print "Generated new start and finish points"
			elif event.key == pygame.K_s:
				# Save map: get filename
				filename = raw_input("Save map to: ")
				with open(filename,"w") as mapfile:
					mapfile.write(str((start_x,start_y)))		# Write start
					mapfile.write("\n")
					mapfile.write(str((goal_x,goal_y)))			# Write goal
					mapfile.write("\n")
					
					for area in areacoordinates:				# Write hard to traverse area centers
						mapfile.write(str((area[0],area[1])))		
						mapfile.write("\n")
					
					for y in range(len(grid[x])):				# Write each cell
						for x in range(len(grid)):					
							mapfile.write(str(grid[x][y]))		
						mapfile.write("\n")
					
					mapfile.close()
				print "Map saved!"
			elif event.key == pygame.K_l:
				# Load map: get filename
				filename = raw_input("Load map from: ")
				with open(filename,"r") as mapfile:
					new_start = make_tuple(mapfile.readline())
					start_x = new_start[0]
					start_y = new_start[1]
					new_goal = make_tuple(mapfile.readline())
					goal_x = new_goal[0]
					goal_y = new_goal[1]
					
					for i in range(8):
						mapfile.readline()
					
					for y in range(len(grid[x])):				# Read each cell
						for x in range(len(grid)):					
							grid[x][y] = mapfile.read(1)
						mapfile.read(1)
					
					mapfile.close()
					GridSurface = drawGrid(GridSurface)
				print "Map loaded!"
			elif event.key == pygame.K_UP:
				if cursor_y-1 >= 0:
					cursor_y -= 1
			elif event.key == pygame.K_LEFT:
				if cursor_x-1 >= 0:
					cursor_x -= 1
			elif event.key == pygame.K_RIGHT:
				if cursor_x+1 < GridCols:
					cursor_x += 1
			elif event.key == pygame.K_DOWN:
				if cursor_y+1 < GridRows:
					cursor_y += 1
		# Draw grid
		drawScreen(GridSurface)

pygame.quit()