# PDF Metadata Modifier / Watermark Adder
[![Generic badge](https://img.shields.io/badge/Python-3.8.16-blue.svg)](https://www.python.org/downloads/release/python-373/)
[![Generic badge](https://img.shields.io/badge/build-passing-GREEN.svg)]()
[![Generic badge](https://img.shields.io/badge/version-1.0-GREEN.svg)]()
[![Generic badge](https://img.shields.io/badge/Build-MacOS/Linux-GREEN.svg)]()
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/abaker2010/nightcap/blob/master/LICENSE)

This is a simple program that is a PoC for modification of the metadata on a pdf file and adding a watermark from text on to each page in the pdf file. 

## Metadata Modification 
There are a few options for modification of the metadata that exists on the original file
- Keep existing metadata
- Replace metadata

## Watermark 
Currently the watermark is being converted from text into a 'pdf' this is basically just an image that has the .pdf extension instead of .jpg/.png/etc. This allows for us to create the image, then trick the pdf library into reading in the file to then merge the image to each page of the pdf that we are trying to apply the watermark to. 

## Objects

### PDFMetadata
This object pretty simple, and does the heavy lifting of the modification of the metadata. The parameters are as follows: 
- `metadata: Dict[str, str]` - A dictionary representation of the new metadata that we would like to apply
- `originalPDF: str` - Original on Input PDF that we would like to modify the metadata of.
- `modifiedPDF: str` - Output PDF File that we would like to create when writing the new version of the PDF file with the modified metadata.
- `keepOriginalMetadata: bool (True)` - This boolean allows us to keep or discard the original metadata that was existing on the PDF before we started to modify the file. This defaults to True if not set.
### PDFWatermark 
This object has a single job and that is to go through the process of actually applying the watermark to the PDF file. The parameters are as follows: 
- `watermarkPDF: str` - The PDF file that contains the watermark that we would like to apply to each page in the PDF.
- `pdfFile: str` - This is the PDF that we would like to apply the watermark to. Since there is no reason to have the original PDF file when applying the watermark we are able to override this same file when saving the PDF.
### Watermark
This object creates the actual watermark, converting the text into an image that we are able to then use for the watermark.pdf file that would be applied to the modified PDF file. The parameters are as follows: 
- `watermarkText: str` - The text that we would like to convert into an image. Please note that as this is a PoC long text will cause the PDF to look distorted due to the lake of splitting the text into multiple lines to accommodate for the width/height of the PDF file. When using try to keep the text length short to avoid the issue.
- `watermarkPDF: str` - The name of the file for the watermark to be saved to.
- watermarkColor: (int, int, int, int) - Apply colorization to the watermark the orientation of the Tuple values follow the RGB color schema with the last being for the transparency. IE: (R, G, B, T)
- `watermarkFontPath: int` - The path to the otf or ttf file that needs to be applied to allow for the conversion.
- `watermarkFontSize: int` - This allows for scaling when taking the text and converting it into an image using the correct sizing from the otf/ttf file. 


## Installation
Simple installation, this program only requires a few packages to generate the modified PDF file. For the installation of the pip packages use the command below that fits your environment.

#### Virtual Env

`python -m pip install -r requirements.txt`

#### Default Installation

`python3 -m pip install -r requirements.txt`


## Usage
Since this is a PoC a lot of the information is hardcoded and can be found in the `pdfeditor.py` file under the region `User Modifiable Information`. 

## PDF Input/Output Location
All input/output PDF files can be found in the `pdf_files` folder.
The input file for the PoC is called `example.pdf` with nothing but 3 pages of test data. There are 2 PDF files that are created during the process `modified.pdf` (the final PDF file) and `watermark.pdf`. 

## Checking Metadata
During testing to check if the metadata had been modified by the program I used a tool called `exiftool`, allowing me to quickly investigate the `modified.pdf` files metadata. If you are interested in using this tool it can be found at https://exiftool.org