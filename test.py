import io
import os

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
    ZerothIFD.BlackLevelDeltaH: ((1, 1), (1, 1), (1, 1), ),  # srational
    ExifIFD.DateTimeOriginal: "2099:09:29 10:10:10",  # ascii
    ExifIFD.LensMake: "LM",  # ascii
    ExifIFD.OECF: b"\xaa\xaa\xaa\xaa\xaa\xaa",  # undefined
    ExifIFD.Sharpness: 65535,  # short
    ExifIFD.ISOSpeed: 4294967295,  # long
    ExifIFD.ExposureTime: (4294967295, 1),  # rational
    ExifIFD.ExposureBiasValue: (2147483647, -2147483648),  # srational
    ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1), ),  # rational
    ZerothIFD.GPSTag: {
        GPSIFD.GPSVersionID: 255,  # byte
        GPSIFD.GPSDateStamp: "1999:99:99 99:99:99",  # ascii
        GPSIFD.GPSDifferential: 65535,  # short
        GPSIFD.GPSLatitude: (4294967295, 1),  # rational
        }
    }

INPUT_FILE_JPG = os.path.join("images", "01.jpg")
INPUT_FILE_TIF = os.path.join("images", "01.tif")

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

    def test_no_exif_file_generate(self):
        f = io.BytesIO()
        exif = Exif()
        im1 = Image.new("RGBA", (16, 16))
        im1.save(f, format="JPEG", exif=exif.to_bytes())
        f.seek(0)
        im2 = Image.open(f)
        im2.close()

    def test_ExifReader(self):
        with self.assertRaises(ValueError):
            _ExifReader("dummy")

        with self.assertRaises(ValueError):
            e = _ExifReader(b"Exif\x00\x00")
            e.get_info((100, 1, b"dummy"))

    def test_Exif(self):
        with self.assertRaises(ValueError):
            Exif(0)

        exif = Exif()
        self.assertDictEqual(exif, {})

        exif2 = Exif(exif.to_bytes())
        self.assertDictEqual(exif2, {})

    def test_load_jpg(self):
        f = io.BytesIO()
        exif = Exif(INPUT_FILE_JPG)
        im1 = Image.new("RGBA", (16, 16))
        im1.save(f, format="JPEG", exif=exif.to_bytes())
        f.seek(0)
        im2 = Image.open(f)
        im2.close()

    def test_load_tif(self):
        f = io.BytesIO()
        exif = Exif(INPUT_FILE_TIF)
        im1 = Image.new("RGBA", (16, 16))
        im1.save(f, format="JPEG", exif=exif.to_bytes())
        f.seek(0)
        im2 = Image.open(f)
        im2.close()

    def test_load_jpeg_on_memory(self):
        with open(INPUT_FILE_JPG, "rb") as f:
            data = f.read()
        f = io.BytesIO()
        exif = Exif(data)
        im1 = Image.new("RGBA", (16, 16))
        im1.save(f, format="JPEG", exif=exif.to_bytes())
        f.seek(0)
        im2 = Image.open(f)
        im2.close()

    def test_load_tif_on_memory(self):
        with open(INPUT_FILE_TIF, "rb") as f:
            data = f.read()
        f = io.BytesIO()
        exif = Exif(data)
        im1 = Image.new("RGBA", (16, 16))
        im1.save(f, format="JPEG", exif=exif.to_bytes())
        f.seek(0)
        im2 = Image.open(f)
        im2.close()


if __name__ == "__main__":
    unittest.main()
