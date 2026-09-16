# === Stage 32: Add pagination helpers for long console output ===
# Project: RoutePlanner
def page_output(text, page_size=80):
    lines = text.splitlines()
    for i in range(0, len(lines), page_size):
        chunk = lines[i:i + page_size]
        print(''.join(chunk))
        if i + page_size < len(lines):
            print('[... more output ...]')
            return
