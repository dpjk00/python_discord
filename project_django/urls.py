from django.contrib import admin
from django.urls import path, include


#passy na konto to superuser i strong123

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dscrd.urls')),
    path('api/', include('dscrd.api.urls'))
]
