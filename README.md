# Certificate-Creater-Script

## How it work?

- Design your certificate in the ppt file.
- Make sure the certificate dimensions are: 3508, 2481 pixels. 36.54, 25.84 in.
- The text in the middle should not be moved otherwise you have to do changes to where you want to put the attendees and event name. You can change that in line 29 for attendees name and line 35 for event name. The function draw.text() is the one that write, so you need to do your changes in its first parameter.
- Use the function createCertificate to create your certificates. It takes:
    - Event name.
    - List of attendees.
- Run the code.
- You will get your certificates in this shape:
    - [attendees name]_certificate.png

