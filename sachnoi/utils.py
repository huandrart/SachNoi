
from gtts import gTTS
import os
from django.conf import settings

def generate_audio(book):
    """
    mô tả : gTTTS lấy text_book trong database để chuyển văn bản sách -> giọng nói 
    gTTS sau khi tạo xong audio mp3 thì lưu vào folder gốc của dự án Django là media/
    """
    # Đảm bảo thư mục lưu trữ tồn tại
    audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio_files')
    os.makedirs(audio_dir, exist_ok=True)  

    # Đường dẫn file đầy đủ
    audio_path = os.path.join(audio_dir, f"{book.id}.mp3")

    # Tạo file audio từ text_content
    tts = gTTS(text=book.text_content, lang='vi' , slow=False)  # Bạn có thể thay đổi ngôn ngữ nếu cần
    tts.save(audio_path)  # Lưu file audio vào thư mục đã định

    # Lưu đường dẫn tương đối vào trường audio_file
    book.audio_file = f"audio_files/{book.id}.mp3"
    book.save()


