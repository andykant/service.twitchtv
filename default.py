import xbmc
import urllib
import urllib2
from resources.lib.croniter import croniter
from datetime import datetime
import simplejson as json

# API
BASE = 'https://api.twitch.tv/kraken'
GAMES = '/games/top'
STREAMS = '/streams'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'

def get_json(url = '', params = {}):
  request = urllib2.Request(
    BASE + url + '?' + urllib.urlencode(params), 
    None, 
    { 'User-Agent': USER_AGENT, 'Accept': 'application/vnd.twitchtv.v3+json' }
  )
  opener = urllib2.build_opener()
  response = json.load(opener.open(request))
  # xbmc.log(json.dumps(response, sort_keys = False, indent = 2))
  return response

class Twitch:
  def __init__(self):
    data = get_json(STREAMS, { 'game': 'League of Legends', 'limit': 8 })

if __name__ == '__main__':
  Twitch()
  del Twitch
