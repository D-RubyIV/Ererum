import sys

from flask import Flask, request, jsonify
import os
rest = Flask(__name__)

# Đảm bảo Flask tìm được các tệp tĩnh và templates khi ứng dụng đóng gói
if getattr(sys, 'frozen', False):
    # Khi ứng dụng chạy dưới dạng .exe
    bundle_dir = sys._MEIPASS
    rest.template_folder = os.path.join(bundle_dir, 'templates')
    rest.static_folder = os.path.join(bundle_dir, 'static')

records = []

@rest.route('/')
def home():
    return "Hello from Flask!"


