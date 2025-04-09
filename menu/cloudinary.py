import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.conf import settings

cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE['dwydieekv'],
    api_key=settings.CLOUDINARY_STORAGE['631672334757896'],
    api_secret=settings.CLOUDINARY_STORAGE['OnFU9RbD8exho3hHfhKRaHnMPrY'],
    secure=True
)