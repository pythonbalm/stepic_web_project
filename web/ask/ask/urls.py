from django.conf.urls import url, include
from django.contrib import admin
from qa.views import test

urlpatterns = [
    url(r'^$', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask', test),
    url(r'^popular/', test),
    url(r'^new/', test),
    url(r'^admin/', admin.site.urls),
    url(r'^question/(?P<num>\d+)/$', test)
]
