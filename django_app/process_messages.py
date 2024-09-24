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

def get_total_successful_integrations(data):
    successful_messages = []

    for message in data:
        if message["documentMigration"]["successful"] == True:
           successful_messages.append(message)

    break_down = get_count_by_clinical_type(successful_messages)

    return {"success_count": len(successful_messages), **break_down}


def get_total_failed_integrations(data):

    failed_messages = []

    for message in data:
        if message["documentMigration"]["successful"] == False:
            failed_messages.append(message)
    break_down = get_count_by_clinical_type(failed_messages)

    return {"failed_count": len(failed_messages), **break_down}

def get_count_by_clinical_type(data):
    counts = {}
    for message in data:
        message_clinical_type = message["payload"]["attachment"]["clinicalType"]
        if counts[message_clinical_type]:
            counts[message_clinical_type] += 1
        else: counts[message_clinical_type] = 1

    return counts

