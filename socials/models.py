from django.db import models
from users.models import UserAccount
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode  
from django.utils.encoding import force_bytes

def user_directory_path(instance, filename):
    # File sẽ được upload vào thư mục MEDIA_ROOT/user_<id>/<filename>
    return f'user_{urlsafe_base64_encode(force_bytes(instance.album.author.id))}/{filename}'

class Social(models.Model):
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.author.email}/{self.title}'

class Photo(models.Model):
    album = models.ForeignKey(Social, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
