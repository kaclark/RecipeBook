# Importing library
import cv2
from pyzbar.pyzbar import decode
import sys
import requests
from tempfile import NamedTemporaryFile
import subprocess
from bs4 import BeautifulSoup
  
# Make one method to decode the barcode
def BarcodeReader(image):
     
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
       
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes: 
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
            # Print the barcode data
                #print(barcode.type)
                return str(barcode.data, 'UTF-8')
                 
    #Display the image
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
 
if __name__ == "__main__":
  # Take the image from user
    image=sys.argv[1]
    pcode = BarcodeReader(image)
    url_prefix = "https://world.openfoodfacts.org/product/"
    r = requests.get(url_prefix + pcode)
    r_html = r.content
    
    #TODO: Load Temp file into lynx through subprocess
    #f = NamedTemporaryFile()
    #f.write(r_html)
    #f_path = f.name
    #lynx_search = subprocess.run(["sh", "-c", "lynx -force_html " + f_path])

    soup = BeautifulSoup(r_html, 'html.parser')
    title = soup.find('title')
    print(title.string)
