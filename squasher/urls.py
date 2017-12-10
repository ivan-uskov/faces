from django.conf.urls import url
from django.contrib import admin

from squasher.view.HomeView import HomePageView
from squasher.view.SquashView import SquashPageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^squash$', SquashPageView.as_view(), name='squash'),
]
