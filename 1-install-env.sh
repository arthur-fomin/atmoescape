#!/bin/sh
python -m venv .venv
./.venv/bin/python -m pip install --index-url https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt 
