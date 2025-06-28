from notion_client import Client
from config import NOTION_TOKEN, DATABASE_ID

# 初始化 Notion 客户端
notion = Client(auth=NOTION_TOKEN)

# 尝试向数据库添加一个测试页面
try:
    response = notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "作品标题": {
                "title": [{"text": {"content": "测试连接成功"}}]
            },
            "作者": {
                "multi_select": [{"name": "系统"}]
            },
            "类型": {
                "select": {"name": "文字"}
            }
        }
    )
    print("✅ 连接成功！页面已创建。")
    print(f"页面链接：https://www.notion.so/{response['id'].replace('-', '')}")
except Exception as e:
    print("❌ 连接失败，请检查 token、数据库 ID 或权限设置")
    print("错误信息：", e)
