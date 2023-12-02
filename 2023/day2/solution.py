
redMax = 12
greenMax = 13
blueMax = 14

class CubeSet:
  blue = 0
  red = 0
  green = 0

  def addCubes(self, color: str, number: int):
    if color == 'blue':
      self.blue += number
    elif color == 'red':
      self.red += number
    elif color == 'green':
      self.green += number
  def __str__(self):
    return f"blue - {self.blue} red - {self.red} green - {self.green}"

class Game:
  def __init__(self, id) -> None:
    self.id = int(id)
    self.cubeSets = []
  
  def addSet(self, cubeSet):
    self.cubeSets.append(cubeSet)

games = []

with open('input') as fp:
  for line in fp:
    gameStr, cubes = line.split(':')
    game = Game(gameStr.split(' ')[1])

    cubes = cubes.strip()
    for setStr in cubes.split(';'):
      setStr = setStr.strip()
      set = CubeSet()
      for cube in setStr.split(','):
        cube = cube.strip()
        count, color = cube.split(' ')
        set.addCubes(color, int(count))
      
      game.addSet(set)
    games.append(game)

count = 0
# Task 1
for game in games:
  filteredSet = list(filter(lambda set: (set.red <= redMax) and (set.blue <= blueMax) and (set.green <= greenMax), game.cubeSets))
  if len(filteredSet) == len(game.cubeSets):
    count += game.id

print("Task 1")
print(count)

#Task2
countT2 = 0

for game in games:
  red = max(game.cubeSets, key=lambda s: s.red).red
  blue = max(game.cubeSets, key=lambda s: s.blue).blue
  green = max(game.cubeSets, key=lambda s: s.green).green

  countT2 += red * blue * green

print("Task 2")
print(countT2)
