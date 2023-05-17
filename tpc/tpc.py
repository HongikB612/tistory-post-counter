# SPDX-FileCopyrightText: © 2023 Lee Junseon (nx006) <limazero14@gmail.com>
# SPDX-License-Identifier: Apache-2.0 license

from datetime import datetime

import requests


def fetch_blog_posts_in_period(user_blog_url, start_date, end_date, access_token):
    """
    Fetches a list of post URLs from a specified Tistory blog within a certain date range.

    Uses the Tistory API's post list endpoint (https://www.tistory.com/apis/post/list).

    For more detail, read tistory API here: https://tistory.github.io/document-tistory-apis/apis/v1/post/list.html

    Args:
        user_blog_url (str): The name of the Tistory blog.
        start_date (datetime.datetime): The start date of the range.
        end_date (datetime.datetime): The end date of the range.
        access_token (str): The access token for the Tistory API.

    Returns:
        list of str: A list of post URLs from the specified blog within the specified date range.
    """
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
    """
    Fetches a list of post URLs from a list of specified Tistory blogs within a certain date range.

    Uses the fetch_blog_posts_in_period function to fetch the posts from each individual blog.

    For more detail, read tistory API here: https://tistory.github.io/document-tistory-apis/apis/v1/post/list.html

    Args:
        user_blog_url_list (list of str): The list of Tistory blog names.
        start_date (datetime.datetime): The start date of the range.
        end_date (datetime.datetime): The end date of the range.
        access_token (str): The access token for the Tistory API.

    Returns:
        list of str: A list of post URLs from the specified blogs within the specified date range.
    """
    all_posts = []

    for user_blog_url in user_blog_url_list:
        user_posts = fetch_blog_posts_in_period(user_blog_url, start_date, end_date, access_token)
        all_posts.extend(user_posts)

    return all_posts