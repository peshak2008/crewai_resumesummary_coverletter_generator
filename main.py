import json
from utils.error_check import check_errors
from utils.notion import create_notion_database_page
from utils.resume_convert import docx_to_md
from utils.scrape_jobs import scrape_jobs
from utils.crew import JobSearchCrewManager
from utils.config import notion_config, scrape_config


# Run error checks
check_errors()

# Convert the resume from docx to md (markdown) format, runs only if the md file does not exist
docx_to_md()

# Check if scraping is enabled in the configuration
if scrape_config.get("perform_scrape", False):
    # Scrape the job description from the website
    scrape_jobs()


# Read output.json to get the list of job descriptions
output_file_path = 'output.json'
with open(output_file_path, 'r') as file:
    job_descriptions = json.load(file)


# Check if job_descriptions is a non-empty list
if not isinstance(job_descriptions, list) or not job_descriptions:
    raise ValueError("job_descriptions must be a non-empty list.")

# Assuming job_descriptions is a list of job descriptions
# For each index in the list, create a task for each job description
for job_index, job_description in enumerate(job_descriptions):

    # Create an instance of JobSearchCrewManager for each job index
    manager = JobSearchCrewManager(job_index)
    # Execute the job search process
    job_details = manager.kickoff()


    # Check if save_to_notion is set to True, if NOTION_INTEGRATION_TOKEN is set, and if database_id is provided
    if notion_config.get("save_to_notion", False):
        # Extract job_url from the current job description, if it exists
        job_url = job_description.get('url', 'unknown')
        # Extract necessary details from job_details
        job_title = job_details.get('job_title', 'unknown')
        company_name = job_details.get('company_name', 'unknown')
        company_industry = job_details.get('company_industry', 'unknown')
        salary_range = job_details.get('salary_range', 'unknown')
        job_location = job_details.get('job_location', 'unknown')
        role_seniority = job_details.get('role_seniority', 'unknown')
        role_discipline = job_details.get('role_discipline', 'unknown')
        # Update Notion database for each job
        create_notion_database_page(job_title, company_name, company_industry, salary_range, job_url, job_location, role_seniority, role_discipline)