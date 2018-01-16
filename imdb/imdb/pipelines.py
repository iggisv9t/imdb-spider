# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


# CREATE TABLE all_data(movie_id TEXT, name TEXT, rating TEXT, rec TEXT, genre TEXT, country TEXT, director TEXT, date TEXT)

class ImdbPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect("./im.db")

    def process_item(self, item, spider):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO all_data VALUES " +
                    "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"\
                    .format(item['movie_id'], item['name']\
                    .replace("'", "''").replace('"', '""'), item['rating'], # replace ' and " for sqlite
                    '|'.join(item['rec']), '|'.join(item['genre']),
                    '|'.join(item['country']),
                    str(item['director']).replace("'", "''").replace('"', '""'),
                    item['date'])
        )
        self.conn.commit()
        return item
