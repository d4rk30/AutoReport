
# core/report_generator.py

import os
import hashlib
from docxtpl import DocxTemplate
from datetime import datetime

# 获取当前脚本所在的目录
# os.path.dirname(__file__) 返回当前脚本的目录
# os.path.abspath() 将其转换为绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')  # 模板文件目录
REPORTS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'reports')  # 输出报告的目录

# 确保报告目录存在
os.makedirs(REPORTS_DIR, exist_ok=True)

def get_file_md5(file_path):
    """计算文件的MD5哈希值"""
    if not os.path.exists(file_path):
        return "文件未找到"
    
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def generate_report(version, data, bin_file_path):
    """
    通用报告生成函数

    :param version: 'v8' 或 'v9'
    :param data: 包含表单数据的字典
    :param bin_file_path: 上传的bin文件的路径
    """
    template_name = f'{version}_rule_template.docx'
    template_path = os.path.join(TEMPLATE_DIR, template_name)

    # 准备模板上下文
    context = {
        'fileID': data.get(f'{version}_doc_number'),
        f'{version}_test_time': data.get(f'{version}_test_time'),
        f'{version}_explanation': data.get(f'{version}_release_notes'),
        f'{version}_rules': [
            data.get(f'{version}_rule1'),
            data.get(f'{version}_rule2'),
            data.get(f'{version}_rule3'),
            data.get(f'{version}_rule4'),
            data.get(f'{version}_rule5'),
        ],
        f'{version}_rule_version': data.get(f'{version}_version'),
        f'{version}_bin_name': os.path.basename(bin_file_path),
        f'{version}_md5': get_file_md5(bin_file_path)
    }

    # 过滤掉空的规则
    context[f'{version}_rules'] = [rule for rule in context[f'{version}_rules'] if rule and rule.strip()]

    # 渲染模板
    tpl = DocxTemplate(template_path)
    tpl.render(context)

    # 保存文件
    output_filename = f'网络威胁联防阻断系统（网盾K01）规则库升级更新说明文档_{version}_{datetime.now().strftime("%Y%m%d%H%M%S")}.docx'
    output_path = os.path.join(REPORTS_DIR, output_filename)
    tpl.save(output_path)
    
    return output_path
