# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GSAttkspiderPipeline:
    def process_item(self, item, spider):
        return item

class CSVPipeline:
    index = 0
    file = None
    filename = 'group.csv'

    def open_spider(self, spider):
        """
        打开spider时，打开文档
        :param spider:
        :return:
        """
        self.file = open(self.filename, 'w', encoding='utf-8-sig')

    def process_item(self, item, spider):
        pass