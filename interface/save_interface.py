import os
import re
from config.save_config import BASE_DATA_DIR

def sanitize_filename(name):
    """去除非法字符，适用于 Windows 文件系统"""
    return re.sub(r'[\\/:*?"<>|\r\n]', '_', name)

def generate_unique_filename(directory, base_name, ext=".txt"):
    """
    检查目标目录下是否已有同名文件，若有则添加递增编号
    """
    i = 1
    filename = f"{base_name}{ext}"
    while os.path.exists(os.path.join(directory, filename)):
        filename = f"{base_name} ({i}){ext}"
        i += 1
    return filename

def save_to_notion_format(content, author, title, content_type="article"):
    """
    保存为 Notion 接受的结构：
    - 结构：BASE_DATA_DIR/作者/作品名.txt
    - 可接受类型参数（目前预留，未来可扩展使用）
    """
    author = sanitize_filename(author)
    title = sanitize_filename(title or "untitled")

    save_dir = os.path.join(BASE_DATA_DIR, author)
    os.makedirs(save_dir, exist_ok=True)

    filename = generate_unique_filename(save_dir, title)
    file_path = os.path.join(save_dir, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"保存成功：{file_path}")
    return file_path
