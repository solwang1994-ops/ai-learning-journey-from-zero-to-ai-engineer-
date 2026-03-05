# ================================
# 🌐 Day 1: Hello Web - 让Python联网！
# 作者：老王
# 日期：2026年
# ================================

import requests
import re

def fetch_website_title(url):
    """
    获取指定网址的标题
    参数: url - 要访问的网站地址
    返回: 网页标题字符串，失败则返回None
    """
    try:
        print(f"🌐 正在访问：{url} ...")
        
        # 发送HTTP GET请求
        response = requests.get(url, timeout=10)
        response.encoding = response.apparent_encoding  # 自动检测编码
        
        # 检查响应状态码
        if response.status_code == 200:
            print("✅ 连接成功！")
            
            # 使用正则表达式提取<title>标签内容
            match = re.search(r'<title>(.*?)</title>', response.text, re.DOTALL)
            
            if match:
                title = match.group(1).strip()
                print(f"📰 网页标题是：【{title}】")
                return title
            else:
                print("❌ 未找到<title>标签")
                return None
        else:
            print(f"❌ 访问失败，状态码：{response.status_code}")
            return None
            
    except Exception as e:
        print(f"💥 发生错误：{e}")
        return None

if __name__ == "__main__":
    # 主程序入口
    print("=" * 50)
    print("🚀 老王的第一个AI联网程序启动！")
    print("=" * 50)
    
    # 测试目标1：百度
    target_url_1 = "https://www.baidu.com"
    fetch_website_title(target_url_1)
    
    print("-" * 50)
    
    # 测试目标2：Python官网（挑战题）
    target_url_2 = "https://www.python.org"
    fetch_website_title(target_url_2)
    
    print("=" * 50)
    print("✅ 今日任务完成！你已成功让Python‘上网’！")
    print("=" * 50)