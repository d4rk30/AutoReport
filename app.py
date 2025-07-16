

# app.py

import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from core.report_generator import generate_report

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 用于flash消息

# 配置上传文件夹和报告文件夹
UPLOAD_FOLDER = 'uploads'
REPORTS_DIR = 'reports'
ALLOWED_EXTENSIONS = {'bin'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['REPORTS_DIR'] = REPORTS_DIR

# 确保上传和报告文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 从表单获取数据
        form_data = request.form.to_dict()

        # 处理V8文件上传
        v8_file = request.files.get('v8_bin_file')
        v8_file_path = None
        if v8_file and allowed_file(v8_file.filename):
            filename = secure_filename(v8_file.filename)
            v8_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            v8_file.save(v8_file_path)
            flash(f'V8文件 {filename} 上传成功！', 'success')
        elif v8_file:
            flash('V8文件格式不支持！', 'error')
            return redirect(url_for('index'))

        # 处理V9文件上传
        v9_file = request.files.get('v9_bin_file')
        v9_file_path = None
        if v9_file and allowed_file(v9_file.filename):
            filename = secure_filename(v9_file.filename)
            v9_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            v9_file.save(v9_file_path)
            flash(f'V9文件 {filename} 上传成功！', 'success')
        elif v9_file:
            flash('V9文件格式不支持！', 'error')
            return redirect(url_for('index'))

        # 根据同步选项处理V9数据
        for key in ['doc_number', 'test_time', 'release_notes', 'rule1', 'rule2', 'rule3', 'rule4', 'rule5']:
            if f'same_{key}' in form_data:
                form_data[f'v9_{key}'] = form_data.get(f'v8_{key}')

        # 单独处理版本号的同步，因为V9版本号是转换而来的，不是直接复制
        if 'same_version' in form_data:
            # 前端JS已经处理了转换，后端直接从表单获取即可
            pass

        # 生成报告
        generated_files = []
        if v8_file_path:
            report_path = generate_report('v8', form_data, v8_file_path)
            generated_files.append(os.path.basename(report_path))
            flash(f'V8报告已生成: {os.path.basename(report_path)}', 'success')

        if v9_file_path:
            report_path = generate_report('v9', form_data, v9_file_path)
            generated_files.append(os.path.basename(report_path))
            flash(f'V9报告已生成: {os.path.basename(report_path)}', 'success')

        if not generated_files:
            flash('没有生成任何报告。', 'error')

        return render_template('index.html', generated_files=generated_files)

    return render_template('index.html')

@app.route('/reports/<filename>')
def download_report(filename):
    return send_from_directory(app.config['REPORTS_DIR'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
