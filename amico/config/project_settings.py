
#The project name.
PROJECT_NAME  = r''
#The absolutely sys path of the project.
PATH = r''
#The max nums of the concurrent running tasks at one time in the project
CONCURRENCY = 1000
# The request sender module of our project.
CRAWLING_REQUESTER_MODULE = 'amico.crawl.requester'
#The custom command module path,i.g."myproject.commands"
#If one of the customised commands overrides the native command,
#the native one will be replaced.
COMMANDS_NEW_MODULE = ''
# Log mode.
LOG_ENABLE = True
# Log level to record.
LOG_LEVEL = 'INFO'
# Log encoding for our log file.
LOG_FILE_ENCODING = 'UTF-8'
# Save the logging into a disk file.
LOG_FILE_SAVE_PATH = r'log.log'
# Logging date format.
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
# The logging format corresponding to several level.
LOG_FORMAT = {
    'DEBUG'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'INFO'      : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'WARNING'   : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'ERROR'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'CRITICAL'  : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
}
# Middleware for common usage of the project.
MIDDLEWARE_COMMON_INSTALL = {
'request':
    {
        'amico.middlewares.requestwares.ListHandle'     : 1000,
        'amico.middlewares.requestwares.Rules'          : 1000,
        'amico.middlewares.requestwares.HeadersHandle'  : 890,
        'amico.middlewares.requestwares.Robotstxt'      : 100,
        #place your custom common request handling middleware here
        #e.g. <middleware module path>:<priority>
    },
    'response':
    {
        'amico.middlewares.responsewares.RetryPages'    : 1000,
        # place your custom common response handling middleware here
        # e.g. <middleware module path>:<priority>
    },
    'both':
    {
        'amico.middlewares.CrawlFilter' : 900,
        'amico.middlewares.HttpProxy'   : 800,
        'amico.middlewares.ServerCtrl'  : 700,
        # place your custom common middleware(both on request and response) here
        # e.g. <middleware module path>:<priority>
    }
}
# Project requests queue module.
PROJECT_REQUESTS_QUEUE = 'amico.datatype.queue.Priority'
# If turn on the spider server of telnet.
SPIDER_SERVER_ENABLE = True
SPIDER_SERVER_HOST = '127.0.0.1'
SPIDER_SERVER_PORT = 2232
# The module of spider server commands.
SPIDER_SERVER_COMMANDS_MODULE = 'amico.subcmd'
# Backup settings for amico project.
SPIDER_BACKUP_SETTINGS = 'amico.config.spider_settings'
# The spiders module.
SPIDER_MODULE = 'spiders'