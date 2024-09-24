def get_total_successful_integrations(data):
    count = 0
    for message in data:
        if message["documentMigration"]["successful"] == True:
            count += 1
    return count

def get_total_failed_integrations(data):
    count = 0
    for message in data:
        if message["documentMigration"]["successful"] == True:
            count += 1
    return count