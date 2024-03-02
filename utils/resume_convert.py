from docx import Document
import os
from utils.config import resume_name  

#Put the resume in default_resume folder. And make sure the file name is the same as the one in the config.py file

# Define the path to the default_resume folder relative to this script
default_resume_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'default_resume')

def docx_to_md():
    # Construct the full path to the .docx file
    docx_path = os.path.join(default_resume_folder, resume_name)
    
    # Derive the Markdown file path from the .docx path
    md_path = os.path.splitext(docx_path)[0] + '.md'
    
    # Check if the Markdown file already exists
    if os.path.exists(md_path):
        print(f"Markdown file {md_path} already exists. No action taken.")
        return
    
    # Load the .docx file
    doc = Document(docx_path)
    
    # Extract text from each paragraph in the document
    text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
    
    # Save the extracted text to a .md file
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(text)
    
    print(f"Markdown file {md_path} created successfully.")

# Example usage
if __name__ == "__main__":
    docx_to_md()