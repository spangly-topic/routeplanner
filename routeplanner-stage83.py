# === Stage 83: Add regression tests for the final demo workflow ===
# Project: RoutePlanner
def test_demo_workflow_end_to_end():
    from routeplanner import RoutePlanner
    from routeplanner.models import Stop, Schedule, Distance, CompletionNote

    planner = RoutePlanner()

    stops = [
        Stop(id="s1", name="A"),
        Stop(id="s2", name="B"),
        Stop(id="s3", name="C"),
    ]
    planner.add_stops(stops)

    planner.add_distance("s1", "s2", 10.0)
    planner.add_distance("s2", "s3", 20.0)
    planner.add_distance("s3", "s1", 15.0)

    planner.add_schedule(
        Schedule(
            id="d1",
            date="2024-01-01",
            route=["s1", "s2", "s3"],
            start_time="08:00",
        )
    )

    planner.complete_delivery(
        "d1",
        CompletionNote(id="n1", stop="s3", note="Package delivered", completed_at="10:00")
    )

    total = planner.total_distance("d1")
    assert total == 30.0
    assert planner.is_complete("d1")
    assert planner.status("d1") == "completed"
    assert planner.delivery_note("d1", "s3").note == "Package delivered"
    assert planner.delivery_note("d1", "s1") is None
    assert planner.stops("d1") == ["s1", "s2", "s3"]
