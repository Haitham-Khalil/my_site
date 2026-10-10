from django.shortcuts import get_object_or_404, render

from blog.models import Post


def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request): # this view function is responsible for rendering the starting page of the blog, displaying the latest 3 posts. 

    latest_posts = Post.objects.all().order_by("-date")[:3] # this line of code retrieves the latest 3 posts from the database, and ordering them by date in descending order.
    return render(request, "blog/index.html", {
      "latest_posts": latest_posts
    })


def posts(request): # this view function is responsible for rendering the page that displays all the posts in the blog.
    all_posts = Post.objects.all().order_by("-date") # this line of code retrieves all the posts from the database, and ordering them by date in descending order.
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug): # this view function is responsible for rendering the page that displays the details of a single post, based on the slug provided in the URL.
    identified_post = get_object_or_404(Post, slug=slug) # this line of code retrieves the post from the database that matches the provided slug. If no post is found, it raises a 404 error.
    return render(request, "blog/post-detail.html", {
      "post": identified_post,
      "post_tags": identified_post.tags.all()
    })