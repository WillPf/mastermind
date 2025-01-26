import PySimpleGUI as sg
from gui import *
import random as r

def main():
    colors = ["blue", "green", "orange", "yellow", "purple", "red"]
    sequence = create_sequence(colors)
    player_guess = []
    line = 0
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel": 
            break
        if event in colors:
            if len(player_guess) < 4:
                player_guess.append(event)
        for i in range(len(player_guess)):
            window[f"{line}{i}"].update(source=f"./images/{player_guess[i]}.png", size=(43, 43), subsample=6)
        if len(player_guess) == 4:
            black, white = (check_answer(sequence, player_guess))
            window[line].update(f"{"⚫️" * black}{"⚪️" * white}")
            if black == 4:
                with open("./stats.txt", "a") as f:
                    f.write(stats(line, black))
                if show_answer(sequence, "w") == "quit":
                    break
                restart()
            line += 1
            if line > 9:
                with open("./stats.txt", "a") as f:
                    f.write(stats(line, black))
                if show_answer(sequence, "l") == "quit":
                    break
                restart()
        
            player_guess = []
    window.close()


def create_sequence(colors):
    return [r.choice(colors) for _ in range(4)]


def check_answer(seq, player):
    copy_seq = seq.copy()
    same_place = 0
    same_color = 0
    for i in range(len(copy_seq)):
        if copy_seq[i] == player[i]:
            same_place += 1
    for color in player:
        if color in copy_seq:
            same_color += 1
            copy_seq.pop(copy_seq.index(color))
    same_color -= same_place
    return same_place, same_color

def restart():
    for i in range(10):
        for j in range(4):
            window[f"{i}{j}"].update("./images/empty.png", size=(43, 43), subsample=6)
        window[i].update("")
    main()

def show_answer(seq, str):
    if str == "w":
        text = "You Won! The balls were:"
    else:
        text = "You Lost :( The balls were:"
    layout = [
        [sg.Push(), sg.Text(text, font=("", 18)), sg.Push()],
        [sg.Image(f"./images/{color}.png", **img) for color in seq],
        [sg.Button("Retry"), sg.Push(), sg.Button("Quit")]
        ]
    window = sg.Window("", layout, size=(400, 300))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: 
            break
        if event == "Quit":
            window.close()
            return "quit"
        elif event == "Retry":
            break
    window.close()


def stats(line, black):
    if black == 4:
        return f"Game won in {line + 1} steps\n"
    return "Game lost\n"


if __name__ == "__main__":
    main()