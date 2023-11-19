import random
import itertools

def new_deck():
    output_liste = []
    typer = ["c", "h", "s", "d"]
    for type in typer:
        for i in range(2, 15):
            output_liste.append((i, type))
    return output_liste

def shuffle(liste):
    liste = liste.copy()
    random.shuffle(liste)
    return liste

def check_values(play):
    liste_med_tall = [play[0][0], play[1][0], play[2][0]]
    if liste_med_tall[0] == liste_med_tall[1] and liste_med_tall[0] == liste_med_tall[2]:
        return 5
    sortert_liste = sorted(liste_med_tall)
    if sortert_liste[0] == (sortert_liste[1] - 1)and sortert_liste[0] == (sortert_liste[2] - 2):
        return 4
    if sortert_liste[0] == sortert_liste[1] or sortert_liste[1] == sortert_liste[2]:
        return 2
    return 1

def check_suits(play):
    liste_med_typer = [play[0][1], play[1][1], play[2][1]]
    if liste_med_typer[0] == liste_med_typer[1] and liste_med_typer[0] == liste_med_typer[2]:
        return 3
    return 1

def evaluate_play(play):
    return check_values(play) + check_suits(play) - 1

hand1 = [(7, "c"), (4, "s"), (9, "c"), (4, "c"), (6, "h")]

def coumputer_play(hand):
    kombinasjoner = list(itertools.combinations(hand, 3))
    beste_kombo = kombinasjoner[0]
    for kombinasjon in kombinasjoner:
        if evaluate_play(kombinasjon) > evaluate_play(beste_kombo):
            beste_kombo = kombinasjon
    for i in range(4, -1, -1):
        if hand[i] in beste_kombo:
            del hand[i]
    return beste_kombo

def hand_to_string(hand):
    card_dict = {10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"}
    output_string = ""
    for card in hand:
        if card[0] in card_dict:
            output_string += card_dict[card[0]]
        else:
            output_string += str(card[0])
        output_string += card[1] + " "
    return output_string.strip()

def human_play(hand):
    valg = input(f"Velg 3 av disse kortene: {hand_to_string(hand)}: ")
    choices = valg.split(" ")

    if not len(set(choices)) == 3:
        print("Skriv inn 3 unike tall!")
        return human_play(hand)

    valgte_kort = []

    for choice in choices:
        if not choice.isdigit():
            print(f"{choice} er ikke et tall >:(")
            return human_play(hand)
        
        choice_value = int(choice)
        if not 1 <= choice_value <= 5:
            print(f"{choice} er ikke et tall mellom 1 og 5")
            return human_play(hand)
        
        valgte_kort.append(hand[choice_value - 1])
    
    for i in range(4, -1, -1):
        if hand[i] in valgte_kort:
            del hand[i]
    return valgte_kort

print(human_play(hand1))

print(hand1)