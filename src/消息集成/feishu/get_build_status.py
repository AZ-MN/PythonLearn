import requests


def get_build_status():
    # Jenkins 服务器的 URL
    jenkins_url = 'http://localhost:8080/'
    # Jenkins 用户名和 API Token
    username = 'Huxley'
    api_token = '1125ad1ac904cece9ca858e51f92d565b8'

    # 设定任务的名称
    job_name = 'Feishu_MSG'
    # 构建 URL
    build_url = f'{jenkins_url}/job/{job_name}/lastBuild/api/json'

    # 获取构建信息
    response = requests.get(build_url, auth=(username, api_token))
    build_info = response.json()

    # 打印获取的构建信息
    # print(build_info)

    # 检测构建状态
    build_status = build_info['result']

    if build_status is None:
        return None
    else:
        return build_status

