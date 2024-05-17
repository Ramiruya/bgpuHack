import scrapy


class BSPU_SPIDER(scrapy.Spider):
    name = 'bspu'
    allowed_domains = ['bspu.ru']
    start_urls = ["https://bspu.ru/"]
    # Исправление кодировки для записи в json
    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8",
    }

    # Начало парсинга
    def parse(self, response):
        # Проход по блоку с ссылками на факультеты
        div = response.xpath('//div[@id="mn-block-1"]')
        for a in div.xpath('.//a'):
            # Получение ссылки на факультет
            href = a.xpath('./@href')
            # logging.debug(href)
            yield response.follow(href.get(), callback=self.parse_link_users)

    # Парсинг ссылки на сотрудников факультета
    def parse_link_users(self, response):
        search_text = 'Сотрудники'
        # Получение ссылки
        faculty_users = response.xpath(f'//a[text()="{search_text}"]/@href')
        # logging.debug('Получение ссылки на сотрудников %s', response)
        yield response.follow(faculty_users.get(), callback=self.parse_faculty)

    # Парсинг фио, получение кафедры сотрудников, должностей по странице сотрудников
    def parse_faculty(self, response):
        # logging.debug(response)
        # Блок с фио всех сотрудников
        for section in response.xpath('//section[@class="p-b-1 docs-component"]'):
            # Блок одного сотрудника
            for div in section.xpath('.//div[@class="media-body"]'):
                # Блок ФИО с ссылкой
                for h4 in div.xpath('.//h4'):
                    a = h4.xpath('.//a')
                    # Получение названия института
                    faculty_name = a.xpath(
                        '//span[@class="header-title-text font-opiumnewc text-uppercase"]//text()').extract_first()
                    # Получение ссылки на сотрудника и его ФИО
                    href = a.xpath('./@href').extract_first()
                    text = a.xpath('./text()').extract_first()
                    # logging.info(type(text))
                # Блок с кафедрой и должностью
                for div1 in div.xpath('.//div[@class="text-muted"]'):
                    # Получение кафдеры
                    department = div1.xpath('.//a/text()').extract_first()
                    # Получение должности
                    post = div1.xpath('.//following-sibling::text()').get().strip()[2:]
                    # Запись в json
                    yield {
                        'faculty_name': faculty_name,
                        'department': department,
                        'post': post,
                        'user_link': href,
                        'fio': text
                    }
