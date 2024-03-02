# Custom Resume and Cover Letter Generator

This library harnesses AI and the CrewAI library, developed by @joaomdmoura (https://github.com/joaomdmoura/crewAI/commits?author=joaomdmoura), to generate custom resume summary and cover letters. It utilizes candidate-provided resumes and job descriptions scraped from Indeed or other job listing platforms. The goal is to assist job seekers in customizing their applications for specific job openings, thereby increasing their chances of getting selected by job application systems and securing an interview. Make sure to review generated documents and confirm it presents your skills and background the way you expect.

## Key Deliverables

This package provides a comprehensive solution for job seekers to enhance their job application process. Here are the key deliverables:

- **Custom Resume Summary Generation**: Generates tailored resume summary, candidate title, and location by integrating the candidate's skills and experiences with specific job descriptions.

- **Custom Cover Letter Creation**: Crafts personalized cover letters that address the specific requirements of each job opening, highlighting the candidate's suitability.

- **PDF Conversion**: Offers the capability to save generated resumes and cover letters as PDFs, ensuring consistent formatting across different platforms and devices.

- **Notion Integration**: Supports updating a Notion database with job application details, making it easier to track and organize job search efforts.

- **Job Description Scraping**: Includes functionality to automatically scrape job descriptions from specified URLs, facilitating the customization process.

- **AI-Enhanced Content**: Utilizes AI to analyze job descriptions and candidate resumes, ensuring that generated documents are highly relevant and tailored.

These features are designed to streamline the job application process, making it more efficient and increasing the chances of securing interviews.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Dependencies listed in `requirements.txt`
- An API key from OpenAI for the Crew AI integration
- Notion Integration API secret if you are exporting to notion

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.
3. Obtain an OpenAI API key and set it in your environment variables as `OPENAI_API_KEY`.
4. For notion integration, see the relevant section below.

### Configuration

Before using the library, you need to set up the following:

- **Resume and Template**: Place your `resume.docx` in the `default_resume` folder. Also, provide a template resume in the same folder, which serves as a placeholder for the title, summary, and title sections. See the provided example in the default_resume folder. The files names must match the values in the config.py file

- **Configurations**: In the `config.py` file, update the following settings:
  - `indeed_urls` or any other job listing URLs you wish to scrape.
  - `selector`: CSS selector for scraping specific parts of the job listing page. If no selector is provided, the entire body will be scraped.
  - `candidate_name`, `resume_name`, and `resume_template_name`: Update these fields with your information and file names.
  - `default_location`, `default_job_title` and `default_skills_summary`: These will be used if the tool cannot deduce this information from the provided job descriptions.
- **Scraping**: Set `perform_scrape` to `true` to enable automatic scraping of job descriptions. If set to `false`, you must manually create `output.json` in the main directory, which should be an array of strings containing different job descriptions.

- **Output Structure**: The library organizes generated content into a structured directory system for ease of access and management. For each company, a dedicated folder is created. Within each company's folder, subfolders are named after job titles for which the candidate is applying. This structure facilitates a clear and organized way to store and retrieve generated documents. The following files are created within each job title folder:

  - **Candidate Skills Summary**: A text file named `{candidate_name}_Skills_Summary.txt` summarizing the candidate's skills extracted from their resume. This summary highlights the skills most relevant to the job application, tailored to match the requirements of the specific job listing. It serves as a quick reference for both the candidate and potential employers to understand the candidate's qualifications at a glance.

  - **Job Description Summary**: A text file named `Job_Description_Summary.txt` containing a concise summary of the job description. This document distills the key points and requirements from the job listing, providing a quick reference for the candidate. It helps the candidate to tailor their application and prepare for interviews by focusing on the most relevant aspects of the job.

  - **Custom Resume**: A document named `Resume_{candidate_name}_{company_name}_{job_title}.docx` generated by integrating the candidate's skills and experiences with the job description. This custom resume emphasizes the candidate's qualifications that are most relevant to the job, thereby increasing the chances of catching the employer's attention.

  - **Custom Cover Letter**: A document named `Cover Letter_{candidate_name}_{company_name}_{job_title}.docx` crafted to complement the custom resume. This cover letter addresses the specific company and job title, highlighting how the candidate's background and skills make them the ideal fit for the position. It serves as a personal introduction and a compelling argument for the candidate's candidacy.

## Saving Resumes and Cover Letters as PDFs

The custom resume and cover letter generator offers the capability to save generated documents as PDFs. This feature is particularly beneficial for job application systems, as PDFs are widely accepted and maintain consistent formatting across different platforms and devices. However, setting up this feature requires additional steps and ensuring that all necessary libraries are installed.

## Customizable Resume Fields

In the `config.py` file, you have the option to set certain fields to `true` for customization in your resume. These fields include `title`, `summary`, and `location`. Customizing these fields is crucial for tailoring your resume to match specific job descriptions, thereby increasing your chances of passing through Applicant Tracking Systems (ATS) and catching the attention of hiring managers. Here's a breakdown of each field and its importance:

### Title

The `title` field in your resume is pivotal as it directly reflects the job position you are applying for. Setting this to `true` in the `config.py` allows the generator to customize the title to match the job description closely. This alignment shows potential employers that your professional experience and aspirations are in direct correlation with the job role, making you a better fit for the position.

### Summary

The `summary` section of your resume is where you can shine by integrating keywords and phrases that match the job description. By setting the `summary` field to `true`, the generator will tailor this section with keywords that resonate with the job description and requirements. This not only helps in passing the ATS but also in making your resume stand out to the hiring manager by highlighting how your skills and experiences align with what they are looking for.

### Location

Customizing the `location` on your resume by setting it to `true` in the `config.py` demonstrates your interest or availability in the job's geographic location. This is particularly important for jobs that have a specific location requirement. It signals to employers that you are either already in the vicinity or are willing to relocate for the position, making you a more appealing candidate.

By customizing these three fields—`title`, `summary`, and `location`—you significantly enhance your resume's relevance to the job you're applying for. This tailored approach ensures that your application is not only ATS-friendly but also tailored to the specific job opening, thereby increasing your chances of securing an interview.

Make sure the resume template has placeholder for the fields that will need to be populated.

### Benefits

- **Consistent Formatting**: PDFs ensure that your resume and cover letter look the same on any device or software, preserving your document's layout and design.
- **Widely Accepted**: Most job application systems and employers prefer or require PDFs due to their compatibility and security features.
- **Professional Appearance**: PDFs provide a professional look to your documents, which can make a positive impression on potential employers.

### Setup

To enable the conversion of DOCX documents to PDFs, you need to have LibreOffice installed on your system. LibreOffice is a free and open-source office suite that includes a command-line tool for converting documents to various formats, including PDF.

#### Installation of LibreOffice

- **Windows**: Download and install LibreOffice from [the official website](https://www.libreoffice.org/download/download/). During installation, ensure that the option to add LibreOffice to the system PATH is selected.
- **macOS**: Install LibreOffice using Homebrew with the command `brew install --cask libreoffice`, or download it from the official website.
- **Linux**: Use your distribution's package manager to install LibreOffice. For example, on Ubuntu, you can use `sudo apt-get install libreoffice`.

#### Configuration

After installing LibreOffice, you need to ensure that the `create_pdf` option in the `utils/config.py` file is set to `True`.

This setting instructs the script to convert the generated DOCX files (resumes and cover letters) into PDF format. The conversion process is handled automatically by the script using the LibreOffice command-line interface.

### Troubleshooting

If you encounter issues with PDF conversion, ensure the following:

- LibreOffice is correctly installed and accessible from the command line. You can test this by running `soffice --version` in your terminal.
- The `create_pdf` option in `config.py` is set to `True`.
- Your system's PATH environment variable includes the directory where LibreOffice is installed.

By following these steps and ensuring your system is correctly configured, you can take advantage of the PDF conversion feature to create professional-looking resumes and cover letters that are ready for submission to job application systems.

# Notion Integration

The custom resume and cover letter generator supports integration with Notion, allowing users to automatically update a Notion database with job application details. This feature is particularly useful for tracking job applications and organizing job search efforts.

## Setting Up Notion API

To use the Notion integration, you first need to set up the Notion API and obtain the necessary credentials. Follow these steps to get started:

1. **Create a Notion Integration**:

   - Go to [Notion Integrations](https://www.notion.so/my-integrations) and click on the "+ New integration" button.
   - Give your integration a name, associate it with your workspace, and note down the "Internal Integration Token" provided. This token will be used as your `NOTION_INTEGRATION_TOKEN` environment variable.

2. **Share a Database with Your Integration**:

   - Create a new database in Notion or use an existing one.
   - Click on the "Share" button at the top right of the database page, and add your integration by searching for the name you gave it.
   - Once added, your integration can now access and modify this database.

3. **Find Your Database ID**:
   - The database ID can be found in the URL when you open your database in a web browser. The URL format is `https://www.notion.so/{workspace_name}/{database_id}?v={view_id}`. The `database_id` is the string between the last slash (`/`) and the question mark (`?`).

## Configuration

To enable Notion integration in the custom resume and cover letter generator, you need to update the `utils/config.py` file and set environment variables:

- **Environment Variable**:

  - Set `NOTION_INTEGRATION_TOKEN` in your environment variables to the token you obtained when creating your Notion integration.

- **Config File (`utils/config.py`)**:
  - Set `save_to_notion` to `True` in the `notion_config` dictionary.
  - Update the `database_id` field with your Notion database ID.

## Notion Database Fields

The following table outlines the fields that the script will create in the Notion database, their sources, and their default values if not known.

| Field Name       | Source                        | Default Value | Description                                                                               |
| ---------------- | ----------------------------- | ------------- | ----------------------------------------------------------------------------------------- |
| Job Title        | `job_details` from AI         | "unknown"     | The title of the job obtained from the job search process.                                |
| Company Name     | `job_details` from AI         | "unknown"     | The name of the company offering the job.                                                 |
| Company Industry | `job_details` from AI         | "unknown"     | The industry sector the company belongs to.                                               |
| Salary Range     | `job_details` from AI         | "unknown"     | The salary range offered for the job.                                                     |
| Job URL          | `job_description` from output | "unknown"     | The URL to the job posting. If not present in the job description, defaults to "unknown". |
| Job Location     | `job_details` from AI         | "unknown"     | The location where the job is based.                                                      |
| Role Seniority   | `job_details` from AI         | "unknown"     | The seniority level required for the job.                                                 |
| Role Discipline  | `job_details` from AI         | "unknown"     | The discipline or field the job is related to.                                            |

- If any of the fields are not explicitly provided by their respective sources, they will default to "unknown". This ensures that the Notion database update process can proceed without errors, even if some information is missing.

## Usage

To generate a custom resume and cover letter, simply run the main script:
python main.py

This will initiate the scraping process (if enabled), analyze the job descriptions, and generate customized documents based on the provided resume and job listings.

## Credits

This library utilizes the Crew AI library for processing and generating text. For more information, visit [Crew AI](https://www.crewai.com/).

## License

This project is open-sourced under the MIT license. Feel free to fork, modify, and use it in your projects.

## Contact

For questions or feedback, reach out to me, Peter Isaac, on Twitter: [https://twitter.com/mr_pisaac](https://twitter.com/mr_pisaac).

## Best Practices

- Always review the generated documents for accuracy and personal touch.
- Keep your `resume.docx` and template resume up-to-date in the `default_resume` folder.
- Regularly update the `config.py` file to reflect changes in job listing URLs or your personal information.
- Test the library with different job descriptions to ensure it meets your needs.
- Contribute to the library by sharing improvements or reporting issues.

Happy job hunting!
