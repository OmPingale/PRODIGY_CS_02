from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_img = Image.new(img.mode, (width, height))

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_img.putpixel((x, y), encrypted_pixel)

    encrypted_img.save("encrypted_image.jpg")
    print("Image encrypted successfully.")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    decrypted_img = Image.new(img.mode, (width, height))

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_img.putpixel((x, y), decrypted_pixel)

    decrypted_img.save("decrypted_image.jpg")
    print("Image decrypted successfully.")

# Example usage:
image_path = "example.jpg"
encryption_key = 50

encrypt_image(image_path, encryption_key)
decrypt_image("encrypted_image.jpg", encryption_key)
