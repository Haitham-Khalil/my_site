from django.shortcuts import render

from blog import views as blog_views


# Handling the homepage URL:
def homepage(request):
    # return HttpResponse("You're at the homepage.")
    return render(request, "blog/index.html", {
        "posts": blog_views.posts[:3],  # The latest three thoughts on the homepage.
    })
