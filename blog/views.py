from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
posts_dictionary = {
    # The keys are the slugs (The dynamic segments in the actual URL), and the values are the titles of the posts, and these values will appear on the /posts URL.
    "post1": "The Future of Artificial Intelligence",
    "post2": "How the Internet Actually Works",
    "post3": "Why Learning to Code Is Important",
    "post4": "Building Your First Django Website",
    "post5": "The Rise of Cybersecurity",
    "post6": "How Technology Is Changing Education",
}


def index(request):
    # list_items = ""  # All the list items of the HTML unordered list will be stored in this variable.
    list_of_slugs = list(
        posts_dictionary.keys())
    # )  # Getting the list of slugs from the dictionary keys.

    # for slug in list_of_slugs:
    #     dynamic_path = reverse("post_detail", args=[slug])
    #     list_items += f"<li><a href={dynamic_path}>{posts_dictionary[slug]}</a></li>"

    # response_data = f"""
    # <h1>Blog Posts</h1>
    # <ul>
    #     {list_items}
    # </ul>
    # """
    # return HttpResponse(response_data)
    index_context = {
        "slugs": list_of_slugs,
        "posts_dictionary": posts_dictionary,
    }
    return render(request, "blog/index.html")


def post_detail(request, slug):
    # return HttpResponse(f"Hello, world. You're at the blog post with slug: {slug}")
    pass
