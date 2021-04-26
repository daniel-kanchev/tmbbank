BOT_NAME = 'tmbbank'
SPIDER_MODULES = ['tmbbank.spiders']
NEWSPIDER_MODULE = 'tmbbank.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
    'tmbbank.pipelines.DatabasePipeline': 300,
}
FEED_EXPORT_ENCODING = 'utf-8'

LOG_LEVEL = 'WARNING'
DOWNLOAD_DELAY = 1
# LOG_LEVEL = 'DEBUG'
