import io

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from PIL import Image
from EXIF import Exif, GPSGroup, ImageGroup, PhotoGroup


EXIF_DICT = {
    ImageGroup.ProcessingSoftware: "PIL",  # ascii
    ImageGroup.Make: "Make",  # ascii
    ImageGroup.Artist: "Mr. Foo",
    ImageGroup.Model: "XXX-XXX",  # ascii
    ImageGroup.ClipPath: 255,  # byte
    ImageGroup.Rating: 65535,  # short
    ImageGroup.XClipPathUnits: 4294967295,  # long
    ImageGroup.XResolution: (4294967295, 1),  # rational
    ImageGroup.CameraCalibration1: (2147483647, -2147483648),  # srational
    PhotoGroup.DateTimeOriginal: "2099:09:29 10:10:10",  # ascii
    PhotoGroup.LensMake: "LensMake",  # ascii
    PhotoGroup.Sharpness: 65535,  # short
    PhotoGroup.ISOSpeed: 4294967295,  # long
    PhotoGroup.ExposureTime: (4294967295, 1),  # rational
    PhotoGroup.ExposureBiasValue: (2147483647, -2147483648),  # srational
    ImageGroup.GPSTag: {
        GPSGroup.GPSVersionID: 255,  # byte
        GPSGroup.GPSDateStamp: "1999:99:99 99:99:99",  # ascii
        GPSGroup.GPSDifferential: 65535,  # short
        GPSGroup.GPSLatitude: (4294967295, 1),  # rational
        }
    }


class ExifTests(unittest.TestCase):
    def test_roundtrip(self):
        exif = Exif(EXIF_DICT)
        exif.load(exif.to_bytes())
        exif.pop(34665)  # Exif IFD pointer
        self.assertDictEqual(exif, EXIF_DICT)

    def test_file_generate(self):
        f = io.BytesIO()
        exif = Exif(EXIF_DICT)
        im1 = Image.new("RGBA", (16, 16))
        im1.save(f, format="JPEG", exif=exif.to_bytes())
        f.seek(0)
        im2 = Image.open(f)
        im2.close()


if __name__ == "__main__":
    unittest.main()
