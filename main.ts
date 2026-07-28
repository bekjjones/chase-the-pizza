sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    pizza.setPosition(randint(0, scene.screenWidth()), randint(0, scene.screenHeight()))
    info.startCountdown(3)
})
let pizza: Sprite = null
scene.setBackgroundColor(10)
let mySprite = sprites.create(assets.image`Smiley`, SpriteKind.Player)
controller.moveSprite(mySprite)
pizza = sprites.create(assets.image`Pizza`, SpriteKind.Food)
