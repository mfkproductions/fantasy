teams = []

class Team:
  def __init__(self, name, conf, div):
    self.name = name
    self.conf = conf
    self.div = div

  def __str__(self):
    return self.name + ':\t' + self.conf + self.div
  
  def cmp_div(self, other):
    return self.div == other.div and self.conf == other.conf

  def cmp_conf(self, other):
    return self.conf == other.conf

def get_teams():
  return teams

def get_team(name, debug = False):
  name = name.replace("("," ").replace(")"," ").replace('\n',' ')
  name = name.replace("Fortyniners","49ers")
  for word in name.strip().split(' '):
    for team in teams:
      if any(word.lower() == part.lower() for part  in team.name.split(' ')):
        return team
  print "ERROR: Cannot find " + name
  return None

def cmp_div(name1, name2):
  return get_team(name1).cmp_div(get_team(name2))

def cmp_conf(name1, name2):
  return get_team(name1).cmp_conf(get_team(name2))


def init_teams():
  teams.append(Team('Giants', 'NFC', 'East'))
  teams.append(Team('Eagles', 'NFC', 'East'))
  teams.append(Team('Redskins', 'NFC', 'East'))
  teams.append(Team('Cowboys', 'NFC', 'East'))

  teams.append(Team('Cardinals', 'NFC', 'West'))
  teams.append(Team('Rams', 'NFC', 'West'))
  teams.append(Team('Seahawks', 'NFC', 'West'))
  teams.append(Team('49ers', 'NFC', 'West'))

  teams.append(Team('Buccaneers', 'NFC', 'South'))
  teams.append(Team('Falcons', 'NFC', 'South'))
  teams.append(Team('Saints', 'NFC', 'South'))
  teams.append(Team('Panthers', 'NFC', 'South'))

  teams.append(Team('Packers', 'NFC', 'North'))
  teams.append(Team('Vikings', 'NFC', 'North'))
  teams.append(Team('Bears', 'NFC', 'North'))
  teams.append(Team('Lions', 'NFC', 'North'))
  
  teams.append(Team('Jets', 'AFC', 'East'))
  teams.append(Team('Patriots', 'AFC', 'East'))
  teams.append(Team('Dolphins', 'AFC', 'East'))
  teams.append(Team('Bills', 'AFC', 'East'))

  teams.append(Team('Broncos', 'AFC', 'West'))
  teams.append(Team('Raiders', 'AFC', 'West'))
  teams.append(Team('Chiefs', 'AFC', 'West'))
  teams.append(Team('Chargers', 'AFC', 'West'))

  teams.append(Team('Jaguars', 'AFC', 'South'))
  teams.append(Team('Colts', 'AFC', 'South'))
  teams.append(Team('Titans', 'AFC', 'South'))
  teams.append(Team('Texans', 'AFC', 'South'))

  teams.append(Team('Steelers', 'AFC', 'North'))
  teams.append(Team('Ravens', 'AFC', 'North'))
  teams.append(Team('Bengals', 'AFC', 'North'))
  teams.append(Team('Browns', 'AFC', 'North'))

init_teams()
##print cmp_conf('giants','vikings')
##print cmp_conf('raiders','vikings')

