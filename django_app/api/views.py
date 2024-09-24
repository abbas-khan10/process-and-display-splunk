import json
from datetime import datetime
import gviz_api

from api.repository import get_json_data_from_database


def index(request):
    response = get_json_data_from_database()
    return response


def get_data_table_object():

    schema = [
        {"id": "eventId", "label": "Event ID", "type": "string"},
        {
            "id": "eventGeneratedDateTime",
            "label": "Event Generated DateTime",
            "type": "datetime",
        },
        {"id": "eventType", "label": "Event Type", "type": "string"},
        {
            "id": "reportingSystemSupplier",
            "label": "Reporting System Supplier",
            "type": "string",
        },
        {
            "id": "reportingPracticeOdsCode",
            "label": "Reporting Practice ODS Code",
            "type": "string",
        },
        {
            "id": "requestingPracticeOdsCode",
            "label": "Requesting Practice ODS Code",
            "type": "string",
        },
        {
            "id": "requestingPracticeName",
            "label": "Requesting Practice Name",
            "type": "string",
        },
        {
            "id": "requestingPracticeIcbOdsCode",
            "label": "Requesting Practice ICB ODS Code",
            "type": "string",
        },
        {
            "id": "requestingPracticeIcbName",
            "label": "Requesting Practice ICB Name",
            "type": "string",
        },
        {
            "id": "sendingPracticeOdsCode",
            "label": "Sending Practice ODS Code",
            "type": "string",
        },
        {"id": "sendingPracticeName", "label": "Sending Practice Name", "type": "string"},
        {
            "id": "sendingPracticeIcbOdsCode",
            "label": "Sending Practice ICB ODS Code",
            "type": "string",
        },
        {
            "id": "sendingPracticeIcbName",
            "label": "Sending Practice ICB Name",
            "type": "string",
        },
        {"id": "conversationId", "label": "Conversation ID", "type": "string"},
        {
            "id": "registrationEventDateTime",
            "label": "Registration Event DateTime",
            "type": "datetime",
        },
        {
            "id": "requestingSupplierName",
            "label": "Requesting Supplier Name",
            "type": "string",
        },
        {"id": "sendingSupplierName", "label": "Sending Supplier Name", "type": "string"},
    ]

    data_array = get_json_data_from_database()

    data_table = gviz_api.DataTable(json.dumps(schema))
    data_table.LoadData(data_array)
    return data_table.ToJSon()


def is_same_day(date_string, target_date="2024-09-20"):
    input_date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S").date()
    target_date = datetime.strptime(target_date, "%Y-%m-%d").date()
    return input_date == target_date
