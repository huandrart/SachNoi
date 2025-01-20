# File này : Tự động tạo file mp3 từ utils.py khi có sách mới được cập nhật 

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Books
from .utils import generate_audio

@receiver(post_save, sender=Books)
def create_audio_file(sender, instance, created, **kwargs):
    if created or (instance.text_content and not hasattr(instance, '_already_handled')):
        # Đánh dấu instance đã được xử lý
        instance._already_handled = True
        # Gọi hàm generate_audio
        generate_audio(instance)



