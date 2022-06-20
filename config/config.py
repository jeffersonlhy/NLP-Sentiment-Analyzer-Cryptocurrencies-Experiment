TARGET_TOKENS = ['SOL', 'BNB', 'DOT', 'AVAX', 'FLOW', 'IMX', 'RON', 'AXS', 'SAND', 'MANA', 'APE']

DAYS_DELTA_LIMIT = 7

TARGET_NEWS_SOURCE = ['coindesk', 'cryptonews', 'theblockcrypto', 'bitcoin', 'cointelegraph'] # the domain name

# Website config
coindesk_config = {
    'url': 'https://www.coindesk.com',
    'sections': [
        'https://www.coindesk.com/markets/',
        'https://www.coindesk.com/business/',
        'https://www.coindesk.com/tech/'
    ]
}

cryptonews_config = {
    'url': 'https://cryptonews.com',
    'sections': [
        'https://cryptonews.com/news/altcoin-news/',
        'https://cryptonews.com/news/blockchain-news/',
        'https://cryptonews.com/news/cryptonews-deals/'
        'https://cryptonews.com/news/press-releases/'
    ]
}

theblockcrypto_config = {
    'url': 'https://www.theblockcrypto.com',
    'sections': [
        # 'https://www.theblockcrypto.com/news+'
    ]
}

bitcoin_config = {
    'url': 'https://www.bitcoin.com',
    'sections': [
        'https://news.bitcoin.com/'
    ]
}

cointelegraph_config = {
    'url' : 'https://cointelegraph.com',
    'sections': [
        'https://cointelegraph.com/tags/altcoin',
        'https://cointelegraph.com/tags/blockchain'
        'https://cointelegraph.com/tags/adoption'
    ]
}

# Classification criteria (checking with OR)
sol_corpus = {
    'single': ['sol', 'solana'],
    'phrase': []
    }
bnb_corpus = {
    'single': ['bnb', 'binance'],
    'phrase': []
}
dot_corpus = {
    'single': ['dot', 'polkadot'],
    'phrase': []
}
avax_corpus = {
    'single': ['avax', 'avalanche', 'avalabs'],
    'phrase': []
}
flow_corpus = {
    'single': ['flow'],
    'phrase': []
}
imx_corpus = {
    'single': ['imx'],
    'phrase': ['immutable x']
}
ron_corpus = {
    'single': ['ron', 'ronin'],
    'phrase': []
}
axs_corpus = {
    'single': ['axie'],
    'phrase': ['axie infinity']
}
sand_corpus = {
    'single': ['sand', 'sandbox'],
    'phrase': []
}
mana_corpus = {
    'single': ['mana', 'decentraland'],
    'phrase': []
}

ape_corpus = {
    'single': ['apecoin', 'ape'],
    'phrase': []
}


sol_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': sol_corpus,
    'twitter_source_id': [
        951329744804392960, # solana
        2327407569, # aeyakovenko
    ],
    'twitter_source_url': [
        'https://twitter.com/solana', 
        'https://twitter.com/aeyakovenko'
    ]
}

bnb_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': bnb_corpus,
    'twitter_source_id': [
        902926941413453824, # cz_binance
        877807935493033984, # aeyakovenko
    ],
    'twitter_source': ['https://twitter.com/cz_binance', 'https://twitter.com/binance']
}

dot_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': dot_corpus,
    'twitter_source_id': [
        1595615893, # polkadot
        33962758, # gavofyork
        2254182852 # jutta
    ],
    'twitter_source': [
        'https://twitter.com/Polkadot',
        'https://twitter.com/gavofyork',
        'https://twitter.com/jutta_steiner']
}

avax_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': avax_corpus,
    'twitter_source_id':[
        1055894724245155841, # avalancheavax 
        1275068809699708931, # avalabsofficial
        399412477, # el33th4xor
        995834351316324352, # kevinsekniqi
        816589, # lavery
    ],
    'twitter_source': [
        'https://twitter.com/avalancheavax',
        'https://twitter.com/avalabsofficial',
        'https://twitter.com/el33th4xor',
        'https://twit ter.com/kevinsekniqi',
        'https://twitter.com/Lavery']
}

flow_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': flow_corpus,
    'twitter_source_id':[],
    'twitter_source': []
}

imx_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': imx_corpus,
    'twitter_source_id':[
        1233171399872638976, # Immutable
        73778438, # 0xferg
    ],
    'twitter_source': [
        'https://twitter.com/Immutable',
        'https://twitter.com/0xferg']
}

ron_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': ron_corpus,
    'twitter_source_id':[],
    'twitter_source': []
}

axs_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': axs_corpus,
    'twitter_source_id':[
        957716432430641152, # Axieinfinity
        1368163995694157825, # SkyMavisHQ
        2415460460, # trungfinity
        2731277064, # Psycheout86
    ],
    'twitter_source': [
        'https://twitter.com/AxieInfinity'
        'https://twitter.com/SkyMavisHQ'
        'https://twitter.com/trungfinity',
        'https://twitter.com/Psycheout86']
}

sand_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': sand_corpus,
    'twitter_source_id':[
        3291830170, # decentraland
        30473929, # eordano
    ],
    'twitter_source': [
        'https://twitter.com/decentraland',
        'https://twitter.com/eordano'
    ]
}

mana_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': mana_corpus,
    'twitter_source_id':[
        3291830170, # decentraland
        30473929, # eordano
    ],
    'twitter_source': [
        'https://twitter.com/decentraland',
        'https://twitter.com/eordano']
}

ape_config = {
    'news_source': TARGET_NEWS_SOURCE,
    'news_corpus': ape_corpus,
    'twitter_source_id':[
        1489018530511175681, # apecoin
        811350,              # alexisohanian
        1388236590049206272, # amytongwu
        16168217,            # ysiu
        1034448733793083392, # crypto_counsl
        1381699264011771906, # BoredApeYc
        1357749263632109570, # yugalabs
        1485775646869630978, # VStrangeYUGA 
        1454200401142501376, # SodaOps
    ],
    'twitter_source': [
        'https://twitter.com/apecoin',
        'https://twitter.com/alexisohanian',
        'https://twitter.com/amytongwu',
        'https://twitter.com/ysiu',
        'https://twitter.com/Crypto_Counsel',
        'https://twitter.com/BoredApeYC',
        'https://twitter.com/yugalabs',
        'https://twitter.com/VStrangeYUGA',
        'https://twitter.com/SodaOps']
}

WEBSITE_CONFIG = {
  'coindesk': coindesk_config,
  'cryptonews': cryptonews_config,
  'theblockcrypto': theblockcrypto_config,
  'bitcoin': bitcoin_config,
  'cointelegraph': cointelegraph_config
}

TOKEN_CONFIG = {
    'SOL': sol_config,
    'BNB': bnb_config,
    'DOT': dot_config,
    'AVAX': avax_config,
    'FLOW': flow_config,
    'IMX': imx_config,
    'RON': ron_config,
    'AXS': axs_config,
    'SAND': sand_config,
    'MANA': mana_config,
    'APE': ape_config
}

