from django.conf.urls import include, url
from django.contrib import admin
from store.views import index

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^store/', include('store.urls'), name='store'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
