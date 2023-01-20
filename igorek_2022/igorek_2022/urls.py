
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello_world.urls')),
    path('', include('project.urls')),
    path('blog/', include('blog.urls')),


]
