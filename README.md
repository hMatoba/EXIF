EXIF
=====================

Use Exif object with PIL or Pillow.


How to Use
--------
    from PIL import Image
    from EXIF import Exif

    d = {11: "PIL",
         272: "XXX-XXX",
         282: (300, 1),
         283: (200, 1),
         18246: 3,
         36867: "2099:09:29 10:10:10",
         41994: 1,
         42035: "LensMake",
         34853: {0: 2, 2: (1, 300), 29: "1999:99:99 99:99:99"}}
    exif = Exif()
    exif.update(d)
    exif[271] = "Make"
    im1 = Image.new("RGBA", (16, 16))
    im1.save("im1.jpg", exif=exif.to_bytes())


Environment
--------
  Checked on Python 2.7 and 3.4.
