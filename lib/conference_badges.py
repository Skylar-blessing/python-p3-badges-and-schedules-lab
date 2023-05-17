def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speakers):
    return ["Hello, {}! You'll be assigned to room {}!".format(name, room_number+1) for room_number, name in enumerate(speakers)]

def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)
