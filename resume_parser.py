import pdfplumber

class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {
            "Education": [],
            "Experience": [],
            "Projects": [],
            "Skills": [],
            "Certifications": []
        }

    def parse(self):
        with pdfplumber.open(self.file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() + '\n'

        self.extract_information(text)
        return self.data

    def extract_information(self, text):
        # Basic parsing logic, you can enhance this further
        lines = text.split('\n')
        current_section = None

        for line in lines:
            line = line.strip()
            if line.lower().startswith("education"):
                current_section = "Education"
            elif line.lower().startswith("experience"):
                current_section = "Experience"
            elif line.lower().startswith("projects"):
                current_section = "Projects"
            elif line.lower().startswith("skills"):
                current_section = "Skills"
            elif line.lower().startswith("certifications"):
                current_section = "Certifications"
            elif current_section:
                self.data[current_section].append(line)
