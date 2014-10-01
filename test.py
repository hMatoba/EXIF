import os
import unittest

from PIL import Image
from EXIF import *


class ExifTests(unittest.TestCase):
    def test_roundtrip(self):
        d = {ImageGroup.ProcessingSoftware: "PIL",
             ImageGroup.Make: "Make",
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
        exif = Exif(d)
        exif.load(exif.to_bytes())
        exif.pop(34665) # Exif IFD pointer
        self.assertDictEqual(exif, d)

    def test_file_generate(self):
        d = {11: "PIL",
             271: "Make",
             272: "XXX-XXX",
             282: (300, 1),
             283: (200, 1),
             18246: 3,
             36867: "2099:09:29 10:10:10",
             41994: 1,
             42035: "LensMake",
             34853: {0: 2, 2: (1, 300), 29: "1999:99:99 99:99:99"}}
        exif = Exif(d)
        im1 = Image.new("RGBA", (16, 16))
        im1.save("im1.jpg", exif=exif.to_bytes())
        im2 = Image.open("im1.jpg")
        im2.close()


if __name__ == "__main__":
    unittest.main()
