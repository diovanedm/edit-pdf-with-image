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


def invert_to_pdf(image_paths, file_name, output_folder): 
  images = []
  for image in image_paths:
    images.append(Image.open(image))
    os.remove(image)

  # Criar pasta se não existir
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  pdf_path =  os.path.join(output_folder, file_name)
      
  images[0].save(
      pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
  )
  



def proccess_folder(input_folder = "./cifras", output_folder = "./cifras-alteradas"):
  for root, dirs, files in os.walk(input_folder):
    for file in files:
      if file.endswith(".pdf"):
        file = os.path.join(root, file)
        paths = convert_pdf_to_images(file)
        inverted_paths = []

        for path in paths:
          inverted_paths.append(invert_image(path))

        invert_to_pdf(inverted_paths, file.split('/')[-1], output_folder)
        print("File " + file + " has been processed")

# Digitar o nome da pasta que contém os arquivos pdf
folder_name = input("Digite o nome da pasta que contém os arquivos pdf: ")
output_folder = input("Digite o nome da pasta de saída: ")
proccess_folder(folder_name, output_folder)