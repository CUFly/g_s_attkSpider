import scrapy
from scrapy import Request
# from ..items import GSAttkspiderItem

class MitreSpider(scrapy.Spider):
    name = 'mitre'
    allowed_domains = ['attack.mitre.org']
    current_page = 1

    def start_requests(self):
        # start_urls = "https://attack.mitre.org/groups/G0001/"
        start_urls = "https://attack.mitre.org/software/S0001/"
        yield Request(start_urls)

    def parse(self, response):
        # try:
        #     group = response.xpath("//div[@class='container-fluid']/h1/text()").extract_first().strip('\n').strip()
        #     g_id = response.xpath("//div[@class='card-body']/div[1]/text()").extract_first().strip(': ')
        #     # Associated_Groups = response.xpath("//div[@class='card-body']/div[contains(text(),'Associated')]/text()").extract_first().strip(': ')
        #     softwares = response.xpath("//table/tbody/tr/td[1]/a/text()").extract()
        #     dic = {
        #         'g_id': g_id,
        #         'group': group,
        #         # 'Associated_Groups': Associated_Groups,
        #         'softwares': softwares
        #     }
        #     print(dic)
        #     # item = GSAttkspiderItem()
        #     # item['group'] = group
        #     # item['g_id'] = g_id
        #     # item['Associated_Groups'] = Associated_Groups
        #     # item['softwares'] = softwares
        #     yield dic
        # except:
        #     pass
        try:
            software = response.xpath("//div[@class='container-fluid']/h1/text()").extract_first().strip('\n').strip()
            # print(software)
            s_id = response.xpath("//div[@class='card-body']/div[1]/text()").extract_first().strip(': ')
            # print(s_id)
            # Associated_Groups = response.xpath("//div[@class='card-body']/div[contains(text(),'Associated')]/text()").extract_first().strip(': ')
            groups = response.xpath("//table/tbody/tr/td[1]/a/text()").extract()
            # print(groups)
            dic = {
                's_id': s_id,
                'software': software,
                # 'Associated_Groups': Associated_Groups,
                'groups': groups
            }
            print(dic)
            # item = GSAttkspiderItem()
            # item['group'] = group
            # item['g_id'] = g_id
            # item['Associated_Groups'] = Associated_Groups
            # item['softwares'] = softwares
            yield dic
        except:
            pass
        while True:
            if self.current_page > 512:
                break
            self.current_page += 1
            # next_url = "https://attack.mitre.org/groups/G%04d/" % self.current_page
            next_url = "https://attack.mitre.org/software/S%04d/" % self.current_page
            yield Request(next_url)



