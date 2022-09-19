from ics import Calendar, Event

def write(outfile, teams):
    c = Calendar(creator="hockeysched_ics")
    for team in teams:
        for game in team['games']:
            if game.is_past:
                name = game.result
            else:
                name = game.summary
            e = Event(
                name=name,
                location=game.location,
                begin=game.getStartFmt(),
                end=game.getEndFmt(),
                description=game.description,
            )
            c.events.add(e)

    with open(outfile, "w") as fp:
        fp.writelines(c.serialize_iter())
        