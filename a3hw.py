while True:
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Value = input("Enter a letter or number: ").upper()
    if Value not in Alphabet:
      print("Input is not a valid letter.")
    else:
      print("Input is a valid letter.")
 