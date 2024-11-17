import json

a = [{"name":"小明"},{"name":"小李"}]
json_a = json.dumps(a, ensure_ascii=False)
print(type(json_a))
print(json_a)

py_a = json.loads(json_a)
print(type(a))
print(py_a)

b = '[{"name":"小明"},{"name":"小李"}]'
py1_a = json.loads(b)
print(type(py1_a))
print(py1_a)