import csv
import tweepy
import os

list_owner = 'addyosmani'
list_name = 'google-designers'
key = {}
key['consumerKey'] = '2ZEoM1dqbSRanyIHfS1hA'
key['consumerSecret'] = 'C9XTgD9vnqw6dbWa9TLihWWUNkDVwikZgnYfwF582k'
key['accessToken'] = '7605412-I1tZGjFWtey1J9QDvhoP0XYAB3TpOlxgbOEFcrKPkc'
key['accessTokenSecret'] = 'gsdQNVcgI3ihA7oqWix24IQY4ZXWqVSYy27toObhFBla4'
results_file = csv.writer(open('group_members.csv', 'a'))
if os.stat("group_members.csv").st_size == 0:
  results_file.writerow(["Name", "Location"])

auth = tweepy.OAuthHandler(key['consumerKey'], key['consumerSecret'])
auth.set_access_token(key['accessToken'], key['accessTokenSecret'])

api = tweepy.API(auth)

for member in tweepy.Cursor(api.list_members, list_owner, list_name).items():
  memberName = member.name
  print memberName.encode('utf-8')
  memberLocation = member.location
  if ' ' in memberName:
    results_file.writerow([memberName.encode('utf-8'), memberLocation.encode('utf-8')])
    print("Name: " + memberName.encode('utf-8') + "        Location: " + memberLocation.encode('utf-8'))
