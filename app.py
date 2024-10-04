from flask import Flask, render_template, request
from resume_parser import ResumeParser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return "No file part"
    
    file = request.files['resume']
    if file.filename == '':
        return "No selected file"

    file_path = f"./uploads/{file.filename}"
    file.save(file_path)

    parser = ResumeParser(file_path)
    data = parser.parse()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
