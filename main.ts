controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`detective boogie`)
    animation.runImageAnimation(
    mySprite,
    assets.animation`boogies animation`,
    200,
    true
    )
})
let mySprite: Sprite = null
tiles.setTilemap(tilemap`sneek city`)
mySprite = sprites.create(assets.image`detective boogie`, SpriteKind.Player)
tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 7))
scene.cameraFollowSprite(mySprite)
controller.moveSprite(mySprite)
