from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *

text = [
    "Arstotzka is the first!"
]

def img(z, v):
    z = "foto/" + z + '.jpg'
    im = Image.new('RGB', (1366, 768), color="#000000")
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 32, encoding='UTF-8')
    draw_text.v(
        (683, 100),
        v,
        fill= "#FFFFFF",
        font= font
    )
    im.save(z)

def video():
    direct = 'foto/'
    files= os.listdir(direct)
    imag = list(filter(lambda x: x.endswith('.jpg'), files))
    clips = [ImageClip('foto/'+ m).set_duration(2) for m  in imag]

    final = concatenate_videoclips(clips, method='compose')
    final.write_videofile('video.mp4',fps=24)

for i in range(len(text)):
    img(str(i), text[i])

video()