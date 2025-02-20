from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Tải mô hình và tokenizer về máy
model_name = "bigscience/bloom-560m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Hàm để sinh câu trả lời
def ask_bloom(question, context):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

    output = model.generate(input_ids, max_new_tokens=100)
    answer = tokenizer.decode(output[0], skip_special_tokens=True)

    return answer.split("Answer:")[-1].strip()

# Chạy thử
# context = "Học viện Công nghệ Bưu chính Viễn thông tự hào là đơn vị đào tạo, nghiên cứu trọng điểm, chủ lực của Ngành Thông tin và Truyền thông Việt Nam.Học viện Công nghệ Bưu chính Viễn thông được thành lập theo quyết định số 516/TTg của Thủ tướng Chính phủ ngày 11 tháng 7 năm 1997 trên cơ sở sắp xếp lại 4 đơn vị thành viên thuộc Tổng Công ty Bưu chính Viễn thông Việt Nam, nay là Tập đoàn Bưu chính Viễn thông Việt Nam là Viện Khoa học Kỹ thuật Bưu điện, Viện Kinh tế Bưu điện, Trung tâm đào tạo Bưu chính Viễn thông 1 và 2. Các đơn vị tiền thân của Học viện là những đơn vị có bề dày lịch sử hình thành và phát triển với xuất phát điểm từ Trường Đại học Bưu điện 1953.Từ ngày 1/7/2014, thực hiện Quyết định của Thủ tướng Chính phủ, Bộ trưởng Bộ Thông tin và Truyền thông đã ban hành Quyết định số 878/QĐ-BTTTT điều chuyển quyền quản lý Học viện từ Tập đoàn Bưu chính Viễn thông Việt Nam về Bộ Thông tin và Truyền thông. Học viện Công nghệ Bưu chính Viễn thông là đơn vị sự nghiệp trực thuộc Bộ. Là trường đại học, đơn vị nghiên cứu, phát triển nguồn nhân lực trọng điểm của Ngành Thông tin và Truyền thông."
# question = "Học viện Công nghệ Bưu chính Viễn thông được thành lập khi nào?"

# print("BOT:", ask_bloom(question, context))
