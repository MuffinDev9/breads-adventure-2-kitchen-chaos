namespace SpriteKind {
    export const End = SpriteKind.create()
    export const Spike = SpriteKind.create()
    export const Portal = SpriteKind.create()
    export const BOSS = SpriteKind.create()
    export const SECONDSTAGE = SpriteKind.create()
    export const LASTSTAGE = SpriteKind.create()
    export const Spoon = SpriteKind.create()
    export const HurtBySpikes = SpriteKind.create()
    export const HurtBySpikes2 = SpriteKind.create()
    export const HurtBySpikes3 = SpriteKind.create()
}
// Creates Levels.
function Levels () {
    for (let value of sprites.allOfKind(SpriteKind.Portal)) {
        value.destroy()
    }
    for (let value2 of sprites.allOfKind(SpriteKind.Enemy)) {
        value2.destroy()
    }
    for (let value3 of sprites.allOfKind(SpriteKind.End)) {
        value3.destroy()
    }
    for (let value4 of sprites.allOfKind(SpriteKind.Spike)) {
        value4.destroy()
    }
    CurrentLervel += 1
    Deaths = 0
    Bossexists = false
    if (CurrentLervel == 1) {
        scene.setTileMap(assets.image`Tutorial`, TileScale.Sixteen)
    } else if (CurrentLervel == 2) {
        scene.setTileMap(assets.image`1-1`, TileScale.Sixteen)
    } else if (CurrentLervel == 3) {
        scene.setTileMap(assets.image`1-2`, TileScale.Sixteen)
    } else if (CurrentLervel == 4) {
        scene.setTileMap(assets.image`1-3`, TileScale.Sixteen)
    } else if (CurrentLervel == 5) {
        scene.setTileMap(assets.image`1-4`, TileScale.Sixteen)
    } else if (CurrentLervel == 6) {
        scene.setBackgroundImage(assets.image`DARK`)
        scene.setTile(13, assets.image`DarkBrick`, true)
        CANDOJAM = true
        scene.setTileMap(assets.image`2-1`, TileScale.Sixteen)
    } else if (CurrentLervel == 7) {
        scene.setTileMap(assets.image`2-2`, TileScale.Sixteen)
    } else if (CurrentLervel == 8) {
        scene.setTileMap(assets.image`2-3`, TileScale.Sixteen)
    } else if (CurrentLervel == 9) {
        scene.setTileMap(assets.image`2-4`, TileScale.Sixteen)
    } else if (CurrentLervel == 10) {
        scene.setBackgroundColor(9)
        scene.setTile(13, assets.image`Block`, true)
        SpikesMove = 0
        scene.setTileMap(assets.image`3-1`, TileScale.Sixteen)
    } else {
        game.over(true)
    }
    scene.placeOnRandomTile(mySprite, 5)
    for (let value5 of scene.getTilesByType(9)) {
        Goal = sprites.create(assets.image`GOOOL`, SpriteKind.End)
        scene.place(value5, Goal)
    }
    for (let value6 of scene.getTilesByType(2)) {
        Cleaver = sprites.create(assets.image`KLEEVEE`, SpriteKind.Spike)
        animation.runImageAnimation(
        Cleaver,
        assets.animation`ANIMECLEAVER`,
        150,
        true
        )
        scene.place(value6, Cleaver)
    }
    for (let value7 of scene.getTilesByType(6)) {
        MyEnemy = sprites.create(assets.image`Toaster`, SpriteKind.Enemy)
        scene.place(value7, MyEnemy)
        MyEnemy.follow(mySprite, 30)
    }
    for (let value8 of scene.getTilesByType(8)) {
        Bportal = sprites.create(assets.image`BPortal`, SpriteKind.Portal)
        scene.place(value8, Bportal)
    }
    for (let value9 of scene.getTilesByType(10)) {
        SPOON = sprites.create(assets.image`Spoo`, SpriteKind.Spoon)
        scene.place(value9, SPOON)
        SPOON.follow(mySprite, 50)
    }
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (CANDOJAM) {
        if (LR == 1) {
            projectile = sprites.createProjectileFromSprite(assets.image`Marmalade`, mySprite, -125, 0)
        } else {
            projectile = sprites.createProjectileFromSprite(assets.image`Marmalade`, mySprite, 125, 0)
        }
    } else {
        game.showLongText("NO JAM YET", DialogLayout.Bottom)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.BOSS, function (sprite, otherSprite) {
    if (sprite.y < otherSprite.y) {
        sprite.vy = -100
        Fork.destroy()
        music.playMelody("A G A B - - - - ", 416)
        for (let value10 of scene.getTilesByType(15)) {
            Fork2 = sprites.create(assets.image`FORK2`, SpriteKind.SECONDSTAGE)
            scene.place(value10, Fork2)
            Fork2.follow(mySprite, 50)
        }
    } else {
        scene.placeOnRandomTile(mySprite, 1)
        info.changeLifeBy(-1)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.pewPew.play()
    if (LR == 2) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`JUMP`,
        50,
        false
        )
    } else if (LR == 1) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`JUMP0`,
        50,
        false
        )
    }
    mySprite.vy = -200
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Portal, function (sprite, otherSprite) {
    scene.placeOnRandomTile(mySprite, 1)
    if (!(Bossexists)) {
        if (CurrentLervel == 5) {
            for (let value11 of scene.getTilesByType(15)) {
                Fork = sprites.create(assets.image`FORK`, SpriteKind.BOSS)
                scene.place(value11, Fork)
                Fork.follow(mySprite, 40)
                Bossexists = true
            }
        } else if (CurrentLervel == 9) {
            for (let value12 of scene.getTilesByType(15)) {
                Whisk = sprites.create(assets.image`Rusty`, SpriteKind.HurtBySpikes)
                scene.place(value12, Whisk)
                Whisk.follow(mySprite, 70)
                Bossexists = true
            }
        }
    }
})
function Tiles () {
    scene.setTile(13, assets.image`Block`, true)
    scene.setTile(5, img`
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
        `, false)
    scene.setTile(14, img`
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
        `, false)
    scene.setTile(2, img`
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
        `, false)
    scene.setTile(6, img`
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
        `, false)
    scene.setTile(15, assets.image`BossBrick`, true)
    scene.setTile(1, img`
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
        `, false)
    scene.setTile(8, img`
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
        `, false)
    scene.setTile(9, img`
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
        `, false)
    scene.setTile(10, img`
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
        `, false)
    scene.setTile(3, assets.image`ze-red-fing`, false)
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.setImage(assets.image`Aaron0`)
        LR = 1
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.LASTSTAGE, function (sprite, otherSprite) {
    if (sprite.y < otherSprite.y) {
        sprite.vy = -100
        Final_fork.destroy(effects.fire, 500)
        music.playMelody("A G A B - - - - ", 416)
        scene.setTileAt(scene.getTile(18, 5), 9)
        for (let value13 of scene.getTilesByType(9)) {
            Goal = sprites.create(assets.image`GOOOL`, SpriteKind.End)
            scene.place(value13, Goal)
        }
    } else {
        scene.placeOnRandomTile(mySprite, 1)
        info.changeLifeBy(-1)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Spoon, function (sprite, otherSprite) {
    otherSprite.destroy(effects.fire, 200)
    if (sprite.y < otherSprite.y) {
        sprite.vy = -150
        music.playMelody("A G A B - - - - ", 416)
    } else {
        info.changeLifeBy(-1)
    }
})
sprites.onOverlap(SpriteKind.HurtBySpikes, SpriteKind.Spike, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 1000)
    music.playMelody("A G A B - - - - ", 416)
    for (let value14 of scene.getTilesByType(15)) {
        Whisk2 = sprites.create(assets.image`Rusty2`, SpriteKind.HurtBySpikes2)
        scene.place(value14, Whisk2)
        Whisk2.follow(mySprite, 90)
    }
})
sprites.onOverlap(SpriteKind.HurtBySpikes3, SpriteKind.Player, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    scene.placeOnRandomTile(mySprite, 5)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.End, function (sprite, otherSprite) {
    Levels()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Spoon, function (sprite, otherSprite) {
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.HurtBySpikes2, SpriteKind.Spike, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 1000)
    music.playMelody("A G A B - - - - ", 416)
    for (let value142 of scene.getTilesByType(15)) {
        Whisk3 = sprites.create(assets.image`Rusty3`, SpriteKind.HurtBySpikes3)
        scene.place(value142, Whisk3)
        Whisk3.follow(mySprite, 110)
    }
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.setImage(assets.image`Aaron`)
        LR = 2
    }
})
sprites.onOverlap(SpriteKind.HurtBySpikes3, SpriteKind.Spike, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 1000)
    scene.setTileAt(scene.getTile(27, 9), 9)
    Bossexists = false
    music.playMelody("A G A B - - - - ", 416)
    for (let value132 of scene.getTilesByType(9)) {
        Goal = sprites.create(assets.image`GOOOL`, SpriteKind.End)
        scene.place(value132, Goal)
    }
})
sprites.onOverlap(SpriteKind.HurtBySpikes, SpriteKind.Player, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    scene.placeOnRandomTile(mySprite, 5)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SECONDSTAGE, function (sprite, otherSprite) {
    if (sprite.y < otherSprite.y) {
        sprite.vy = -100
        Fork2.destroy()
        music.playMelody("A G A B - - - - ", 416)
        for (let value15 of scene.getTilesByType(15)) {
            Final_fork = sprites.create(assets.image`FORK3`, SpriteKind.LASTSTAGE)
            scene.place(value15, Final_fork)
            Final_fork.follow(mySprite, 60)
        }
    } else {
        scene.placeOnRandomTile(mySprite, 1)
        info.changeLifeBy(-1)
    }
})
info.onLifeZero(function () {
    if (Deaths == 0) {
        info.setLife(3)
        scene.placeOnRandomTile(mySprite, 5)
        Deaths += 1
    } else if (Deaths == 1) {
        info.setLife(5)
        scene.placeOnRandomTile(mySprite, 5)
        Deaths += 1
    } else if (Deaths == 2) {
        game.over(false)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Spike, function (sprite, otherSprite) {
    if (CurrentLervel != 10) {
        scene.placeOnRandomTile(mySprite, 5)
        info.changeLifeBy(-1)
    } else {
    	
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy(effects.fire, 500)
})
sprites.onOverlap(SpriteKind.HurtBySpikes2, SpriteKind.Player, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    scene.placeOnRandomTile(mySprite, 5)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.fire, 200)
    if (sprite.y < otherSprite.y) {
        sprite.vy = -100
        music.playMelody("A G A B - - - - ", 416)
    } else {
        info.changeLifeBy(-1)
    }
})
let Whisk3: Sprite = null
let Whisk2: Sprite = null
let Final_fork: Sprite = null
let Whisk: Sprite = null
let Fork2: Sprite = null
let Fork: Sprite = null
let projectile: Sprite = null
let SPOON: Sprite = null
let Bportal: Sprite = null
let MyEnemy: Sprite = null
let Cleaver: Sprite = null
let Goal: Sprite = null
let SpikesMove = 0
let Bossexists = false
let Deaths = 0
let LR = 0
let vy = 0
let mySprite: Sprite = null
let CANDOJAM = false
let CurrentLervel = 0
game.splash("After Bread's Adventure,", "The Mad Scientist")
game.splash("Contacted One Of His", "Siblings:")
game.splash("William,", "The Mad Chef!")
game.splash("And Told Him", "to Get The Bread")
game.splash("Dead Or", "Alive!")
game.splash("So Now The Bread", "Has To Kill Him.")
game.splash("Or", "Something")
scene.setBackgroundColor(9)
CurrentLervel = 0
CANDOJAM = false
mySprite = sprites.create(assets.image`Aaron`, SpriteKind.Player)
mySprite.ay = 500
let vx = 100
controller.moveSprite(mySprite, vx, vy)
LR = 2
scene.cameraFollowSprite(mySprite)
info.setLife(3)
Tiles()
Levels()
game.onUpdate(function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        animation.stopAnimation(animation.AnimationTypes.All, mySprite)
        if (LR == 2) {
            mySprite.setImage(assets.image`Aaron`)
        } else if (LR == 1) {
            mySprite.setImage(assets.image`Aaron0`)
        }
    }
})
forever(function () {
    controller.moveSprite(mySprite, vx, vy)
})
game.onUpdateInterval(500, function () {
    if (CurrentLervel == 10) {
        SpikesMove += 1
        scene.setTileAt(scene.getTile(SpikesMove, 6), 13)
        scene.setTileAt(scene.getTile(SpikesMove, 7), 13)
        scene.setTileAt(scene.getTile(SpikesMove, 8), 13)
        scene.setTileAt(scene.getTile(SpikesMove, 9), 13)
        scene.setTileAt(scene.getTile(SpikesMove, 10), 13)
        scene.setTileAt(scene.getTile(SpikesMove, 11), 13)
    }
})
