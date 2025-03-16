#!/bin/bash
echo "Cập nhật mã nguồn từ GitHub..."
git pull origin main

echo "Cài đặt các thư viện cần thiết..."
pip install -r requirements.txt

echo "Khởi chạy chương trình..."
python3 app.py
