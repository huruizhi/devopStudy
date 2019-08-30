Django 分页原理 / 日志

## 分页

1. 拿到page => str

2. 获取数据库数据

3. 对数据进行处理，分页

   end = page * 数量   start = (page - 1) * 数量

4. 转json

5. 返回HttpResponse

paginator 与 page对象

1. 总页数
2. 上一页 下一页

## 日志

1. 记录器 -- Logger
2. 处理程序 -- Handle
3. 过滤器 -- Filter
4. 格式化 -- Formatter

内置logger

- django 获取所有日志
- django.request 获取请求的日志

## View 

- TemplateView
- ListView
  - model
  - template_name
  - paginate_by

