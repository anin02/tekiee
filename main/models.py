import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # Nama kacamata
    price = models.IntegerField()  # Harga kacamata
    description = models.TextField()  # Deskripsi kacamata
    #frame_material = models.CharField(max_length=255, blank=True, null=True)  # Bahan bingkai
    # lens_type = models.CharField(max_length=255, blank=True, null=True)  # Jenis lensa
    #color = models.CharField(max_length=50, blank=True, null=True)  # Warna kacamata
    #stock = models.IntegerField(default=0)  # Jumlah stok
    #image = models.ImageField(upload_to='products/', blank=True, null=True)  # Gambar kacamata
    #brand = models.CharField(max_length=255, blank=True, null=True)  # Merek kacamata

    @property
    def __str__(self):
        return self.name
