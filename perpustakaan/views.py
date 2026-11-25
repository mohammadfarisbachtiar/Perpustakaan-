
from rest_framework import viewsets
from .models import Buku, Anggota, Peminjaman
from .serializers import (
    BukuSerializer,
    AnggotaSerializer,
    PeminjamanSerializer
)


class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer


class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer


class PeminjamanViewSet(viewsets.ModelViewSet):
    queryset = Peminjaman.objects.all()
    serializer_class = PeminjamanSerializer
