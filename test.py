name = "Antonina"
letter_a_or_i = False
letter_n = False
letter_o = False
name = name.lower()

for i in range(len(name)):
  if (name[i] == 'a' or name[i] == 'i') and letter_a_or_i == False:
    print("A or I is in the name")
    letter_a_or_i = True
  if (name[i] == 'o') and (letter_n == False and letter_o == False):
    for e in range(len(name)):
      if name[e] == 'n':
        print("O and N is in the name")
        letter_n = True
        letter_o = True
        break
  if name[i] == 'n' and letter_n == False:
    for j in range(len(name)):
      if name[j] != 'o':
        print("Only N is in the name")
        letter_n = True
        break
  if name[i] != 'n' and name[i] == 'o' and letter_n == False and letter_o == False:
    print("There is no N in the name, but there might be O")