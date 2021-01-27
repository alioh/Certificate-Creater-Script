# Certificate Creator

Automatically create certificates for your event attendees.

## How it work?

- Design your certificate in the ppt file.
- Make sure the certificate dimensions are: 3508, 2481 pixels. 36.54, 25.84 in.
- The text in the middle should not be moved otherwise you have to do changes to where you want to put the attendees and event name. You can change that in line 29 for attendees name and line 35 for event name.The function [draw.text()](https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html) is the one that write, so you need to do your changes in its first parameter to relocated the x,y location of the text.
- To change the font, add the font .ttf file location in line 9.
- To change the text size, pass it as points to [ImageFont.truetype()](https://pillow.readthedocs.io/en/3.0.x/reference/ImageFont.html) size parameter in line 9.
- To change the text output color, write it as text like this: `'rgb(73, 85, 125)'` and then pass it to draw.text() function.
- If you want to use Arabic, make sure to use [arabic_reshaper](https://github.com/mpcabd/python-arabic-reshaper) and [bidi.algorithm](https://pypi.org/project/python-bidi/) packages, otherwise the text will be reversed:
    - Arabic_reshaper.reshape() in line 27 takes the text and reshape it.
    - Bidi.algorithm's get_display() function display the text after reshaping in its correct form.
    - More about this [here](https://gist.github.com/amrza/04658c71ac02d82580855f89b9b3dff4).
- Use the function createCertificate to create your certificates. It takes two parameters:
    - Event name as text.
    - Attendees as list.
- Run the code.
- You will get your certificates in this shape:
    - [attendees name]_certificate.png


## To add:
- The ability to automatically send emails to each attendees.
- Read from excel or csv instead of manually put names in the script file.


If you have any ideas or want to contribute, contact me [here](http://www.alioh.com/).

reference: [1](https://haptik.ai/tech/putting-text-on-image-using-python/)