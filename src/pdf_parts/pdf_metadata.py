from typing import Dict
from pypdf import PdfReader, PdfWriter, DocumentInformation

class PDFMetadata(object):
    def __init__(self, metadata: Dict[str, str], originalPDF: str = "", modifiedPDF: str = "", 
                 keepOriginalMetadata: bool = True) -> None:
        self.metadata: Dict[str, str] = metadata
        self.modifiedPDF: str = modifiedPDF
        self.keepOriginalMetadata: bool = keepOriginalMetadata

        try:
            self.pdfFileReader = PdfReader(originalPDF)
        except Exception as e:
            raise Exception("ERROR READING PDF FILE :: %s" % (originalPDF))
        
        try:
            self.pdfFileWriter = PdfWriter()
        except Exception as e:
            raise Exception("ERROR CREATING PDF WRITER :: %s" % (e))
        

    def write(self):
        try:
            metadata = {}
            if self.keepOriginalMetadata:
                metadata = {**dict(self.read()), **self.metadata}
            else:
                metadata = self.metadata

            # region Adding pages to the writer
            for page in self.pdfFileReader.pages:
                self.pdfFileWriter.add_page(page)
            # endregion

            # region Writing Final PDF
            self.pdfFileWriter.add_metadata(metadata)
            with open(self.modifiedPDF, "wb") as file:
                self.pdfFileWriter.write(file)
            # endregion
        except Exception as e:
            raise Exception("ERROR WRITING METADATA TO FILE :: %s" % str(e))

    def read(self) -> DocumentInformation:
        try:
            return self.pdfFileReader.metadata
        except Exception as e:
            raise Exception("ERROR READING METADATA FROM FILE :: %s" % str(e))