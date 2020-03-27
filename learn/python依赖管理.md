# 虚拟环境

> python3 自带 venv 工具

## 创建

```
python -m venv venv
```

## 激活虚拟环境

```
source venv/bin/activate
```

## 退出虚拟环境

```
deactivate
```

# 依赖管理-pip

- 生成requirements.txt文件

```
pip freeze > requirements.txt
```

- 重构项目环境

```
pip install -r requirements.txt
```

