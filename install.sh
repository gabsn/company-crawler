#!/bin/bash

PROJECT_NAME=company-crawler

echo "Installing virtualenv..."
if [ -n "$(pip list | grep -F virtualenv)" ]; then
    pip install virtualenv
fi

echo "Installing virtualenvwrapper..."
if [ -n "$(pip list | grep -F virtualenvwrapper)" ]; then
    export WORKON_HOME=$HOME/.virtualenvs
fi

echo "Creating $PROJECT_NAME environment..."
source `which virtualenvwrapper.sh`
if [ ! -d $WORKON_HOME/$PROJECT_NAME ]; then
    mkvirtualenv $PROJECT_NAME
    workon $PROJECT_NAME
    pip install -r requirements.txt
else
    echo "$PROJECT_NAME environment already exists."
fi

echo "Adding binaries to \$PATH..."
export COMPANY_CRAWLER=$(pwd)
if [ $(echo $PATH | grep -q "$COMPANY_CRAWLER/bin") ]; then
    export PATH=$PATH:$COMPANY_CRAWLER/bin
fi
    echo "Binaries already added to \$PATH."

echo "Installed successfully!\n"
echo "Use: crawl [links|companies]\n"
