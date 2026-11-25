
from rest_framework.routers import DefaultRouter
from .views import (
    BukuViewSet,
    AnggotaViewSet,
    PeminjamanViewSet
)

router = DefaultRouter()

router.register('buku', BukuViewSet, basename='buku')
router.register('anggota', AnggotaViewSet, basename='anggota')
router.register('peminjaman', PeminjamanViewSet, basename='peminjaman')

urlpatterns = router.urls
