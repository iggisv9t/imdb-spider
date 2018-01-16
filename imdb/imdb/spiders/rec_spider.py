import scrapy
from imdb.items import MovieItem

class LikeSpider(scrapy.Spider):
    """docstring for LikeSpider."""
    name = 'rec'
    allowed_domains = ['www.imdb.com']

    def start_requests(self):
        with open('/home/sv9t/imdb/data/startlinks.txt') as fp:
            urls = [line[:-1] for line in fp]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,
                meta={'proxy':'http://YOU_RPROXY_IP:PORT'})

    def parse(self, response):
        item = MovieItem()
        item['name'] = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        item['director'] = response\
            .xpath('//span[@itemprop="director"]/a/span/text()').extract_first()
        item['genre'] = response\
            .xpath('//span[@itemprop="genre"]/text()').extract()
        item['movie_id'] = response\
            .xpath('//meta[@property="pageId"]/@content').extract_first()
        item['date'] = response\
            .xpath('//meta[@itemprop="datePublished"]/@content').extract_first()
        item['country'] = response\
            .xpath('//*[@id="titleDetails"]/div[2]/a/text()').extract()
        item['rating'] = response\
            .xpath('//span[@itemprop="ratingValue"]/text()').extract_first()
        item['rec'] = response\
            .xpath('//div[@class="rec_item"]/@data-tconst').extract()

        requests = []
        for mid in item['rec']:
            if mid not in self.ready_urls:
                url = 'http://www.imdb.com/title/{}/'.format(mid)
                # print('\n-----{}------'.format(url))
                requests.append(scrapy.Request(url=url, callback=self.parse,
                     meta={'proxy':'http://YOU_RPROXY_IP:PORT'}))
        return [item] + requests
