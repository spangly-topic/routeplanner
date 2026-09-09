# === Stage 16: Add argparse support for the most common commands ===
# Project: RoutePlanner
import argparse

def register_cli():
    parser = argparse.ArgumentParser(description="RoutePlanner CLI")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("plan", help="plan a delivery route")
    p.add_argument("--stops", nargs="+", help="stop ids")
    p.add_argument("--schedule", help="schedule name")

    p = sub.add_parser("complete", help="mark a stop as completed")
    p.add_argument("stop_id", help="stop id to complete")

    p = sub.add_parser("list-stops", help="list all stops")
    p.add_argument("--completed", action="store_true", help="show only completed")

    p = sub.add_parser("show", help="show stop details")
    p.add_argument("stop_id", help="stop id")

    return parser
