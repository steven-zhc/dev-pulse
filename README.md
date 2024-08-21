# DevPulse

DevPulse is a developer tool designed to help users stay updated on the latest activities and trends in GitHub projects. It provides clear, concise insights into repository developments without requiring deep technical expertise.

## Features

- **GitHub Integration**: Fetch repository information, including recent commits, open issues, and pull requests.
- **LLM-Based Summarization**: Summarizes GitHub updates using Large Language Models (to be introduced in Version 1.0).
- **PostgreSQL Database Storage****: Stores repository data locally, allowing easy access without needing to re-enter repository locations.
- **Command-Line Interface (CLI)**: A simple, user-friendly CLI tool to interact with the GitHub API and the PostgreSQL database.
- **Web-Based UI**: (Planned for Version 1.0) A web interface to view and interact with repository data.

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- Git

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone git@github.com:steven-zhc/dev-pulse.git
   cd dev-pulse
   ```

2. **Set Up the Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL Database**
- Create a PostgreSQL database and user:

   ```bash
   psql postgres
   ```

   Inside the PostgreSQL shell:
   ```sql
   CREATE DATABASE devpulse_db;
   CREATE USER devpulse_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE devpulse_db TO devpulse_user;
   \q
   ```

5. **Set Up Environment Variables**

   Add your GitHub token and PostgreSQL credentials to your environment:

   ```bash
   export GITHUB_TOKEN=your_github_token
   export DATABASE_URL='postgresql://devpulse_user:your_password@localhost/devpulse_db'
   ```

# Usage
## Running the CLI Tool

Fetch repository information:

```bash
python src/cli.py <repo_owner/repo_name>
```

Example:

```bash
python src/cli.py octocat/Hello-World
```

## List All Stored Repositories

```bash
python src/cli.py
```
# Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

# License
This project is licensed under the MIT License.
