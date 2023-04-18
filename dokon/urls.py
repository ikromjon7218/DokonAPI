from django.contrib import admin
from django.urls import path, include
# from drf_yasg.views import get_schema_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('mahsulot/<int:pk>/izohlar/', Izoh_Mahsulot_APIView.as_view()),

    path('userlar/', include('userapp.urls')),
    path('bolimlar/', include("asosiy.urls")),
    # path('bolimlar/', include("buyurtma.urls")),
    # path('bolimlar/', include("userapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)