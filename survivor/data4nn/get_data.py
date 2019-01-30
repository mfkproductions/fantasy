import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import urllib2
from bs4 import BeautifulSoup as bs
def key(year, team):
  return team + "_" + str(year)
def get_results(year, team):
  driver = webdriver.Firefox()
  driver.implicitly_wait(4)
  driver.get("http://killersports.com/nfl/query?sdql=team+%3D+" + team + "+and+season+%3D+" + str(year))
#  time.sleep(2)
#  driver.refresh()
  try:
    driver.find_element_by_id("DT_Table")
  except:
    print "Unable to access " + key(year,team)
  html = driver.page_source.encode('utf8')
  driver.quit()
  f = open("./data/" + key(year,team) + ".htm", 'w')
  f.write(html)
  f.close()

teams = [
'Giants      ',
'Eagles      ',
'Redskins    ',
'Cowboys     ',
'Cardinals   ',
'Rams        ',
'Seahawks    ',
'49ers       ',
'Bucaneers   ',
'Falcons     ',
'Saints      ',
'Panthers    ',
'Packers     ',
'Vikings     ',
'Bears       ',
'Lions       ',
'Jets        ',
'Patriots    ',
'Dolphins    ',
'Bills       ',
'Broncos     ',
'Raiders     ',
'Chiefs      ',
'Chargers    ',
'Jaguars     ',
'Colts       ',
'Titans      ',
'Texans      ',
'Steelers    ',
'Ravens      ',
'Bengals     ',
'Browns      ']



for yr in [2010, 2011, 2012, 2013, 2014, 2015, 2016]:
  #for tm in teams:
    get_results(yr,"Buccaneers")
    time.sleep(15)
