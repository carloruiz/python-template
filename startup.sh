#!/bin/bash

find . -type f -not -path '*/\.*' -exec sed -i '' "s/APP/$1/g" {} +
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

