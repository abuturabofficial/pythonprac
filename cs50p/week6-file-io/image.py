from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        # # Print metadata info of an image
        # print(img.size)
        # print(img.format)
        # Rotate an Image
        img = img.rotate(180)
        # Apply a filter
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")


if __name__ == "__main__":
    main()
