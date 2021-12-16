@namespace
class SpriteKind:
    End = SpriteKind.create()
    Spike = SpriteKind.create()
    Portal = SpriteKind.create()
    BOSS = SpriteKind.create()
    SECONDSTAGE = SpriteKind.create()
    LASTSTAGE = SpriteKind.create()
    Spoon = SpriteKind.create()
    HurtBySpikes = SpriteKind.create()
    HurtBySpikes2 = SpriteKind.create()
# Creates Levels.
def Levels():
    global CurrentLervel, Deaths, CANDOJAM, Goal, Cleaver, MyEnemy, Bportal, SPOON
    for value in sprites.all_of_kind(SpriteKind.Portal):
        value.destroy()
    for value2 in sprites.all_of_kind(SpriteKind.enemy):
        value2.destroy()
    for value3 in sprites.all_of_kind(SpriteKind.End):
        value3.destroy()
    for value4 in sprites.all_of_kind(SpriteKind.Spike):
        value4.destroy()
    CurrentLervel += 1
    Deaths = 0
    if CurrentLervel == 1:
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    elif CurrentLervel == 2:
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    elif CurrentLervel == 3:
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    elif CurrentLervel == 4:
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    elif CurrentLervel == 5:
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    elif CurrentLervel == 6:
        scene.set_background_image(assets.image("""
            DARK
        """))
        scene.set_tile(13,
            img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            True)
        CANDOJAM = True
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    elif CurrentLervel == 7:
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    elif CurrentLervel == 8:
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    elif CurrentLervel == 9:
        scene.set_tile_map(img("""
                . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . . 
                            . . . . . . . . . .
            """),
            TileScale.SIXTEEN)
    else:
        game.over(True)
    scene.place_on_random_tile(mySprite, 5)
    for value5 in scene.get_tiles_by_type(9):
        Goal = sprites.create(assets.image("""
            GOOOL
        """), SpriteKind.End)
        scene.place(value5, Goal)
    for value6 in scene.get_tiles_by_type(2):
        Cleaver = sprites.create(assets.image("""
            KLEEVEE
        """), SpriteKind.Spike)
        animation.run_image_animation(Cleaver,
            assets.animation("""
                ANIMECLEAVER
            """),
            150,
            True)
        scene.place(value6, Cleaver)
    for value7 in scene.get_tiles_by_type(6):
        MyEnemy = sprites.create(assets.image("""
            Toaster
        """), SpriteKind.enemy)
        scene.place(value7, MyEnemy)
        MyEnemy.follow(mySprite, 30)
    for value8 in scene.get_tiles_by_type(8):
        Bportal = sprites.create(assets.image("""
            BPortal
        """), SpriteKind.Portal)
        scene.place(value8, Bportal)
    for value9 in scene.get_tiles_by_type(10):
        SPOON = sprites.create(assets.image("""
            Spoo
        """), SpriteKind.Spoon)
        scene.place(value9, SPOON)
        SPOON.follow(mySprite, 50)

def on_on_overlap(sprite2, otherSprite2):
    global Fork, Whisk
    scene.place_on_random_tile(mySprite, 1)
    if CurrentLervel == 5:
        for value11 in scene.get_tiles_by_type(15):
            Fork = sprites.create(assets.image("""
                FORK
            """), SpriteKind.BOSS)
            scene.place(value11, Fork)
            Fork.follow(mySprite, 40)
    elif CurrentLervel == 9:
        for value12 in scene.get_tiles_by_type(15):
            Whisk = sprites.create(assets.image("""
                Rusty
            """), SpriteKind.HurtBySpikes)
            scene.place(value12, Whisk)
sprites.on_overlap(SpriteKind.player, SpriteKind.Portal, on_on_overlap)

def on_on_overlap2(sprite3, otherSprite3):
    global Goal
    if sprite3.y < otherSprite3.y:
        sprite3.vy = -100
        Final_fork.destroy(effects.fire, 500)
        music.play_melody("A G A B - - - - ", 416)
        scene.set_tile_at(scene.get_tile(18, 5), 9)
        for value13 in scene.get_tiles_by_type(9):
            Goal = sprites.create(assets.image("""
                GOOOL
            """), SpriteKind.End)
            scene.place(value13, Goal)
    else:
        scene.place_on_random_tile(mySprite, 1)
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.LASTSTAGE, on_on_overlap2)

def on_on_overlap3(sprite5, otherSprite5):
    global Whisk2
    sprite5.destroy(effects.fire, 1000)
    for value14 in scene.get_tiles_by_type(15):
        Whisk2 = sprites.create(assets.image("""
            Rusty2
        """), SpriteKind.HurtBySpikes2)
sprites.on_overlap(SpriteKind.HurtBySpikes, SpriteKind.Spike, on_on_overlap3)

def on_b_pressed():
    global projectile
    if MenuIndex == 0:
        if CANDOJAM:
            if LR == 1:
                projectile = sprites.create_projectile_from_sprite(assets.image("""
                    Marmalade
                """), mySprite, -125, 0)
            else:
                projectile = sprites.create_projectile_from_sprite(assets.image("""
                    Marmalade
                """), mySprite, 125, 0)
        else:
            game.show_long_text("NO JAM YET", DialogLayout.BOTTOM)
    else:
        CloseMenu()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap4(sprite4, otherSprite4):
    otherSprite4.destroy(effects.fire, 200)
    if sprite4.y < otherSprite4.y:
        sprite4.vy = -150
        music.play_melody("A G A B - - - - ", 416)
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Spoon, on_on_overlap4)

def on_on_overlap5(sprite, otherSprite):
    global Fork2
    if sprite.y < otherSprite.y:
        sprite.vy = -100
        Fork.destroy()
        music.play_melody("A G A B - - - - ", 416)
        for value10 in scene.get_tiles_by_type(15):
            Fork2 = sprites.create(assets.image("""
                FORK2
            """), SpriteKind.SECONDSTAGE)
            scene.place(value10, Fork2)
            Fork2.follow(mySprite, 50)
    else:
        scene.place_on_random_tile(mySprite, 1)
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.BOSS, on_on_overlap5)

def on_on_overlap6(sprite7, otherSprite7):
    sprite7.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Spoon, on_on_overlap6)

def on_a_pressed():
    if MenuIndex == 0:
        music.pew_pew.play()
        if LR == 2:
            animation.run_image_animation(mySprite, assets.animation("""
                JUMP
            """), 50, False)
        elif LR == 1:
            animation.run_image_animation(mySprite, assets.animation("""
                JUMP0
            """), 50, False)
        mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def Tiles():
    scene.set_tile(13,
        img("""
            d 1 1 1 1 1 1 1 1 1 1 1 1 1 1 b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    1 d d d d d d d d d d d d d d b 
                    b b b b b b b b b b b b b b b b
        """),
        True)
    scene.set_tile(5,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        False)
    scene.set_tile(14,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . e e e e e e e e e e . . . 
                    . . e 7 7 1 7 7 7 7 7 1 7 e . . 
                    . . e 7 1 7 1 7 7 7 1 7 1 e . . 
                    . . e 7 1 1 1 7 7 7 7 7 7 e . . 
                    . . e 7 1 7 1 7 7 7 7 1 7 e . . 
                    . . e 7 7 7 7 7 7 7 7 1 7 e . . 
                    . . . e e e e e e e e e e . . . 
                    . . . . . . . e e . . . . . . . 
                    . . . . . . . e e . . . . . . . 
                    . . . . . . . e e . . . . . . . 
                    . . . . . . . e e . . . . . . . 
                    . . . . . . . e e . . . . . . .
        """),
        False)
    scene.set_tile(2,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        False)
    scene.set_tile(6,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        False)
    scene.set_tile(15,
        img("""
            f f f f f f f f f f f f f f f f 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f 
                    f 5 f f f f f f f f f f f f 5 f 
                    f 5 f f f f 5 5 5 5 f f f f 5 f 
                    f 5 f f f 5 5 5 5 5 5 f f f 5 f 
                    f 5 f f f 5 f 5 5 f 5 f f f 5 f 
                    f 5 f f f 5 5 5 5 5 5 f f f 5 f 
                    f 5 f f f 5 5 5 5 5 5 f f f 5 f 
                    f 5 f f f 5 5 5 5 5 f f f f 5 f 
                    f 5 f f f f 5 f 5 f f f f f 5 f 
                    f 5 f 5 5 f f f f f f 5 5 f 5 f 
                    f 5 f f f 5 f 5 5 f 5 f f f 5 f 
                    f 5 f f f 5 5 f f 5 5 f f f 5 f 
                    f 5 f 5 5 f f f f f f 5 5 f 5 f 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f 
                    f f f f f f f f f f f f f f f f
        """),
        True)
    scene.set_tile(1,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        False)
    scene.set_tile(8,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        False)
    scene.set_tile(9,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        False)
    scene.set_tile(10,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        False)

def on_left_pressed():
    global LR
    if MenuIndex == 0:
        if mySprite.vy == 0:
            mySprite.set_image(assets.image("""
                Aaron0
            """))
            LR = 1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def CloseMenu():
    global MenuIndex
    MenuIndex = 0
    blockMenu.close_menu()

def on_on_overlap7(sprite9, otherSprite9):
    scene.place_on_random_tile(mySprite, 5)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Spike, on_on_overlap7)

def on_on_overlap8(sprite8, otherSprite8):
    global Final_fork
    if sprite8.y < otherSprite8.y:
        sprite8.vy = -100
        Fork2.destroy()
        music.play_melody("A G A B - - - - ", 416)
        for value15 in scene.get_tiles_by_type(15):
            Final_fork = sprites.create(assets.image("""
                FORK3
            """), SpriteKind.LASTSTAGE)
            scene.place(value15, Final_fork)
            Final_fork.follow(mySprite, 60)
    else:
        scene.place_on_random_tile(mySprite, 1)
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.SECONDSTAGE, on_on_overlap8)

def on_right_pressed():
    global LR
    if MenuIndex == 0:
        if mySprite.vy == 0:
            mySprite.set_image(assets.image("""
                Aaron
            """))
            LR = 2
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap9(sprite11, otherSprite11):
    otherSprite11.destroy(effects.fire, 200)
    if sprite11.y < otherSprite11.y:
        sprite11.vy = -100
        music.play_melody("A G A B - - - - ", 416)
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap9)

def on_on_overlap10(sprite6, otherSprite6):
    Levels()
sprites.on_overlap(SpriteKind.player, SpriteKind.End, on_on_overlap10)

def Startup():
    global MenuIndex, CurrentLervel, CANDOJAM, mySprite, vx, vy, LR
    game.splash("After Bread's Adventure,", "The Mad Scientist")
    game.splash("Contacted One Of His", "Siblings:")
    game.splash("William,", "The Mad Chef!")
    game.splash("And Told Him", "to Get The Bread")
    game.splash("Dead Or", "Alive!")
    game.splash("So Now The Bread", "Has To Kill Him.")
    game.splash("Or", "Something")
    scene.set_background_color(9)
    MenuIndex = 0
    CurrentLervel = 0
    CANDOJAM = False
    mySprite = sprites.create(assets.image("""
        Aaron
    """), SpriteKind.player)
    mySprite.ay = 500
    vx = 100
    vy = 0
    controller.move_sprite(mySprite, vx, vy)
    LR = 2
    scene.camera_follow_sprite(mySprite)
    info.set_life(3)
    Tiles()
    Levels()

def on_life_zero():
    global Deaths
    if Deaths == 0:
        info.set_life(3)
        scene.place_on_random_tile(mySprite, 5)
        Deaths += 1
    elif Deaths == 1:
        info.set_life(5)
        scene.place_on_random_tile(mySprite, 5)
        Deaths += 1
    elif Deaths == 2:
        game.over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap11(sprite10, otherSprite10):
    sprite10.destroy()
    otherSprite10.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap11)

def on_menu_option_selected(option, index):
    if MenuIndex == 1:
        if option == "Start":
            Startup()
            blockMenu.close_menu()
blockMenu.on_menu_option_selected(on_menu_option_selected)

vy = 0
vx = 0
Fork2: Sprite = None
projectile: Sprite = None
LR = 0
Whisk2: Sprite = None
Final_fork: Sprite = None
Whisk: Sprite = None
Fork: Sprite = None
SPOON: Sprite = None
Bportal: Sprite = None
MyEnemy: Sprite = None
Cleaver: Sprite = None
Goal: Sprite = None
mySprite: Sprite = None
CANDOJAM = False
Deaths = 0
CurrentLervel = 0
MenuIndex = 0
MenuIndex = 1
blockMenu.show_menu(["Start"], MenuStyle.LIST, MenuLocation.FULL_SCREEN)
blockMenu.set_colors(10, 8)

def on_on_update():
    if MenuIndex == 0:
        if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
            animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
            if LR == 2:
                mySprite.set_image(assets.image("""
                    Aaron
                """))
            elif LR == 1:
                mySprite.set_image(assets.image("""
                    Aaron0
                """))
game.on_update(on_on_update)

def on_forever():
    if MenuIndex == 0:
        controller.move_sprite(mySprite, vx, vy)
forever(on_forever)
