import base64
from PIL import Image
from io import BytesIO

def image_to_base64(image_path):
    try:
        with open(image_path, "rd") as image_file:
            image_content = image_file.read()
            base64_data = base64.b64encode(image_content).decode("utf-8")

            return base64_data
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    image_path = input("Enter image path: ")

    base46_data = image_to_base64(image_path)

    if not base46_data.startswith("Error"):
        print("\nBase64 representation of the image:")
        print(base46_data)
    else:
        print(base46_data)

if __name__ == "__main__":
    main()