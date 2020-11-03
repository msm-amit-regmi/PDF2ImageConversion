# PDF2ImageConversion
This project is about conversion of PDF file to Image format (jpg, png, jpeg).

# Installation
1. pip install pdf2image (reference: https://pypi.org/project/pdf2image/0.1.4/)
3. conda install -c conda-forge poppler (for anaconda users)
2. Library wraped by python as pdf2image
  i. https://poppler.freedesktop.org/
  ii. https://sourceforge.net/projects/poppler-win32/

# Introduction
pdftoimage is the piece of software that does the actual magic. It is distributed as part of a greater package called poppler. Testing results are here: https://tickets.tools.misumi.jp/confluence/display/3D2MPROJECT/3.5.2+2D+PDF+Analysis+Web+Service
  
# Test results for PDF2JPEG:
i. A4 PDF drawings → 600 DPI Resolution JPG image → 19 seconds.

ii. A4 PDF drawings → 300 DPI Resolution JPG image → 6.83 seconds.

iii. A4 PDF drawings → 200 DPI Resolution JPG image → 3 seconds.

iv. A4 PDF drawings → 150 DPI Resolution JPG image → 1.5 seconds.

# Test results for PDF2PNG:

i. A4 PDF drawings → 300 DPI Resolution PNG image → 6.8 seconds.

ii. A4 PDF drawings → 200 DPI Resolution JPG image → 3 seconds.

iii. A4 PDF drawings → 150 DPI Resolution JPG image → 1.4 seconds.

# Reference
i. https://simply-python.com/tag/pdf2image/

ii. https://stackoverflow.com/questions/46184239/extract-a-page-from-a-pdf-as-a-jpeg

iii. https://github.com/Belval/pdf2image

