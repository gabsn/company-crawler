#!/bin/bash

PROJECT_NAME=company-crawler
export CC_ROOT=$(pwd)

if [ -n $(pip list | grep -F virtualenvwrapper) ]; then
    echo "Installing virtualenvwrapper..."
    pip install virtualenvwrapper
    export WORKON_HOME=$HOME/.virtualenvs
fi

echo "Creating $PROJECT_NAME environment..."
source `which virtualenvwrapper.sh`
if [ ! -d $WORKON_HOME/$PROJECT_NAME ]; then
    mkvirtualenv $PROJECT_NAME
    workon $PROJECT_NAME
else
    echo "$PROJECT_NAME environment already exists."
fi

echo "Installing dependencies"
pip install -r requirements.txt

echo "Adding binaries to \$PATH..."
if [ -n $(echo $PATH | grep -q "$CC_ROOT/bin") ]; then
    export PATH=$CC_ROOT/bin:$PATH
fi
    echo "Binaries already added to \$PATH."

echo "Installed successfully!\n"
echo "Use: crawl [links|companies]\n"
