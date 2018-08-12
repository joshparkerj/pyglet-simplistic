import pyglet

clickCount=0

window = pyglet.window.Window(480,360)

treasure = pyglet.sprite.Sprite(img=pyglet.resource.image('riches.png'))

clicks = pyglet.text.Label(text="Clicks: " + str(clickCount), x=5, y=345)

sound = pyglet.resource.media('cash.wav', streaming=False)

spinCoin = pyglet.image.ImageGrid(pyglet.image.load('coin.png'), 6, 1)
coin = pyglet.image.Animation.from_image_sequence(spinCoin,1/24.0)
coins = []

def animateCoins(dt):
 for i in range(len(coins)):
  if coins[i].opacity <= 0:
   del coins[i]
   return
  coins[i].y += 1
  coins[i].opacity -= 3

@window.event
def on_draw():
 treasure.draw()
 clicks.draw()
 for coin in coins:
  coin.draw()

@window.event
def on_mouse_press(a,b,c,d):
 global clickCount
 clickCount += 1
 clicks.text = "Clicks: " + str(clickCount)
 sound.play()
 coins.append(pyglet.sprite.Sprite(
  img=coin,
  x=a, y=b))

pyglet.clock.schedule_interval(animateCoins, 1/120.0)

music = pyglet.media.Player()
music.queue(pyglet.resource.media('news.wav'))
music.play()

pyglet.app.run()