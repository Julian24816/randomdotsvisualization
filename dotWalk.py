from turtle import *
from random import choice as rchoice

from helpers import prepare, restore
from choices import weighted_choice, alwayscolor


def chooseByHand(vertices=3, **kwargs):
    prepare()
    vpos = []
    def clickListener(x, y):
        vpos.append((x,y))
        goto(x, y)
        dot(5, "black")
        if len(vpos) == vertices:
            onscreenclick(None)
            draw(vpos, **kwargs)
            restore()
    onscreenclick(clickListener)


    
def equilateral(vertices=3, radius=300, **kwargs):
    prepare()
    vpos = []
    for d in (i/vertices*360 for i in range(vertices)):
        setheading(d + 90)
        fd(radius)
        dot(5, "black")
        vpos.append(pos())
        bk(radius)
    draw(vpos, **kwargs)
    restore()
    


def draw(vertex_positions, dots=10**4, dot_size=2, update_every=10**3,
         walk_percentage=0.5, same_dest_multiplier=1,
         choice=rchoice, color=alwayscolor("blue")):
    update()
    setpos(vertex_positions[0])
    last_dest,depth = None,0
    for i in range(1, dots + 1):
        dest = choice(vertex_positions)
        depth = depth + 1 if last_dest == dest else 0
        last_dest = dest
        setheading(towards(dest))
        fd(distance(dest) * walk_percentage)
        dot(dot_size * same_dest_multiplier ** depth,
            color(vertex_positions.index(dest), depth))
        if i % update_every == 0:
            update()
            print(i, "points drawn")
    

if __name__ == "__main__":
    from choices import depthcolor, weighted_choice

    ht()
    equilateral(3, walk_percentage=0.4, dots=10**5,
                color=depthcolor("yellow", "blue"),
                choice=weighted_choice(2, 3, 3))
    
