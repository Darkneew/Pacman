import sys, pygame
from pygame.locals import *
pygame.init()


size = width, height = 380,500
black = (0, 0, 0)
blue = (52, 152, 235)

game = {
  "pacman": {
    "pos": {
      "x": 180,
      "y": 280
    },
    "mouth":True,
    "strong": False,
    "direction": 0
  },
  "blue": {
    "pos": {
      "x": 200,
      "y": 220
    },
    "direction": 3
  },
  "pink": {
    "pos": {
      "x": 200,
      "y": 240
    },
    "direction": 2
  },
  "red": {
    "pos": {
      "x": 160,
      "y": 240
    },
    "direction": 1
  },
  "orange": {
    "pos": {
      "x": 160,
      "y": 220
    },
    "direction": 0
  },
  "balls": [],
  "ia": {},
  "walls": [[0,0],[0,20],[0,40],[0,60],[0,80],[0,100],[0,120],[0,140],[0,160],[0,180],[0,200],[0,220],[0,240],[0,260],[0,280],[0,300],[0,320],[0,340],[0,360],[0,380],[0,400],[0,420],[0,440],[0,460],[0,480],[360,0],[360,20],[360,40],[360,60],[360,80],[360,100],[360,120],[360,140],[360,160],[360,180],[360,200],[360,220],[360,240],[360,260],[360,280],[360,300],[360,320],[360,340],[360,360],[360,380],[360,400],[360,420],[360,440],[360,460],[360,480]]
}

def inWall(pos):
  vraiOuFaux = False
  for wall in game.walls:
    if pos.x == wall.x and pos.y == wall.y:
      vraiOuFaux = True
  return vraiOuFaux

def Reposition():
  return True

screen = pygame.display.set_mode(size)

# Drawing the map
screen.fill(black)
for wall in game["walls"]:  
  pygame.draw.rect(screen, blue, (wall[0],wall[1],20,20))
while True:# LOOP Principale
  # Exit proprement
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  # Decisions des IAs
  # Tout afficher
  Reposition()
  pygame.display.flip()
  pygame.time.delay(100)