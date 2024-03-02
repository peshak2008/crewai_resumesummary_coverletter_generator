
llm_model="gpt-4-turbo-preview" #Set the language model to be used for the resume generation. GPT-4 is the recommended model for complex tasks like resume generation

scrape_config = {
    "perform_scrape": True, #set to False if you want to manually provide the job descriptions in output.json
    "url": [
    "https://www.indeed.com/jobs?q=software+engineer&l=Dallas,+TX&vjk=21778de12073f889",
    "https://www.indeed.com/jobs?q=software+engineer&l=Dallas,+TX&vjk=ac9c11a73f520f58"
    ],
    "selector": "#jobsearch-ViewjobPaneWrapper",  #If not used, the body of the page will be scraped
    "wait_for_selector_timeout": 2000,
    "output_to_file": True,
}

# Notion configuration: Set save_to_notion to True if you want to save the job details to Notion database. Read the README for more details on how to set up Notion integration
notion_config = {
    "save_to_notion": True,
    "database_id": "" #If save_to_notion is set to True, provide the database id of the Notion database. Read the README for more details on how to get the database id
}

# Set to True if you want to create a PDF resume from the generated resume. Make sure LibreOffice is installed on your system. If issues arise, set to False
create_pdf = True


# Determine which sections of the resume to update by AI. For the sections to be updated, set the value to True and make sure the resume template has these sections as {TITLE}, {SUMMARY}, {LOCATION}
resume_sections_to_update = {
    'title': True,
    'summary': True,
    'location': True,
}


resume_name = "Software_Engineer_Resume_John_Doe.docx" # add the resume in the default_resume folder
resume_template="Software_Engineer_Resume_John_Doe_Template.docx" # add the resume template in the default_resume folder


candidate_name = "John Doe" #Name of the candidate
default_job_title = "Software Engineer" # default job title to be used if AI fails to extract the job title from the job description
default_skills_summary="""
Highly skilled and results-oriented software engineer with over 10 years of experience in software development, project management, and team leadership. Expertise in developing scalable software solutions, leading technical teams, and delivering high-quality projects on time and within budget. Adept at driving the adoption of new technologies and best practices to enhance product development processes. Proven ability to work in dynamic and fast-paced environments, solving complex technical challenges.
""" #Default skills summary to be used if AI fails to extract the skills summary from the resume
default_location = "New York, NY" #Set the location to your preferred location. It will be used if AI fails to extract the location from the job description