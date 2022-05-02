from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('web/', include('web.urls')),
    path('admin/', admin.site.urls),
]
