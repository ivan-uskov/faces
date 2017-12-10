from django.views.generic.base import View
from django.shortcuts import render


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.pug', {"foo": "bar"})
