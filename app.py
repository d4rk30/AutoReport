from flask import Flask, render_template, request, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 用于flash消息

# 配置上传文件夹
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'bin'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 确保上传文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取表单数据
        v9_version = request.form.get('v9_version')
        doc_number = request.form.get('doc_number')
        test_time = request.form.get('test_time')
        v9_release_notes = request.form.get('v9_release_notes')
        v9_rule1 = request.form.get('v9_rule1')
        v9_rule2 = request.form.get('v9_rule2')
        v9_rule3 = request.form.get('v9_rule3')
        v9_rule4 = request.form.get('v9_rule4')
        v9_rule5 = request.form.get('v9_rule5')
        
        # 处理文件上传
        uploaded_file = None
        if 'v9_bin_file' in request.files:
            file = request.files['v9_bin_file']
            if file and file.filename != '':
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    uploaded_file = filename
                    flash(f'文件 {filename} 上传成功！', 'success')
                else:
                    flash('不支持的文件格式！', 'error')
        
        # 这里可以添加数据保存逻辑
        flash('表单提交成功！', 'success')
        
        # 打印表单数据（用于调试）
        print(f"V9版本号: {v9_version}")
        print(f"文档编号: {doc_number}")
        print(f"送测时间: {test_time}")
        print(f"V9发布说明: {v9_release_notes}")
        print(f"V9规则1: {v9_rule1}")
        print(f"V9规则2: {v9_rule2}")
        print(f"V9规则3: {v9_rule3}")
        print(f"V9规则4: {v9_rule4}")
        print(f"V9规则5: {v9_rule5}")
        print(f"上传文件: {uploaded_file}")
        
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 