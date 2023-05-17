# SPDX-FileCopyrightText: © 2023 Lee Junseon (nx006) <limazero14@gmail.com>
# SPDX-License-Identifier: Apache-2.0 license

from datetime import datetime
from typing import Union

import requests


def fetch_blog_posts_in_period(
        blog_name: str,
        start_date: datetime,
        end_date: datetime,
        access_token: str) -> list[str]:
    """
    Fetches a list of post URLs from a specified Tistory blog within a certain date range.

    Uses the Tistory API's post list endpoint (https://www.tistory.com/apis/post/list).

    For more detail, read tistory API here: https://tistory.github.io/document-tistory-apis/apis/v1/post/list.html

    Args:
        blog_name (str): The name of the Tistory blog.
        start_date (datetime.datetime): The start date of the range.
        end_date (datetime.datetime): The end date of the range.
        access_token (str): The access token for the Tistory API.

    Returns:
        list of str: A list of post URLs from the specified blog within the specified date range.
    """
    posts: list[str] = []
    page_number: int = 1

    while True:
        # Construct the API URL
        api_url: str = f"https://www.tistory.com/apis/post/list?access_token={access_token}&output=json&blogName={blog_name}&page={page_number}"

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


def fetch_blog_posts_in_period_all(
        user_blog_url_list: list[str],
        start_date: datetime,
        end_date: datetime,
        access_token: str) -> list[dict[str, Union[list[str], str]]]:
    """
    Fetches a list of post URLs from a list of specified Tistory blogs within a certain date range.

    Uses the fetch_blog_posts_in_period function to fetch the posts from each individual blog.

    Args:
        user_blog_url_list (list of str): The list of Tistory blog names.
        start_date (datetime.datetime): The start date of the range.
        end_date (datetime.datetime): The end date of the range.
        access_token (str): The access token for the Tistory API.

    Returns:
        list of dict: A list of dictionaries, where each dictionary represents a blog and contains
                      the blog name ('blog_name') and the list of post URLs ('posts') from that blog
                      within the specified date range.
    """
    all_posts: list[dict[str, Union[list[str], str]]] = []

    for user_blog_url in user_blog_url_list:
        user_posts = fetch_blog_posts_in_period(user_blog_url, start_date, end_date, access_token)
        all_posts.append({
            "blog_name": user_blog_url,
            "posts": user_posts,
        })

    return all_posts
