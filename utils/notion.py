from notion_client import Client
from dotenv import load_dotenv
import os
from datetime import datetime
from utils.config import notion_config


# Load environment variables
load_dotenv()

# Get the integration token from environment variables
integration_token = os.getenv('NOTION_INTEGRATION_TOKEN')
notion = Client(auth=integration_token)

database_id = notion_config["database_id"]


def create_notion_database_page(job_title, company_name,company_industry, salary_range, job_url, job_location, role_seniority, role_discipline):
    # Get the current date in ISO 8601 format
    created_date = datetime.now().strftime("%Y-%m-%d")


    
    # Define the properties for the new page (row in the database)
    new_page_properties = {
        "Job Title": {
            "title": [
                {
                    "text": {
                        "content": job_title
                    }
                }
            ]
        },
        "Company Name": {
            "rich_text": [
                {
                    "text": {
                        "content": company_name
                    }
                }
            ]
        },
        "Company Industry": {
            "rich_text": [
                {
                    "text": {
                        "content": company_industry
                    }
                }
            ]
        },
        "Salary Range": {
            "rich_text": [
                {
                    "text": {
                        "content": salary_range
                    }
                }
            ]
        },
        "Job URL": {
            "url": job_url
        },
        "Job Location": {
            "rich_text": [
                {
                    "text": {
                        "content": job_location
                    }
                }
            ]
        },
        "Role Seniority": {
             "rich_text": [
                {
                    "text": {
                        "content": role_seniority
                    }
                }
            ]
        },
        "Role Discipline": {
            "rich_text": [
                {
                    "text": {
                        "content": role_discipline
                    }
                }
            ]
        },
        "Created Date": {
            "date": {
                "start": created_date
            }
        },
    }
    
    # Use the pages.create method to add a new row to the database
    try:
        response = notion.pages.create(parent={"database_id": database_id}, properties=new_page_properties)
        print("New row added successfully to the notion database")
    except Exception as e:
        print("Failed to add a new row to the notion database:", e)

if __name__ == "__main__":
    # Example usage
    create_notion_database_page( "Software Engineer", "Notion Inc","technology", "$100k-$150k", "https://notion.so/job", "San Francisco, CA", "Senior", "Engineering")  

