# K01规则交付文档生成器

一个基于Flask的Web应用程序，用于生成K01规则交付文档。

## 功能特性

- 美观的Bootstrap界面
- 完整的表单验证
- 文件上传功能
- 响应式设计
- Flash消息提示

## 表单字段

1. V9规则版本号
2. 文档编号
3. 送测时间
4. V9发布说明
5. V9规则1
6. V9规则2
7. V9规则3
8. V9规则4
9. V9规则5
10. V9 bin 包文件上传

## 安装和运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
python app.py
```

### 3. 访问应用

打开浏览器访问：http://localhost:8080

## 项目结构

```
AutoReport/
├── app.py                 # Flask主应用文件
├── requirements.txt       # Python依赖
├── README.md             # 项目说明
├── templates/
│   └── index.html        # 表单页面模板
├── static/
│   └── css/
│       └── style.css     # 自定义样式
└── uploads/              # 文件上传目录（自动创建）
```

## 技术栈

- **后端**: Flask
- **前端**: Bootstrap 5, Jinja2模板
- **样式**: 自定义CSS
- **文件处理**: Werkzeug

## 注意事项

- 支持的文件格式：.bin, .txt, .zip, .rar
- 上传的文件会保存在 `uploads/` 目录中
- 表单数据会在控制台打印（用于调试）
- 所有字段都是必填的 