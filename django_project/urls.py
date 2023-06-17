from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from users import views

urlpatterns = [
    path('markdownx/', include('markdownx.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #path('shop/', include('shop.urls')),
    path('', include('shop.urls')),
    #path('profile/', views.profile),
    #path('users/', include('users.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)