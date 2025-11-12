#!/usr/bin/env bash

ruby_output=ruby.txt
python_output=python.txt

ruby main.rb $1 > $ruby_output
python3 main.py $1 > $python_output

diff -y --color=always $ruby_output $python_output

rm $ruby_output
rm $python_output
