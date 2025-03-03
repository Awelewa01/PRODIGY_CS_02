# PRODIGY_CS_02
This is a simple image encyrption tool.
It uses the pillow library for image manipulation.
It defines a main function which interacts with the user to determine whether to perform encryption or decryption, get the image path and output path for encrypted/decrypted image, and the key for pixel manipulation.
It defines an encryption fuction which applies XOR algorithm with the key.
It also defines a decryption function which appplies XOR algorithm with the key.
XOR operation for pixel manipulation is reversible.

This tool encrypts an image "prodigy_image.png" and encrypts it to "prodigy_image_encrypted.png".
The program was run again to decyrpt "prodigy_image_encrypted.png" to "prodigy_image_decrypted.png"
The program was run on Visual Studio Code.
It was oberserved that both "prodigy_image_encrypted.png" and "prodigy_image_decrypted.png" are same.
