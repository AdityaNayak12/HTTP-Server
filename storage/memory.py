database = []
next_id = 1

def add_record(data:dict) -> dict:

    global next_id

    record = data.copy()
    record["id"] = next_id
    next_id+=1

    database.append(record)
    return record


