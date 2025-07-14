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
        # V8数据
        v8_doc_number = request.form.get('v8_doc_number')
        v8_test_time = request.form.get('v8_test_time')
        v8_version = request.form.get('v8_version')
        v8_release_notes = request.form.get('v8_release_notes')
        v8_rule1 = request.form.get('v8_rule1')
        v8_rule2 = request.form.get('v8_rule2')
        v8_rule3 = request.form.get('v8_rule3')
        v8_rule4 = request.form.get('v8_rule4')
        v8_rule5 = request.form.get('v8_rule5')
        
        # V9数据
        v9_doc_number = request.form.get('v9_doc_number')
        v9_test_time = request.form.get('v9_test_time')
        v9_version = request.form.get('v9_version')
        v9_release_notes = request.form.get('v9_release_notes')
        v9_rule1 = request.form.get('v9_rule1')
        v9_rule2 = request.form.get('v9_rule2')
        v9_rule3 = request.form.get('v9_rule3')
        v9_rule4 = request.form.get('v9_rule4')
        v9_rule5 = request.form.get('v9_rule5')
        
        # 同步选项
        same_doc_number = request.form.get('same_doc_number')
        same_test_time = request.form.get('same_test_time')
        same_version = request.form.get('same_version')
        same_release_notes = request.form.get('same_release_notes')
        same_rule1 = request.form.get('same_rule1')
        same_rule2 = request.form.get('same_rule2')
        same_rule3 = request.form.get('same_rule3')
        same_rule4 = request.form.get('same_rule4')
        same_rule5 = request.form.get('same_rule5')
        
        # 处理文件上传
        uploaded_v8_file = None
        uploaded_v9_file = None
        
        # V8文件上传
        if 'v8_bin_file' in request.files:
            file = request.files['v8_bin_file']
            if file and file.filename != '':
                if allowed_file(file.filename):
                    filename = secure_filename(f"v8_{file.filename}")
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    uploaded_v8_file = filename
                    flash(f'V8文件 {filename} 上传成功！', 'success')
                else:
                    flash('V8文件格式不支持！', 'error')
        
        # V9文件上传
        if 'v9_bin_file' in request.files:
            file = request.files['v9_bin_file']
            if file and file.filename != '':
                if allowed_file(file.filename):
                    filename = secure_filename(f"v9_{file.filename}")
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    uploaded_v9_file = filename
                    flash(f'V9文件 {filename} 上传成功！', 'success')
                else:
                    flash('V9文件格式不支持！', 'error')
        
        # 这里可以添加数据保存逻辑
        flash('表单提交成功！', 'success')
        
        # 打印表单数据（用于调试）
        print("=== V8版本 ===")
        print(f"V8文档编号: {v8_doc_number}")
        print(f"V8送测时间: {v8_test_time}")
        print(f"V8版本号: {v8_version}")
        print(f"V8发布说明: {v8_release_notes}")
        print(f"V8规则1: {v8_rule1}")
        print(f"V8规则2: {v8_rule2}")
        print(f"V8规则3: {v8_rule3}")
        print(f"V8规则4: {v8_rule4}")
        print(f"V8规则5: {v8_rule5}")
        print(f"V8上传文件: {uploaded_v8_file}")
        print("=== V9版本 ===")
        print(f"V9文档编号: {v9_doc_number}")
        print(f"V9送测时间: {v9_test_time}")
        print(f"V9版本号: {v9_version}")
        print(f"V9发布说明: {v9_release_notes}")
        print(f"V9规则1: {v9_rule1}")
        print(f"V9规则2: {v9_rule2}")
        print(f"V9规则3: {v9_rule3}")
        print(f"V9规则4: {v9_rule4}")
        print(f"V9规则5: {v9_rule5}")
        print(f"V9上传文件: {uploaded_v9_file}")
        print("=== 同步选项 ===")
        print(f"文档编号同步: {same_doc_number}")
        print(f"送测时间同步: {same_test_time}")
        print(f"版本号同步: {same_version}")
        print(f"发布说明同步: {same_release_notes}")
        print(f"规则1同步: {same_rule1}")
        print(f"规则2同步: {same_rule2}")
        print(f"规则3同步: {same_rule3}")
        print(f"规则4同步: {same_rule4}")
        print(f"规则5同步: {same_rule5}")
        
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 