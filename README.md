# Company crawler

Crawling of Linkedin company pages and building of the database associated.

## Setup

1. Install pip

  ```bash
  sudo apt-get install pip
  ```

2. Clone the project

  ```bash
  cd $(PROJECT_ROOT)
  git clone https://github.com/gabsn/company-crawler.git
  cd company-crawler
  source install.sh
  ```

## Commands

1. Get all company page urls and put them in a Mongo database

  ```bash
  crawl links
  ```

2. Download each company page, parse it and put the data in another database

  ```bash
  crawl companies
  ```
