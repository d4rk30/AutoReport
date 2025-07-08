from docxtpl import DocxTemplate
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')

context_v8 = {
    'fileID': 'K01-policy-202508',
    'v8_test_time': today,
    'v8_explanation': '此次在8.26801基础上新增了8条、优化了0条。此次规则更新在组件防护方面有显著效果',
    'v8_rule1': '增加了请求中检测到金蝶Apusic中间件存在jndi注入漏洞',
    'v8_rule2': '增加了请求中检测到泛微ecology9 FileDownloadLocation任意文件下载漏洞',
    'v8_rule3': '增加了请求中检测到畅捷通T+ InitContext处存在登录绕过漏洞',
    'v8_rule4': '增加了请求中检测到畅捷通T+ Save*InfoToFile处存在任意文件上传漏洞',
    'v8_rule5': '增加了请求中检测到畅捷通T+ Get*All处存在敏感信息泄露漏洞',
    'v8_rule_version': '8.26901',
    'v8_bin_name': '8.26901.bin',
    'v8_md5': '5bbaf353539d1b301176d78ce083c482'
}

context_v9 = {
    'fileID': 'K01-policy-202508',
    'v9_test_time': today,
    'v9_explanation': '此次在9.268基础上新增了8条、优化了0条。此次规则更新在组件防护方面有显著效果',
    'v9_rule1': '增加了请求中检测到金蝶Apusic中间件存在jndi注入漏洞',
    'v9_rule2': '增加了请求中检测到泛微ecology9 FileDownloadLocation任意文件下载漏洞',
    'v9_rule3': '增加了请求中检测到畅捷通T+ InitContext处存在登录绕过漏洞',
    'v9_rule4': '增加了请求中检测到畅捷通T+ Save*InfoToFile处存在任意文件上传漏洞',
    'v9_rule5': '增加了请求中检测到畅捷通T+ Get*All处存在敏感信息泄露漏洞',
    'v9_rule_version': '9.268',
    'v9_bin_name': '9.268.bin',
    'v9_md5': '5bbaf353539d1b301176d78ce083c482',
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
    generate_report_v9()
