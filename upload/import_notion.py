import os
import datetime
from notion_client import Client
from config import NOTION_TOKEN, DATABASE_ID

# 初始化 Notion 客户端
notion = Client(auth=NOTION_TOKEN)

# 设置素材目录路径
data_dir = "./data"
valid_ext = [".txt", ".docx"]

# 遍历所有素材文件
for root, dirs, files in os.walk(data_dir):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext not in valid_ext:
            continue

        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, data_dir)
        path_parts = rel_path.split(os.sep)

        try:
            author = path_parts[0]
            is_serial = "是" if len(path_parts) >= 3 else "否"
            title = os.path.splitext(file)[0]

            # 打开文件内容作为上传附件
            with open(file_path, "rb") as f:
                file_data = f.read()

            # 创建页面 + 上传文件块
            response = notion.pages.create(
                parent={"database_id": DATABASE_ID},
                properties={
                    "作品标题": {"title": [{"text": {"content": title}}]},
                    "作者": {"multi_select": [{"name": author}]},
                    "类型": {"select": {"name": "文字"}},
                    "是否为连载": {"select": {"name": is_serial}},
                    "作品文件路径": {"rich_text": [{"text": {"content": rel_path}}]},
                    "导入时间": {"date": {"start": datetime.datetime.now().isoformat()}}
                }
            )

            # 获取页面 ID
            page_id = response["id"]

            # 上传文件为附件块
            upload_response = notion.blocks.children.append(
                block_id=page_id,
                children=[
                    {
                        "object": "block",
                        "type": "file",
                        "file": {
                            "type": "file",
                            "file": {
                                "name": file,
                                "data": file_data,
                            }
                        }
                    }
                ]
            )

            print(f"✅ 成功导入并上传文件：{title}（作者：{author}）")

        except Exception as e:
            print(f"❌ 导入失败：{file_path}")
            print("错误信息：", e)
