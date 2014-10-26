import io

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from PIL import Image
from EXIF import Exif, ZerothIFD, ExifIFD, GPSIFD, _ExifReader


EXIF_DICT = {
    ZerothIFD.ProcessingSoftware: "PIL",  # ascii
    ZerothIFD.Make: "Make",  # ascii
    ZerothIFD.Model: "XXX-XXX",  # ascii
    ZerothIFD.JPEGTables: b"\xaa\xaa",  # undefined
    ZerothIFD.ClipPath: 255,  # byte
    ZerothIFD.Rating: 65535,  # short
    ZerothIFD.XClipPathUnits: 4294967295,  # long
    ZerothIFD.XResolution: (4294967295, 1),  # rational
    ZerothIFD.CameraCalibration1: (2147483647, -2147483648),  # srational
    ExifIFD.DateTimeOriginal: "2099:09:29 10:10:10",  # ascii
    ExifIFD.LensMake: "LM",  # ascii
    ExifIFD.OECF: b"\xaa\xaa\xaa\xaa\xaa\xaa",  # undefined
    ExifIFD.Sharpness: 65535,  # short
    ExifIFD.ISOSpeed: 4294967295,  # long
    ExifIFD.ExposureTime: (4294967295, 1),  # rational
    ExifIFD.ExposureBiasValue: (2147483647, -2147483648),  # srational
    ZerothIFD.GPSTag: {
        GPSIFD.GPSVersionID: 255,  # byte
        GPSIFD.GPSDateStamp: "1999:99:99 99:99:99",  # ascii
        GPSIFD.GPSDifferential: 65535,  # short
        GPSIFD.GPSLatitude: (4294967295, 1),  # rational
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

    def test_exif_reader(self):
        with self.assertRaises(ValueError):
            _ExifReader("dummy")


if __name__ == "__main__":
    unittest.main()
