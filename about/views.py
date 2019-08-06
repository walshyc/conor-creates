from django.shortcuts import render

def about_page(request):
    # Display the about page

    return render(request, 'about.html')