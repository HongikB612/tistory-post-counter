# SPDX-FileCopyrightText: © 2023 Lee Junseon (nx006) <limazero14@gmail.com>
# SPDX-License-Identifier: Apache-2.0

import os
import webbrowser
from datetime import datetime

from dotenv import load_dotenv

import tpc

load_dotenv()

if __name__ == "__main__":
    # 참여자 명단
    blog_name_list = [
        "nx006",
        "jungmin402",
        "studying-ddomi",
        "didrecord",
        "jjiye716",
        "gugu76",
    ]

    start_date = datetime(2023, 5, 14)
    end_date = datetime(2023, 5, 28)

    access_token: str = os.getenv('ACCESS_TOKEN')
    if access_token == '' or access_token is None:
        client_id: str = os.getenv('CLIENT_ID')
        redirect_uri: str = os.getenv('REDIRECT_URI')

        auth_url: str = tpc.get_authorization_url(
            client_id=client_id,
            redirect_uri=redirect_uri,
        )

        print(f'Move to the following URL and authorize the app: {auth_url}')
        webbrowser.open(auth_url)
        code = input('Input provided code: ').strip()

        secret_key: str = os.getenv('SECRET_KEY')

        try:
            access_token = tpc.get_access_token(
                client_id=client_id,
                client_secret=secret_key,
                redirect_uri=redirect_uri,
                code=code
            )
        except Exception as e:
            print(e)
            exit(1)

    print(f'Access token: {access_token}')

    blog_posts = tpc.fetch_blog_posts_in_period_all(blog_name_list, start_date, end_date, access_token)
    for blog in blog_posts:
        print(f"Blog: {blog['blog_name']} : {len(blog['posts'])}")
        for post in blog['posts']:
            print(f"  Post: {post}")
