#cl1, cl2, cl3, cl4, cl5, cl6, cl7 are the horizontal rows
#krix- selected stone
#krix0- 2 stone you want to change

#kricol - it seems that something superfluous
#pointka - number of points
#ktmr - timer
#clp1, clp2, clp3, clp4, clp5, clp6, clp7- this is for animation
#mcnn - Style

# image any one can write down, simply changing the value here
# imagebutton idle ("k" + str (globals () ["cl" + str (z)] [i]) + ". w")
# on
# imagebutton idle ("k" + str (globals () ["cl" + str (z)] [i]) + ". png")


image kg="kg.w"   #background image
init python:
    import time

    style.mcnn = Style(style.default)
    style.mcnn.set_parent(style.button)
    style.mcnn.color = "#beddff"
    style.mcnn.size = 70
    style.mcnn.outlines = [(2, "#6e6e6e", 0, 0)]

    def check_matches(row_lists, col_lists, points, timer):
        # Helper to check for horizontal and vertical matches
        def match_line(line, idx, length=3):
            if idx <= len(line) - length:
                val = line[idx]
                if val > 0 and all(line[idx + j] == val for j in range(length)):
                    return True
            return False

        def clear_line(line, idx, length=3):
            for j in range(length):
                line[idx + j] = 0

        # Horizontal matches
        for z, row in enumerate(row_lists):
            for i in range(len(row)):
                if match_line(row, i):
                    val = row[i]
                    points += sum(row[i + j] for j in range(3)) * 2
                    # Check for 4 and 5 in a row
                    if i <= len(row) - 4 and row[i] == row[i + 3]:
                        if i <= len(row) - 5 and row[i] == row[i + 4]:
                            points += row[i + 4] * 4
                            timer += 4
                            row[i + 4] = 0
                        points += row[i + 3] * 3
                        timer += 2
                        row[i + 3] = 0
                    clear_line(row, i)
        # Vertical matches
        for i in range(len(row_lists[0])):
            for z in range(len(row_lists) - 2):
                if all(row_lists[z + j][i] == row_lists[z][i] and row_lists[z][i] > 0 for j in range(3)):
                    val = row_lists[z][i]
                    points += sum(row_lists[z + j][i] for j in range(3)) * 2
                    # Check for 4 and 5 in a column
                    if z <= len(row_lists) - 4 and row_lists[z][i] == row_lists[z + 3][i]:
                        if z <= len(row_lists) - 5 and row_lists[z][i] == row_lists[z + 4][i]:
                            points += row_lists[z + 4][i] * 4
                            timer += 4
                            row_lists[z + 4][i] = 0
                        points += row_lists[z + 3][i] * 3
                        timer += 2
                        row_lists[z + 3][i] = 0
                    for j in range(3):
                        row_lists[z + j][i] = 0
        return points, timer

    def drop_stones(row_lists, anim_lists, timer):
        # Drop stones and fill empty spaces
        for z in reversed(range(len(row_lists))):
            for i in range(len(row_lists[z])):
                if row_lists[z][i] == 0:
                    anim_lists[z][i] -= 32
                    # Find stone above
                    for above in reversed(range(z)):
                        if row_lists[above][i] > 0:
                            row_lists[z][i] = row_lists[above][i]
                            row_lists[above][i] = 0
                            break
                    else:
                        row_lists[z][i] = renpy.random.randint(1, 6)
                    for _ in range(4):
                        anim_lists[z][i] += 8
                        renpy.pause(.0000001)
                    timer += 0.1
        return timer

    def krib():
        global cl1, cl2, cl3, cl4, cl5, cl6, cl7, kricol, krix, krix0, pointka, ktmr, clp1, clp2, clp3, clp4, clp5, clp6, clp7
        row_lists = [cl1, cl2, cl3, cl4, cl5, cl6]
        anim_lists = [clp1, clp2, clp3, clp4, clp5, clp6]
        # Check matches and drop stones repeatedly
        for _ in range(6):
            pointka, ktmr = check_matches(row_lists, row_lists, pointka, ktmr)
            renpy.pause(0.05)
        for _ in range(6):
            ktmr = drop_stones(row_lists, anim_lists, ktmr)
        return

screen krix:
    text "[pointk]" style "mcnn"
    text str(int(ktmr)) style "mcnn" xalign .99
    timer 1 repeat True action If(ktmr > 0, true=SetVariable('ktmr', ktmr - 1), false=Return())
    for z in range(1, 7):
        for i in range(0, 9):
            imagebutton idle("k" + str(globals()["cl" + str(z)][i]) + ".w") xpos(i * 80 + 260) ypos(z * 80 + 20) action [SetVariable('krix', i), SetVariable('kriy', z), ui.callsinnewcontext("krich")]

screen krixx:
    text "[pointk]" style "mcnn"
    text str(int(ktmr)) style "mcnn" xalign .99
    timer 1 repeat True action If(ktmr > 0, true=SetVariable('ktmr', ktmr - 1), false=Return())
    for z in range(1, 7):
        for i in range(0, 9):
            image("k" + str(globals()["cl" + str(z)][i]) + ".w") xpos(i * 80 + 260) ypos(z * 80 + 20 + globals()["clp" + str(z)][i])

label krich:
    show screen krixx
    if krix >= 0:
        if krix in (krix0 + 1, krix0 - 1) and kriy == kriy0:
            pass
        elif kriy in (kriy0 + 1, kriy0 - 1) and krix == krix0:
            pass
        else:
            jump krich3
        if krix0 >= 0:
            $krixxx = globals()["cl" + str(kriy)][krix]
            $globals()["cl" + str(kriy)][krix] = globals()["cl" + str(kriy0)][krix0]
            $globals()["cl" + str(kriy0)][krix0] = krixxx
            label krich2:
                $krib()
                if pointka > 0:
                    $pointloop += 1
                    $pointk += pointka
                    $pointka = 0
                    jump krich2
                if pointloop == 0:
                    $krixxx = globals()["cl" + str(kriy0)][krix0]
                    $globals()["cl" + str(kriy0)][krix0] = globals()["cl" + str(kriy)][krix]
                    $globals()["cl" + str(kriy)][krix] = krixxx
                $pointloop = 0
                $krix = -1
                $krix0 = -1
        else:
            label krich3:
                $krix0 = krix
                $kriy0 = kriy
    return

label krix:
    scene kg
    python:
        cl0, cl1, cl2, cl3, cl4, cl5, cl6, cl7, krix, kriy, kris, krin, kriw, krie, kricol, krix, krix0, kriy, kriy0, pointk, pointloop, ktmr, pointka = [], [], [], [], [], [], [], [], 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 120, 0
        for z in range(1, 7):
            for i in range(0, 9):
                globals()["cl" + str(z)].append(renpy.random.randint(1, 6))
        clp0, clp1, clp2, clp3, clp4, clp5, clp6, clp7 = [], [], [], [], [], [], [], []
        for z in range(1, 7):
            for i in range(0, 9):
                globals()["clp" + str(z)].append(0)
    call screen krix
    return
