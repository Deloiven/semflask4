import argparse
import time
import os
import requests

URLS = [
    'https://w.forfun.com/fetch/74/74739e1770f31cdbfdde99cc0b2925d3.jpeg',
    'https://w.forfun.com/fetch/3d/3d757d42200293776418dd0eb181a974.jpeg',
    'https://w.forfun.com/fetch/db/db6e862725f8e449427d1de5b2be0835.jpeg',
    'https://fikiwiki.com/uploads/posts/2022-02/1644965580_6-fikiwiki-com-p-kartinki-priroda-na-zastavku-telefona-6.jpg',
    'https://w.forfun.com/fetch/1f/1ff02e3ba9cecf53fa276611f21c6881.jpeg',
    'https://w.forfun.com/fetch/dd/ddd0eae2de4804b32793a55fa961ca15.jpeg'
    'https://w.forfun.com/fetch/98/98a1c8e3f881d7d684ca07efb39a5f0a.jpeg',
    'https://mobimg.b-cdn.net/v3/fetch/f4/f4e488ef69ea10573c0ce9cfbaf08643.jpeg'
]


start_func_time = time.time()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    return args.url_list


def img_saver(urls):
    if not os.path.exists('images'):
        os.makedirs('images')
    for url in urls:
        start_time = time.time()
        response = requests.get(url)
        filename = f'{url.split("/")[-1]}'
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.content)
        print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


if __name__ == '__main__':
    img_saver(URLS)   # for regular urls list
    # img_saver(create_parser())  # for args via cmd
    print(f'Elapsed time: {(time.time() - start_func_time):.2f} seconds')