import uuid

from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # Batas maksimum 255 karakter
    price = models.IntegerField()  # Format harga
    description = models.TextField()  # Deskripsi produk

    @property
    def __str__(self):
        return self.name  # Menampilkan nama produk saat di-representasi sebagai string
