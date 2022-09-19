import siahl
import write_ics
import sys

TEAMS = [
    {'name':'Stampede',   'url':'https://stats.sharksice.timetoscore.com/display-schedule?team=53&league=1&stat_class=1', 'games':[]},
    {'name':'Gang Green', 'url':'https://stats.sharksice.timetoscore.com/display-schedule?team=79&league=1&stat_class=1', 'games':[]}
]

def main():
    if len(sys.argv) != 2:
        print("Must supply ics file name")
        return -1

    outfile = sys.argv[1]

    for team in TEAMS:
        team['games'] = siahl.read_all_games(team['name'], team['url']) 
    
    write_ics.write(outfile, TEAMS)

if __name__ == "__main__":
    main()