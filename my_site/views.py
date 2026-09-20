from django.shortcuts import render


# Handling the homepage URL:
def homepage(request):
    # return HttpResponse("You're at the homepage.")
    return render(request, "blog/index.html")
