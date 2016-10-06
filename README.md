# Company crawler

Crawling of Linkedin company pages and building of the database associated.

## Setup

1. Install pip, virtualenv

  ```bash
  sudo apt-get install python-pip virtualenv
  ```

2. Clone the project

  ```bash
  git clone https://github.com/gabsn/company-crawler.git
  cd company-crawler
  ```
3. Create a new virtual environment
  
  ```bash
  virtualenv env
  source env/bin/activate
  pip install -r requirements.txt
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
