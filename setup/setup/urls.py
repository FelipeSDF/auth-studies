from django.contrib import admin
from django.urls import path, include
from auth_setup import views as auth_setup
from django.conf import settings
from django.conf.urls.static import static
app_name = 'global'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_setup.home, name='home'),
    path('post/', auth_setup.post, name='post'),
    path('post/posted', auth_setup.post, name='posted'),
    path('auth/', include('auth_setup.urls'))
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)