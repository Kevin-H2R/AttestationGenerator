from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

nameX = 160
nameY = 262

bornX = 160
bornY = 298

liveX = 160
liveY = 339

doneAtX = 445
doneAtY = 832
dayX = 567
monthX = 597

signatureX = 564
signatureY = 850

fontSize = 32
deltaY = (fontSize / 2) + 4


checkboxX = 58
checkedHeight = [493, 583, 636, 675, 729]

checkedByUser = sys.argv[8]

img = Image.open("img.jpeg")
draw = ImageDraw.Draw(img)

# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("fonts/otto.ttf", fontSize)
smallFont = ImageFont.truetype("fonts/otto.ttf", fontSize // 2)
crossFont = ImageFont.truetype("fonts/alanis.ttf", fontSize + 12)
signatureFont = ImageFont.truetype("fonts/arty.otf", fontSize + 12)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((nameX, nameY - deltaY), sys.argv[1] + " " + sys.argv[2], (10,10,10), font=font)
draw.text((bornX, bornY - deltaY), sys.argv[3], (10, 10, 10), font=font)
draw.text((liveX, liveY - deltaY), sys.argv[4], (10, 10,10), font=font)
draw.text((checkboxX, checkedHeight[checkedByUser] - deltaY), "X", (10, 10, 10), font=crossFont)
draw.text((doneAtX, doneAtY - 3), sys.argv[5], (10, 10, 10), font=smallFont)
draw.text((dayX, doneAtY - 10), sys.argv[6], (10, 10, 10), font=font)
draw.text((monthX, doneAtY - 10), sys.argv[7], (10, 10, 10), font=font)
draw.text((signatureX, signatureY), sys.argv[1] + " " + sys.argv[2], (10, 10, 10), font=signatureFont)
img.save('attestation.jpg')