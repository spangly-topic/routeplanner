# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: RoutePlanner
def format_color(text, fg=None, bg=None, bold=False, dim=False):
    codes = []
    if bold:
        codes.append('1')
    if dim:
        codes.append('2')
    if fg:
        codes.append(str(fg))
    if bg:
        codes.append('4' + str(bg))
    if not codes:
        return text
    return '\033[' + ';'.join(codes) + 'm' + text + '\033[0m'

class ColoredRoutePlanner(RoutePlanner):
    def __init__(self, use_color=True):
        super().__init__()
        self.use_color = use_color and os.environ.get('NO_COLOR') is None

    def _c(self, text, fg=None, bg=None, bold=False, dim=False):
        return format_color(text, fg, bg, bold, dim) if self.use_color else text

    def print_stops(self, stops):
        header = self._c('ROUTE PLAN', fg=36, bold=True)
        print(header)
        for i, stop in enumerate(stops, 1):
            status = stop['completed'] and 'DONE' or 'PENDING'
            status_c = self._c(status, fg=32 if stop['completed'] else 31, bold=True)
            print(f'  {i}. {stop["name"]} - {stop["address"]}')
            print(f'     time: {stop["schedule"]}')
            print(f'     distance: {stop["distance"]} km')
            if stop.get('notes'):
                print(f'     notes: {self._c(stop["notes"], fg=35, dim=True)}')
            print()

    def print_summary(self, stops):
        done = sum(1 for s in stops if s['completed'])
        total = len(stops)
        dist = sum(s['distance'] for s in stops)
        print(self._c('SUMMARY', fg=36, bold=True))
        print(f'  Stops: {done}/{total} completed')
        print(f'  Total distance: {dist:.1f} km')
        print(f'  Remaining: {total - done} stops')
