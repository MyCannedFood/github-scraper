# GitHub Scraper

A powerful and efficient automated tool designed to scan GitHub profiles and organizations for specific keywords across all their repositories. Leveraging the power of Selenium and Firefox (GeckoDriver), this tool dives deep into repository contents to find exactly what you're looking for.


## Features

- Automated Discovery: Automatically identifies all public repositories under a target profile or organization.
- Deep Content Search: Scans the raw content of files within repositories for specific keywords.
- Real-time Feedback: Provides instant console output for found matches and scan progress.
- Robust Error Handling: Gracefully handles network issues, missing files, and timeouts.
- Modern Tech Stack: Built with Python and Selenium for maximum compatibility with modern web structures.

## Prerequisites

Before running the scraper, ensure you have the following installed:

1. **Python 3.7+**
2. **Firefox Browser**
3. **GeckoDriver** (Must be in your system PATH)
4. **Selenium**: `pip install selenium`

## Getting Started

### 1. Installation

Clone the repository and install the dependencies:

```bash
git clone <repository-url>
cd GithubScraper
pip install -r requirements.txt
```

### 2. Configuration

The script will prompt you for two inputs:
- `Target profile`: The GitHub username or organization name (e.g., `octocat`).
- `Target search key`: The keyword or string you want to find within the repositories.

### 3. Usage

Run the scraper using Python:

```bash
python githubScraper.py
```

## How it Works

1. Profile Navigation: The script navigates to the repositories tab of the target profile.
2. Repository Identification: It uses CSS selectors to identify and collect URLs for all available repositories.
3. File Scanning: For each repository, it lists files and accesses their "Raw" content.
4. Match Detection: It checks every file for the specified `target_key` and logs hits to the console.


## ️ Disclaimer

This tool is for educational and research purposes only. Please ensure you comply with GitHub's [Terms of Service](https://docs.github.com/en/site-policy/github-terms-of-service/github-terms-of-service) and [Rate Limiting policies](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting). Use responsibly!

---

<p align="center">
  Built with ❤️ for Security Researchers and Developers
</p>
