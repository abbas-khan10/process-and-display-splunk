import os
import json

from api.models import Message

folder_path = "data"
json_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]

data_array = []


def migrate_data():
    for file_name in json_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            eventType = data.get("eventType", None)
            if eventType is not None and eventType == "DOCUMENT_RESPONSES":
                data_array.append(data)


def get_integrations_counts():
    successful_messages = []
    failed_messages = []

    for message in data_array:
        validated_message = Message.model_valiate(message)
        if validated_message.documentMigration.successful == True:
           successful_messages.append(validated_message)
        else: failed_messages.append(validated_message)

    success_break_down = get_count_by_clinical_type(successful_messages)
    failed_break_down = get_count_by_clinical_type(failed_messages)



    return {"success_count": len(successful_messages), "failed_count": len(failed_messages),
            "success_breakdown": success_break_down, "failed_breakdown": failed_break_down}


def get_count_by_clinical_type(messages):
    counts = {}
    for message in messages:
        message_clinical_type = message.payload.attachment.clinicalType
        if counts[message_clinical_type]:
            counts[message_clinical_type] += 1
        else: counts[message_clinical_type] = 1

    return counts

def get_json_data_from_database():
    message_counts = get_integrations_counts()
    response = []

    for message in message_counts:
        json_message = message.model_dump_json
        response.append(json_message)

    return response
