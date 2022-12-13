import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    card_prompt = input("Press Enter to pick a card or Q and Enter to quit: ")
    if card_prompt == "q":
        break
    else:
        random_card = random.choice(diamonds)
        diamonds.remove(random_card)
        hand.append(random_card)
    print("Your hand:", (hand))
    print("Remaining Cards:", diamonds)

if not diamonds:
    print("There are no more cards to pick")