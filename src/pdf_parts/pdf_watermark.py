from reportlab.pdfgen.canvas import Canvas
from pypdf import PdfReader, PdfWriter, Transformation

class PDFWatermark(object):
    def __init__(self, watermarkPDF: str, 
                 pdfFile: str = "") -> None:
        self.watermarkPDF: str = watermarkPDF
        self.pdfFile: str = pdfFile
        

    def applyWatermark(self):
        try:
            watermark = PdfReader(open(self.watermarkPDF, "rb")).pages[0]
            output_file = PdfWriter()
            input_file = PdfReader(open(self.pdfFile, "rb"))
            
            # region Adding pages to the writer
            for page in input_file.pages:
                output_file.add_page(page)
            # endregion

            for page in output_file.pages:
                page.merge_transformed_page(
                    watermark,
                    Transformation().rotate(45.0).scale(2),
                    expand=True
                )

            with open(self.pdfFile, "wb") as file:
                output_file.write(file)
        except Exception as e:
            raise Exception("ERROR APPLYING WATERMARK TO PDF :: %s" % (str(e)))
        
