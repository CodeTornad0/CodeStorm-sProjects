import sys
import time
import random
import pygame as py

py.init()
py.display.set_caption("Reaction Time Test")
FONT = py.font.SysFont("Roboto", 90)


def Create_Var_FONT(text):
    return FONT.render(text, True, "black")


def Create_Var_Rect(var):
    return var.get_rect(center=(360, 360))


screen = py.display.set_mode((720, 720))
start = Create_Var_FONT("Click To Start")
start_rect = Create_Var_Rect(start)
waiting = Create_Var_FONT("Waiting...")
waiting_rect = Create_Var_Rect(waiting)
click = Create_Var_FONT("Click Now!")
click_rect = Create_Var_Rect(click)
state = "Click To Start"

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.MOUSEBUTTONDOWN:
            if state == "Click To Start":
                state = "Waiting"
            elif state == "Waiting":
                time.sleep(1)
            elif state == "Test Starting":
                end_time = time.time()
                state = "Showing Results"
            else:
                state = "Click To Start"

    screen.fill("white")
    if state == "Click To Start":
        screen.blit(start, start_rect)
    elif state == "Waiting":
        screen.fill("yellow")
        screen.blit(waiting, waiting_rect)
        py.display.update()
        delay = random.uniform(1, 10)
        time.sleep(delay)
        state = "Test Starting"
        start_time = time.time()
    elif state == "Test Starting":
        screen.fill("green")
        screen.blit(click, click_rect)
    else:
        reaction_time = round((end_time - start_time) * 1000)
        score = Create_Var_FONT(f"Score: {reaction_time} ms")
        score_rect = Create_Var_Rect(score)
        screen.blit(score, score_rect)
    py.display.update()
