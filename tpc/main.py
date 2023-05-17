import tpc

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    # 참여자 명단
    blog_name_list = [
        "nx006",
        "studying-ddomi",
        "didrecord",
        "jjiye716",
        "gugu76",
    ]

    start_date = datetime(2023, 5, 14)
    end_date = datetime(2023, 5, 28)

    access_token: str = os.getenv('ACCESS_TOKEN')

    blog_posts = tpc.fetch_blog_posts_in_period_all(blog_name_list, start_date, end_date, access_token)
    for blog in blog_posts:
        print(f"Blog: {blog['blog_name']}")
        for post in blog['posts']:
            print(f"  Post: {post}")
