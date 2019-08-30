from turtle import *

before = True, True, True
prepared = False

def prepare():
    global before
    goto(0,0)
    clear()
    before = isvisible(), isdown(), tracer()
    ht()
    pu()
    tracer(False)
    
def restore():
    if before[0]: st()
    if before[1]: pd()
    tracer(before[2])

def fill(seq, n, filler):
    return [*seq] + [filler for i in range(len(seq), n)]
