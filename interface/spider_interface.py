from lofterCrawler import l9_author_txt, l13_like_share_tag
from config.login_info import login_auth, login_key
from config.save_config import BASE_DATA_DIR


def crawl_author_homepage(
    link: str,
    target_tags: list = None,
    tags_filter_mode: str = "in",
    get_comm: int = 0,
    additional_break: int = 0,
    start_time: str = "",
    end_time: str = "",
    merge_titles: list = None,
    auto_chapter: int = 1,
    additional_chapter_index: int = 1,
    chapter_mode: str = "group"
):
    """
    爬取作者主页上的博客内容（文本/文章）
    """
    if target_tags is None:
        target_tags = []
    if merge_titles is None:
        merge_titles = []

    l9_author_txt.run(
        author_url=link,
        target_tags=target_tags,
        tags_filter_mode=tags_filter_mode,
        get_comm=get_comm,
        additional_break=additional_break,
        start_time=start_time,
        end_time=end_time,
        merge_titles=merge_titles,
        auto_chapter_handle=auto_chapter,
        additional_chapter_index=additional_chapter_index,
        chapter_mode=chapter_mode
    )



def crawl_like_page(
    link: str,
    mode: str = "like1",  # 可选值: like1, like2, share, tag
    save_mode: dict = None,
    classify_by_tag: int = 0,
    prior_tags: list = None,
    agg_non_prior_tag: int = 0,
    start_time: str = "",
    tag_filt_num: int = 50,
    min_hot: int = 0,
    print_level: int = 0,
    save_img_in_text: int = 0,
    base_path: str = BASE_DATA_DIR
):
    """
    爬取喜欢页、推荐页或 tag 页的博客内容。
    """
    if save_mode is None:
        save_mode = {"article": 1, "text": 0, "long article": 1, "img": 0}
    if prior_tags is None:
        prior_tags = []

    login_info = {"login_key": login_key, "login auth": login_auth}
    l13_like_share_tag.run(
        url=link,
        mode=mode,
        save_mode=save_mode,
        classify_by_tag=classify_by_tag,
        prior_tags=prior_tags,
        agg_non_prior_tag=agg_non_prior_tag,
        login_info=login_info,
        start_time=start_time,
        tag_filt_num=tag_filt_num,
        min_hot=min_hot,
        print_level=print_level,
        save_img_in_text=save_img_in_text,
        base_path=base_path
    )
