# solve.py
from parse import AVAILABLE


def solve(world):

    # ordenar los servidores por capacidad desc
    sorted_servers = sorted(world['servers'], key=lambda s: s.capacity / s.size, reverse=True)

    current_row = -1
    up_down = 1

    for server in sorted_servers:

        visited = 0
        next_row = 1  # call to the txema's function

        while visited < len(world['rows']) and next_row:
            # encontrar el primer hueco libre
            try:
                row = world['rows'][next_row]
                first_available = row.index(AVAILABLE)
                # ver si cabe
                slot_in_row = row[first_available: first_available + server.size]
                insertable = all([slot == AVAILABLE for slot in slot_in_row])

                if insertable:
                    # si cabe -> guardo y lo pongo con el server id
                    row[first_available: first_available + server.size] = [server.id for _ in
                                                                              range(server.size)]
                    world['rows'][next_row] = row
                    # llamar a la función de txema again
                    next_row += 1
                    visited = next_row % len(world['rows'])

                    break
            except:
                pass

            # llamar a la función de txema again
            next_row += 1
            visited += next_row



    # colocar por orden uno en cada row
    print(world)
    return world
