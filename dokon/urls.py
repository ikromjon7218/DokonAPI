from django.contrib import admin
from django.urls import path, include
# from drf_yasg.views import get_schema_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('userapp.urls')),
    path('bolimlar/', include("asosiy.urls")),
    path('buyurtmalar/', include("buyurtma.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)