def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    pizza.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
    info.start_countdown(3)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

pizza: Sprite = None
scene.set_background_color(10)
mySprite = sprites.create(assets.image("""
    Smiley
    """), SpriteKind.player)
controller.move_sprite(mySprite)
pizza = sprites.create(assets.image("""
    Pizza
    """), SpriteKind.food)