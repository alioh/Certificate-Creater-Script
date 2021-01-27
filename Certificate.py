from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import os

#   Load preferable font
font = ImageFont.truetype('calibri.ttf', size=150)

#   Certificate size
(x, y) = (3508, 2481)

#   Output color
color = 'rgb(73, 85, 125)'

#   Loop through names and write/save
def createCertificate(workshop, attendees_list):
    for i in attendees_list:
        img = Image.open('Certificate.png')
        draw = ImageDraw.Draw(img)

        #   Size of text
        w, h = draw.textsize(i, font)

        reshaped_attendees_name = arabic_reshaper.reshape(i)
        text_attendees_name = get_display(reshaped_attendees_name)
        draw.text((((x/2)-(w/2.5)), ((y - h) / 2)-310), text_attendees_name, fill=color, font=font)

        p, q = draw.textsize(workshop, font)

        reshaped_workshop = arabic_reshaper.reshape(workshop)
        workshop_name = get_display(reshaped_workshop)
        draw.text((((x/2)-(p/2.5)), ((y - q) / 2)+50), workshop_name, fill=color, font=font)

        img.save(f'{i}_certificate.png')

att = ["أسم المتدرب الأول", "أسم المتدرب الثاني"]
createCertificate("عنوان لورشة العمل", att)