import requests
import jsonpath
import yaml
'''
pip install PyYaml
import yaml
yaml.load()  json转字典
yaml.dump(data,file)  写入yaml  data写入数据 file文件
'''
def weixin_token():
        '''获取token'''
        url = ''
        response = requests.get(url=url)
        # 格式化服务端返回的值
        result = response.json()
        token = jsonpath.jsonpath(result, "$.access_token")[0]
        # print(token)
        return token

def read_yaml(file):
        '''读取'''
        file = open(file, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        return file_data
def write_yaml(file,data1):
        '''写入'''
        data={"token":data1}
        print(data)
        file = open(file, 'w', encoding='utf-8')
        yaml.dump(data,file)
        file.close()
print(weixin_token())

print(write_yaml('token.yaml',weixin_token()))
print(read_yaml('token.yaml'))
