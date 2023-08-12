from typing import List, Dict
from PIL import Image, ImageFont

class Watermark(object):
    def __init__(self, watermarkText: str, 
                 watermarkPDF: str = "", 
                 watermarkColor: (int, int, int, int) = (238, 238, 238, 10),
                 watermarkFontPath: str = "",
                 watermarkFontSize: int = 36) -> None:
        self.watermarkText: str = watermarkText
        self.watermarkPDF: str = watermarkPDF
        self.watermarkColor: (int, int, int, int) = watermarkColor
        self.watermarkFontPath: str = watermarkFontPath
        self.watermarkFontSize: int = watermarkFontSize

    # This will return the path to the watermark that was created
    def create_watermark(self):
        try:
            font = ImageFont.truetype(self.watermarkFontPath, size=self.watermarkFontSize)
            mask_image = font.getmask(self.watermarkText, "L")
            img = Image.new("RGBA", mask_image.size)
            img.im.paste(self.watermarkColor, (0, 0) + mask_image.size, mask_image)  # need to use the inner `img.im.paste` due to `getmask` returning a core
            img.save(self.watermarkPDF)

        except Exception as e:
            raise Exception("ERROR CREATING WATERMARK IMAGE :: %s" % (str(e)))
        