from django.contrib import admin
from django.urls import path, include
import products.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.homepage, name="home"),
    path('accounts/', include('accounts.urls'))
]
