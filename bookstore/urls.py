from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^$', index, name='home'),
    url(r'^store/', include('store.urls'), name='store'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
]
