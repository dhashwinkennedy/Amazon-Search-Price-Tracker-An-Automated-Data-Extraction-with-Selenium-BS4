<div align="center">

# 🛒 Amazon Search Price Tracker

### Automated product intelligence — scrape ASINs & pricing from Amazon search results at scale

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=FFD43B)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?style=flat-square&logo=selenium&logoColor=white)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-Parsing-8B0000?style=flat-square&logo=python&logoColor=white)
![WebDriver Manager](https://img.shields.io/badge/webdriver--manager-Auto%20Driver-FF6F00?style=flat-square&logo=googlechrome&logoColor=white)
![JSON](https://img.shields.io/badge/Storage-JSON-292929?style=flat-square&logo=json&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)
![Status](https://img.shields.io/badge/Status-Educational-6366F1?style=flat-square)

<br/>

> **A Python-based web scraping project** that automates the collection of product identifiers (ASINs) and pricing  
> from Amazon search results using **Selenium** and **BeautifulSoup4** — demonstrating dynamic page automation,  
> structured data extraction, and local JSON-based persistence.

</div>

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🌐 **Dynamic Scraping** | Uses Selenium to handle JavaScript-rendered pages |
| 🔖 **ASIN Extraction** | Pulls unique product identifiers from search result cards |
| 💰 **Price Extraction** | Collects pricing data directly from search listings |
| 📄 **Automated Pagination** | Traverses multiple result pages automatically |
| 🔧 **Driver Auto-Management** | Powered by `webdriver-manager` — no manual ChromeDriver setup |
| 💾 **Local Data Persistence** | Saves structured output to `data.json` |
| ⏱️ **Randomized Delays** | Simulates natural browsing behavior to reduce detection risk |

---

## 🛠️ Tech Stack

<table>
  <tr>
    <td align="center" width="140">
      <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=FFD43B" /><br/>
      <sub><b>Core Language</b></sub>
    </td>
    <td align="center" width="140">
      <img src="https://img.shields.io/badge/-Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white" /><br/>
      <sub><b>Browser Automation</b></sub>
    </td>
    <td align="center" width="140">
      <img src="https://img.shields.io/badge/-BeautifulSoup4-8B0000?style=flat-square&logo=python&logoColor=white" /><br/>
      <sub><b>HTML Parsing</b></sub>
    </td>
    <td align="center" width="140">
      <img src="https://img.shields.io/badge/-webdriver--manager-FF6F00?style=flat-square&logo=googlechrome&logoColor=white" /><br/>
      <sub><b>Driver Management</b></sub>
    </td>
    <td align="center" width="140">
      <img src="https://img.shields.io/badge/-JSON-292929?style=flat-square&logo=json&logoColor=white" /><br/>
      <sub><b>Data Storage</b></sub>
    </td>
  </tr>
</table>

---

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dhashwinkennedy/Amazon-Search-Price-Tracker-An-Automated-Data-Extraction-with-Selenium-BS4
cd your-repo-name
```

### 2️⃣ (Recommended) Create a Virtual Environment

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`**

```
selenium
beautifulsoup4
webdriver-manager
```

---

## ▶️ Usage

### Running the Scraper

```bash
python main.py
```

The script will:

1. 🌐 Open a Chrome browser session via Selenium
2. 🔍 Navigate to Amazon search results for the configured query
3. 📋 Extract ASINs and prices from each product card on the page
4. 📄 Automatically advance to subsequent pages
5. 💾 Append all collected data to `data.json`

---

## 📦 Output Format

All scraped records are saved locally to `data.json`. Each entry follows this structure:

```json
[
  {
    "asin": "B09XYZ1234",
    "price": "$29.99"
  },
  {
    "asin": "B08ABC5678",
    "price": "$14.49"
  }
]
```

---

## 📁 Project Structure

```
your-repo-name/
├── main.py              # Entry point — orchestrates the scraping workflow
├── scraper.py           # Core scraping logic (Selenium + BeautifulSoup4)
├── data.json            # Output file — persisted ASIN & price records
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚖️ Legal & Ethical Considerations

> [!WARNING]
> **Educational Use Only**
>
> This project is developed **strictly for educational and research purposes** to demonstrate web automation and data parsing techniques. It is **not intended for commercial use**, large-scale data harvesting, or any activity that violates applicable laws or platform terms of service.

> [!IMPORTANT]
> **Amazon Terms of Service Compliance**
>
> Automated scraping of Amazon's website may violate their [Conditions of Use](https://www.amazon.com/gp/help/customer/display.html?nodeId=508088). By using this project, you acknowledge that:
>
> - You are solely responsible for how you use this tool
> - Amazon's robots.txt and ToS should be respected at all times
> - This tool should **never** be used in production or at commercial scale
> - The authors assume **no liability** for misuse of this codebase

> [!NOTE]
> **Responsible Usage Guidelines**
>
> ✅ Use only for personal learning and academic research  
> ✅ Limit request frequency to avoid server strain  
> ✅ Review and comply with the target site's Terms of Service before use  
> ❌ Do not use for commercial data collection  
> ❌ Do not deploy at scale or in automated pipelines without explicit permission  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/dhashwinkennedy/Amazon-Search-Price-Tracker-An-Automated-Data-Extraction-with-Selenium-BS4/issues).

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with 🐍 Python · 🌐 Selenium · 🍜 BeautifulSoup4

*Built for learning. Use responsibly.*

</div>