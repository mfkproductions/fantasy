from bs4 import BeautifulSoup as bs
import team_data as td
games = {}

class GameData:
  def __init__(self, name, week, spread, home, overunder, opponent, pf, pa, result):
    self.name = name 
    self.week = week
    self.spread = spread
    self.home = home
    self.overunder = overunder
    self.opponent = opponent
    self.result = result
    self.pf = pf
    self.pa = pa
  def __str__(self):
    retstr =  '\t'.join([self.spread,str(self.home),self.overunder,self.opponent,self.result])
    return retstr

def key(team, year, week):
  return td.get_team(team).name + "_" + str(year) + "_" + str(week).strip()

DATE        = 0
DAY         = 2
WEEK        = 3
OPPONENT    = 6
HOME        = 7
FINAL       = 12
SPREAD      = 13
OVERUNDER   = 14
RESULT      = 20


def load_results_from_file(team, year):
  fname = "./data/" + team + "_" + str(year) + ".htm"
  f = open(fname, 'r')
  html = f.read()
  f.close()
  
  soup = bs(html)
  for tab in soup.find_all("table", {"id":"DT_Table"}):
    rows = tab.find_all('tr')
    for row in rows:
      if "Date" not in row.get_text():
        cols = []
        for td in row.find_all('td'):
          cols.append(td.get_text())
      
        if int(cols[WEEK]) > 17:
          continue

        week = cols[WEEK]
        scores = cols[FINAL].split('-')
        pf = scores[0]
        pa = scores[1]
        game = GameData(team, week, cols[SPREAD], 'home' in cols[HOME], cols[OVERUNDER], cols[OPPONENT].strip(), pf, pa, cols[RESULT])
        games[key(team, year, week)] = game

def get_record(year,week,team, start=1):
  team = td.get_team(team).name
  w = 0
  l = 0 
  d = 0
  pct = 0
  tpf = 0
  tpa = 0
  for i in range (start,week):
    ky = key(team, year, i)
    if ky in games:
      game = games[ky]
    else:
      continue
    tpf = tpf + int(game.pf)
    tpa = tpa + int(game.pa)
    if 'W' in game.result:
      w = w + 1
    elif 'L' in game.result:
      l = l + 1
    elif 'P' in game.result:
      d = d + 1
    else:
      print ky + "unexpected " + game.result
  if w + l + d > 0:
    pct = float(w) / float(w + l + d)
  return [pct,tpf,tpa] #[w, l, d, pct]

def get_game(year,week,team):
  ky = key(team, year, week)
  if ky in games:
    game = games[ky]
  else:
    return ""
  [record, tpf, tpa] = get_record(year,week,team)
  [last3, last3_tpf,last3_tpa] = get_record(year,week,team,week-4)
  [opp_record, opp_tpf, opp_tpa] = get_record(year,week,game.opponent)
  [opp_last3, opp_last3_tpf, opp_last3_tpa] = get_record(year,week,game.opponent,week-4)
  div_game = td.get_team(team).cmp_div(td.get_team(game.opponent))
  conf_game = td.get_team(team).cmp_conf(td.get_team(game.opponent))
  small_num = 0.00001
  return ','.join([game.week,
                   game.spread,
                   str(int(game.home)),game.overunder,
                   "%.3f" % (tpf/(opp_tpf + small_num)), 
                   "%.3f" %(tpa/(opp_tpa + small_num)), 
                   "%.3f" % (last3_tpf/(opp_last3_tpf + small_num)), 
                   "%.3f" % (last3_tpa/(opp_last3_tpa + small_num)), 
                   "%.3f" % (record/(opp_record + small_num)), 
                   "%.3f" %(last3/(opp_last3 + small_num)), 
                   str(int(div_game)), 
                   str(int(conf_game)), 
                   str(int("W" in game.result)) ])

def load_results():
  for team in td.get_teams():
    for year in range(2010,2016):
      load_results_from_file(team.name, year)

load_results()

f = open("./game_data.csv", 'w')

header = ','.join(["Spread","Home","O/U","pct", "L3", "OppPct", "OppL3", "DivGame", "ConGame", "Result" ]) + "\n"
#f.write(header)
for team in td.get_teams():
  for week in range(4,16):
    for year in range(2010,2017):
      game = get_game(year,week,team.name)
      if game:
        f.write(game + '\n')
f.close()
