#!/bin/bash

PROJECT_NAME=company-crawler
export CC_ROOT=$(pwd)

echo "Adding binaries to \$PATH...\n"
if [ -n $(echo $PATH | grep -q "$CC_ROOT/bin") ]; then
    export PATH=$CC_ROOT/bin:$PATH
fi

if [ -n $(echo $PYTHONPATH | grep -q "$CC_ROOT") ]; then
    export PYTHONPATH=$CC_ROOT:$PYTHONPATH
fi

echo "Use: crawl [links|companies]\n"
