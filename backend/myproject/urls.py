from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myproject.core.urls', namespace='myproject.core')),
    path('admin/', admin.site.urls),
    #path('', include('myproject.core.urls'))
]
