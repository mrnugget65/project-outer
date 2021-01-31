def on_right_pressed():
    mySprite.set_image(assets.image("""
        detective boogie
    """))
    animation.run_image_animation(mySprite,
        assets.animation("""
            boogies animation
        """),
        500,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

mySprite: Sprite = None
tiles.set_tilemap(tilemap("""
    sneek city
"""))
mySprite = sprites.create(assets.image("""
        detective boogie
    """),
    SpriteKind.player)
tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 7))
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite)