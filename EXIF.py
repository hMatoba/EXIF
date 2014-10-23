import struct


TAGS = {
    'Image': {11: {'name': 'ProcessingSoftware', 'type': 'Ascii'},
              254: {'name': 'NewSubfileType', 'type': 'Long'},
              255: {'name': 'SubfileType', 'type': 'Short'},
              256: {'name': 'ImageWidth', 'type': 'Long'},
              257: {'name': 'ImageLength', 'type': 'Long'},
              258: {'name': 'BitsPerSample', 'type': 'Short'},
              259: {'name': 'Compression', 'type': 'Short'},
              262: {'name': 'PhotometricInterpretation', 'type': 'Short'},
              263: {'name': 'Threshholding', 'type': 'Short'},
              264: {'name': 'CellWidth', 'type': 'Short'},
              265: {'name': 'CellLength', 'type': 'Short'},
              266: {'name': 'FillOrder', 'type': 'Short'},
              269: {'name': 'DocumentName', 'type': 'Ascii'},
              270: {'name': 'ImageDescription', 'type': 'Ascii'},
              271: {'name': 'Make', 'type': 'Ascii'},
              272: {'name': 'Model', 'type': 'Ascii'},
              273: {'name': 'StripOffsets', 'type': 'Long'},
              274: {'name': 'Orientation', 'type': 'Short'},
              277: {'name': 'SamplesPerPixel', 'type': 'Short'},
              278: {'name': 'RowsPerStrip', 'type': 'Long'},
              279: {'name': 'StripByteCounts', 'type': 'Long'},
              282: {'name': 'XResolution', 'type': 'Rational'},
              283: {'name': 'YResolution', 'type': 'Rational'},
              284: {'name': 'PlanarConfiguration', 'type': 'Short'},
              290: {'name': 'GrayResponseUnit', 'type': 'Short'},
              291: {'name': 'GrayResponseCurve', 'type': 'Short'},
              292: {'name': 'T4Options', 'type': 'Long'},
              293: {'name': 'T6Options', 'type': 'Long'},
              296: {'name': 'ResolutionUnit', 'type': 'Short'},
              301: {'name': 'TransferFunction', 'type': 'Short'},
              305: {'name': 'Software', 'type': 'Ascii'},
              306: {'name': 'DateTime', 'type': 'Ascii'},
              315: {'name': 'Artist', 'type': 'Ascii'},
              316: {'name': 'HostComputer', 'type': 'Ascii'},
              317: {'name': 'Predictor', 'type': 'Short'},
              318: {'name': 'WhitePoint', 'type': 'Rational'},
              319: {'name': 'PrimaryChromaticities', 'type': 'Rational'},
              320: {'name': 'ColorMap', 'type': 'Short'},
              321: {'name': 'HalftoneHints', 'type': 'Short'},
              322: {'name': 'TileWidth', 'type': 'Short'},
              323: {'name': 'TileLength', 'type': 'Short'},
              324: {'name': 'TileOffsets', 'type': 'Short'},
              325: {'name': 'TileByteCounts', 'type': 'Short'},
              330: {'name': 'SubIFDs', 'type': 'Long'},
              332: {'name': 'InkSet', 'type': 'Short'},
              333: {'name': 'InkNames', 'type': 'Ascii'},
              334: {'name': 'NumberOfInks', 'type': 'Short'},
              336: {'name': 'DotRange', 'type': 'Byte'},
              337: {'name': 'TargetPrinter', 'type': 'Ascii'},
              338: {'name': 'ExtraSamples', 'type': 'Short'},
              339: {'name': 'SampleFormat', 'type': 'Short'},
              340: {'name': 'SMinSampleValue', 'type': 'Short'},
              341: {'name': 'SMaxSampleValue', 'type': 'Short'},
              342: {'name': 'TransferRange', 'type': 'Short'},
              343: {'name': 'ClipPath', 'type': 'Byte'},
              344: {'name': 'XClipPathUnits', 'type': 'Long'},
              345: {'name': 'YClipPathUnits', 'type': 'Long'},
              346: {'name': 'Indexed', 'type': 'Short'},
              347: {'name': 'JPEGTables', 'type': 'Undefined'},
              351: {'name': 'OPIProxy', 'type': 'Short'},
              512: {'name': 'JPEGProc', 'type': 'Long'},
              513: {'name': 'JPEGInterchangeFormat', 'type': 'Long'},
              514: {'name': 'JPEGInterchangeFormatLength', 'type': 'Long'},
              515: {'name': 'JPEGRestartInterval', 'type': 'Short'},
              517: {'name': 'JPEGLosslessPredictors', 'type': 'Short'},
              518: {'name': 'JPEGPointTransforms', 'type': 'Short'},
              519: {'name': 'JPEGQTables', 'type': 'Long'},
              520: {'name': 'JPEGDCTables', 'type': 'Long'},
              521: {'name': 'JPEGACTables', 'type': 'Long'},
              529: {'name': 'YCbCrCoefficients', 'type': 'Rational'},
              530: {'name': 'YCbCrSubSampling', 'type': 'Short'},
              531: {'name': 'YCbCrPositioning', 'type': 'Short'},
              532: {'name': 'ReferenceBlackWhite', 'type': 'Rational'},
              700: {'name': 'XMLPacket', 'type': 'Byte'},
              18246: {'name': 'Rating', 'type': 'Short'},
              18249: {'name': 'RatingPercent', 'type': 'Short'},
              32781: {'name': 'ImageID', 'type': 'Ascii'},
              33421: {'name': 'CFARepeatPatternDim', 'type': 'Short'},
              33422: {'name': 'CFAPattern', 'type': 'Byte'},
              33423: {'name': 'BatteryLevel', 'type': 'Rational'},
              33432: {'name': 'Copyright', 'type': 'Ascii'},
              33434: {'name': 'ExposureTime', 'type': 'Rational'},
              34377: {'name': 'ImageResources', 'type': 'Byte'},
              34665: {'name': 'ExifTag', 'type': 'Long'},
              34675: {'name': 'InterColorProfile', 'type': 'Undefined'},
              34853: {'name': 'GPSTag', 'type': 'Long'},
              34857: {'name': 'Interlace', 'type': 'Short'},
              34858: {'name': 'TimeZoneOffset', 'type': 'Long'},
              34859: {'name': 'SelfTimerMode', 'type': 'Short'},
              37387: {'name': 'FlashEnergy', 'type': 'Rational'},
              37388: {'name': 'SpatialFrequencyResponse', 'type': 'Undefined'},
              37389: {'name': 'Noise', 'type': 'Undefined'},
              37390: {'name': 'FocalPlaneXResolution', 'type': 'Rational'},
              37391: {'name': 'FocalPlaneYResolution', 'type': 'Rational'},
              37392: {'name': 'FocalPlaneResolutionUnit', 'type': 'Short'},
              37393: {'name': 'ImageNumber', 'type': 'Long'},
              37394: {'name': 'SecurityClassification', 'type': 'Ascii'},
              37395: {'name': 'ImageHistory', 'type': 'Ascii'},
              37397: {'name': 'ExposureIndex', 'type': 'Rational'},
              37398: {'name': 'TIFFEPStandardID', 'type': 'Byte'},
              37399: {'name': 'SensingMethod', 'type': 'Short'},
              40091: {'name': 'XPTitle', 'type': 'Byte'},
              40092: {'name': 'XPComment', 'type': 'Byte'},
              40093: {'name': 'XPAuthor', 'type': 'Byte'},
              40094: {'name': 'XPKeywords', 'type': 'Byte'},
              40095: {'name': 'XPSubject', 'type': 'Byte'},
              50341: {'name': 'PrintImageMatching', 'type': 'Undefined'},
              50706: {'name': 'DNGVersion', 'type': 'Byte'},
              50707: {'name': 'DNGBackwardVersion', 'type': 'Byte'},
              50708: {'name': 'UniqueCameraModel', 'type': 'Ascii'},
              50709: {'name': 'LocalizedCameraModel', 'type': 'Byte'},
              50710: {'name': 'CFAPlaneColor', 'type': 'Byte'},
              50711: {'name': 'CFALayout', 'type': 'Short'},
              50712: {'name': 'LinearizationTable', 'type': 'Short'},
              50713: {'name': 'BlackLevelRepeatDim', 'type': 'Short'},
              50714: {'name': 'BlackLevel', 'type': 'Rational'},
              50715: {'name': 'BlackLevelDeltaH', 'type': 'SRational'},
              50716: {'name': 'BlackLevelDeltaV', 'type': 'SRational'},
              50717: {'name': 'WhiteLevel', 'type': 'Short'},
              50718: {'name': 'DefaultScale', 'type': 'Rational'},
              50719: {'name': 'DefaultCropOrigin', 'type': 'Short'},
              50720: {'name': 'DefaultCropSize', 'type': 'Short'},
              50721: {'name': 'ColorMatrix1', 'type': 'SRational'},
              50722: {'name': 'ColorMatrix2', 'type': 'SRational'},
              50723: {'name': 'CameraCalibration1', 'type': 'SRational'},
              50724: {'name': 'CameraCalibration2', 'type': 'SRational'},
              50725: {'name': 'ReductionMatrix1', 'type': 'SRational'},
              50726: {'name': 'ReductionMatrix2', 'type': 'SRational'},
              50727: {'name': 'AnalogBalance', 'type': 'Rational'},
              50728: {'name': 'AsShotNeutral', 'type': 'Short'},
              50729: {'name': 'AsShotWhiteXY', 'type': 'Rational'},
              50730: {'name': 'BaselineExposure', 'type': 'SRational'},
              50731: {'name': 'BaselineNoise', 'type': 'Rational'},
              50732: {'name': 'BaselineSharpness', 'type': 'Rational'},
              50733: {'name': 'BayerGreenSplit', 'type': 'Long'},
              50734: {'name': 'LinearResponseLimit', 'type': 'Rational'},
              50735: {'name': 'CameraSerialNumber', 'type': 'Ascii'},
              50736: {'name': 'LensInfo', 'type': 'Rational'},
              50737: {'name': 'ChromaBlurRadius', 'type': 'Rational'},
              50738: {'name': 'AntiAliasStrength', 'type': 'Rational'},
              50739: {'name': 'ShadowScale', 'type': 'SRational'},
              50740: {'name': 'DNGPrivateData', 'type': 'Byte'},
              50741: {'name': 'MakerNoteSafety', 'type': 'Short'},
              50778: {'name': 'CalibrationIlluminant1', 'type': 'Short'},
              50779: {'name': 'CalibrationIlluminant2', 'type': 'Short'},
              50780: {'name': 'BestQualityScale', 'type': 'Rational'},
              50781: {'name': 'RawDataUniqueID', 'type': 'Byte'},
              50827: {'name': 'OriginalRawFileName', 'type': 'Byte'},
              50828: {'name': 'OriginalRawFileData', 'type': 'Undefined'},
              50829: {'name': 'ActiveArea', 'type': 'Short'},
              50830: {'name': 'MaskedAreas', 'type': 'Short'},
              50831: {'name': 'AsShotICCProfile', 'type': 'Undefined'},
              50832: {'name': 'AsShotPreProfileMatrix', 'type': 'SRational'},
              50833: {'name': 'CurrentICCProfile', 'type': 'Undefined'},
              50834: {'name': 'CurrentPreProfileMatrix', 'type': 'SRational'},
              50879: {'name': 'ColorimetricReference', 'type': 'Short'},
              50931: {'name': 'CameraCalibrationSignature', 'type': 'Byte'},
              50932: {'name': 'ProfileCalibrationSignature', 'type': 'Byte'},
              50934: {'name': 'AsShotProfileName', 'type': 'Byte'},
              50935: {'name': 'NoiseReductionApplied', 'type': 'Rational'},
              50936: {'name': 'ProfileName', 'type': 'Byte'},
              50937: {'name': 'ProfileHueSatMapDims', 'type': 'Long'},
              50938: {'name': 'ProfileHueSatMapData1', 'type': 'Float'},
              50939: {'name': 'ProfileHueSatMapData2', 'type': 'Float'},
              50940: {'name': 'ProfileToneCurve', 'type': 'Float'},
              50941: {'name': 'ProfileEmbedPolicy', 'type': 'Long'},
              50942: {'name': 'ProfileCopyright', 'type': 'Byte'},
              50964: {'name': 'ForwardMatrix1', 'type': 'SRational'},
              50965: {'name': 'ForwardMatrix2', 'type': 'SRational'},
              50966: {'name': 'PreviewApplicationName', 'type': 'Byte'},
              50967: {'name': 'PreviewApplicationVersion', 'type': 'Byte'},
              50968: {'name': 'PreviewSettingsName', 'type': 'Byte'},
              50969: {'name': 'PreviewSettingsDigest', 'type': 'Byte'},
              50970: {'name': 'PreviewColorSpace', 'type': 'Long'},
              50971: {'name': 'PreviewDateTime', 'type': 'Ascii'},
              50972: {'name': 'RawImageDigest', 'type': 'Undefined'},
              50973: {'name': 'OriginalRawFileDigest', 'type': 'Undefined'},
              50974: {'name': 'SubTileBlockSize', 'type': 'Long'},
              50975: {'name': 'RowInterleaveFactor', 'type': 'Long'},
              50981: {'name': 'ProfileLookTableDims', 'type': 'Long'},
              50982: {'name': 'ProfileLookTableData', 'type': 'Float'},
              51008: {'name': 'OpcodeList1', 'type': 'Undefined'},
              51009: {'name': 'OpcodeList2', 'type': 'Undefined'},
              51022: {'name': 'OpcodeList3', 'type': 'Undefined'}},
    'Photo': {33434: {'name': 'ExposureTime', 'type': 'Rational'},
              33437: {'name': 'FNumber', 'type': 'Rational'},
              34850: {'name': 'ExposureProgram', 'type': 'Short'},
              34852: {'name': 'SpectralSensitivity', 'type': 'Ascii'},
              34855: {'name': 'ISOSpeedRatings', 'type': 'Short'},
              34856: {'name': 'OECF', 'type': 'Undefined'},
              34864: {'name': 'SensitivityType', 'type': 'Short'},
              34865: {'name': 'StandardOutputSensitivity', 'type': 'Long'},
              34866: {'name': 'RecommendedExposureIndex', 'type': 'Long'},
              34867: {'name': 'ISOSpeed', 'type': 'Long'},
              34868: {'name': 'ISOSpeedLatitudeyyy', 'type': 'Long'},
              34869: {'name': 'ISOSpeedLatitudezzz', 'type': 'Long'},
              36864: {'name': 'ExifVersion', 'type': 'Undefined'},
              36867: {'name': 'DateTimeOriginal', 'type': 'Ascii'},
              36868: {'name': 'DateTimeDigitized', 'type': 'Ascii'},
              37121: {'name': 'ComponentsConfiguration', 'type': 'Undefined'},
              37122: {'name': 'CompressedBitsPerPixel', 'type': 'Rational'},
              37377: {'name': 'ShutterSpeedValue', 'type': 'SRational'},
              37378: {'name': 'ApertureValue', 'type': 'Rational'},
              37379: {'name': 'BrightnessValue', 'type': 'SRational'},
              37380: {'name': 'ExposureBiasValue', 'type': 'SRational'},
              37381: {'name': 'MaxApertureValue', 'type': 'Rational'},
              37382: {'name': 'SubjectDistance', 'type': 'Rational'},
              37383: {'name': 'MeteringMode', 'type': 'Short'},
              37384: {'name': 'LightSource', 'type': 'Short'},
              37385: {'name': 'Flash', 'type': 'Short'},
              37386: {'name': 'FocalLength', 'type': 'Rational'},
              37396: {'name': 'SubjectArea', 'type': 'Short'},
              37500: {'name': 'MakerNote', 'type': 'Undefined'},
              37510: {'name': 'UserComment', 'type': 'Ascii'},
              37520: {'name': 'SubSecTime', 'type': 'Ascii'},
              37521: {'name': 'SubSecTimeOriginal', 'type': 'Ascii'},
              37522: {'name': 'SubSecTimeDigitized', 'type': 'Ascii'},
              40960: {'name': 'FlashpixVersion', 'type': 'Undefined'},
              40961: {'name': 'ColorSpace', 'type': 'Short'},
              40962: {'name': 'PixelXDimension', 'type': 'Long'},
              40963: {'name': 'PixelYDimension', 'type': 'Long'},
              40964: {'name': 'RelatedSoundFile', 'type': 'Ascii'},
              40965: {'name': 'InteroperabilityTag', 'type': 'Long'},
              41483: {'name': 'FlashEnergy', 'type': 'Rational'},
              41484: {'name': 'SpatialFrequencyResponse', 'type': 'Undefined'},
              41486: {'name': 'FocalPlaneXResolution', 'type': 'Rational'},
              41487: {'name': 'FocalPlaneYResolution', 'type': 'Rational'},
              41488: {'name': 'FocalPlaneResolutionUnit', 'type': 'Short'},
              41492: {'name': 'SubjectLocation', 'type': 'Short'},
              41493: {'name': 'ExposureIndex', 'type': 'Rational'},
              41495: {'name': 'SensingMethod', 'type': 'Short'},
              41728: {'name': 'FileSource', 'type': 'Undefined'},
              41729: {'name': 'SceneType', 'type': 'Undefined'},
              41730: {'name': 'CFAPattern', 'type': 'Undefined'},
              41985: {'name': 'CustomRendered', 'type': 'Short'},
              41986: {'name': 'ExposureMode', 'type': 'Short'},
              41987: {'name': 'WhiteBalance', 'type': 'Short'},
              41988: {'name': 'DigitalZoomRatio', 'type': 'Rational'},
              41989: {'name': 'FocalLengthIn35mmFilm', 'type': 'Short'},
              41990: {'name': 'SceneCaptureType', 'type': 'Short'},
              41991: {'name': 'GainControl', 'type': 'Short'},
              41992: {'name': 'Contrast', 'type': 'Short'},
              41993: {'name': 'Saturation', 'type': 'Short'},
              41994: {'name': 'Sharpness', 'type': 'Short'},
              41995: {'name': 'DeviceSettingDescription', 'type': 'Undefined'},
              41996: {'name': 'SubjectDistanceRange', 'type': 'Short'},
              42016: {'name': 'ImageUniqueID', 'type': 'Ascii'},
              42032: {'name': 'CameraOwnerName', 'type': 'Ascii'},
              42033: {'name': 'BodySerialNumber', 'type': 'Ascii'},
              42034: {'name': 'LensSpecification', 'type': 'Rational'},
              42035: {'name': 'LensMake', 'type': 'Ascii'},
              42036: {'name': 'LensModel', 'type': 'Ascii'},
              42037: {'name': 'LensSerialNumber', 'type': 'Ascii'}},
    'GPSInfo': {0: {'name': 'GPSVersionID', 'type': 'Byte'},
                1: {'name': 'GPSLatitudeRef', 'type': 'Ascii'},
                2: {'name': 'GPSLatitude', 'type': 'Rational'},
                3: {'name': 'GPSLongitudeRef', 'type': 'Ascii'},
                4: {'name': 'GPSLongitude', 'type': 'Rational'},
                5: {'name': 'GPSAltitudeRef', 'type': 'Byte'},
                6: {'name': 'GPSAltitude', 'type': 'Rational'},
                7: {'name': 'GPSTimeStamp', 'type': 'Rational'},
                8: {'name': 'GPSSatellites', 'type': 'Ascii'},
                9: {'name': 'GPSStatus', 'type': 'Ascii'},
                10: {'name': 'GPSMeasureMode', 'type': 'Ascii'},
                11: {'name': 'GPSDOP', 'type': 'Rational'},
                12: {'name': 'GPSSpeedRef', 'type': 'Ascii'},
                13: {'name': 'GPSSpeed', 'type': 'Rational'},
                14: {'name': 'GPSTrackRef', 'type': 'Ascii'},
                15: {'name': 'GPSTrack', 'type': 'Rational'},
                16: {'name': 'GPSImgDirectionRef', 'type': 'Ascii'},
                17: {'name': 'GPSImgDirection', 'type': 'Rational'},
                18: {'name': 'GPSMapDatum', 'type': 'Ascii'},
                19: {'name': 'GPSDestLatitudeRef', 'type': 'Ascii'},
                20: {'name': 'GPSDestLatitude', 'type': 'Rational'},
                21: {'name': 'GPSDestLongitudeRef', 'type': 'Ascii'},
                22: {'name': 'GPSDestLongitude', 'type': 'Rational'},
                23: {'name': 'GPSDestBearingRef', 'type': 'Ascii'},
                24: {'name': 'GPSDestBearing', 'type': 'Rational'},
                25: {'name': 'GPSDestDistanceRef', 'type': 'Ascii'},
                26: {'name': 'GPSDestDistance', 'type': 'Rational'},
                27: {'name': 'GPSProcessingMethod', 'type': 'Undefined'},
                28: {'name': 'GPSAreaInformation', 'type': 'Undefined'},
                29: {'name': 'GPSDateStamp', 'type': 'Ascii'},
                30: {'name': 'GPSDifferential', 'type': 'Short'}},
}


class ImageGroup:
    """Exif tag number reference - 0th IFD"""
    ProcessingSoftware = 11
    NewSubfileType = 254
    SubfileType = 255
    ImageWidth = 256
    ImageLength = 257
    BitsPerSample = 258
    Compression = 259
    PhotometricInterpretation = 262
    Threshholding = 263
    CellWidth = 264
    CellLength = 265
    FillOrder = 266
    DocumentName = 269
    ImageDescription = 270
    Make = 271
    Model = 272
    StripOffsets = 273
    Orientation = 274
    SamplesPerPixel = 277
    RowsPerStrip = 278
    StripByteCounts = 279
    XResolution = 282
    YResolution = 283
    PlanarConfiguration = 284
    GrayResponseUnit = 290
    GrayResponseCurve = 291
    T4Options = 292
    T6Options = 293
    ResolutionUnit = 296
    TransferFunction = 301
    Software = 305
    DateTime = 306
    Artist = 315
    HostComputer = 316
    Predictor = 317
    WhitePoint = 318
    PrimaryChromaticities = 319
    ColorMap = 320
    HalftoneHints = 321
    TileWidth = 322
    TileLength = 323
    TileOffsets = 324
    TileByteCounts = 325
    SubIFDs = 330
    InkSet = 332
    InkNames = 333
    NumberOfInks = 334
    DotRange = 336
    TargetPrinter = 337
    ExtraSamples = 338
    SampleFormat = 339
    SMinSampleValue = 340
    SMaxSampleValue = 341
    TransferRange = 342
    ClipPath = 343
    XClipPathUnits = 344
    YClipPathUnits = 345
    Indexed = 346
    JPEGTables = 347
    OPIProxy = 351
    JPEGProc = 512
    JPEGInterchangeFormat = 513
    JPEGInterchangeFormatLength = 514
    JPEGRestartInterval = 515
    JPEGLosslessPredictors = 517
    JPEGPointTransforms = 518
    JPEGQTables = 519
    JPEGDCTables = 520
    JPEGACTables = 521
    YCbCrCoefficients = 529
    YCbCrSubSampling = 530
    YCbCrPositioning = 531
    ReferenceBlackWhite = 532
    XMLPacket = 700
    Rating = 18246
    RatingPercent = 18249
    ImageID = 32781
    CFARepeatPatternDim = 33421
    CFAPattern = 33422
    BatteryLevel = 33423
    Copyright = 33432
    ExposureTime = 33434
    ImageResources = 34377
    ExifTag = 34665
    InterColorProfile = 34675
    GPSTag = 34853
    Interlace = 34857
    TimeZoneOffset = 34858
    SelfTimerMode = 34859
    FlashEnergy = 37387
    SpatialFrequencyResponse = 37388
    Noise = 37389
    FocalPlaneXResolution = 37390
    FocalPlaneYResolution = 37391
    FocalPlaneResolutionUnit = 37392
    ImageNumber = 37393
    SecurityClassification = 37394
    ImageHistory = 37395
    ExposureIndex = 37397
    TIFFEPStandardID = 37398
    SensingMethod = 37399
    XPTitle = 40091
    XPComment = 40092
    XPAuthor = 40093
    XPKeywords = 40094
    XPSubject = 40095
    PrintImageMatching = 50341
    DNGVersion = 50706
    DNGBackwardVersion = 50707
    UniqueCameraModel = 50708
    LocalizedCameraModel = 50709
    CFAPlaneColor = 50710
    CFALayout = 50711
    LinearizationTable = 50712
    BlackLevelRepeatDim = 50713
    BlackLevel = 50714
    BlackLevelDeltaH = 50715
    BlackLevelDeltaV = 50716
    WhiteLevel = 50717
    DefaultScale = 50718
    DefaultCropOrigin = 50719
    DefaultCropSize = 50720
    ColorMatrix1 = 50721
    ColorMatrix2 = 50722
    CameraCalibration1 = 50723
    CameraCalibration2 = 50724
    ReductionMatrix1 = 50725
    ReductionMatrix2 = 50726
    AnalogBalance = 50727
    AsShotNeutral = 50728
    AsShotWhiteXY = 50729
    BaselineExposure = 50730
    BaselineNoise = 50731
    BaselineSharpness = 50732
    BayerGreenSplit = 50733
    LinearResponseLimit = 50734
    CameraSerialNumber = 50735
    LensInfo = 50736
    ChromaBlurRadius = 50737
    AntiAliasStrength = 50738
    ShadowScale = 50739
    DNGPrivateData = 50740
    MakerNoteSafety = 50741
    CalibrationIlluminant1 = 50778
    CalibrationIlluminant2 = 50779
    BestQualityScale = 50780
    RawDataUniqueID = 50781
    OriginalRawFileName = 50827
    OriginalRawFileData = 50828
    ActiveArea = 50829
    MaskedAreas = 50830
    AsShotICCProfile = 50831
    AsShotPreProfileMatrix = 50832
    CurrentICCProfile = 50833
    CurrentPreProfileMatrix = 50834
    ColorimetricReference = 50879
    CameraCalibrationSignature = 50931
    ProfileCalibrationSignature = 50932
    AsShotProfileName = 50934
    NoiseReductionApplied = 50935
    ProfileName = 50936
    ProfileHueSatMapDims = 50937
    ProfileHueSatMapData1 = 50938
    ProfileHueSatMapData2 = 50939
    ProfileToneCurve = 50940
    ProfileEmbedPolicy = 50941
    ProfileCopyright = 50942
    ForwardMatrix1 = 50964
    ForwardMatrix2 = 50965
    PreviewApplicationName = 50966
    PreviewApplicationVersion = 50967
    PreviewSettingsName = 50968
    PreviewSettingsDigest = 50969
    PreviewColorSpace = 50970
    PreviewDateTime = 50971
    RawImageDigest = 50972
    OriginalRawFileDigest = 50973
    SubTileBlockSize = 50974
    RowInterleaveFactor = 50975
    ProfileLookTableDims = 50981
    ProfileLookTableData = 50982
    OpcodeList1 = 51008
    OpcodeList2 = 51009
    OpcodeList3 = 51022
    NoiseProfile = 51041


class PhotoGroup:
    """Exif tag number reference - Exif IFD"""
    ExposureTime = 33434
    FNumber = 33437
    ExposureProgram = 34850
    SpectralSensitivity = 34852
    ISOSpeedRatings = 34855
    OECF = 34856
    SensitivityType = 34864
    StandardOutputSensitivity = 34865
    RecommendedExposureIndex = 34866
    ISOSpeed = 34867
    ISOSpeedLatitudeyyy = 34868
    ISOSpeedLatitudezzz = 34869
    ExifVersion = 36864
    DateTimeOriginal = 36867
    DateTimeDigitized = 36868
    ComponentsConfiguration = 37121
    CompressedBitsPerPixel = 37122
    ShutterSpeedValue = 37377
    ApertureValue = 37378
    BrightnessValue = 37379
    ExposureBiasValue = 37380
    MaxApertureValue = 37381
    SubjectDistance = 37382
    MeteringMode = 37383
    LightSource = 37384
    Flash = 37385
    FocalLength = 37386
    SubjectArea = 37396
    MakerNote = 37500
    UserComment = 37510
    SubSecTime = 37520
    SubSecTimeOriginal = 37521
    SubSecTimeDigitized = 37522
    FlashpixVersion = 40960
    ColorSpace = 40961
    PixelXDimension = 40962
    PixelYDimension = 40963
    RelatedSoundFile = 40964
    InteroperabilityTag = 40965
    FlashEnergy = 41483
    SpatialFrequencyResponse = 41484
    FocalPlaneXResolution = 41486
    FocalPlaneYResolution = 41487
    FocalPlaneResolutionUnit = 41488
    SubjectLocation = 41492
    ExposureIndex = 41493
    SensingMethod = 41495
    FileSource = 41728
    SceneType = 41729
    CFAPattern = 41730
    CustomRendered = 41985
    ExposureMode = 41986
    WhiteBalance = 41987
    DigitalZoomRatio = 41988
    FocalLengthIn35mmFilm = 41989
    SceneCaptureType = 41990
    GainControl = 41991
    Contrast = 41992
    Saturation = 41993
    Sharpness = 41994
    DeviceSettingDescription = 41995
    SubjectDistanceRange = 41996
    ImageUniqueID = 42016
    CameraOwnerName = 42032
    BodySerialNumber = 42033
    LensSpecification = 42034
    LensMake = 42035
    LensModel = 42036
    LensSerialNumber = 42037


class GPSGroup:
    """Exif tag number reference - GPS IFD"""
    GPSVersionID = 0
    GPSLatitudeRef = 1
    GPSLatitude = 2
    GPSLongitudeRef = 3
    GPSLongitude = 4
    GPSAltitudeRef = 5
    GPSAltitude = 6
    GPSTimeStamp = 7
    GPSSatellites = 8
    GPSStatus = 9
    GPSMeasureMode = 10
    GPSDOP = 11
    GPSSpeedRef = 12
    GPSSpeed = 13
    GPSTrackRef = 14
    GPSTrack = 15
    GPSImgDirectionRef = 16
    GPSImgDirection = 17
    GPSMapDatum = 18
    GPSDestLatitudeRef = 19
    GPSDestLatitude = 20
    GPSDestLongitudeRef = 21
    GPSDestLongitude = 22
    GPSDestBearingRef = 23
    GPSDestBearing = 24
    GPSDestDistanceRef = 25
    GPSDestDistance = 26
    GPSProcessingMethod = 27
    GPSAreaInformation = 28
    GPSDateStamp = 29
    GPSDifferential = 30


TYPES = {"Byte": 1,
         "Ascii": 2,
         "Short": 3,
         "Long": 4,
         "Rational": 5,
         "Undefined": 7,
         "SLong": 9,
         "SRational": 10}


EXIF_POINTER = 34665


GPS_POINTER = 34853


class _ExifReader(object):
    LITTLE_ENDIAN = b"\x49\x49"

    def __init__(self, data):
        if data[0: 6] == b"Exif\x00\x00":
            self.exif_str = data[6:]
            endian = self.exif_str[0:2]
            if endian == self.LITTLE_ENDIAN:
                self.endian_mark = "<"
            else:
                self.endian_mark = ">"
        else:
            raise ValueError("Given data in not Exif")

    def get_exif(self):
        exif_dict = {}
        gps_dict = {}

        pointer = struct.unpack(self.endian_mark + "L", self.exif_str[4:8])[0]
        zeroth_dict = self.get_ifd_dict(pointer)

        if EXIF_POINTER in zeroth_dict:
            pointer = struct.unpack(self.endian_mark + "L",
                                    zeroth_dict[EXIF_POINTER][2])[0]
            exif_dict = self.get_ifd_dict(pointer)

        if GPS_POINTER in zeroth_dict:
            pointer = struct.unpack(self.endian_mark + "L",
                                    zeroth_dict[GPS_POINTER][2])[0]
            gps_dict = self.get_ifd_dict(pointer)

        return zeroth_dict, exif_dict, gps_dict

    def get_ifd_dict(self, pointer):
        ifd_dict = {}
        tag_count = struct.unpack(self.endian_mark + "H",
                                  self.exif_str[pointer: pointer+2])[0]
        offset = pointer + 2
        for x in range(tag_count):
            pointer = offset + 12 * x
            tag_code = struct.unpack(
                self.endian_mark + "H",
                self.exif_str[pointer: pointer+2])[0]
            value_type = struct.unpack(
                self.endian_mark + "H",
                self.exif_str[pointer + 2: pointer + 4])[0]
            value_num = struct.unpack(
                self.endian_mark + "L",
                self.exif_str[pointer + 4: pointer + 8])[0]
            value = self.exif_str[pointer+8: pointer+12]
            # print(tag_code, [value_type, value_num, value])
            ifd_dict.update({tag_code: [value_type, value_num, value]})
        return ifd_dict

    def get_info(self, val):
        data = None

        if val[0] == 1:  # BYTE
            if not isinstance(val[2][0], int):
                data = int(val[2][0].encode("hex"), 16)
            else:
                data = val[2][0]
        elif val[0] == 2:  # ASCII
            if val[1] > 4:
                pointer = struct.unpack(self.endian_mark + "L", val[2])[0]
                data = self.exif_str[pointer: pointer+val[1] - 1]
            else:
                data = val[2][0: val[1] - 1]
            try:
                data = data.decode()
            except:
                pass
        elif val[0] == 3:  # SHORT
            data = struct.unpack(self.endian_mark + "H", val[2][0:2])[0]
        elif val[0] == 4:  # LONG
            data = struct.unpack(self.endian_mark + "L", val[2])[0]
        elif val[0] == 5:  # RATIONAL
            pointer = struct.unpack(self.endian_mark + "L", val[2])[0]
            length = val[1]
            if length > 1:
                data = tuple(
                    (struct.unpack(self.endian_mark + "L", self.exif_str[pointer + x * 8: pointer + 4 + x * 8])[0],
                     struct.unpack(self.endian_mark + "L", self.exif_str[pointer + 4 + x * 8: pointer + 8 + x * 8])[0])
                    for x in range(val[1])
                )
            else:
                data = (
                    struct.unpack(self.endian_mark + "L",
                                  self.exif_str[pointer: pointer + 4])[0],
                    struct.unpack(self.endian_mark + "L",
                                  self.exif_str[pointer + 4: pointer + 8])[0])
        elif val[0] == 7:  # UNDEFINED BYTES
            if val[1] > 4:
                pointer = struct.unpack(self.endian_mark + "L", val[2])[0]
                data = self.exif_str[pointer: pointer+val[1]]
            else:
                data = val[2][0: val[1]]
        elif val[0] == 9:  # SLONG
            data = struct.unpack(self.endian_mark + "l", val[2])[0]
        elif val[0] == 10:  # SRATIONAL
            pointer = struct.unpack(self.endian_mark + "L", val[2])[0]
            data = (struct.unpack(self.endian_mark + "l",
                                  self.exif_str[pointer: pointer + 4])[0],
                    struct.unpack(self.endian_mark + "l",
                                  self.exif_str[pointer + 4: pointer + 8])[0])

        return data


class Exif(dict):
    """Use like dict
    exif = Exif()
    exif[271] = "Sony"
    """
    TIFF_HEADER_LENGTH = 8

    def __init__(self, data=None):
        pass
        if isinstance(data, (bytes, str)):
            self.load(data)
        elif isinstance(data, dict):
            self.update(data)
        elif data is None:
            pass
        else:
            raise ValueError("To initialize, pass a bytes, dict or nothing.")

    def to_bytes(self):
        """Returns exif bytes
        """
        zeroth_ifd, exif_ifd, gps_ifd = self._split_ifd()
        header = b"\x45\x78\x69\x66\x00\x00\x4d\x4d\x00\x2a\x00\x00\x00\x08"
        exif_is = False
        gps_is = False

        if len(exif_ifd):
            zeroth_ifd.update({34665: 1})
            exif_is = True
        if len(gps_ifd):
            zeroth_ifd.update({34853: 1})
            gps_is = True

        zeroth_set = self._dict_to_bytes(zeroth_ifd, "Image", 0)
        zeroth_length = (len(zeroth_set[0]) + exif_is * 12 + gps_is * 12 + 4 +
                         len(zeroth_set[1]))

        if exif_is:
            exif_set = self._dict_to_bytes(exif_ifd, "Photo", zeroth_length)
            exif_bytes = b"".join(exif_set)
            exif_length = len(exif_bytes)
        else:
            exif_bytes = b""
            exif_length = 0
        if gps_is:
            gps_set = self._dict_to_bytes(gps_ifd, "GPSInfo",
                                          zeroth_length + exif_length)
            gps_bytes = b"".join(gps_set)
            gps_length = len(gps_bytes)
        else:
            gps_bytes = b""
            gps_length = 0

        if exif_is:
            pointer_value = self.TIFF_HEADER_LENGTH + zeroth_length
            pointer_str = struct.pack(">I", pointer_value)
            key = 34665
            key_str = struct.pack(">H", key)
            type_str = struct.pack(">H", TYPES["Long"])
            length_str = struct.pack(">I", 1)
            exif_pointer = key_str + type_str + length_str + pointer_str
        else:
            exif_pointer = b""
        if gps_is:
            pointer_value = (self.TIFF_HEADER_LENGTH + zeroth_length +
                             exif_length)
            pointer_str = struct.pack(">I", pointer_value)
            key = 34853
            key_str = struct.pack(">H", key)
            type_str = struct.pack(">H", TYPES["Long"])
            length_str = struct.pack(">I", 1)
            gps_pointer = key_str + type_str + length_str + pointer_str
        else:
            gps_pointer = b""
        zeroth_bytes = (zeroth_set[0] + exif_pointer + gps_pointer +
                        b"\x00\x00\x00\x00" + zeroth_set[1])

        return header + zeroth_bytes + exif_bytes + gps_bytes

    def load(self, input_data):
        """Loads exif as dict from exif bytes
        """
        exif_reader = _ExifReader(input_data)
        zeroth_ifd, exif_ifd, gps_ifd = exif_reader.get_exif()
        zeroth_dict = dict((key, exif_reader.get_info(zeroth_ifd[key]))
                           for key in zeroth_ifd if key in TAGS["Image"])
        exif_dict = dict((key, exif_reader.get_info(exif_ifd[key]))
                         for key in exif_ifd if key in TAGS["Photo"])
        gps_dict = dict((key, exif_reader.get_info(gps_ifd[key]))
                        for key in gps_ifd if key in TAGS["GPSInfo"])

        if len(exif_dict):
            # zeroth_dict.pop(EXIF_POINTER)
            zeroth_dict.update(exif_dict)
        if len(gps_dict):
            zeroth_dict.update({GPS_POINTER: gps_dict})
        self.clear()
        self.update(zeroth_dict)

    def _split_ifd(self):
        exif_dict = self
        zeroth_ifd = dict((key, exif_dict[key])
                          for key in exif_dict if key in TAGS["Image"])
        exif_ifd = dict((key, exif_dict[key])
                        for key in exif_dict if key in TAGS["Photo"])
        gps_ifd = zeroth_ifd[GPS_POINTER] if GPS_POINTER in zeroth_ifd else {}
        return zeroth_ifd, exif_ifd, gps_ifd

    def _dict_to_bytes(self, ifd_dict, name, ifd_offset):
        exif_ifd_is = False
        gps_ifd_is = False
        tag_count = len(ifd_dict)
        entry_header = struct.pack(">H", tag_count)
        if name == "Image":
            entries_length = 2 + tag_count * 12 + 4
        else:
            entries_length = 2 + tag_count * 12
        entries = b""
        values = b""

        for n, key in enumerate(sorted(ifd_dict)):
            if key == 34665:
                exif_ifd_is = True
                continue
            elif key == 34853:
                gps_ifd_is = True
                continue

            raw_value = ifd_dict[key]
            key_str = struct.pack(">H", key)
            value_type = TAGS[name][key]["type"]
            type_str = struct.pack(">H", TYPES[value_type])
            if value_type == "Byte":
                length = 1
                value_str = struct.pack('>B', raw_value)[0:1] + b"\x00" * 3
            elif value_type == "Short":
                length = 2
                value_str = struct.pack('>H', raw_value)[0:2] + b"\x00" * 2
            elif value_type == "Long":
                length = 1
                value_str = struct.pack('>L', raw_value)
            elif value_type == "SLong":
                length = 1
                value_str = struct.pack('>l', raw_value)
            elif value_type == "Ascii":
                new_value = raw_value.encode() + b"\x00"
                length = len(new_value)
                if length > 4:
                    offset = (self.TIFF_HEADER_LENGTH + ifd_offset +
                              entries_length + len(values))
                    value_str = struct.pack(">I", offset)
                    values += new_value
                else:
                    value_str = new_value
            elif value_type == "Rational":
                length = 1
                num, den = raw_value
                new_value = struct.pack(">L", num) + struct.pack(">L", den)
                offset = (self.TIFF_HEADER_LENGTH + ifd_offset +
                          entries_length + len(values))
                value_str = struct.pack(">I", offset)
                values += new_value
            elif value_type == "SRational":
                length = 1
                num, den = raw_value
                new_value = struct.pack(">l", num) + struct.pack(">l", den)
                offset = (self.TIFF_HEADER_LENGTH + ifd_offset +
                          entries_length + len(values))
                value_str = struct.pack(">I", offset)
                values += new_value
            elif value_type == "Undefined":
                new_value = raw_value.encode()
                length = len(new_value)
                if len(raw_value) > 4:
                    offset = (self.TIFF_HEADER_LENGTH + ifd_offset +
                              entries_length + len(values))
                    value_str = struct.pack(">I", offset)
                    values += new_value
                else:
                    value_str = new_value

            length_str = struct.pack(">I", length)
            entries += key_str + type_str + length_str + value_str
        return (entry_header + entries, values)
