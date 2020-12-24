import time
import os
from playsound import playsound
import random

t = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
     ""]


def ref_not_input():
    print("\n" + "\n".join(t), end="")


def draw_text(row, text, align="left"):
    g = 0
    for i in list(text):
        if ord(i) > 127:
            g += 2
        else:
            g += 1
    if align == "right":
        t[row] = f'{" " * (120 - g)}{text}'
    else:
        t[row] = text
    ref_not_input()


def refresh():
    print("\n" + "\n".join(t), end="")
    return input("")


class Character:
    texts = dict()

    def __init__(self, name, disp_name, picture=None):
        global texts

        self.name = name
        self.disp_name = disp_name
        self.picture = picture
        for i in os.listdir(f"./{name}/"):
            with open(f"./{name}/{i}", "r", encoding='utf-8') as f:
                self.texts[i.split(".")[0]] = f.readlines()


draw_text(29, "BGM. 彼岸帰航　～ Riverside View", "right")
playsound(os.path.abspath(f"sounds/bg/test/{random.randint(1, 19)}.mp3"), block=False)
draw_text(28, "이름을 입력해주세요: ", "left")
player = Character(name="AlphaGot", disp_name=refresh())
draw_text(22, "-" * 120)
draw_text(28, "-" * 120)
draw_text(23, player.disp_name + "의 말: ")
draw_text(24, "  " + player.texts["start_01"][0])
refresh()
