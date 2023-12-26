
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('user.urls')),
    path('ingredient/', include('ingredient.urls')),
    path('recipes/', include('recipes.urls')),
]
