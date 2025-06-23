def missionaries_and_cannibals():
    left = [3, 3] 
    right = [0, 0]
    boat = 'left'
    steps = [
        [0, 2], [0, 1], [2, 0], [1, 1],
        [2, 0], [0, 1], [0, 2], [1, 0],
        [1, 1], [2, 0], [0, 2]
    ]
    print("Left Side | Right Side | Boat Side")
    for move in steps:
        if boat == 'left':
            left[0] -= move[0]
            left[1] -= move[1]
            right[0] += move[0]
            right[1] += move[1]
            boat = 'right'
        else:
            left[0] += move[0]
            left[1] += move[1]
            right[0] -= move[0]
            right[1] -= move[1]
            boat = 'left'
        
        print(f"   {left}   |   {right}   |   {boat}")
missionaries_and_cannibals()