from docxtpl import DocxTemplate
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')

context_v8 = {
    'fileID': 'K01-policy-202509',
    'v8_test_time': today,
    'v8_explanation': '此次在8.26901基础上调整了5条规则，新增了5条。此次规则更新在组件防护方面有显著效果',
    'v8_rule1': '增加了请求中检测到爱数AnyShare智能内容管理平台存在远程命令执行漏洞',
    'v8_rule2': '增加了请求中检测到明源云erp存在认证绕过漏洞',
    'v8_rule3': '增加了请求中检测到扁鹊飞救智能急救与质控系统GetLyfsByParams存在SQL注入漏洞',
    'v8_rule4': '增加了请求中检测到章管家存在任意用户添加漏洞',
    'v8_rule5': '增加了请求中检测到Unibox路由器pms_check.php存在远程命令执行漏洞',
    'v8_rule_version': '8.27001',
    'v8_bin_name': '8.27001.bin',
    'v8_md5': '085f524802ed33dd99853f17bcc13cbd'
}

context_v9 = {
    'fileID': 'K01-policy-202509',
    'v9_test_time': today,
    'v9_explanation': '此次在9.269基础上新增了6条规则。此次规则更新在组件防护方面有显著效果',
    'v9_rule1': '增加了请求中检测到爱数AnyShare智能内容管理平台存在远程命令执行漏洞',
    'v9_rule2': '增加了请求中检测到明源云erp存在认证绕过漏洞',
    'v9_rule3': '增加了请求中检测到扁鹊飞救智能急救与质控系统GetLyfsByParams存在SQL注入漏洞',
    'v9_rule4': '增加了请求中检测到章管家存在任意用户添加漏洞',
    'v9_rule5': '增加了请求中检测到Unibox路由器pms_check.php存在远程命令执行漏洞',
    'v9_rule_version': '9.270',
    'v9_bin_name': '9.270.bin',
    'v9_md5': '171b24ec5ab7434b1c7375d95b722529',
}


def generate_report_v8():
    tpl = DocxTemplate('v8_rule_template.docx')
    tpl.render(context_v8)
    tpl.save('网络威胁联防阻断系统（网盾K01）规则库升级更新说明文档.docx')


def generate_report_v9():
    tpl = DocxTemplate('v9_rule_template.docx')
    tpl.render(context_v9)
    tpl.save('网络威胁联防阻断系统（网盾K01）规则库升级更新说明文档.docx')


if __name__ == '__main__':
    generate_report_v8()
