
from django.db import models


class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=150)
    penerbit = models.CharField(max_length=150)
    tahun_terbit = models.PositiveIntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    stok = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.judul


class Anggota(models.Model):
    nama = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    no_telepon = models.CharField(max_length=20)
    alamat = models.TextField()

    def __str__(self):
        return self.nama


class Peminjaman(models.Model):
    STATUS_CHOICES = [
        ('dipinjam', 'Dipinjam'),
        ('dikembalikan', 'Dikembalikan'),
    ]

    anggota = models.ForeignKey(
        Anggota, on_delete=models.CASCADE
    )
    buku = models.ForeignKey(
        Buku, on_delete=models.CASCADE
    )
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_kembali = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='dipinjam'
    )

    def __str__(self):
        return f"{self.anggota.nama} - {self.buku.judul}"
