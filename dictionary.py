meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "REL": "Też tak mam",
            "SUS": "Coś podejrzanego"
            }

for x in range(5):

    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

    if word in meme_dict.keys():
      print(meme_dict[word])
    else:
      print("Nie ma słowa w słowniku")
