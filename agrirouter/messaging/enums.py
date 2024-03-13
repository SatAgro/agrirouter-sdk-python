from agrirouter.api.enums import BaseEnum


class TechnicalMessageType(BaseEnum):
    """
    Technical message type.
    """

    EMPTY = ""
    CAPABILITIES = "dke:capabilities"
    SUBSCRIPTION = "dke:subscription"
    LIST_ENDPOINTS = "dke:list_endpoints"
    LIST_ENDPOINTS_UNFILTERED = "dke:list_endpoints_unfiltered"
    FEED_CONFIRM = "dke:feed_confirm"
    FEED_DELETE = "dke:feed_delete"
    FEED_HEADER_QUERY = "dke:feed_header_query"
    FEED_MESSAGE_QUERY = "dke:feed_message_query"
    CLOUD_ONBOARD_ENDPOINTS = "dke:cloud_onboard_endpoints"
    CLOUD_OFFBOARD_ENDPOINTS = "dke:cloud_offboard_endpoints"


class CapabilityType(BaseEnum):
    """
    Type of the capability.
    """

    ISO_11783_TASK_DATA_ZIP = "iso:11783:-10:taskdata:zip"
    ISO_11783_DEVICE_DESCRIPTION = "iso:11783:-10:device_description:protobuf"
    ISO_11783_TIMELOG = "iso:11783:-10:time_log:protobuf"
    IMG_BMP = "img:bmp"
    IMG_JPEG = "img:jpeg"
    IMG_PNG = "img:png"
    SHP_SHAPE_ZIP = "shp:shape:zip"
    DOC_PDF = "doc:pdf"
    VID_AVI = "vid:avi"
    VID_MP4 = "vid:mp4"
    VID_WMV = "vid:wmv"
    GPS_INFO = "gps:info"


class CapabilityDirectionType(BaseEnum):
    """
    Direction of the capability.
    """

    SEND = "SEND"
    RECEIVE = "RECEIVE"
    SEND_RECEIVE = "SEND_RECEIVE"
