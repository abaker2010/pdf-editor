from typing import Dict
import shutil
from pypdf import DocumentInformation
from src.pdf_parts.pdf_metadata import PDFMetadata
from src.pdf_parts.pdf_watermark import PDFWatermark
from src.pdf_parts.watermark import Watermark

if __name__ == "__main__":
    try:
        # region User Modifiable Information
        metadata: Dict[str, str] = {
            "/UserID" : "So User ID Here"
        }

        originalFileName: str = "./pdf_files/example.pdf"
        modifiedFileName: str = "./pdf_files/modified.pdf"
        watermarkPDF: str = "./pdf_files/watermark.pdf"

        watermarkFontSize: int = 36
        watermarkFontPath: str = "./font/MesloLGS NF Regular.ttf"
        # watermarkColor: (int, int, int, int) = (238, 238, 238, 10)
        watermarkColor: (int, int, int, int) = (0, 0, 0, 40)
        watermarkText: str = "UserID Here"
        # endregion


        print("[+] Creating copy of original file to apply changes")
        shutil.copyfile(originalFileName, modifiedFileName)
        print("[✓] Created new file :: %s" % (str(modifiedFileName)))



        # region Create the watermark image
        waterMark = Watermark(watermarkText=watermarkText, watermarkPDF=watermarkPDF,
                              watermarkColor=watermarkColor, watermarkFontPath=watermarkFontPath,
                              watermarkFontSize=watermarkFontSize)
        waterMark.create_watermark()
        # endregion

        # region Apply watermark image to pdf
        print("\n\n[-] Applying custom watermark (%s) to PDF :: %s" % (str(watermarkPDF), str(modifiedFileName)))
        pdfWatermark: PDFWatermark = PDFWatermark(watermarkPDF=watermarkPDF, pdfFile=modifiedFileName)
        pdfWatermark.applyWatermark()
        print("\n[✓] Applied watermark to modified file :: %s" % (str(modifiedFileName)))
        # endregion

        # region Apply custom metadata to pdf
        pdfFile = PDFMetadata(metadata=metadata, originalPDF=modifiedFileName, modifiedPDF=modifiedFileName, keepOriginalMetadata=True)
        originalMetadata: DocumentInformation = pdfFile.read()

        print("[-] Original metadata from file :: %s" % (str(modifiedFileName)))
        for k, v in originalMetadata.items():
            key_cleaned = str(k).replace("/", "")
            print("\t[+] %s : %s" % (key_cleaned, v))

        print("\n[-] Metadata to write to file")
        for k, v in metadata.items():
            print("\t[+] %s : %s" % (str(k), str(v)))

        print("\n[-] Writing new file :: %s" % (str(modifiedFileName)))
        pdfFile.write()

        print("\n[-] New metadata on file :: %s" % (str(modifiedFileName)))
        pdfModifiedFile = PDFMetadata(metadata=metadata, originalPDF=modifiedFileName, modifiedPDF="")
        modifiedMetadata: DocumentInformation = pdfModifiedFile.read()
        for k, v in modifiedMetadata.items():
            key_cleaned = str(k).replace("/", "")
            print("\t[+] %s : %s" % (key_cleaned, v))

        print("\n[✓] Applied modified metadata to modified file :: %s" % (str(modifiedFileName)))
        # endregion
        
       
        
    except Exception as e:
        print(e)