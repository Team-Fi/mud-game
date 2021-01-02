import time
import os
from playsound import playsound
import random

t = [["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
     ""],
     ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
      "",
      ""]
     ]


def ref_not_input():
    print("\n" + "\n".join(t[0]), end="")


def draw_text(row, text, align="left"):
    g = 0
    for i in list(text):
        if ord(i) > 255:
            g += 2
        else:
            g += 1
    if align == "right":
        t[0][row] = f'{" " * (120 - g)}{text}'
    else:
        t[0][row] = text
    ref_not_input()


def clear_ln(row):
    t[0][row] = ""
    ref_not_input()


def refresh():
    print("\n" + "\n".join(t[0]), end="")
    return input("")


def draw_comment(character, comment, number):
    """
    character: type Character
    comment: type string
    number: type int

    Returns: None
    """
    goza = character.texts[comment][:]
    while len(goza) < 4:
        goza.append("")
    draw_text(24, goza[number])
    draw_text(25, goza[number + 1])
    draw_text(26, goza[number + 2])
    draw_text(27, goza[number + 3])


class Character:
    texts = dict()

    def __init__(self, name, disp_name, picture=None):
        self.name = name
        self.disp_name = disp_name
        self.picture = picture
        for i in os.listdir(f"./texts/{name}/"):
            with open(f"./texts/{name}/{i}", "r", encoding='utf-8') as f:
                self.texts[i.split(".")[0]] = f.readlines()


with open("./texts/common/name/bg.txt", "r", encoding='utf-8') as f:
    bg_name = f.readlines()
print(bg_name)
bg_index = 20  # random.randint(1, 19)
draw_text(29, f"BGM. {bg_name[bg_index - 1]}", "right")
draw_text(28, "이름을 입력해주세요: ", "left")
player = Character(name="AlphaGot", disp_name=refresh())
draw_text(22, "-" * 120)
draw_text(23, player.disp_name + "의 말: ")
draw_comment(player, "start_01", 0)
with open("./texts/common/staffroll/test.txt", "r") as f:
    playsound(os.path.abspath(f"sounds/bg/test/{bg_index}.mp3"), block=False)
    staffroll = f.readlines()
    print(staffroll)
    time.sleep(44)
    for i in range(-19, len(staffroll)):
        for j in range(0, 20):
            try:
                if i + j > -1:
                    draw_text(j, staffroll[i + j].replace("\n", ""))
                else:
                    draw_text(j, "" * 120)
            except:
                draw_text(j, "" * 120)
            draw_text(28, f'Debug {"-" * 2}{"%2d" % bg_index}-{"%3d" % i}{"-" * 106}')
        time.sleep((60/150) * 1.6)
refresh()
