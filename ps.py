"""simple pyglet demo"""
from dataclasses import dataclass
import pyglet

window = pyglet.window.Window(480,360)

treasure = pyglet.sprite.Sprite(img=pyglet.resource.image('riches.png'))

clicks = pyglet.text.Label(text="Clicks: 0", x=5, y=345)

sound = pyglet.resource.media('cash.wav', streaming=False)

spinCoin = pyglet.image.ImageGrid(pyglet.image.load('coin.png'), 6, 1)
coin_image = pyglet.image.Animation.from_image_sequence(spinCoin,1/24.0)
coins = []

@dataclass
class CountClicks:
    """encapsulates click count"""
    click_count: int = 0

    def count(self):
        """increment click count and learn what it is"""
        self.click_count += 1
        return self.click_count

count_clicks = CountClicks()

def animate_coins(time_interval):
    """coin rises and fades"""
    for coin in coins:
        coin.y += 120.0 * time_interval
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
def on_mouse_press(mouse_x,mouse_y, button, modifiers):
    """count the clicks"""
    if button == pyglet.window.mouse.LEFT \
        and modifiers \
            & ~pyglet.window.key.MOD_NUMLOCK \
            & ~pyglet.window.key.MOD_CAPSLOCK \
            & ~pyglet.window.key.MOD_SCROLLLOCK == 0:
        clicks.text = "Clicks: " + str(count_clicks.count())
        sound.play()
        coins.append(pyglet.sprite.Sprite(
            img=coin_image,
            x=mouse_x, y=mouse_y))

pyglet.clock.schedule_interval(animate_coins, 1/120.0)

music = pyglet.media.Player()
music.queue(pyglet.resource.media('news.wav'))
music.play()

pyglet.app.run()
