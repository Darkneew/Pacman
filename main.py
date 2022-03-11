import sys, pygame 
# La ligne ci dessous est a changé pour mettre votre IA a la place de l'exemple ou du test
from test import SetRedDirection as redIa, SetBlueDirection as blueIa, SetPinkDirection as pinkIa, SetOrangeDirection as orangeIa
from ia import Ia as pacmanIa
from pygame.locals import *
pygame.init()
size = width, height = 380,500
black = (0, 0, 0)
blue = (65,105,225)

# Setting up the scene and loading images
screen = pygame.display.set_mode(size)
BALL = pygame.image.load('ressources/ball.png').convert_alpha()
OPACMAN = pygame.image.load('ressources/OPacman.png').convert_alpha()
CPACMAN = pygame.image.load('ressources/CPacman.png').convert_alpha()
RED = pygame.image.load('ressources/Red.png').convert_alpha()
ORANGE = pygame.image.load('ressources/Orange.png').convert_alpha()
BLUE = pygame.image.load('ressources/Blue.png').convert_alpha()
PINK = pygame.image.load('ressources/Pink.png').convert_alpha()

game = {
  "turn":0,
  "score": 0,
  "pacman": {
    "pos": {
      "x": 180,
      "y": 280
    },
    "mouth":True,
    "strong": False,
    "direction": 0,
    "previousDirection": 0
  },
  "blue": {
    "pos": {
      "x": 200,
      "y": 220
    },
    "direction": 3,
    "previousDirection": 3,
    "previousPos":{
      "x": 200,
      "y": 220
    }
  },
  "pink": {
    "pos": {
      "x": 200,
      "y": 240
    },
    "direction": 2,
    "previousDirection": 2,
    "previousPos":{
      "x": 200,
      "y": 240
    }
  },
  "red": {
    "pos": {
      "x": 180,
      "y": 180
    },
    "direction": 1,
    "previousDirection":1,
    "previousPos":{
      "x": 180,
      "y": 180
    }
  },
  "orange": {
    "pos": {
      "x": 160,
      "y": 220
    },
    "direction": 0,
    "previousDirection":0,
    "previousPos":{
      "x": 160,
      "y": 220
    }
  },
  "balls": [[20, 20], [40, 20], [60, 20], [80, 20], [100, 20], [120, 20], [140, 20], [160, 20], [200, 20], [220, 20], [240, 20], [260, 20], [280, 20], [300, 20], [320, 20], [340, 20], [20, 40], [80, 40], [160, 40], [200, 40], [280, 40], [340, 40], [20, 60], [80, 60], [160, 60], [200, 60], [280, 60], [340, 60],[20, 80], [40, 80], [60, 80], [80, 80], [100, 80], [120, 80], [140, 80], [160, 80], [180, 80], [200, 80], [220, 80], [240, 80], [260, 80], [280, 80], [300, 80], [320, 80], [340, 80], [20, 100], [80, 100], [120, 100], [240, 100], [280, 100], [340, 100], [20, 120], [40, 120], [60, 120], [80, 120], [120, 120], [240, 120], [280, 120], [300, 120], [320, 120], [340, 120],[80, 140], [120, 140], [140, 140], [160, 140], [200, 140], [220, 140], [240, 140], [280, 140], [80, 160], [160, 160], [200, 160], [280, 160], [80, 180], [120, 180], [140, 180], [160, 180], [180, 180], [200, 180], [220, 180], [240, 180], [280, 180],[80, 200], [120, 200], [240, 200], [280, 200], [80, 220], [120, 220], [240, 220], [280, 220], [80, 240], [100, 240], [120, 240], [240, 240], [260, 240], [280, 240], [80, 260], [120, 260], [240, 260], [280, 260], [80, 280], [120, 280], [140, 280], [160, 280], [200, 280], [220, 280], [240, 280], [280, 280], [80, 300], [120, 300], [240, 300], [280, 300],[80, 320], [120, 320], [240, 320], [280, 320], [80, 340], [100, 340], [120, 340], [140, 340], [160, 340], [200, 340], [220, 340], [240, 340], [260, 340], [280, 340], [20, 360], [40, 360], [60, 360], [80, 360], [160, 360], [200, 360], [280, 360], [300, 360], [320, 360], [340, 360],[20, 380], [80, 380], [100, 380], [120, 380], [140, 380], [160, 380], [180, 380], [200, 380], [220, 380], [240, 380], [260, 380], [280, 380], [340, 380], [20, 400], [80, 400], [120, 400], [240, 400], [280, 400], [340, 400], [20, 420], [40, 420], [60, 420], [80, 420], [120, 420], [140, 420], [160, 420], [200, 420], [220, 420], [240, 420], [280, 420], [300, 420], [320, 420], [340, 420],[20, 440], [160, 440], [200, 440], [340, 440], [20, 460], [40, 460], [60, 460], [80, 460], [100, 460], [120, 460], [140, 460], [160, 460], [180, 460], [200, 460], [220, 460], [240, 460], [260, 460], [280, 460], [300, 460], [320, 460], [340, 460]],
  "ia": {},
  "walls": [[0,0],[0,20],[0,40],[0,60],[0,80],[0,100],[0,120],[0,140],[0,160],[0,180],[0,200],[0,220],[0,260],[0,280],[0,300],[0,320],[0,340],[0,360],[0,380],[0,400],[0,420],[0,440],[0,460],[0,480],[360,0],[360,20],[360,40],[360,60],[360,80],[360,100],[360,120],[360,140],[360,160],[360,180],[360,200],[360,220],[360,260],[360,280],[360,300],[360,320],[360,340],[360,360],[360,380],[360,400],[360,420],[360,440],[360,460],[360,480],[20,0],[40,0],[60,0],[80,0],[100,0],[120,0],[140,0],[160,0],[180,0],[200,0],[220,0],[240,0],[260,0],[280,0],[300,0],[320,0],[340,0],[20,480],[40,480],[60,480],[80,480],[100,480],[120,480],[140,480],[160,480],[180,480],[200,480],[220,480],[240,480],[260,480],[280,480],[300,480],[320,480],[340,480],[180, 20], [40, 40], [60, 40], [100, 40], [120, 40], [140, 40], [180, 40], [220, 40], [240, 40], [260, 40], [300, 40], [320, 40], [40, 60], [60, 60], [100, 60], [120, 60], [140, 60], [180, 60], [220, 60], [240, 60], [260, 60], [300, 60], [320, 60],[40, 100], [60, 100], [100, 100], [140, 100], [160, 100], [180, 100], [200, 100], [220, 100], [260, 100], [300, 100], [320, 100], [100, 120], [140, 120], [160, 120], [180, 120], [200, 120], [220, 120], [260, 120],[20, 140], [40, 140], [60, 140], [100, 140], [180, 140], [260, 140], [300, 140], [320, 140], [340, 140], [20, 160], [40, 160], [60, 160], [100, 160], [120, 160], [140, 160], [180, 160], [220, 160], [240, 160], [260, 160], [300, 160], [320, 160], [340, 160], [20, 180], [40, 180], [60, 180], [100, 180], [260, 180], [300, 180], [320, 180], [340, 180],[20, 200], [40, 200], [60, 200], [100, 200], [140, 200], [160, 200], [180, 200], [200, 200], [220, 200], [260, 200], [300, 200], [320, 200], [340, 200], [20, 220], [40, 220], [60, 220], [100, 220], [140, 220], [220, 220], [260, 220], [300, 220], [320, 220], [340, 220], [140, 240], [220, 240],[20, 260], [40, 260], [60, 260], [100, 260], [140, 260], [160, 260], [180, 260], [200, 260], [220, 260], [260, 260], [300, 260], [320, 260], [340, 260], [20, 280], [40, 280], [60, 280], [100, 280], [260, 280], [300, 280], [320, 280], [340, 280], [20, 300], [40, 300], [60, 300], [100, 300], [140, 300], [160, 300], [180, 300], [200, 300], [220, 300], [260, 300], [300, 300], [320, 300], [340, 300],[20, 320], [40, 320], [60, 320], [100, 320], [140, 320], [160, 320], [180, 320], [200, 320], [220, 320], [260, 320], [300, 320], [320, 320], [340, 320], [20, 340], [40, 340], [60, 340], [180, 340], [300, 340], [320, 340], [340, 340], [100, 360], [120, 360], [140, 360], [180, 360], [220, 360], [240, 360], [260, 360],[40, 380], [60, 380], [300, 380], [320, 380], [40, 400], [60, 400], [100, 400], [140, 400], [160, 400], [180, 400], [200, 400], [220, 400], [260, 400], [300, 400], [320, 400], [100, 420], [180, 420], [260, 420],[40, 440], [60, 440], [80, 440], [100, 440], [120, 440], [140, 440], [180, 440], [220, 440], [240, 440], [260, 440], [280, 440], [300, 440], [320, 440]]
}

def nextpos(pos, direction):
  pos["y"] = pos["y"] + 20
  nextdir = 3
  if inWall(pos) or direction == 1:
    pos["y"] = pos["y"] - 40
    nextdir = 1
    if inWall(pos) or direction == 3:
      pos["y"] = pos["y"] + 20
      pos["x"] = pos["x"] - 20
      nextdir = 2
      if inWall(pos) or direction == 0:
        pos["x"] = pos["x"] + 40
        nextdir = 0
        if inWall(pos) or direction == 2:
          raise Exception("No escape route")
  return (pos, nextdir)

def inBall(pos): # Check si une position correspond à une balle
  vraiOuFaux = False
  for ball in game["balls"]:
    if pos["x"] == ball[0] and pos["y"] == ball[1]:
      vraiOuFaux = True
      break
  return vraiOuFaux

def inWall(pos): # Check si une position corespond a un mur
  vraiOuFaux = False
  for wall in game["walls"]:
    if pos["x"] == wall[0] and pos["y"] == wall[1]:
      vraiOuFaux = True
      break
  return vraiOuFaux

def Reposition(): 
  # Repositionne toute les entités du jeu
  # Reposition du pacman
  if game["pacman"]["pos"]["x"] == 0 and game["pacman"]["pos"]["y"] == 240:
    game["pacman"]["pos"]["x"] = 360
  if game["pacman"]["pos"]["x"] == 360 and game["pacman"]["pos"]["y"] == 240:
    game["pacman"]["pos"]["x"] = 0
  game["pacman"]["previousDirection"] = game["pacman"]["direction"]
  game["pacman"]["direction"] = pacmanIa(game)
  inAWall = False
  if game["pacman"]["direction"] == 0:
    game["pacman"]["pos"]["x"] = game["pacman"]["pos"]["x"] + 20
    if inWall(game["pacman"]["pos"]):
      game["pacman"]["pos"]["x"] = game["pacman"]["pos"]["x"] - 20
      inAWall = True
  elif game["pacman"]["direction"] == 1:
    game["pacman"]["pos"]["y"] = game["pacman"]["pos"]["y"] - 20
    if inWall(game["pacman"]["pos"]):
      game["pacman"]["pos"]["y"] = game["pacman"]["pos"]["y"] + 20
      inAWall = True
  elif game["pacman"]["direction"] == 2:
    game["pacman"]["pos"]["x"] = game["pacman"]["pos"]["x"] - 20
    if inWall(game["pacman"]["pos"]):
      game["pacman"]["pos"]["x"] = game["pacman"]["pos"]["x"] + 20
      inAWall = True
  elif game["pacman"]["direction"] == 3:
    game["pacman"]["pos"]["y"] = game["pacman"]["pos"]["y"] + 20
    if inWall(game["pacman"]["pos"]):
      game["pacman"]["pos"]["y"] = game["pacman"]["pos"]["y"] - 20
      inAWall = True
  else :
    inAWall = True
  if inAWall :
    game["pacman"]["direction"] = game["pacman"]["previousDirection"]
    game["pacman"]["pos"], game["pacman"]["direction"] = nextpos(game["pacman"]["pos"], game["pacman"]["direction"])
  # Si il mange une boule
  for i in range(len(game["balls"])):
    ball = game["balls"][i]
    if game["pacman"]["pos"]["x"] == ball[0] and game["pacman"]["pos"]["y"] == ball[1]:
      del game["balls"][i]
      game["score"] = game["score"] + 1
      break
  # Reposition de red
  game["red"]["previousPos"]["x"] = game["red"]["pos"]["x"]
  game["red"]["previousPos"]["y"] = game["red"]["pos"]["y"]
  if game["pacman"]["pos"]["x"] == game["red"]["pos"]["x"] and game["pacman"]["pos"]["y"] == game["red"]["pos"]["y"]:
    return False
  if game["red"]["pos"]["x"] == 0 and game["red"]["pos"]["y"] == 240:
    game["red"]["pos"]["x"] = 360
  if game["red"]["pos"]["x"] == 360 and game["red"]["pos"]["y"] == 240:
    game["red"]["pos"]["x"] = 0
  game["red"]["previousDirection"] = game["red"]["direction"]
  game["red"]["direction"] = redIa(game)
  inAWall = False
  if game["red"]["direction"] == 0:
    game["red"]["pos"]["x"] = game["red"]["pos"]["x"] + 20
    if inWall(game["red"]["pos"]) or game["red"]["previousDirection"] == 2:
      game["red"]["pos"]["x"] = game["red"]["pos"]["x"] - 20
      inAWall = True
  elif game["red"]["direction"] == 1:
    game["red"]["pos"]["y"] = game["red"]["pos"]["y"] - 20
    if inWall(game["red"]["pos"]) or game["red"]["previousDirection"] == 3:
      game["red"]["pos"]["y"] = game["red"]["pos"]["y"] + 20
      inAWall = True
  elif game["red"]["direction"] == 2:
    game["red"]["pos"]["x"] = game["red"]["pos"]["x"] - 20
    if inWall(game["red"]["pos"]) or game["red"]["previousDirection"] == 0:
      game["red"]["pos"]["x"] = game["red"]["pos"]["x"] + 20
      inAWall = True
  elif game["red"]["direction"] == 3:
    game["red"]["pos"]["y"] = game["red"]["pos"]["y"] + 20
    if inWall(game["red"]["pos"]) or game["red"]["previousDirection"] == 1:
      game["red"]["pos"]["y"] = game["red"]["pos"]["y"] - 20
      inAWall = True
  else :
    inAWall = True
  if inAWall :
    game["red"]["direction"] = game["red"]["previousDirection"]
    game["red"]["pos"], game["red"]["direction"] = nextpos(game["red"]["pos"], game["red"]["direction"])
  if game["pacman"]["pos"]["x"] == game["red"]["pos"]["x"] and game["pacman"]["pos"]["y"] == game["red"]["pos"]["y"]:
    return False
  # Reposition de orange
  game["orange"]["previousPos"]["x"] = game["orange"]["pos"]["x"]
  game["orange"]["previousPos"]["y"] = game["orange"]["pos"]["y"]
  if game["pacman"]["pos"]["x"] == game["orange"]["pos"]["x"] and game["pacman"]["pos"]["y"] == game["orange"]["pos"]["y"]:
    return False
  if game["orange"]["pos"]["x"] == 0 and game["orange"]["pos"]["y"] == 240:
    game["orange"]["pos"]["x"] = 360
  if game["orange"]["pos"]["x"] == 360 and game["orange"]["pos"]["y"] == 240:
    game["orange"]["pos"]["x"] = 0
  game["orange"]["previousDirection"] = game["orange"]["direction"]
  game["orange"]["direction"] = orangeIa(game)
  inAWall = False
  if game["orange"]["direction"] == 0:
    game["orange"]["pos"]["x"] = game["orange"]["pos"]["x"] + 20
    if inWall(game["orange"]["pos"]) or game["orange"]["previousDirection"] == 2:
      game["orange"]["pos"]["x"] = game["orange"]["pos"]["x"] - 20
      inAWall = True
  elif game["orange"]["direction"] == 1:
    game["orange"]["pos"]["y"] = game["orange"]["pos"]["y"] - 20
    if inWall(game["orange"]["pos"]) or game["orange"]["previousDirection"] == 3:
      game["orange"]["pos"]["y"] = game["orange"]["pos"]["y"] + 20
      inAWall = True
  elif game["orange"]["direction"] == 2:
    game["orange"]["pos"]["x"] = game["orange"]["pos"]["x"] - 20
    if inWall(game["orange"]["pos"]) or game["orange"]["previousDirection"] == 0:
      game["orange"]["pos"]["x"] = game["orange"]["pos"]["x"] + 20
      inAWall = True
  elif game["orange"]["direction"] == 3:
    game["orange"]["pos"]["y"] = game["orange"]["pos"]["y"] + 20
    if inWall(game["orange"]["pos"]) or game["orange"]["previousDirection"] == 1:
      game["orange"]["pos"]["y"] = game["orange"]["pos"]["y"] - 20
      inAWall = True
  else :
    inAWall = True
  if inAWall :
    game["orange"]["direction"] = game["orange"]["previousDirection"]
    game["orange"]["pos"], game["orange"]["direction"] = nextpos(game["orange"]["pos"], game["orange"]["direction"])
  if game["pacman"]["pos"]["x"] == game["orange"]["pos"]["x"] and game["pacman"]["pos"]["y"] == game["orange"]["pos"]["y"]:
    return False
  # Reposition de blue
  game["blue"]["previousPos"]["x"] = game["blue"]["pos"]["x"]
  game["blue"]["previousPos"]["y"] = game["blue"]["pos"]["y"]
  if game["pacman"]["pos"]["x"] == game["blue"]["pos"]["x"] and game["pacman"]["pos"]["y"] == game["blue"]["pos"]["y"]:
    return False
  if game["blue"]["pos"]["x"] == 0 and game["blue"]["pos"]["y"] == 240:
    game["blue"]["pos"]["x"] = 360
  if game["blue"]["pos"]["x"] == 360 and game["blue"]["pos"]["y"] == 240:
    game["blue"]["pos"]["x"] = 0
  game["blue"]["previousDirection"] = game["blue"]["direction"]
  game["blue"]["direction"] = blueIa(game)
  inAWall = False
  if game["blue"]["direction"] == 0:
    game["blue"]["pos"]["x"] = game["blue"]["pos"]["x"] + 20
    if inWall(game["blue"]["pos"]) or game["blue"]["previousDirection"] == 2:
      game["blue"]["pos"]["x"] = game["blue"]["pos"]["x"] - 20
      inAWall = True
  elif game["blue"]["direction"] == 1:
    game["blue"]["pos"]["y"] = game["blue"]["pos"]["y"] - 20
    if inWall(game["blue"]["pos"]) or game["blue"]["previousDirection"] == 3:
      game["blue"]["pos"]["y"] = game["blue"]["pos"]["y"] + 20
      inAWall = True
  elif game["blue"]["direction"] == 2:
    game["blue"]["pos"]["x"] = game["blue"]["pos"]["x"] - 20
    if inWall(game["blue"]["pos"]) or game["blue"]["previousDirection"] == 0:
      game["blue"]["pos"]["x"] = game["blue"]["pos"]["x"] + 20
      inAWall = True
  elif game["blue"]["direction"] == 3:
    game["blue"]["pos"]["y"] = game["blue"]["pos"]["y"] + 20
    if inWall(game["blue"]["pos"]) or game["blue"]["previousDirection"] == 1:
      game["blue"]["pos"]["y"] = game["blue"]["pos"]["y"] - 20
      inAWall = True
  else :
    inAWall = True
  if inAWall :
    game["blue"]["direction"] = game["blue"]["previousDirection"]
    game["blue"]["pos"], game["blue"]["direction"] = nextpos(game["blue"]["pos"], game["blue"]["direction"])
  if game["pacman"]["pos"]["x"] == game["blue"]["pos"]["x"] and game["pacman"]["pos"]["y"] == game["blue"]["pos"]["y"]:
    return False
  # Reposition de pink
  game["pink"]["previousPos"]["x"] = game["pink"]["pos"]["x"]
  game["pink"]["previousPos"]["y"] = game["pink"]["pos"]["y"]
  if game["pacman"]["pos"]["x"] == game["pink"]["pos"]["x"] and game["pacman"]["pos"]["y"] == game["pink"]["pos"]["y"]:
    return False
  if game["pink"]["pos"]["x"] == 0 and game["pink"]["pos"]["y"] == 240:
    game["pink"]["pos"]["x"] = 360
  if game["pink"]["pos"]["x"] == 360 and game["pink"]["pos"]["y"] == 240:
    game["pink"]["pos"]["x"] = 0
  game["pink"]["previousDirection"] = game["pink"]["direction"]
  game["pink"]["direction"] = pinkIa(game)
  inAWall = False
  if game["pink"]["direction"] == 0:
    game["pink"]["pos"]["x"] = game["pink"]["pos"]["x"] + 20
    if inWall(game["pink"]["pos"]) or game["pink"]["previousDirection"] == 2:
      game["pink"]["pos"]["x"] = game["pink"]["pos"]["x"] - 20
      inAWall = True
  elif game["pink"]["direction"] == 1:
    game["pink"]["pos"]["y"] = game["pink"]["pos"]["y"] - 20
    if inWall(game["pink"]["pos"]) or game["pink"]["previousDirection"] == 3:
      game["pink"]["pos"]["y"] = game["pink"]["pos"]["y"] + 20
      inAWall = True
  elif game["pink"]["direction"] == 2:
    game["pink"]["pos"]["x"] = game["pink"]["pos"]["x"] - 20
    if inWall(game["pink"]["pos"]) or game["pink"]["previousDirection"] == 0:
      game["pink"]["pos"]["x"] = game["pink"]["pos"]["x"] + 20
      inAWall = True
  elif game["pink"]["direction"] == 3:
    game["pink"]["pos"]["y"] = game["pink"]["pos"]["y"] + 20
    if inWall(game["pink"]["pos"]) or game["pink"]["previousDirection"] == 1:
      game["pink"]["pos"]["y"] = game["pink"]["pos"]["y"] - 20
      inAWall = True
  else :
    inAWall = True
  if inAWall :
    game["pink"]["direction"] = game["pink"]["previousDirection"]
    game["pink"]["pos"], game["pink"]["direction"] = nextpos(game["pink"]["pos"], game["pink"]["direction"])
  if game["pacman"]["pos"]["x"] == game["pink"]["pos"]["x"] and game["pacman"]["pos"]["y"] == game["pink"]["pos"]["y"]:
    return False
  return True

def PositionDecalee(pos, px, direction):
  x = pos["x"]
  y = pos["y"]
  if direction == 0:
    x -= px
  if direction == 1:
    y += px
  if direction == 2:
    x += px
  if direction == 3:
    y -= px
  return [x,y]

# Drawing the map
screen.fill(black)
for wall in game["walls"]:  
  pygame.draw.rect(screen, blue, (wall[0],wall[1],20,20))
pygame.draw.rect(screen, black, (180,200,20,20))
for ball in game["balls"]:
  screen.blit(BALL, ball)
screen.blit(OPACMAN, [game["pacman"]["pos"]["x"],game["pacman"]["pos"]["y"]])

# Add walls not drawn
#game["walls"].append([-20,240])
#game["walls"].append([380,240])

while True:# LOOP Principale
  # Exit proprement
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      print(game["score"])
      sys.exit()
  abool = Reposition()
  # Apparition des fantomes
  game["turn"] = 1 + game["turn"]
  if game["turn"] == 12:
    pygame.draw.rect(screen, black, (game["blue"]["pos"]["x"], game["blue"]["pos"]["y"],20,20))
    game["blue"]["direction"] = 0
    game["blue"]["pos"]["x"] = 180
    game["blue"]["pos"]["y"] = 180
    game["blue"]["previousPos"]["x"] = 180
    game["blue"]["previousPos"]["y"] = 180
  if game["turn"] == 2:
    pygame.draw.rect(screen, black, (game["pink"]["pos"]["x"], game["pink"]["pos"]["y"],20,20))
    game["pink"]["direction"] = 0
    game["pink"]["pos"]["x"] = 180
    game["pink"]["pos"]["y"] = 180
    game["pink"]["previousPos"]["x"] = 180
    game["pink"]["previousPos"]["y"] = 180
  if game["turn"] == 22:
    pygame.draw.rect(screen, black, (game["orange"]["pos"]["x"], game["orange"]["pos"]["y"],20,20))
    game["orange"]["pos"]["x"] = 180
    game["orange"]["direction"] = 2
    game["orange"]["pos"]["y"] = 180
    game["orange"]["previousPos"]["x"] = 180
    game["orange"]["previousPos"]["y"] = 180
  if not abool :
    print("Pacman has been caught")
    print(game["score"])
    sys.exit()
    break
  # l'animation
  for i in range(20):
    px = 20 - i
    pacmanPos = pacmanX, pacmanY = PositionDecalee(game["pacman"]["pos"], px, game["pacman"]["direction"])
    redPos = redX, redY = PositionDecalee(game["red"]["pos"], px, game["red"]["direction"])
    screen.blit(RED, redPos)
    orangePos = orangeX, orangeY = PositionDecalee(game["orange"]["pos"], px, game["orange"]["direction"])
    screen.blit(ORANGE, orangePos)
    bluePos = blueX, blueY = PositionDecalee(game["blue"]["pos"], px, game["blue"]["direction"])
    screen.blit(BLUE, bluePos)
    pinkPos = pinkX, pinkY = PositionDecalee(game["pink"]["pos"], px, game["pink"]["direction"])
    screen.blit(PINK, pinkPos)
    if i >= 10:
      screen.blit(CPACMAN, pacmanPos)
    else:
      screen.blit(pygame.transform.rotate(OPACMAN, 90* game["pacman"]["direction"]), pacmanPos)
    pygame.display.flip()
    pygame.draw.rect(screen, black, (pacmanX, pacmanY, 20, 20))
    pygame.draw.rect(screen, black, (redX, redY, 20, 20))
    if inBall(game["red"]["previousPos"]):
      screen.blit(BALL, (game["red"]["previousPos"]["x"], game["red"]["previousPos"]["y"]))
    pygame.draw.rect(screen, black, (orangeX, orangeY, 20, 20))
    if inBall(game["orange"]["previousPos"]):
      screen.blit(BALL, (game["orange"]["previousPos"]["x"], game["orange"]["previousPos"]["y"]))
    pygame.draw.rect(screen, black, (blueX, blueY, 20, 20))
    if inBall(game["blue"]["previousPos"]):
      screen.blit(BALL, (game["blue"]["previousPos"]["x"], game["blue"]["previousPos"]["y"]))
    pygame.draw.rect(screen, black, (pinkX, pinkY, 20, 20))
    if inBall(game["pink"]["previousPos"]):
      screen.blit(BALL, (game["pink"]["previousPos"]["x"], game["pink"]["previousPos"]["y"]))
    pygame.time.delay(35)