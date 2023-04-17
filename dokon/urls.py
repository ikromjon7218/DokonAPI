from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from buyurtma.views import *
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register("bolimlar", BolimViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chegirmalilar/', ChegirmalarAPIView.as_view()),
    path('mahsulot/<int:pk>/izohlar/', Izoh_Mahsulot_APIView.as_view()),
    path('mahsulotlar/', MahsulotAPIView.as_view()),
    path('mahsulot/<int:pk>/', Bitta_MahsulotAPIView.as_view()),
    path('izohochir/', IzohOchir.as_view()),
    path('buyurtma/', BuyurtmaAPIView.as_view()),
    path('savatitem/', SavatItemAPIView.as_view()),

    path('userlar/', include('userapp.urls')),
    # path('', include("buyurtma.urls")),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)