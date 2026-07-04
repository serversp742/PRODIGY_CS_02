from PIL import Image

def encrypt_image(image_path, key, output_path="encrypted.png"):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key , g ^ key, b ^ key)
    img.save(output_path)
    print(f"[✔] Encrypted → '{output_path}'")

def decrypt_image(image_path, key, output_path="decrypted.png"):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key , g ^ key, b ^ key)
    img.save(output_path)
    print(f"[✔] Decrypted → '{output_path}'")

def swap_pixels(image_path, output_path="swapped.png"):
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    all_pixels = list(img.getdata())[::-1]
    img.putdata(all_pixels)
    img.save(output_path)
    print(f"[✔] Swapped → '{output_path}'")

def main():
    print("=" * 40)
    print("IMAGE ENCRYPTION TOOL")
    print("=" * 40)
    while True:
       print("1. Encrypt  2. Decrypt  3. Swap Pixels ")
       choice = input("Choice: ").strip()
       image_path = input("Image path: ").strip()

       if choice in ("1", "2"):
          key = int(input("Key: ").strip())
          if choice == "1":
            encrypt_image(image_path, key)
          else:
            decrypt_image(image_path, key)
       elif choice == "3":
           swap_pixels(image_path)
       else:
           print("Thank you")
           break

if __name__ == "__main__":
     main()