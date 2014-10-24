EXIF
====

|Build Status| |Coverage Status|

Use EXIF object with PIL or Pillow.

How to Use
----------

.. code:: python

    from PIL import Image
    from EXIF import *

    d = {ImageGroup.ProcessingSoftware: "PIL",
         ImageGroup.Model: "XXX-XXX",
         ImageGroup.XResolution: (300, 1),
         ImageGroup.YResolution: (200, 1),
         ImageGroup.Rating: 3,
         PhotoGroup.DateTimeOriginal: "2099:09:29 10:10:10",
         PhotoGroup.Sharpness: 1,
         PhotoGroup.LensMake: "LensMake",
         ImageGroup.GPSTag: {GPSGroup.GPSVersionID: 2,
                             GPSGroup.GPSLatitude: (1, 300),
                             GPSGroup.GPSDateStamp: "1999:99:99 99:99:99"}}
    exif = Exif()
    exif.update(d)
    exif[271] = "Make"
    im1 = Image.new("RGBA", (16, 16))
    im1.save("im1.jpg", exif=exif.to_bytes())

Environment
-----------

Checked on Python 2.6, 2.7, 3.2, 3.3 and 3.4.

.. |Build Status| image:: https://travis-ci.org/hMatoba/EXIF.svg?branch=master
   :target: https://travis-ci.org/hMatoba/EXIF
.. |Coverage Status| image:: https://coveralls.io/repos/hMatoba/EXIF/badge.png?branch=master
   :target: https://coveralls.io/r/hMatoba/EXIF?branch=master