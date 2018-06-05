from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import products.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.homepage, name="home"),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
