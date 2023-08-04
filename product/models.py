from django.db import models
from PIL import Image
from django.conf import settings

"""
Product:
    product_name: Char
    short_description: Text
    long_description: Text
    image: Image
    slug: Slug
    marketing_price: Float
    marketing_off_price: Float
    product_type: Choices
        ('V', Variable)
        ('S', Simple)
"""


class Product(models.Model):
    product_name = models.CharField(
        default='name_product',
        max_length=255, blank=True)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(
        upload_to='product_image/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    marketing_price = models.FloatField()
    marketing_off_price = models.FloatField(default=0)
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple'),
        )
    )

    @staticmethod
    def resize_image(img, new_width=800):

        media_root = settings.MEDIA_ROOT
        img_full_path = f'{media_root}/{img.name}'
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            print('Original Width is lower than the new one')
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        print('Resize applyed')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self) -> str:
        return self.product_name


"""
    Variation:
        product_name: char
        product: FK Product
        marketing_price = Float
        marketing_off_price = Float
        stock = Int

"""


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    marketing_price = models.FloatField()
    marketing_off_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.product_name or self.product.product_name
