# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: RoutePlanner
def merge_imports(source_lines):
    """Merge duplicate imports while preserving first-seen order."""
    seen = set()
    merged = []
    for line in source_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if stripped.startswith('import '):
            module = extract_module(stripped)
            if module and module not in seen:
                seen.add(module)
                merged.append(line)
        elif stripped.startswith('from '):
            module = extract_module(stripped)
            if module and module not in seen:
                seen.add(module)
                merged.append(line)
    return merged


def extract_module(import_line):
    """Extract the module name from an import statement."""
    body = import_line.split('import')[1].strip()
    if body.startswith('from '):
        return body.split(' ')[0].strip()
    return body.split(',')[0].split('.')[0].strip()
