# === Stage 55: Add a setting to disable colorized output ===
# Project: RoutePlanner
USE_COLOR = False


def colorize(text, color):
    if USE_COLOR:
        return text
    return "\033[1;{c}m{text}\033[0m".format(c=color, text=text)


def print_route(title, stops):
    print(colorize(title, "green"))
    for i, stop in enumerate(stops, start=1):
        print("  {n}. {name} ({dist} km)".format(n=i, name=stop["name"], dist=stop["distance"]))


def print_schedule(schedule):
    print(colorize("Schedule:", "yellow"))
    for time, location in schedule.items():
        print("  {t}: {loc}".format(t=time, loc=location))


def print_completion_notes(notes):
    if USE_COLOR:
        print("Completion notes:")
    for note in notes:
        print("  " + note)
