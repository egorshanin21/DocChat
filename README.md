# **DocChat Web App**
![logo-removebg-preview.png](..%2F..%2FDownloads%2Flogo-removebg-preview.png)

## DocChat is a web application coded on Django framework and Python, that allows you upload your own documents and address questions based on these materials, using the powerful capabilities of LLM models to provide context-sensitive answers.

# **DocChat Features:**
#### - Allows the user to upload PDF, docx, txt files into the chat;
#### - Receive answers to questions from the context of the documents you downloaded;
#### - DocChat stores information from all files you download;
#### - Access to all user chats has been developed, which allows the user to speed up his interaction with the chat;
#### - Convenient and understandable interface which was based on the style of the well-known ChatGPT.

# **How to install project:**
#### 1. Clone the repository to your computer
#### Command: git clone git@github.com:egorshanin21/DocChat.git
#### 2. Navigate to the project directory cd DocChat
#### Command: cd DocChat
#### 3. Create a virtual environment to install dependencies in and activate it
#### Command to venv: 
####                - python -m venv myenv (create venv);
####                - source myenv/bin/activate (activate your venv).
#### Command to poetry:
####                 - pip install poetry (poetry environment install);
####                 - poetry new myproject (create you poetry venv);
####                 - poetry shell (activate poetry).
#### 4. There is a file 'example_env' in the project, rename it to '.env' and fill in the fields with your data.
#### 5. Create your OPEN AI account ( https://openai.com/blog/openai-api ) and find API Key in order to obtain credentials for .env file ( OPENAI_API_KEY ).
#### 6. Install the dependencies
#### Command:
####        - pip install -r requirements.txt (for venv);
####        - poetry install --no-root (for poetry).
#### 7. Make migrations using the command: python manage.py migrate
#### 8. Create a superuser python manage.py createsuperuser
#### 9. Run the program python manage.py runserver
#### 10. Follow the link http://127.0.0.1:8000/ and enjoy!

# Used technologies:
#### - Python 3.11.5
#### - Django 4.2.7
#### - Langchain (gpt-3.5-turbo, OpenAIEmbeddings, ChatOpenAI, ConversationBufferMemory, FAISS, RecursiveCharacterTextSplitter)
#### - PostgreSQL
#### - OpenAI API
#### - HTML
#### - CSS
#### - Docker
#### - Github

# Developers:
#### 1. Yehor Shanin
#### 2. Vitaliy Kirienko
#### 3. Konstantyn Zagorodnui
#### 4. Ruslan Sirenko