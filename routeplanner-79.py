# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: RoutePlanner
def self_check(stops, distances, schedules, completion_notes):
    assert stops, "no stops defined"
    assert set(distances) >= set(stops), "missing distances"
    assert set(schedules) >= set(stops), "missing schedules"
    assert set(completion_notes) >= set(stops), "missing completion notes"
    for stop in stops:
        assert distances[stop] >= 0, f"negative distance at {stop}"
        assert schedules[stop] >= 0, f"negative schedule at {stop}"
        assert stop in completion_notes, f"no completion note for {stop}"
        assert "status" in completion_notes[stop], f"missing status for {stop}"
    print("All validations passed")
    print("Demo:")
    for stop in stops:
        print(f"  {stop}: distance={distances[stop]}, schedule={schedules[stop]}, note={completion_notes[stop]['status']}")
    total_distance = sum(distances.values())
    total_time = sum(schedules.values())
    print(f"Total distance: {total_distance}, total scheduled time: {total_time}")
    return True
