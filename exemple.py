import math

def SetRedDirection (game):
  '''
  set the red ghost direction
  '''
  def inWall(pos):
    vraiOuFaux = False
    for wall in game.walls:
      if pos.x == wall.x and pos.y == wall.y:
        vraiOuFaux = True
    return vraiOuFaux
  def calcdist(pos1, pos2): # Calcule la distance entre 2 points
    dist1 = pos1.x - pos2.x
    if dist1 < 0:
      dist1 = dist1 * -1
    dist2 = pos1.y - pos2.y
    if dist2 < 0:
      dist2 = dist2 * -1
    return math.sqrt(dist1 ** 2 + dist2 ** 2)
  favDirection = 0
  favDistance = 1000
  game.red.pos.x += 1
  if calcdist(game.red.pos, game.pacman.pos) < favDistance and (not inWall(game.red.pos)):
    favDistance = calcdist(game.red.pos, game.pacman.pos)
    favDirection = 0
    game.red.pos.x -= 2
  if calcdist(game.red.pos, game.pacman.pos) < favDistance and (not inWall(game.red.pos)):
    favDistance = calcdist(game.red.pos, game.pacman.pos)
    favDirection = 2
  game.red.pos.x += 1
  game.red.pos.y += 1
  if calcdist(game.red.pos, game.pacman.pos) < favDistance and (not inWall(game.red.pos)):
    favDistance = clacdist(game.red.pos, game.pacman.pos)
    favDirection = 1
  game.red.pos.y -= 2
  if calcdist(game.red.pos, game.pacman.pos) < favDistance and (not inWall(game.red.pos)):
    favDistance = clacdist(game.red.pos, game.pacman.pos)
    favDirection = 3
  game.red.pos.y += 1
  return favDirection

def SetOrangeDirection (game):
  '''
  set the yellow direction
  '''
  return null

def SetPinkDirection (game):
  '''
  set the red ghost direction
  '''
  return null

def SetBlueDirection (game):
  '''
  set the yellow direction
  '''
  return direction