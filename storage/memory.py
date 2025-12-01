database = []
_next_id = 1


def add_record(data):
    global _next_id

    record = data.copy()
    record["id"] = _next_id
    _next_id += 1
    database.append(record)

    return record
