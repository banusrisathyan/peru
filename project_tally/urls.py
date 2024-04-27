# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from app_tally.views import ProductView, BreastfeedingDetailView,PoopDetailView,UserInfoView

# Create a single router for all models
router = routers.DefaultRouter()
router.register("product", ProductView, basename='product')
router.register("breastfeed-detail", BreastfeedingDetailView, basename='breastfeedingdetail')
router.register("poop_detail", PoopDetailView, basename='poopdetail')
router.register("Userinfo_detail", UserInfoView, basename='Userinfodetail')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
