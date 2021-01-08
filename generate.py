#! /usr/bin/python3

import sys
import os
import errno
import yaml
import requests
from shutil import copyfile

def generate_site():
    try:
        dist = 'dist'
        os.makedirs(dist)

        files_to_copy = [
            "_config.yml",
            "Gemfile",
            "404.html",
            "Gemfile.lock",
        ]

        for file_to_copy in files_to_copy:
            copyfile(
                'templates/' + file_to_copy, 
                dist + '/' + file_to_copy
            )

        with open(r'.site.yaml') as file:
            site_config = yaml.load(file, Loader=yaml.FullLoader)
            print(site_config)


        update_config("dist/_config.yml", site_config["website"])

        for page in site_config["pages"]:
            page_file = dist + '/' + page["name"].strip().lower() + ".md"
            copyfile('templates/page-template.md', page_file)

            response = requests.get(page["discourseTopic"] + ".json")
            content = response.json()["post_stream"]["posts"][0]["cooked"]

            update_page(page_file, page["siteUrl"], content)

    except OSError as e:
        if e.errno == errno.EEXIST:
            print('Snap name already generated')

def update_page(file_name, url, content):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    file_contents = file_contents.replace('PERMALINK', url)
    file_contents = file_contents.replace('CONTENT', content)

    with open(file_name, 'w') as file_handle:
        file_handle.write(file_contents)

def update_config(file_name, config):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    file_contents = file_contents.replace('TITLE', config["name"])
    file_contents = file_contents.replace('BASEURL', config["baseUrl"])
    file_contents = file_contents.replace('URL', config["url"])

    with open(file_name, 'w') as file_handle:
        file_handle.write(file_contents)


generate_site()