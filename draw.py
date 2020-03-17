from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


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

checkedByUser = 4

img = Image.open("img.jpeg")
draw = ImageDraw.Draw(img)

# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("otto.ttf", fontSize)
smallFont = ImageFont.truetype("otto.ttf", fontSize // 2)
crossFont = ImageFont.truetype("alanis.ttf", fontSize + 12)
signatureFont = ImageFont.truetype("arty.otf", fontSize + 12)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((nameX, nameY - deltaY),"Kevin Herrbach",(10,10,10),font=font)
draw.text((bornX, bornY - deltaY),"25-08-1994",(10,10,10),font=font)
draw.text((liveX, liveY - deltaY),"6 rue Darblay, Saint-Germain-les-Corbeil, 91250",(10,10,10),font=font)
draw.text((checkboxX, checkedHeight[checkedByUser] - deltaY),"X",(10,10,10),font=crossFont)
draw.text((doneAtX, doneAtY - 3),"Saint-Germain-les-Corbeil",(10,10,10),font=smallFont)
draw.text((dayX, doneAtY - deltaY),"17",(10,10,10),font=font)
draw.text((monthX, doneAtY - deltaY),"03",(10,10,10),font=font)
draw.text((signatureX, signatureY),"Kevin Herrbach",(10,10,10),font=signatureFont)
img.save('sample-out.jpg')