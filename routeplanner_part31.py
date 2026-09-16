# === Stage 31: Add compact table rendering for long lists ===
# Project: RoutePlanner
def render_compact_table(rows, columns, width=80):
    """Render a compact table for long lists.
    
    Args:
        rows: List of lists, where each inner list represents a row.
        columns: List of column names.
        width: Maximum width of the table.
    
    Returns:
        A string representing the table.
    """
    col_widths = [len(col) for col in columns]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
    
    table_width = sum(col_widths) + len(columns) * 2
    if table_width > width:
        scale = width / table_width
        col_widths = [max(int(w * scale), len(col)) for w, col in zip(col_widths, columns)]
    
    def format_row(row):
        return " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
    
    separator = "-+-".join("-" * w for w in col_widths)
    header = " | ".join(col.ljust(col_widths[i]) for i, col in enumerate(columns))
    
    lines = [header, separator]
    for row in rows:
        lines.append(format_row(row))
    
    return "\n".join(lines)
