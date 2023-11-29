
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from stkpush import views
from homeapp import views 


# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('stk/', include('stkpush.urls')),
    path('', include('homeapp.urls')),
    path('admin/', admin.site.urls),
    path('Portal', include('dreg.urls')),


    
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







