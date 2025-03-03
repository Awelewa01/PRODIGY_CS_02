#Load an image and access pixels
from PIL import Image




# Define an encryption function
def encrypt_pixel(input_path, output_path, key):
  image = Image.open(input_path)
  pixels = image.load()
  width, height = image.size
  #Print a sample pixel value
  print("Sample pixel value:", pixels[0,0])   #Prints (R, G, G) or (R, G, B, A) for transparent images

  for x in range (width):
    for y in range (height):
      r, g, b = pixels[x, y][:3]      #Extract only RGB values

      #Apply XOR encryption using the key
      r_encrypted = r ^ key
      g_encrypted = g ^ key
      b_encrypted = b ^ key

      # update the pixel with encrypted key
      pixels[x, y] = (r_encrypted, g_encrypted, b_encrypted)

  #save the encrypted image
  image.save(output_path)
  print("Encrypted image saved as", output_path)

#Define a decryption function.
# XOR is reversible. Decrypting the image is simply applying the XOR with the same key again
def decrypt_pixel(input_path, output_path, key):
  image = Image.open(input_path)
  pixels = image.load()
  width, height = image.size
  #Print a sample pixel value
  print("Sample pixel value:", pixels[0,0])   #Prints (R, G, G) or (R, G, B, A) for transparent images

  for x in range (width):
    for y in range (height):
      r, g, b = pixels[x, y][:3]      #Extract RGB values

      #Apply XOR decryption using the same key
      r_decrypted = r ^ key
      g_decrypted = g ^ key
      b_decrypted = b ^ key

      #Restore the original pixel values
      pixels[x, y] = (r_decrypted, g_decrypted, b_decrypted)

  #Save the decrypted imagae
  image.save(output_path)
  print("Decrypted image saved as", output_path)

#Run The Program
#Define a main function to handle user input
def main():
  print(f"Image Encyption Tool")
  task = input("Do you want to (E)cnrypt or (D)ecrypt an image? ").strip().lower()

  input_path = input("Enter the input image file name (with extension): ").strip().lower()
  output_path = input("Enter the output image file name (with extension): ").strip().lower()
  key = int(input("Enter a numerical key (0 - 255): "))

  if task == "e":
    encrypt_pixel(input_path, output_path, key)
  elif task == "d":
    decrypt_pixel(input_path, output_path, key)
  else:
    print("Invalid option. Kindly choose (E) for Encryption or (D) for Decrption")

if __name__ == "__main__":
  main()