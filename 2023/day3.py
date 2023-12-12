class Number:
  def __init__(self, x, y, value):
    self.x = x
    self.y = y
    self.value = value
  
  def addChar(self, char):
    self.value += char

  def getLength(self):
    return len(self.value)

  def getValue(self):
    return int(self.value)
  
  def __str__(self) -> str:
    return f'{self.value} x=>{self.x} y=>{self.y}'

input = []

with open('input') as fp:
  input = [list(line) for line in fp]


# Part 1
numbers = []  
number = None

for i in range(len(input)):
  for j in range(len(input[i])):
    if input[i][j].isdigit():
      if(number is None):
        number = Number(j, i, input[i][j])
      else:
        number.addChar(input[i][j])
    else:
      if number is not None:
        numbers.append(number)
        number = None

def getNeighbors(number):
  row = number.y
  col = number.x

  neighbors = []

  for i in range(number.getLength()+2):
    if (col-1)+i < 0:
      continue

    if row-1 >= 0:
      neighbors.append(input[row-1][(col-1)+i])

    a = input[row][(col-1)+i]
    if(not a.isdigit()):
      neighbors.append(a)
    if row+1 < len(input):
      neighbors.append(input[row+1][(col-1)+i])

  return neighbors

sum = 0

for number in numbers:
  neighbors = getNeighbors(number)
  neighbors = list(filter(lambda a: (a != '.') and (a != '\n'), neighbors))
  if len(neighbors) != 0:
    sum += number.getValue()

print('Part 1')
print(sum)

# Part 2

def getAdjecentNumbers(x, y):
  retVal = []
  for number in numbers:
    if (number.y+1 >= y) and (number.y-1 <= y):
      if(number.x+number.getLength() >= x) and (number.x-1 <= x):
        retVal.append(number)

  
  return retVal

sum = 0

for i in range(len(input)):
  for j in range(len(input[i])):
    if(input[i][j] == '*'):
      print(f'{input[i][j]} x {j} y {i}')
      a = getAdjecentNumbers(j, i)
      if len(a) == 2:
        for number in a:
          print(number)
        b = a[0].getValue()*a[1].getValue()
        print(b)
        sum += b

print('Part 2')
print(sum)