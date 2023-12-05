import requests
import json
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def download_comments(subreddit):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Failed to download comments for subreddit {subreddit}. Status code: {response.status_code}")
        return None


def download_comments_with_threadpool(subreddit):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(download_comments, [subreddit]))
    return results[0]


def download_comments_with_processpool(subreddit):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(download_comments, [subreddit]))
    return results[0]


if __name__ == "__main__":
    subreddit_name = "YOUR_SUBREDDIT_NAME"

    print("Using ThreadPoolExecutor:")
    comments_threadpool = download_comments_with_threadpool(subreddit_name)

    if comments_threadpool is not None:
        print(f"Downloaded {len(comments_threadpool)} comments.")
    else:
        print("Failed to download comments.")

