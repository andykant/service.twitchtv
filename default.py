# -*- coding: utf-8 -*-
from xbmcswift2 import xbmc
# import xbmc
import urllib
import urllib2
from livestreamer import Livestreamer
from croniter import croniter
from datetime import datetime
import simplejson as json

# API
BASE = 'https://api.twitch.tv/kraken'
GAMES = '/games/top'
STREAMS = '/streams'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'

livestreamer = Livestreamer()

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

def get_url(name = ''):
  plugin = livestreamer.resolve_url("http://twitch.tv/" + name)
  streams = plugin.get_streams()
  stream = streams.get("source")
  # print(stream.url)
  return stream.url

def get_streams(game = '', count = 10):
  response = get_json(STREAMS, { 'game': game, 'limit': count })
  streams = []

  for entry in response['streams']:
    channel = entry['channel']
    streams.append({
      'display_name': channel['display_name'],
      'name': channel['name'],
      'status': channel['status'],
      'preview': entry['preview']['large'],
      # 'url': get_url(channel['name'])
    })

  return streams

class Twitch:
  def __init__(self):
    print('\nLEAGUE OF LEGENDS\n-----------------')
    for stream in get_streams('League of Legends'):
      print(stream['display_name'])

    print('\nHEARTHSTONE\n-----------')
    for stream in get_streams('Hearthstone: Heroes of Warcraft', 5):
      print(stream['display_name'])

    print('\nGAMES\n-----')
    response = get_json(GAMES, { 'limit': 10 })
    for entry in response['top']:
      print(entry['game']['name'] + ': ' + json.dumps(entry['viewers']))

if __name__ == '__main__':
  Twitch()
  del Twitch
