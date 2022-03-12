import scrapy
import csv

class CryptoScraper(scrapy.Spider):
    name = 'crypto_spider'
    start_urls = ["https://www.investing.com/crypto/currencies"]
    output = "crypto_currencies.csv"

    def __init__(self):
        open(self.output, "w").close()

    def parse(self, response):
        crypto_body = response.css("tbody > tr")

        with open(self.output, "a+", newline="") as coin:
            writer = csv.writer(coin)

            for crypto in crypto_body:
                RANK = ".//td[@class='rank icon']/text()"
                NAME = "td > a ::text"
                SYMBOL = ".//td[@class='left noWrap elp symb js-currency-symbol']/text()"
                MARKET_CAP = ".js-market-cap::text"

                COINS = dict()

                COINS["rank"] = crypto.xpath(RANK).get()
                COINS["name"] = crypto.css(NAME).get()
                COINS["symbol"] = crypto.xpath(SYMBOL).get()
                COINS["market_cap"] = crypto.css(MARKET_CAP).get()

                writer.writerow([COINS["rank"], COINS["name"], COINS["symbol"], COINS["market_cap"]])
                yield print(COINS)
