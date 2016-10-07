# Company crawler

Crawling of Linkedin company pages and building of the database associated.

## Setup for Ubuntu

1. Install pip and virtualenv

  ```bash
  sudo apt-get install python-pip virtualenv
  ```
  
2. Clone the project

  ```bash
  git clone https://github.com/gabsn/company-crawler.git
  cd company-crawler
  ```
  
3. Setup a virtual environment

  ```bash
  virtualenv env
  source env/bin/activate
  pip install -r requirements.txt
  ```
  
4. Setup your path

  ```bash
  source install.sh
  ```
  
5. [Install](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/) and setup the Mongo database

  ```bash
  sudo service mongod start
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
