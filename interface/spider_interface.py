from lofterCrawler import l9_author_txt, l13_like_share_tag
from config.login_info import login_auth, login_key
from config.storage_config import data_root

def crawl_author_homepage(link: str):
    """爬取作者主页上的博客内容（文本/文章）"""
    l9_author_txt.run(
        author_url=link,
        target_tags=[],
        tags_filter_mode="in",
        get_comm=0,
        additional_break=0,
        start_time="",
        end_time="",
        merge_titles=[],
        auto_chapter_merge_title=1,
        additional_chapter_index=1
    )

def crawl_like_page(link: str, mode: str = "like1"):
    """爬取喜欢页、推荐页或tag页的博客内容。
    参数:
        link: 喜欢页或tag页链接
        mode: like1 / like2 / share / tag
    """
    login_info = {"login_key": login_key, "login auth": login_auth}
    l13_like_share_tag.run(
        url=link,
        mode=mode,
        save_mode={"article": 1, "text": 1, "long article": 1, "img": 0},
        classify_by_tag=0,
        prior_tags=[],
        agg_non_prior_tag=0,
        login_info=login_info,
        start_time="",
        tag_filt_num=50,
        min_hot=0,
        print_level=0,
        save_img_in_text=0,
        base_path="./data"
    )
