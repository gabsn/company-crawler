#!/bin/bash

if [ -n "$(pip list | grep -F virtualenvwrapper)" ]; then
    export WORKON_HOME=$HOME/.virtualenvs
    #export PROJECT_HOME=$HOME/workspace
fi

source `which virtualenvwrapper.sh`
mkvirtualenv company-crawler
workon company-crawler
pip install -r requirements.txt
