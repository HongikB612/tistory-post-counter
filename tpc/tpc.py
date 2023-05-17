# SPDX-FileCopyrightText: © 2023 Lee Junseon (nx006) <limazero14@gmail.com>
# SPDX-License-Identifier: Apache-2.0 license

from datetime import datetime

import requests


def fetch_blog_posts_in_period(user_blog_url, start_date, end_date, access_token):
    posts = []
    page_number = 1

    while True:
        # Construct the API URL
        api_url = f"https://www.tistory.com/apis/post/list?access_token={access_token}&output=json&blogName={user_blog_url}&page={page_number}"

        # Fetch the JSON data from the API
        response = requests.get(api_url).json()

        # Extract the posts
        for post in response['tistory']['item']['posts']:
            post_date = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
            if start_date <= post_date <= end_date:
                posts.append(post['postUrl'])
            elif post_date < start_date:
                return posts  # Return early if we've moved past the date range

        # Increment the page number for the next iteration
        page_number += 1


def fetch_blog_posts_in_period_all(user_blog_url_list, start_date, end_date, access_token):
    all_posts = []

    for user_blog_url in user_blog_url_list:
        user_posts = fetch_blog_posts_in_period(user_blog_url, start_date, end_date, access_token)
        all_posts.extend(user_posts)

    return all_posts


