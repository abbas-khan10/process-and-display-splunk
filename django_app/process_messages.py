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
    count = 0
    for message in data:
        if message["documentMigration"]["successful"] == True:
            count += 1
    return count

def get_total_failed_integrations(data):
    count = 0

    for message in data:
        if message["documentMigration"]["successful"] == False:
            count += 1
    return count

def get_count_by_clinical_type(data):
    counts = {}
    for message in data:
        message_clinical_type = message["payload"]["attachment"]["clinicalType"]
        if counts[message_clinical_type]:
            counts[message_clinical_type] += 1
        else: counts[message_clinical_type] = 1

    return counts

