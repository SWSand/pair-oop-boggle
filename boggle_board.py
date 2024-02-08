import random

class BoggleBoard:
  

  def __init__(self):

    pass

  def boggle_shake(self):
    list_of_dice = [
    "AAEEGN",
    "ELRTTY",
    "AOOTTW",
    "ABBJOO",
    "EHRTVW",
    "CIMOTU",
    "DISTTY",
    "EIOSST",
    "DELRVY",
    "ACHOPS",
    "HIMNQU",
    "EEINSU",
    "EEGHNW",
    "AFFKPS",
    "HLNNRZ",
    "DEILRX",
  ]

    random.shuffle(list_of_dice)
    for row in range(4):
      row = ''
      for column in range(4):
        row += random.choice(list_of_dice.pop()) + ' '
      print(row)

  def shake(self):
    for row in range(4):
      row = ''
      for column in range(4):
        row += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + ' '
      print(row)

  def qu_boggle_shake(self):
    list_of_dice = [
    "AAEEGN",
    "ELRTTY",
    "AOOTTW",
    "ABBJOO",
    "EHRTVW",
    "CIMOTU",
    "DISTTY",
    "EIOSST",
    "DELRVY",
    "ACHOPS",
    "HIMNQU",
    "EEINSU",
    "EEGHNW",
    "AFFKPS",
    "HLNNRZ",
    "DEILRX",
  ]

    random.shuffle(list_of_dice)
    for row in range(4):
      row = ''
      for column in range(4):
        row += random.choice(list_of_dice.pop()).replace('Q', 'Qu') + ' '
      print(row)    
      
  def board(self):
    print('_ _ _ _\n' * 4)


boggle_board = BoggleBoard()

# boggle_board.board()
# boggle_board.shake()

boggle_board.qu_boggle_shake()
