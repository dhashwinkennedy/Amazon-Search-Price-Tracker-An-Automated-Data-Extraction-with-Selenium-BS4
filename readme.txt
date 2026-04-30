# Amazon Search Price Tracker

A Python-based web scraping project that automates the collection of product identifiers (ASINs) and pricing from Amazon search results using **Selenium** and **BeautifulSoup4**.  
This project is intended to demonstrate dynamic web page automation, data extraction, and local JSON-based data storage.

---

## Features

- **Dynamic scraping** using Selenium for JavaScript-rendered pages
- **ASIN extraction** from Amazon search result cards
- **Price extraction** from search result listings
- **Automated pagination** across multiple result pages
- **Driver auto-management** with `webdriver-manager`
- **Local data persistence** using `data.json`
- **Randomized delays** to simulate more natural browsing behavior

---

## Tech Stack

- Python 3.x
- Selenium
- BeautifulSoup4
- webdriver-manager
- JSON

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/dhashwinkennedy/Amazon-Search-Price-Tracker-An-Automated-Data-Extraction-with-Selenium-BS4


### 2. Install dependencies
'''bash
pip install -r requirements.txt

## WebDriver Setup

This project uses **webdriver-manager**, so you do not need to manually download **chromedriver.exe**.

## Usage

'''bash
python main.py

## Output Format

The scraped data is stored in JSON format.

''json
{
  "B0XXXXXXX1": {
    "2026-04-30": 7999
  },
  "B0XXXXXXX2": {
    "2026-04-30": 12999
  }
}

Each ASIN maps to a dictionary containing the date and the extracted price.

## ⚠️ Educational Use Disclaimer

This project is developed strictly for **educational and learning purposes only**.

It is intended to demonstrate concepts such as:
- Web scraping and data extraction  
- Browser automation using Selenium  
- HTML parsing with BeautifulSoup  
- Data handling and storage using JSON  

This project is **not intended for commercial use, production deployment, or large-scale data collection**.

---

### Compliance Notice

This project is **not affiliated with, endorsed by, or connected to** Amazon or any of its services.

Please be aware that Amazon’s Terms of Service may restrict or prohibit automated data collection, scraping, or bot usage.  
By using this project, you agree that:

- You are solely responsible for ensuring compliance with all applicable **website terms, policies, and legal regulations**  
- You will not use this project in a way that violates any platform’s terms of service  
- You understand the risks associated with automated access to third-party websites  

---

### Responsible Usage

Use this project responsibly and ethically.  
It is recommended to use it only for:
- Personal learning  
- Experimentation  
- Academic purposes  

---

**The author assumes no responsibility or liability for any misuse of this project.**
