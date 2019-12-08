
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


def get_orbit_count(object_name: str, orbits: list) -> int:
    orbit_count = 0

    for obj_1, obj_2 in orbits:
        if obj_2 == object_name:
            return get_orbit_count(obj_1, orbits) + 1

    return orbit_count


def run_program(orbits: list) -> int:
    unique_objects = get_unique_objects(orbits)
    orbit_count = 0

    for unique_object in unique_objects:
        orbit_count += get_orbit_count(unique_object, orbits)

    return orbit_count


orbits = load_input()
orbit_count = run_program(orbits)
print(f'The answer is {orbit_count}')
