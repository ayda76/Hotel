from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

def create_test_image():
    file = BytesIO()

    image = Image.new("RGB", (100, 100), color="white")
    image.save(file, "JPEG")
    file.seek(0)

    return SimpleUploadedFile(
        "test.jpg",
        file.read(),
        content_type="image/jpeg",
    )