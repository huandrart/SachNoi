**Quản Lý Sách Nói và Văn Bản TTS**
Dự án này là một hệ thống quản lý nội dung nhằm hỗ trợ chuyển đổi văn bản sang giọng nói (Text-to-Speech - TTS). 
Mục tiêu chính của dự án là tạo ra một nền tảng thân thiện với người dùng, giúp dễ dàng quản lý nội dung văn bản, tệp âm thanh và các tùy chọn cá nhân hóa giọng đọc.
**Tính năng**
- Xác thực người dùng (đăng ký, đăng nhập).
- Quản lý nội dung sách và văn bản.
- Chuyển đổi văn bản sang giọng nói với các tùy chọn cá nhân hóa.
- Theo dõi lịch sử nghe và lưu trữ vị trí dừng.
- Hỗ trợ các tùy chọn tốc đọ đọc khác nhau .
- Quản lý danh mục, tác giả, và tệp âm thanh.
**Yêu cầu hệ thống**
Node.js
npm hoặc yarn
MongoDB hoặc hệ quản trị cơ sở dữ liệu tương tự
**Cài đặt**
**1 So lenh git**
 git add .
 git commit -m "..."
 git pull
 git push
 git checkout ...
 va 1 so lenh git khac
**Clone kho lưu trữ:**
- git clone <repository-url>  
**Cài đặt backend:**
- Di chuyển vào thư mục backend và cài đặt các dependencies:
- cd backend  
- npm install  
**Cấu hình môi trường:**
- Tạo tệp .env và thiết lập các biến môi trường cần thiết, bao gồm thông tin kết nối cơ sở dữ liệu và các cài đặt khác.
**Cài đặt frontend:**
- Di chuyển vào thư mục frontend và cài đặt các dependencies:
- npm install  
**Chạy ứng dụng**
- cài đặt thêm 1 số môi trường như : pip install gtts, pip install python-decouple, pip install langchain, cài visual_Buildtool , pip thêm 1 số thư viện được yêu cầu
- chạy lệnh python manage.py migrate
python manage.py runserver




