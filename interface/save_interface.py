import os
import re
from config.save_config import BASE_DATA_DIR
from lofterCrawler.l13_like_share_tag import filename_check

def sanitize_filename(name):
    name = name.replace("/", "&").replace("|", "&").replace("\\", "&").replace("<", "《") \
                .replace(">", "》").replace(":", "：").replace('"', '”').replace("?", "？").replace("*", "·"). \
                replace("\n", "").replace("(", "（").replace(
                ")", "）").replace(",", "，").replace("\t", " ")
    name = re.sub(r'[\ud800-\udfff]', '', name)
    name = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]').sub(' ', name)
    return name


def save_to_notion_format(content, author, filename, content_type="article", ext=".txt"):
    """
    保存为 BASE_DATA_DIR/作者/文件名.txt
    - 文件名已由 filename_check 预处理
    """
    author = sanitize_filename(author)
    filename = sanitize_filename(filename or ("untitled" + ext))

    save_dir = os.path.join(BASE_DATA_DIR, author)
    os.makedirs(save_dir, exist_ok=True)

    file_path = os.path.join(save_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"保存成功：{author} - {filename}")
    return file_path