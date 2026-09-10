# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: RoutePlanner
def dry_run(action: str, target: str, **kwargs) -> dict:
    """Simulate a mutating action without persisting changes.
    Returns a dict with 'status', 'message', and 'dry_run' flag."""
    log = {
        "status": "dry_run",
        "action": action,
        "target": target,
        "dry_run": True,
        **kwargs,
    }
    print(f"[DRY RUN] {action} on {target}: {kwargs.get('message', 'simulated')}")
    return log
