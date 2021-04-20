import multiprocessing as mp


old_coords = 0
coords = 0


def newcoords():
    global old_coords, coords
    while True:
        if old_coords != coords:
            print(coords)
            old_coords = coords

proc = mp.Process(target=newcoords())
proc.start()

