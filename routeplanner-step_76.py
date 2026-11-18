# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: RoutePlanner
import sys


def handle_interrupt():
    if 'route' in dir() and route is not None:
        try:
            route.save()
            print('Route saved before exit.')
        except Exception:
            pass
    print('\nInterrupted. Goodbye.')
    sys.exit(0)


try:
    route = RoutePlanner()
    while True:
        choice = input('Command [s]top/[n]ew/[d]istance/[s]chedule/[n]ote/[q]uit: ')
        if choice == 'q':
            break
        elif choice == 's':
            stop = input('Stop name: ')
            route.add_stop(stop)
        elif choice == 'n':
            route.new_route()
        elif choice == 'd':
            route.show_distances()
        elif choice == 'schedule':
            route.show_schedule()
        elif choice == 'note':
            route.add_note()
        else:
            print('Unknown command.')
except KeyboardInterrupt:
    handle_interrupt()
