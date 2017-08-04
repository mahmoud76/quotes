from scrapy import cmdline

cmdline.execute("scrapy crawl quotes -a category=life".split())
