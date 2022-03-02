"""simple pyglet demo"""
import pyglet

CLICK_COUNT=0

window = pyglet.window.Window(480,360)

treasure = pyglet.sprite.Sprite(img=pyglet.resource.image('riches.png'))

clicks = pyglet.text.Label(text="Clicks: " + str(CLICK_COUNT), x=5, y=345)

sound = pyglet.resource.media('cash.wav', streaming=False)

spinCoin = pyglet.image.ImageGrid(pyglet.image.load('coin.png'), 6, 1)
coin_image = pyglet.image.Animation.from_image_sequence(spinCoin,1/24.0)
coins = []

def animate_coins():
    """coin rises and fades"""
    for coin in coins:
        coin.y += 1
        coin.opacity -= 4
    coins[:] = [coin for coin in coins if coin.opacity > 0]

@window.event
def on_draw():
    """what to show in the window"""
    treasure.draw()
    clicks.draw()
    for coin in coins:
        coin.draw()

@window.event
def on_mouse_press(mouse_x,mouse_y):
    """count the clicks"""
    global CLICK_COUNT
    CLICK_COUNT += 1
    clicks.text = "Clicks: " + str(CLICK_COUNT)
    sound.play()
    coins.append(pyglet.sprite.Sprite(
        img=coin_image,
        x=mouse_x, y=mouse_y))

pyglet.clock.schedule_interval(animate_coins, 1/120.0)

music = pyglet.media.Player()
music.queue(pyglet.resource.media('news.wav'))
music.play()

pyglet.app.run()
