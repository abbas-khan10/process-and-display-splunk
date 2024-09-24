import os
import json

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

clinical_types = ["SCANNED_DOCUMENT",
                  "ORIGINAL_TEXT_DOCUMENT",
                  "OCR_TEXT_DOCUMENT",
                  "IMAGE",
                  "AUDIO_DICTATION",
                  "OTHER_AUDIO",
                  "OTHER_DIGITAL_SIGNAL",
                  "EDI_MESSAGE",
                  "NOT_AVAILABLE",
                  "OTHER"]

def get_total_successful_integrations():
    successful_messages = []

    for message in data_array:
        if message["documentMigration"]["successful"] == True:
           successful_messages.append(message)

    break_down = get_count_by_clinical_type(successful_messages)

    return {"success_count": len(successful_messages), **break_down}


def get_total_failed_integrations():

    failed_messages = []

    for message in data_array:
        if message["documentMigration"]["successful"] == False:
            failed_messages.append(message)
    break_down = get_count_by_clinical_type(failed_messages)

    return {"failed_count": len(failed_messages), **break_down}

def get_count_by_clinical_type():
    counts = {}
    for message in data_array:
        message_clinical_type = message["payload"]["attachment"]["clinicalType"]
        if counts[message_clinical_type]:
            counts[message_clinical_type] += 1
        else: counts[message_clinical_type] = 1

    return counts