from PIL import Image, ImageDraw
from moviepy.editor import *
import os

def z(im, x, y):

    im = Image.new('RGB', (200,200), color=('#FAACAC'))
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (x,y),
        'Arstotzka is the first',
        fill=('#1C0606')
        )
a = 'foto'
k = 70
m = 95
s = 0
o = 0

for i in range(10):
    z(a, k, m)
    s += 1
    if s < 5:
        k +=5
        m +=5
    else:
        k -= 5
        m -= 5
    o += 1
    a = a + str(o)
    img = a
    path = os.path.join(r'C:\Users\Егор\slide', 'a.jpg')
    a = Image.open('a.jpg')
    img.save(path)

directory = r'C:\Users\Егор\slide'
files = os.listdir(directory)
images = list(filter(lambda x: x.endswith('.jpg'), files))
clips = [ImageClip(m).set_duration(2) for m in images]

final_clip = concatenate_videoclips(clips, method='compose')
final_clip.write_videofile('video.mp4', fps = 24)