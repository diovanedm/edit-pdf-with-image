# import module
from pdf2image import convert_from_path
from PIL import Image, ImageOps
import os

def convert_pdf_to_images(pdf_path): 
  # Store Pdf with convert_from_path function
  images = convert_from_path(pdf_path)
  path = []
  for i in range(len(images)):
    # Save pages as images in the pdf
    images[i].save('page_'+ str(i) +'.jpg', 'JPEG')
    path.append(os.path.abspath('page_'+ str(i) +'.jpg'))
  return(path)

def invert_image(image_path):
  image = Image.open(image_path)
  
  inverted_image = ImageOps.invert(image)
  inverted_path = 'inverted_image_' + image_path.split('/')[-1]
  inverted_image.save(inverted_path)
  
  os.remove(image_path)
  return inverted_path


def invert_to_pdf(image_paths, file_name): 
  images = []
  for image in image_paths:
    images.append(Image.open(image))
    os.remove(image)

  pdf_path = "./cifras-alteradas/" + file_name
      
  images[0].save(
      pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
  )
  

file = 'cifras/a-alegria-cifra.pdf'
paths = convert_pdf_to_images(file)
inverted_paths = []

for path in paths:
  inverted_paths.append(invert_image(path))

invert_to_pdf(inverted_paths, file.split('/')[-1])