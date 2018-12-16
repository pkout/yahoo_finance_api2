#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

rm -rf $DIR/../dist
python3 $DIR/../setup.py sdist
twine upload $DIR/../dist/*
