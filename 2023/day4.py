class ScratchCard:
  def __init__(self) -> None:
    self.winningNumbers = []
    self.numbers = []
    self.instances = 1

cards = []

with open('input') as fp:
  for line in fp:
    card = ScratchCard()
    _, a = line.split(': ')
    winning, numbers = a.split(' | ')
    print(f'{numbers} : {winning}')
    for number in numbers.split(' '):
      if number != '':
        card.numbers.append(int(number))
    for number in winning.split(' '):
      if number != '':
        card.winningNumbers.append(int(number))
    cards.append(card)

sum = 0

for i in range(len(cards)):
  card = cards[i]
  wins = 0
  for number in card.numbers:
    if number in card.winningNumbers:
      wins += 1
  print(f'Card {i+1}')
  print(f'wins {wins}')
  print(f'instances {card.instances}')

  for j in range(1, wins+1):
    if i+j < len(cards):
      cards[i+j].instances += card.instances

for card in cards:
  sum += card.instances
  print(card.instances)

print('Part 2')
print(sum)