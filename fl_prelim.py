import random

english = ["Armpit", "Arms", "Back", "Beard", "Blood", "Body", "Bone", "Brain", "Breast", "Cheeks", "Chest", "Chin", "Ears", "Eyebrow", "Eyes", "Face", "Fingers", "Forehead", "Hair", "Hands", "Head", "Heart", "Heels", "Hips", "Knees", "Legs", "Lips", "Lungs", "Mouth", "Nails", "Neck", "Nose", "Shoulder", "Skin", "Stomach", "Tongue", "Tooth", "Toe", "Wrist"]

japanese = ["Wakinoshita", "Ude", "Ushiro", "Hige", "Chi", "Karada", "Hone", "Noo", "Chichi", "Hoho", "Mune", "Ago", "Mimi", "Mayuge", "Me", "Kao", "Yubi", "Hitai", "Kami", "Te", "Atama", "Shinzoo", "Kakato", "Koshi", "Hiza", "Ashi", "Kuchibiru", "Hai", "Kuchi", "Tsume", "Kubi", "Hana", "Kata", "Hada", "Onaka", "Shita", "Ha", "Tsumasaki", "Tebuki"]


def translate(inp): 
  abcd = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3
  }
  
  return abcd[inp]

def start_japanese():
  score = 0
  questions_shown = []
  for i in range(0,38):
    q = random.choice(list(set(range(0, len(english) - 1)) - set(questions_shown)))
    questions_shown.append(q)
    opt = print("Whats the Japanese Equivalent of " + english[q])
    choices = [japanese[q]]
    choices_int = [q]
    for z in range (0,3):
      x =random.choice(list(set(range(0, len(english) - 1)) - set(choices_int)))
      choices.append(japanese[x])
      choices_int.append(x)
    shown = []
    abcd = ['A', 'B', 'C', 'D']
    for c in range(0,4): 
      y = random.choice(list(set(range(0,4)) - set(shown)))
      shown.append(y)
      print (abcd[c] + '). ' + choices[y])
    print()
    ans = input("Answer: ")
    if choices[shown[translate(ans)]] == japanese[q]:
      print("Correct")
      score += 1
    else:
      print("Incorrect")
      print("Correct Answer: " + japanese[q])
    print("\n\n")
  #print("Score: " + str(score) + "/10")
  print("\n\n")
  print(score)


def start_english():
  score = 0
  questions_shown = []
  for i in range(0,9):
    q = random.choice(list(set(range(0, len(english) - 1)) - set(questions_shown)))
    questions_shown.append(q)
    opt = print("Whats the English Equivalent of " + japanese[q])
    choices = [english[q]]
    choices_int = [q]
    for z in range (0,3):
      x =random.choice(list(set(range(0, len(english) - 1)) - set(choices_int)))
      choices.append(english[x])
      choices_int.append(x)
    shown = []
    abcd = ['A', 'B', 'C', 'D']
    for c in range(0,4): 
      y = random.choice(list(set(range(0,4)) - set(shown)))
      shown.append(y)
      print (abcd[c] + '). ' + choices[y])
    print()
    ans = input("Answer: ")
    if choices[shown[translate(ans)]] == english[q]:
      print("Correct")
      score += 1
    else:
      print("Incorrect")
      print("Correct Answer: " + english[q])
    print("\n\n")
  #print("Score: " + str(score) + "/10")
  print("\n\n")
  print(score)


def start_identification():
  score = 0
  questions_shown = []
  for i in range(0,38):
    q = random.choice(list(set(range(0, len(english) - 1)) - set(questions_shown)))
    questions_shown.append(q)
    opt = print("Whats the Japanese Equivalent of " + english[q])
    choices = [japanese[q]]
    choices_int = [q]
    ans = input("Answer: ")
    if ans == japanese[q]:
      print("Correct")
      score += 1
    else:
      print("Incorrect")
      print("Correct Answer: " + japanese[q])
    print("\n\n")
  #print("Score: " + str(score) + "/10")
  print("\n\n")
  print(score)

  
while True: 
  #start_japanese()
  start_english()
  #start_identification()
  opt = input("Try again? (y/n): ")
  if opt == 'y' or opt == 'Y': 
    pass
  else:
    break