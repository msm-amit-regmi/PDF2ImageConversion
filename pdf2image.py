import os
import time
from pdf2image import convert_from_path

def compute_pdf2image(filepath, dpi=300):
        img_filename = os.path.splitext(filepath)[0]+'.png'
        start = time.time()
        pages = convert_from_path(filepath, dpi)
        #for page in pages:
                #page.save('out.png','PNG')
        pages[0].save(img_filename,'PNG')
        done = time.time()
        print('pdf conversion time: '+ str(done-start))

if __name__ == "__main__":
        folderpath = r'C:\Users\amit\Desktop\USA2019\Calssification Data\2D_Drawings_Selected'
        for root, dirs, files in os.walk(folderpath):
                for file in files:
                        if os.path.splitext(file)[1].lower() == '.pdf':
                                filepath = root+'\\'+file
                                compute_pdf2image(filepath)