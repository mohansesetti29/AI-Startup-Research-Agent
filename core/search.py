
import urllib.parse
from duckduckgo_search import DDGS


SEARCH_RESULTS = 6

def unwrap_ddg(url):
    try:
        parsed = urllib.parse.urlparse(url)
        if "duckduckgo.com" in parsed.netloc:
            qs = urllib.parse.parse_qs(parsed.query)
            uddg = qs.get("uddg")
            if uddg:
                return urllib.parse.unquote(uddg[0])
    except:
        pass
    return url

def search_web(query, max_results=SEARCH_RESULTS):
    urls = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            link = r.get("href") or r.get("url")
            if link:
                urls.append(unwrap_ddg(link))
    return urls
