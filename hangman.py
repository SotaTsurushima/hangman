def hangman(word):
  wrong = 0
  stages = ["",
            "_____     ",
            "|         ",
            "|    |    ",
            "|    0    ",
            "|   /|\   ",
            "|   / \   ",
            "|         ",
            ]
  
  rletters = list(word)
  board = ["_"] * len(word)
  win = False
  print("ハングマンへようこそ")
