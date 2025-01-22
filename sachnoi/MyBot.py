from langchain.text_splitter import  CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
import os
from getpass import getpass
from decouple import config
# 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough




raw_text = """Học viện Công nghệ Bưu chính Viễn thông tự hào là đơn vị đào tạo, nghiên cứu trọng điểm, chủ lực của Ngành Thông tin và Truyền thông Việt Nam.
Học viện Công nghệ Bưu chính Viễn thông được thành lập theo quyết định số 516/TTg của Thủ tướng Chính phủ ngày 11 tháng 7 năm 1997 trên cơ sở sắp xếp lại 4 đơn vị thành viên thuộc Tổng Công ty Bưu chính Viễn thông Việt Nam, nay là Tập đoàn Bưu chính Viễn thông Việt Nam là Viện Khoa học Kỹ thuật Bưu điện, Viện Kinh tế Bưu điện, Trung tâm đào tạo Bưu chính Viễn thông 1 và 2. Các đơn vị tiền thân của Học viện là những đơn vị có bề dày lịch sử hình thành và phát triển với xuất phát điểm từ Trường Đại học Bưu điện 1953.
Từ ngày 1/7/2014, thực hiện Quyết định của Thủ tướng Chính phủ, Bộ trưởng Bộ Thông tin và Truyền thông đã ban hành Quyết định số 878/QĐ-BTTTT điều chuyển quyền quản lý Học viện từ Tập đoàn Bưu chính Viễn thông Việt Nam về Bộ Thông tin và Truyền thông. Học viện Công nghệ Bưu chính Viễn thông là đơn vị sự nghiệp trực thuộc Bộ. Là trường đại học, đơn vị nghiên cứu, phát triển nguồn nhân lực trọng điểm của Ngành Thông tin và Truyền thông.
Với vị thế là đơn vị đào tạo, nghiên cứu trọng điểm, chủ lực của Ngành Thông tin và Truyền thông Việt Nam, là trường đại học trọng điểm quốc gia trong lĩnh vực ICT, những thành tựu trong gắn kết giữa Nghiên cứu – Đào tạo – Sản xuất kinh doanh năng lực, quy mô phát triển của Học viện hôm nay, Học viện sẽ có những đóng góp hiệu quả phục vụ sự phát triển chung của Ngành Thông tin và truyền thông và sự nghiệp xây dựng, bảo vệ tổ quốc, góp phần để đất nước, để Ngành Thông tin và truyền thông Việt Nam có sự tự chủ, độc lập về khoa học công nghệ và nguồn nhân lực, qua đó tự tin cạnh tranh với các đối thủ lớn và sánh vai với các cường quốc trên thế giới.
Là trường Đại học, đơn vị nghiên cứu, phát triển nguồn nhân lực trọng điểm của Ngành Thông tin và Truyền thông. Học viện sẽ có những đóng góp hiệu quả phục vụ sự phát triển chung của Ngành và sự nghiệp xây dựng, bảo vệ tổ quốc.
"""



# 
# load LLM
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo")

#   Chunking data
text_splitter = CharacterTextSplitter(
        # separator="\n",
        chunk_size=525,
        chunk_overlap=10,
        length_function=len

)

chunks = text_splitter.split_text(raw_text)

# embbdeing data
embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# create vecto store
vectorstore = Chroma.from_texts(texts=chunks, embedding=embedding)


vectorstore.add_texts(chunks)
# retrievel
retriever = vectorstore.as_retriever()
# print(retriever)

# create prompt tempalte
def creat_prompt(template):
    prompt = PromptTemplate(template = template, input_variables=["context", "question"])
    return prompt
template = """<|im_start|>system\nSử dụng thông tin sau đây để trả lời câu hỏi. Nếu bạn không biết câu trả lời, hãy nói không biết, `       đừng cố tạo ra câu trả lời\n
        {context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant"""
prompt = creat_prompt(template)

# chain
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
rag_chain = (
    {"context": retriever|format_docs , "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# question = "Học viện Công nghệ Bưu chính Viễn thông được thành lập khi nào?"
# Demo
# response= rag_chain.invoke(question)
# print(f"BOT:{response}")


def vodka(data,question):
    chunks = text_splitter.split_text(data)
    embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

# create vecto store
    vectorstore = Chroma.from_texts(texts=chunks, embedding=embedding)


    vectorstore.add_texts(chunks)
    # retrievel
    retriever = vectorstore.as_retriever()
    rag_chain = (
    {"context": retriever|format_docs , "question": RunnablePassthrough()}
    | creat_prompt(template)
    | llm
    | StrOutputParser()
    )
    return (str(rag_chain.invoke(question)))
# vodka(raw_text,"")





