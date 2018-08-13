# Mirrors may change over time.
MIRRORS = [
    'libgen.io',
]

DEFAULT_MIRROR = MIRRORS[0]

ENDPOINTS = {
    'search': 'http://{mirror}/search.php'
              '?req={req}&res=100&column={column}',
    'lookup': 'http://{mirror}/json.php'
              '?ids={ids}&fields={fields}',
    'download': 'http://download1.libgen.io/ads.php'
              '?md5={md5}',
}

DEFAULT_FIELDS = [
    'title',
    'id',
    'author',
    'year',
    'edition',
    'pages',
    'identifier',
    'extension',
    'md5',
    'language',
    'filesize',
    'extension',
    'coverurl',

]
