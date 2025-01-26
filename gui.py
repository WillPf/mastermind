import PySimpleGUI as sg

sg.theme('LightGreen7')

img = {"subsample": 4, "size": (64, 64), "enable_events": True, "p": (10, (50, 30))}
empty = {"subsample": 6, "size": (43, 43), "enable_events": True, "p": (10, 5), "source": "./images/empty.png"}


layout = [  [sg.Push(), sg.Image("./images/blue.png", k="blue", **img),
          sg.Image("./images/green.png", k="green", **img),
          sg.Image("./images/orange.png", k="orange", **img),
          sg.Image("./images/purple.png", k="purple", **img),
          sg.Image("./images/red.png", k="red", **img),
          sg.Image("./images/yellow.png", k="yellow", **img), sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"9{i}") for i in range(4)] + [sg.Text("", font=("12"), k=9, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"8{i}") for i in range(4)] + [sg.Text("", font=("12"), k=8, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"7{i}") for i in range(4)] + [sg.Text("", font=("12"), k=7, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"6{i}") for i in range(4)] + [sg.Text("", font=("12"), k=6, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"5{i}") for i in range(4)] + [sg.Text("", font=("12"), k=5, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"4{i}") for i in range(4)] + [sg.Text("", font=("12"), k=4, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"3{i}") for i in range(4)] + [sg.Text("", font=("12"), k=3, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"2{i}") for i in range(4)] + [sg.Text("", font=("12"), k=2, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"1{i}") for i in range(4)] + [sg.Text("", font=("12"), k=1, s=15)] + [sg.Push()],
          [sg.Push()] + [sg.Text("", font=("12"), s=15)] + [sg.Image(**empty, k=f"0{i}") for i in range(4)] + [sg.Text("", font=("12"), k=0, s=15)] + [sg.Push()],
          [sg.Push(), sg.Text("©Willy J. CS50P Final Project 2025", font=("Roboto", 8), text_color="#ffffff")]
          ]


window = sg.Window('Mastermind', layout, size=(700, 720))