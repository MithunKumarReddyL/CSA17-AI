def vacuum_cleaner(loc, state):
    print(f"Initial State: Location = {loc}, {state}")
    if state[loc] == "Dirty":
        print(f"Cleaning {loc}...")
        state[loc] = "Clean"
    other = "Room B" if loc == "Room A" else "Room A"
    print(f"Moving to {other}...")
    if state[other] == "Dirty":
        print(f"Cleaning {other}...")
        state[other] = "Clean"
    print(f"Final State: {state}")
vacuum_cleaner("Room A", {"Room A": "Dirty", "Room B": "Dirty"})