from interface import spider_interface

def test_author():
    author_url = "https://lishu310.lofter.com/"
    spider_interface.crawl_author_homepage(author_url)

def test_like():
    like_url = "https://www.lofter.com/like"
    spider_interface.crawl_like_page(like_url, mode="like1")

def test_tag():
    tag_url = "https://www.lofter.com/tag/%E4%BA%9A%E7%89%B9%E5%85%B0%E8%92%82%E6%96%AF%E7%BA%AA%E4%BA%8B/total"
    spider_interface.crawl_like_page(tag_url, mode="tag")

if __name__ == "__main__":
    test_author()
    # test_like()
    # test_tag()
