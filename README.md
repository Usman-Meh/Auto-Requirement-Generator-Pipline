#  Extracted Data from 20+ Websites and Automatically Extract Requirements

This repository contains a comprehensive project for extracting, processing, and analyzing course data from more than 20 university websites using **Selenium**, **Beautiful Soup (bs4)**, **pandas**, and **Gemini API**. The data is stored in Excel and text files and is formatted into a single CSV file for further analysis.

## Table of Contents
- [Features](#features)
- [Project Workflow](#project-workflow)
- [Data Sources](#data-sources)
- [Technologies Used](#technologies-used)
- [Pipeline Overview](#pipeline-overview)
- [Usage Instructions](#usage-instructions)
- [Folder Structure](#folder-structure)

## Features
- Extracted data from **20+ universities** across various countries.
- Automated web scraping with Selenium and Beautiful Soup.
- Data analysis and formatting using pandas.
- Conversion of extracted data into a single CSV file.
- Prompt generation with the Gemini API for JSON files.
- Multi-step pipeline for data transformation to meet user requirements.

## Project Workflow
1. **Check Existing Data**:
   - Verify if the university data is already present in the Excel file `extracted_web_names.xlsx`.
2. **Scrape New Data**:
   - Navigate to the "Web Data" folder and scrape missing university data using Selenium or Beautiful Soup.
3. **Data Processing**:
   - Format the scraped data using pandas and convert it to a user-friendly format (Excel or CSV).
4. **Prompt Generation**:
   - Use Gemini API to create JSON prompts for further data processing or analysis.
5. **Pipeline Execution**:
   - Consolidate all data of university  into a single CSV file same as all universities.

## Data Sources
### Example University Data:
| University Name                  | URL                                         | Country         |
|----------------------------------|---------------------------------------------|-----------------|
| Avondale University             | https://www.avondale.edu.au/                | Australia       |
| Flinders University             | https://www.flinders.edu.au/                | Australia       |
| Lehigh University               | https://www2.lehigh.edu/                    | United States   |
| Minnesota State University      | https://www.mnsu.edu/                       | United States   |

Full data is available in the `Web Data` folder.

## Technologies Used
- **Selenium**: For dynamic content scraping.
- **Beautiful Soup (bs4)**: For parsing HTML content.
- **pandas**: For data manipulation and formatting.
- **Gemini API**: For generating JSON prompts.
- **Python**: Core programming language for all scripts.

## Pipeline Overview
1. **Data Validation**:
   - Check if the university exists in `extracted_web_names.xlsx`.
2. **Web Scraping**:
   - Use Selenium or bs4 to scrape missing data from university websites.
3. **Data Cleaning**:
   - Clean and structure the scraped data using pandas.
4. **Data Formatting**:
   - Convert the cleaned data into Excel or CSV files as required.
5. **Consolidation**:
   - Merge all individual university data into a single CSV file for easy access.
6. **Prompt Creation**:
   - Generate JSON prompts using Gemini API for advanced analysis.

## Usage Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/Usman-Meh/Web-Scraping-University-Courses-Extracted-Data-from-20-Websites-Using-Selenium-and-Beautiful-Soup.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Check for existing data:
   - Open `extracted_web_names.xlsx` to verify if the university data is already available.
4. Scrape data:
   - Use the provided Selenium or Beautiful Soup scripts to scrape missing university data.
5. Process data:
   - Run the pandas scripts to clean and format the data.
6. Generate prompts:
   - Use the Gemini API script to create JSON files.
7. Consolidate data:
   - Execute the pipeline script to merge all data into a single CSV file.

## Folder Structure
```
.
|-- Web Data/                # Contains  Excel and txt files of university data.
|-- scripts/
    |-- selenium_scraper.py  # Selenium script for scraping dynamic data.
    |-- bs4_scraper.py       # Beautiful Soup script for static content.
    |-- data_processing.py   # pandas script for cleaning and formatting data.
    |-- gemini_prompt.py     # Script for generating JSON prompts using Gemini API.
    |-- pipeline.py          # Full pipeline to consolidate data.
|-- extracted_web_names.xlsx # Excel file listing scraped universities.
|-- requirements.txt         # List of dependencies.
|-- README.md                # Project documentation.
```

---
Feel free to contribute or raise issues for further enhancements!

