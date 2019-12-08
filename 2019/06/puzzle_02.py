
def load_input() -> list:
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            obj_1, obj_2 = line.split(')')
            obj_2 = obj_2.rstrip()
            data.append((obj_1, obj_2))

    return data


def get_unique_objects(orbits: list) -> set:
    unique_objects = set()
    for obj_1, obj_2 in orbits:
        unique_objects.add(obj_1)
        unique_objects.add(obj_2)
    return unique_objects


def get_orbit_path(object_name: str, orbits: list) -> list:
    path = []

    for obj_1, obj_2 in orbits:
        if obj_2 == object_name:
            return get_orbit_path(obj_1, orbits) + [obj_1]

    return path


def run_program(orbits: list) -> int:
    path_1 = get_orbit_path('YOU', orbits)
    path_2 = get_orbit_path('SAN', orbits)
    route = set(path_1).symmetric_difference(set(path_2))
    return len(route)


orbits = load_input()
transfers = run_program(orbits)
print(f'The answer is {transfers}')
