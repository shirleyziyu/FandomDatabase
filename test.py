from interface import spider_interface
from lofterCrawler.l9_author_txt import group_by_titles
from config.save_config import BASE_DATA_DIR
import os

def test_author():
    """
    测试爬取作者主页内容
    """
    author_url = "https://unreasonablebehaviour.lofter.com/" #测试样例
    spider_interface.crawl_author_homepage(author_url)

def test_group_by_title():
    """
    测试自动按系列标题分类保存的文章
    """
    author_name = "布恩迪亚"  # 手动填写作者名，需与保存目录一致
    file_path = os.path.join(BASE_DATA_DIR, author_name)
    group_by_titles(merge_titles=["大地兽为什么不会飞"], file_path=file_path, auto_group_title=False)

def test_like():
    like_url = "https://www.lofter.com/like"
    spider_interface.crawl_like_page(like_url, mode="like1")

def test_tag():
    tag_url = "https://www.lofter.com/tag/%E4%BA%9A%E7%89%B9%E5%85%B0%E8%92%82%E6%96%AF%E7%BA%AA%E4%BA%8B/total"
    spider_interface.crawl_like_page(tag_url, mode="tag")

if __name__ == "__main__":
    test_author()
    # test_group_by_title()
    # test_like()
    # test_tag()
