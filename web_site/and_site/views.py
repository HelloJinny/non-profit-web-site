from django.shortcuts import render

# Create your views here.
def home_page_main(request):
    return render(request, 'and_site/home_page_main.html')
