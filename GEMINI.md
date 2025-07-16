# Gemini Project Configuration (GEMINI.md)

## Project Overview

This project appears to be a Flask web application named "AutoReport". Its primary function seems to be generating Word document (.docx) reports from templates, likely based on uploaded data or predefined rules.

## Key Technologies

- **Backend:** Python, Flask
- **Templating:** Jinja2 (for HTML), docxtpl (for .docx)
- **Document Handling:** python-docx, docxcompose

## Project Structure

- `app.py`: The main Flask application file.
- `requirements.txt`: Python dependencies.
- `templates/`: Contains HTML templates for the web UI.
- `static/`: Holds static assets like CSS and JavaScript.
- `uploads/`: Likely the destination for user-uploaded files.
- `规则库报告/`: Contains Python scripts and `.docx` templates related to report generation.

## Common Commands

Please fill in or correct the commands below.

- **Install Dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
- **Run Application:**
  ```bash
  flask run
  ```
- **Run Tests:**
  ```bash
  # (e.g., pytest)
  ```
- **Lint Code:**
  ```bash
  # (e.g., ruff check . or flake8)
  ```

## Agent Instructions

- (Add any specific instructions or preferences for Gemini here.)
