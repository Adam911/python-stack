# Create the views here.
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    # Adding the Homepage Index view
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Adding the about page
class AboutPageView(TemplateView):
    template_name = 'about.html'
