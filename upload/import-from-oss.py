import os
import datetime
from notion_client import Client
from config import NOTION_TOKEN, DATABASE_ID

# 初始化 Notion 客户端
notion = Client(auth=NOTION_TOKEN)

# OSS 配置（修正区域）
BUCKET_NAME = "notionfiles"
REGION = "oss-cn-wuhan-lr"
OSS_BASE_URL = f"https://{BUCKET_NAME}.{REGION}.aliyuncs.com"

# 本地数据目录
DATA_DIR = "./data"
VALID_EXT = [".txt", ".docx"]

for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext not in VALID_EXT:
            continue

        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, DATA_DIR)
        oss_url = f"{OSS_BASE_URL}/{rel_path.replace(os.sep, '/')}"

        path_parts = rel_path.split(os.sep)
        author = path_parts[0]
        is_serial = "是" if len(path_parts) >= 3 else "否"
        title = os.path.splitext(file)[0]
        now = datetime.datetime.now().isoformat()

        try:
            # 创建 Notion 页面（新增字段：下载链接）
            response = notion.pages.create(
                parent={"database_id": DATABASE_ID},
                properties={
                    "作品标题": {"title": [{"text": {"content": title}}]},
                    "作者": {"multi_select": [{"name": author}]},
                    "类型": {"select": {"name": "文字"}},
                    "是否为连载": {"select": {"name": is_serial}},
                    "作品文件路径": {"rich_text": [{"text": {"content": rel_path}}]},
                    "导入时间": {"date": {"start": now}},
                    "下载链接": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": "点击下载",
                                    "link": {"url": oss_url}
                                }
                            }
                        ]
                    }
                }
            )

            # 获取页面 ID 并添加正文文件块
            page_id = response["id"]
            notion.blocks.children.append(
                block_id=page_id,
                children=[
                    {
                        "object": "block",
                        "type": "file",
                        "file": {
                            "type": "external",
                            "external": {
                                "url": oss_url
                            }
                        }
                    }
                ]
            )

            print(f"✅ 已导入：{title}（作者：{author}）")

        except Exception as e:
            print(f"❌ 导入失败：{rel_path}")
            print("错误信息：", e)
