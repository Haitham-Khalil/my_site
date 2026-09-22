from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(default="") # it's just a CharField with some extra validation, so it checks if the email address is valid or not.

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()

    
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200) # A short summary of the post, which will be displayed on the home page and in the list of posts
    image_name = models.CharField(max_length=100)   
    """ The name of the image file, but not the image itself,
          because we are going to talk about file uploads later, our idea for now is that we pick one of the static image names."""
  
    date = models.DateField(auto_now=True) # We can use auto_now=True when we wanna set a date and that date should always get updated whenever we update the data, so the date gets updated whenever we call save() on a post entry.
    slug = models.SlugField(unique=True,db_index=True) 
    content = models.TextField(validators=[MinLengthValidator(10)]) 
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")







