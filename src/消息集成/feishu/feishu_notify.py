import requests
import json
import os
import time
import hmac
import hashlib
import base64
from get_build_status import get_build_status

# 获取构建状态
BUILD_STATUS = get_build_status()

# 从环境变量获取参数（Jenkins自动注入）
webhook_url = os.getenv("WEBHOOK_URL")  # Webhook地址
secret_key = os.getenv("SECRET_KEY")  # 签名密钥（可选）
job_name = os.getenv("JOB_NAME")  # 任务名称
build_status = BUILD_STATUS  # 状态（SUCCESS/FAILURE）
build_url = os.getenv("BUILD_URL")  # 构建链接
build_user_id = 'cac8efb4'  # 构建人的飞书用户 ID


def generate_sign(timestamp, secret):
    """根据飞书文档生成签名
    :param timestamp: 时间戳（需与消息中的timestamp一致）
    :param secret: 机器人密钥
    :return: 签名"""
    string_to_sign = f"{timestamp}\n{secret}".encode('utf-8')
    hmac_code = hmac.new(string_to_sign, digestmod=hashlib.sha256).digest()
    return base64.b64encode(hmac_code).decode('utf-8')


# 构建消息体（卡片格式）
message = {
    "msg_type": "interactive",
    "card": {
        "header": {
            "title": {"content": "Jenkins构建通知", "tag": "plain_text"},
            "template": "blue" if build_status == "SUCCESS" else "red"
        },
        "elements": [{
            "tag": "div",
            "fields": [
                {"is_short": False,
                 "text": {"content": f"​​**​​任务名称：​​**​​{job_name}", "tag": "lark_md"}},
                {"is_short": False,
                 "text": {
                     "content": f"​​**​​构建状态：​​**​​<font color='{'green' if build_status == 'SUCCESS' else 'red'}'>{build_status}</font>",
                     "tag": "lark_md"}},
                {"is_short": False,
                 "text": {"content": f"​​**​​构建详情：​​**​​[点击查看详情]({build_url})", "tag": "lark_md"}}
            ]
        },
            # 实现@单个用户
            {
                "tag": "div",
                "text": {
                    "content": f"请 <at id={build_user_id}></at> 关注本次构建结果。",
                    "tag": "lark_md"
                }
            },
            # 实现@所有人
            # {
            #     "tag": "div",
            #     "text": {
            #         "content": f"请 <at id=all></at> 关注本次构建结果。",
            #         "tag": "lark_md"
            #     }
            # }
        ]
    }
}

# 添加签名（如果启用了签名校验）
if secret_key:
    timestamp = str(int(time.time()))
    message.update({
        "timestamp": timestamp,
        "sign": generate_sign(timestamp, secret_key)
    })

# 发送请求
response = requests.post(webhook_url, json=message)
print("飞书通知发送结果:", response.text)
