# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CHILD_FOLDER_COUNT = "childFolderCount"
    DISPLAY_NAME = "displayName"
    PARENT_FOLDER_ID = "parentFolderId"
    TOTAL_ITEM_COUNT = "totalItemCount"
    UNREAD_ITEM_COUNT = "unreadItemCount"
    WELL_KNOWN_NAME = "wellKnownName"
    CHILD_FOLDERS = "childFolders"
    MESSAGE_RULES = "messageRules"
    MESSAGES = "messages"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"
    USER_CONFIGURATIONS = "userConfigurations"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CHILD_FOLDERS = "childFolders"
    MESSAGE_RULES = "messageRules"
    MESSAGES = "messages"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"
    USER_CONFIGURATIONS = "userConfigurations"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CHILD_FOLDER_COUNT = "childFolderCount"
    CHILD_FOLDER_COUNT_DESC = "childFolderCount desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    PARENT_FOLDER_ID = "parentFolderId"
    PARENT_FOLDER_ID_DESC = "parentFolderId desc"
    TOTAL_ITEM_COUNT = "totalItemCount"
    TOTAL_ITEM_COUNT_DESC = "totalItemCount desc"
    UNREAD_ITEM_COUNT = "unreadItemCount"
    UNREAD_ITEM_COUNT_DESC = "unreadItemCount desc"
    WELL_KNOWN_NAME = "wellKnownName"
    WELL_KNOWN_NAME_DESC = "wellKnownName desc"

class Enum17(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CHILD_FOLDER_COUNT = "childFolderCount"
    DISPLAY_NAME = "displayName"
    PARENT_FOLDER_ID = "parentFolderId"
    TOTAL_ITEM_COUNT = "totalItemCount"
    UNREAD_ITEM_COUNT = "unreadItemCount"
    WELL_KNOWN_NAME = "wellKnownName"
    CHILD_FOLDERS = "childFolders"
    MESSAGE_RULES = "messageRules"
    MESSAGES = "messages"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"
    USER_CONFIGURATIONS = "userConfigurations"

class Enum19(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CHILD_FOLDER_COUNT = "childFolderCount"
    DISPLAY_NAME = "displayName"
    PARENT_FOLDER_ID = "parentFolderId"
    TOTAL_ITEM_COUNT = "totalItemCount"
    UNREAD_ITEM_COUNT = "unreadItemCount"
    WELL_KNOWN_NAME = "wellKnownName"
    CHILD_FOLDERS = "childFolders"
    MESSAGE_RULES = "messageRules"
    MESSAGES = "messages"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"
    USER_CONFIGURATIONS = "userConfigurations"

class Enum21(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ACTIONS = "actions"
    ACTIONS_DESC = "actions desc"
    CONDITIONS = "conditions"
    CONDITIONS_DESC = "conditions desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    EXCEPTIONS = "exceptions"
    EXCEPTIONS_DESC = "exceptions desc"
    HAS_ERROR = "hasError"
    HAS_ERROR_DESC = "hasError desc"
    IS_ENABLED = "isEnabled"
    IS_ENABLED_DESC = "isEnabled desc"
    IS_READ_ONLY = "isReadOnly"
    IS_READ_ONLY_DESC = "isReadOnly desc"
    SEQUENCE = "sequence"
    SEQUENCE_DESC = "sequence desc"

class Enum22(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIONS = "actions"
    CONDITIONS = "conditions"
    DISPLAY_NAME = "displayName"
    EXCEPTIONS = "exceptions"
    HAS_ERROR = "hasError"
    IS_ENABLED = "isEnabled"
    IS_READ_ONLY = "isReadOnly"
    SEQUENCE = "sequence"

class Enum23(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ACTIONS = "actions"
    CONDITIONS = "conditions"
    DISPLAY_NAME = "displayName"
    EXCEPTIONS = "exceptions"
    HAS_ERROR = "hasError"
    IS_ENABLED = "isEnabled"
    IS_READ_ONLY = "isReadOnly"
    SEQUENCE = "sequence"

class Enum24(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CATEGORIES = "categories"
    CATEGORIES_DESC = "categories desc"
    CHANGE_KEY = "changeKey"
    CHANGE_KEY_DESC = "changeKey desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    BCC_RECIPIENTS = "bccRecipients"
    BCC_RECIPIENTS_DESC = "bccRecipients desc"
    BODY = "body"
    BODY_DESC = "body desc"
    BODY_PREVIEW = "bodyPreview"
    BODY_PREVIEW_DESC = "bodyPreview desc"
    CC_RECIPIENTS = "ccRecipients"
    CC_RECIPIENTS_DESC = "ccRecipients desc"
    CONVERSATION_ID = "conversationId"
    CONVERSATION_ID_DESC = "conversationId desc"
    CONVERSATION_INDEX = "conversationIndex"
    CONVERSATION_INDEX_DESC = "conversationIndex desc"
    FLAG = "flag"
    FLAG_DESC = "flag desc"
    FROM_ENUM = "from"
    FROM_DESC = "from desc"
    HAS_ATTACHMENTS = "hasAttachments"
    HAS_ATTACHMENTS_DESC = "hasAttachments desc"
    IMPORTANCE = "importance"
    IMPORTANCE_DESC = "importance desc"
    INFERENCE_CLASSIFICATION = "inferenceClassification"
    INFERENCE_CLASSIFICATION_DESC = "inferenceClassification desc"
    INTERNET_MESSAGE_HEADERS = "internetMessageHeaders"
    INTERNET_MESSAGE_HEADERS_DESC = "internetMessageHeaders desc"
    INTERNET_MESSAGE_ID = "internetMessageId"
    INTERNET_MESSAGE_ID_DESC = "internetMessageId desc"
    IS_DELIVERY_RECEIPT_REQUESTED = "isDeliveryReceiptRequested"
    IS_DELIVERY_RECEIPT_REQUESTED_DESC = "isDeliveryReceiptRequested desc"
    IS_DRAFT = "isDraft"
    IS_DRAFT_DESC = "isDraft desc"
    IS_READ = "isRead"
    IS_READ_DESC = "isRead desc"
    IS_READ_RECEIPT_REQUESTED = "isReadReceiptRequested"
    IS_READ_RECEIPT_REQUESTED_DESC = "isReadReceiptRequested desc"
    MENTIONS_PREVIEW = "mentionsPreview"
    MENTIONS_PREVIEW_DESC = "mentionsPreview desc"
    PARENT_FOLDER_ID = "parentFolderId"
    PARENT_FOLDER_ID_DESC = "parentFolderId desc"
    RECEIVED_DATE_TIME = "receivedDateTime"
    RECEIVED_DATE_TIME_DESC = "receivedDateTime desc"
    REPLY_TO = "replyTo"
    REPLY_TO_DESC = "replyTo desc"
    SENDER = "sender"
    SENDER_DESC = "sender desc"
    SENT_DATE_TIME = "sentDateTime"
    SENT_DATE_TIME_DESC = "sentDateTime desc"
    SUBJECT = "subject"
    SUBJECT_DESC = "subject desc"
    TO_RECIPIENTS = "toRecipients"
    TO_RECIPIENTS_DESC = "toRecipients desc"
    UNIQUE_BODY = "uniqueBody"
    UNIQUE_BODY_DESC = "uniqueBody desc"
    UNSUBSCRIBE_DATA = "unsubscribeData"
    UNSUBSCRIBE_DATA_DESC = "unsubscribeData desc"
    UNSUBSCRIBE_ENABLED = "unsubscribeEnabled"
    UNSUBSCRIBE_ENABLED_DESC = "unsubscribeEnabled desc"
    WEB_LINK = "webLink"
    WEB_LINK_DESC = "webLink desc"

class Enum25(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CATEGORIES = "categories"
    CHANGE_KEY = "changeKey"
    CREATED_DATE_TIME = "createdDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    BCC_RECIPIENTS = "bccRecipients"
    BODY = "body"
    BODY_PREVIEW = "bodyPreview"
    CC_RECIPIENTS = "ccRecipients"
    CONVERSATION_ID = "conversationId"
    CONVERSATION_INDEX = "conversationIndex"
    FLAG = "flag"
    FROM_ENUM = "from"
    HAS_ATTACHMENTS = "hasAttachments"
    IMPORTANCE = "importance"
    INFERENCE_CLASSIFICATION = "inferenceClassification"
    INTERNET_MESSAGE_HEADERS = "internetMessageHeaders"
    INTERNET_MESSAGE_ID = "internetMessageId"
    IS_DELIVERY_RECEIPT_REQUESTED = "isDeliveryReceiptRequested"
    IS_DRAFT = "isDraft"
    IS_READ = "isRead"
    IS_READ_RECEIPT_REQUESTED = "isReadReceiptRequested"
    MENTIONS_PREVIEW = "mentionsPreview"
    PARENT_FOLDER_ID = "parentFolderId"
    RECEIVED_DATE_TIME = "receivedDateTime"
    REPLY_TO = "replyTo"
    SENDER = "sender"
    SENT_DATE_TIME = "sentDateTime"
    SUBJECT = "subject"
    TO_RECIPIENTS = "toRecipients"
    UNIQUE_BODY = "uniqueBody"
    UNSUBSCRIBE_DATA = "unsubscribeData"
    UNSUBSCRIBE_ENABLED = "unsubscribeEnabled"
    WEB_LINK = "webLink"
    ATTACHMENTS = "attachments"
    EXTENSIONS = "extensions"
    MENTIONS = "mentions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum26(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ATTACHMENTS = "attachments"
    EXTENSIONS = "extensions"
    MENTIONS = "mentions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum27(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CATEGORIES = "categories"
    CHANGE_KEY = "changeKey"
    CREATED_DATE_TIME = "createdDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    BCC_RECIPIENTS = "bccRecipients"
    BODY = "body"
    BODY_PREVIEW = "bodyPreview"
    CC_RECIPIENTS = "ccRecipients"
    CONVERSATION_ID = "conversationId"
    CONVERSATION_INDEX = "conversationIndex"
    FLAG = "flag"
    FROM_ENUM = "from"
    HAS_ATTACHMENTS = "hasAttachments"
    IMPORTANCE = "importance"
    INFERENCE_CLASSIFICATION = "inferenceClassification"
    INTERNET_MESSAGE_HEADERS = "internetMessageHeaders"
    INTERNET_MESSAGE_ID = "internetMessageId"
    IS_DELIVERY_RECEIPT_REQUESTED = "isDeliveryReceiptRequested"
    IS_DRAFT = "isDraft"
    IS_READ = "isRead"
    IS_READ_RECEIPT_REQUESTED = "isReadReceiptRequested"
    MENTIONS_PREVIEW = "mentionsPreview"
    PARENT_FOLDER_ID = "parentFolderId"
    RECEIVED_DATE_TIME = "receivedDateTime"
    REPLY_TO = "replyTo"
    SENDER = "sender"
    SENT_DATE_TIME = "sentDateTime"
    SUBJECT = "subject"
    TO_RECIPIENTS = "toRecipients"
    UNIQUE_BODY = "uniqueBody"
    UNSUBSCRIBE_DATA = "unsubscribeData"
    UNSUBSCRIBE_ENABLED = "unsubscribeEnabled"
    WEB_LINK = "webLink"
    ATTACHMENTS = "attachments"
    EXTENSIONS = "extensions"
    MENTIONS = "mentions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum28(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ATTACHMENTS = "attachments"
    EXTENSIONS = "extensions"
    MENTIONS = "mentions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum29(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CONTENT_TYPE = "contentType"
    CONTENT_TYPE_DESC = "contentType desc"
    IS_INLINE = "isInline"
    IS_INLINE_DESC = "isInline desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    NAME = "name"
    NAME_DESC = "name desc"
    SIZE = "size"
    SIZE_DESC = "size desc"

class Enum30(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CONTENT_TYPE = "contentType"
    IS_INLINE = "isInline"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    NAME = "name"
    SIZE = "size"

class Enum31(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CONTENT_TYPE = "contentType"
    IS_INLINE = "isInline"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    NAME = "name"
    SIZE = "size"

class Enum32(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum33(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    APPLICATION = "application"
    APPLICATION_DESC = "application desc"
    CLIENT_REFERENCE = "clientReference"
    CLIENT_REFERENCE_DESC = "clientReference desc"
    CREATED_BY = "createdBy"
    CREATED_BY_DESC = "createdBy desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    DEEP_LINK = "deepLink"
    DEEP_LINK_DESC = "deepLink desc"
    MENTIONED = "mentioned"
    MENTIONED_DESC = "mentioned desc"
    MENTION_TEXT = "mentionText"
    MENTION_TEXT_DESC = "mentionText desc"
    SERVER_CREATED_DATE_TIME = "serverCreatedDateTime"
    SERVER_CREATED_DATE_TIME_DESC = "serverCreatedDateTime desc"

class Enum34(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLICATION = "application"
    CLIENT_REFERENCE = "clientReference"
    CREATED_BY = "createdBy"
    CREATED_DATE_TIME = "createdDateTime"
    DEEP_LINK = "deepLink"
    MENTIONED = "mentioned"
    MENTION_TEXT = "mentionText"
    SERVER_CREATED_DATE_TIME = "serverCreatedDateTime"

class Enum35(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLICATION = "application"
    CLIENT_REFERENCE = "clientReference"
    CREATED_BY = "createdBy"
    CREATED_DATE_TIME = "createdDateTime"
    DEEP_LINK = "deepLink"
    MENTIONED = "mentioned"
    MENTION_TEXT = "mentionText"
    SERVER_CREATED_DATE_TIME = "serverCreatedDateTime"

class Enum36(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum37(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum38(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum39(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum40(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum41(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum42(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum43(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum44(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum45(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum46(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum47(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum48(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    BINARY_DATA = "binaryData"
    BINARY_DATA_DESC = "binaryData desc"

class Enum49(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    BINARY_DATA = "binaryData"

class Enum5(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CLASSIFY_AS = "classifyAs"
    SENDER_EMAIL_ADDRESS = "senderEmailAddress"

class Enum50(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    BINARY_DATA = "binaryData"

class Enum51(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CATEGORIES = "categories"
    CATEGORIES_DESC = "categories desc"
    CHANGE_KEY = "changeKey"
    CHANGE_KEY_DESC = "changeKey desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    BCC_RECIPIENTS = "bccRecipients"
    BCC_RECIPIENTS_DESC = "bccRecipients desc"
    BODY = "body"
    BODY_DESC = "body desc"
    BODY_PREVIEW = "bodyPreview"
    BODY_PREVIEW_DESC = "bodyPreview desc"
    CC_RECIPIENTS = "ccRecipients"
    CC_RECIPIENTS_DESC = "ccRecipients desc"
    CONVERSATION_ID = "conversationId"
    CONVERSATION_ID_DESC = "conversationId desc"
    CONVERSATION_INDEX = "conversationIndex"
    CONVERSATION_INDEX_DESC = "conversationIndex desc"
    FLAG = "flag"
    FLAG_DESC = "flag desc"
    FROM_ENUM = "from"
    FROM_DESC = "from desc"
    HAS_ATTACHMENTS = "hasAttachments"
    HAS_ATTACHMENTS_DESC = "hasAttachments desc"
    IMPORTANCE = "importance"
    IMPORTANCE_DESC = "importance desc"
    INFERENCE_CLASSIFICATION = "inferenceClassification"
    INFERENCE_CLASSIFICATION_DESC = "inferenceClassification desc"
    INTERNET_MESSAGE_HEADERS = "internetMessageHeaders"
    INTERNET_MESSAGE_HEADERS_DESC = "internetMessageHeaders desc"
    INTERNET_MESSAGE_ID = "internetMessageId"
    INTERNET_MESSAGE_ID_DESC = "internetMessageId desc"
    IS_DELIVERY_RECEIPT_REQUESTED = "isDeliveryReceiptRequested"
    IS_DELIVERY_RECEIPT_REQUESTED_DESC = "isDeliveryReceiptRequested desc"
    IS_DRAFT = "isDraft"
    IS_DRAFT_DESC = "isDraft desc"
    IS_READ = "isRead"
    IS_READ_DESC = "isRead desc"
    IS_READ_RECEIPT_REQUESTED = "isReadReceiptRequested"
    IS_READ_RECEIPT_REQUESTED_DESC = "isReadReceiptRequested desc"
    MENTIONS_PREVIEW = "mentionsPreview"
    MENTIONS_PREVIEW_DESC = "mentionsPreview desc"
    PARENT_FOLDER_ID = "parentFolderId"
    PARENT_FOLDER_ID_DESC = "parentFolderId desc"
    RECEIVED_DATE_TIME = "receivedDateTime"
    RECEIVED_DATE_TIME_DESC = "receivedDateTime desc"
    REPLY_TO = "replyTo"
    REPLY_TO_DESC = "replyTo desc"
    SENDER = "sender"
    SENDER_DESC = "sender desc"
    SENT_DATE_TIME = "sentDateTime"
    SENT_DATE_TIME_DESC = "sentDateTime desc"
    SUBJECT = "subject"
    SUBJECT_DESC = "subject desc"
    TO_RECIPIENTS = "toRecipients"
    TO_RECIPIENTS_DESC = "toRecipients desc"
    UNIQUE_BODY = "uniqueBody"
    UNIQUE_BODY_DESC = "uniqueBody desc"
    UNSUBSCRIBE_DATA = "unsubscribeData"
    UNSUBSCRIBE_DATA_DESC = "unsubscribeData desc"
    UNSUBSCRIBE_ENABLED = "unsubscribeEnabled"
    UNSUBSCRIBE_ENABLED_DESC = "unsubscribeEnabled desc"
    WEB_LINK = "webLink"
    WEB_LINK_DESC = "webLink desc"

class Enum52(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CATEGORIES = "categories"
    CHANGE_KEY = "changeKey"
    CREATED_DATE_TIME = "createdDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    BCC_RECIPIENTS = "bccRecipients"
    BODY = "body"
    BODY_PREVIEW = "bodyPreview"
    CC_RECIPIENTS = "ccRecipients"
    CONVERSATION_ID = "conversationId"
    CONVERSATION_INDEX = "conversationIndex"
    FLAG = "flag"
    FROM_ENUM = "from"
    HAS_ATTACHMENTS = "hasAttachments"
    IMPORTANCE = "importance"
    INFERENCE_CLASSIFICATION = "inferenceClassification"
    INTERNET_MESSAGE_HEADERS = "internetMessageHeaders"
    INTERNET_MESSAGE_ID = "internetMessageId"
    IS_DELIVERY_RECEIPT_REQUESTED = "isDeliveryReceiptRequested"
    IS_DRAFT = "isDraft"
    IS_READ = "isRead"
    IS_READ_RECEIPT_REQUESTED = "isReadReceiptRequested"
    MENTIONS_PREVIEW = "mentionsPreview"
    PARENT_FOLDER_ID = "parentFolderId"
    RECEIVED_DATE_TIME = "receivedDateTime"
    REPLY_TO = "replyTo"
    SENDER = "sender"
    SENT_DATE_TIME = "sentDateTime"
    SUBJECT = "subject"
    TO_RECIPIENTS = "toRecipients"
    UNIQUE_BODY = "uniqueBody"
    UNSUBSCRIBE_DATA = "unsubscribeData"
    UNSUBSCRIBE_ENABLED = "unsubscribeEnabled"
    WEB_LINK = "webLink"
    ATTACHMENTS = "attachments"
    EXTENSIONS = "extensions"
    MENTIONS = "mentions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum53(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ATTACHMENTS = "attachments"
    EXTENSIONS = "extensions"
    MENTIONS = "mentions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum54(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CATEGORIES = "categories"
    CHANGE_KEY = "changeKey"
    CREATED_DATE_TIME = "createdDateTime"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    BCC_RECIPIENTS = "bccRecipients"
    BODY = "body"
    BODY_PREVIEW = "bodyPreview"
    CC_RECIPIENTS = "ccRecipients"
    CONVERSATION_ID = "conversationId"
    CONVERSATION_INDEX = "conversationIndex"
    FLAG = "flag"
    FROM_ENUM = "from"
    HAS_ATTACHMENTS = "hasAttachments"
    IMPORTANCE = "importance"
    INFERENCE_CLASSIFICATION = "inferenceClassification"
    INTERNET_MESSAGE_HEADERS = "internetMessageHeaders"
    INTERNET_MESSAGE_ID = "internetMessageId"
    IS_DELIVERY_RECEIPT_REQUESTED = "isDeliveryReceiptRequested"
    IS_DRAFT = "isDraft"
    IS_READ = "isRead"
    IS_READ_RECEIPT_REQUESTED = "isReadReceiptRequested"
    MENTIONS_PREVIEW = "mentionsPreview"
    PARENT_FOLDER_ID = "parentFolderId"
    RECEIVED_DATE_TIME = "receivedDateTime"
    REPLY_TO = "replyTo"
    SENDER = "sender"
    SENT_DATE_TIME = "sentDateTime"
    SUBJECT = "subject"
    TO_RECIPIENTS = "toRecipients"
    UNIQUE_BODY = "uniqueBody"
    UNSUBSCRIBE_DATA = "unsubscribeData"
    UNSUBSCRIBE_ENABLED = "unsubscribeEnabled"
    WEB_LINK = "webLink"
    ATTACHMENTS = "attachments"
    EXTENSIONS = "extensions"
    MENTIONS = "mentions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum55(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ATTACHMENTS = "attachments"
    EXTENSIONS = "extensions"
    MENTIONS = "mentions"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"

class Enum56(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CONTENT_TYPE = "contentType"
    CONTENT_TYPE_DESC = "contentType desc"
    IS_INLINE = "isInline"
    IS_INLINE_DESC = "isInline desc"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    LAST_MODIFIED_DATE_TIME_DESC = "lastModifiedDateTime desc"
    NAME = "name"
    NAME_DESC = "name desc"
    SIZE = "size"
    SIZE_DESC = "size desc"

class Enum57(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CONTENT_TYPE = "contentType"
    IS_INLINE = "isInline"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    NAME = "name"
    SIZE = "size"

class Enum58(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CONTENT_TYPE = "contentType"
    IS_INLINE = "isInline"
    LAST_MODIFIED_DATE_TIME = "lastModifiedDateTime"
    NAME = "name"
    SIZE = "size"

class Enum59(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum6(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CHILD_FOLDER_COUNT = "childFolderCount"
    CHILD_FOLDER_COUNT_DESC = "childFolderCount desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    PARENT_FOLDER_ID = "parentFolderId"
    PARENT_FOLDER_ID_DESC = "parentFolderId desc"
    TOTAL_ITEM_COUNT = "totalItemCount"
    TOTAL_ITEM_COUNT_DESC = "totalItemCount desc"
    UNREAD_ITEM_COUNT = "unreadItemCount"
    UNREAD_ITEM_COUNT_DESC = "unreadItemCount desc"
    WELL_KNOWN_NAME = "wellKnownName"
    WELL_KNOWN_NAME_DESC = "wellKnownName desc"

class Enum60(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    APPLICATION = "application"
    APPLICATION_DESC = "application desc"
    CLIENT_REFERENCE = "clientReference"
    CLIENT_REFERENCE_DESC = "clientReference desc"
    CREATED_BY = "createdBy"
    CREATED_BY_DESC = "createdBy desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    DEEP_LINK = "deepLink"
    DEEP_LINK_DESC = "deepLink desc"
    MENTIONED = "mentioned"
    MENTIONED_DESC = "mentioned desc"
    MENTION_TEXT = "mentionText"
    MENTION_TEXT_DESC = "mentionText desc"
    SERVER_CREATED_DATE_TIME = "serverCreatedDateTime"
    SERVER_CREATED_DATE_TIME_DESC = "serverCreatedDateTime desc"

class Enum61(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLICATION = "application"
    CLIENT_REFERENCE = "clientReference"
    CREATED_BY = "createdBy"
    CREATED_DATE_TIME = "createdDateTime"
    DEEP_LINK = "deepLink"
    MENTIONED = "mentioned"
    MENTION_TEXT = "mentionText"
    SERVER_CREATED_DATE_TIME = "serverCreatedDateTime"

class Enum62(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLICATION = "application"
    CLIENT_REFERENCE = "clientReference"
    CREATED_BY = "createdBy"
    CREATED_DATE_TIME = "createdDateTime"
    DEEP_LINK = "deepLink"
    MENTIONED = "mentioned"
    MENTION_TEXT = "mentionText"
    SERVER_CREATED_DATE_TIME = "serverCreatedDateTime"

class Enum63(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum64(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum65(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum66(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    VALUE = "value"
    VALUE_DESC = "value desc"

class Enum67(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum68(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    VALUE = "value"

class Enum7(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CHILD_FOLDER_COUNT = "childFolderCount"
    DISPLAY_NAME = "displayName"
    PARENT_FOLDER_ID = "parentFolderId"
    TOTAL_ITEM_COUNT = "totalItemCount"
    UNREAD_ITEM_COUNT = "unreadItemCount"
    WELL_KNOWN_NAME = "wellKnownName"
    CHILD_FOLDERS = "childFolders"
    MESSAGE_RULES = "messageRules"
    MESSAGES = "messages"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"
    USER_CONFIGURATIONS = "userConfigurations"

class Enum8(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CHILD_FOLDERS = "childFolders"
    MESSAGE_RULES = "messageRules"
    MESSAGES = "messages"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"
    USER_CONFIGURATIONS = "userConfigurations"

class Get1ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    OVERRIDES = "overrides"

class Get2ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    OVERRIDES = "overrides"

class Get4ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CHILD_FOLDERS = "childFolders"
    MESSAGE_RULES = "messageRules"
    MESSAGES = "messages"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"
    USER_CONFIGURATIONS = "userConfigurations"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CLASSIFY_AS = "classifyAs"
    CLASSIFY_AS_DESC = "classifyAs desc"
    SENDER_EMAIL_ADDRESS = "senderEmailAddress"
    SENDER_EMAIL_ADDRESS_DESC = "senderEmailAddress desc"

class Get7ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CLASSIFY_AS = "classifyAs"
    SENDER_EMAIL_ADDRESS = "senderEmailAddress"

class Get9ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CHILD_FOLDERS = "childFolders"
    MESSAGE_RULES = "messageRules"
    MESSAGES = "messages"
    MULTI_VALUE_EXTENDED_PROPERTIES = "multiValueExtendedProperties"
    SINGLE_VALUE_EXTENDED_PROPERTIES = "singleValueExtendedProperties"
    USER_CONFIGURATIONS = "userConfigurations"

class MicrosoftGraphBodyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TEXT = "text"
    HTML = "html"

class MicrosoftGraphFollowupFlagStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_FLAGGED = "notFlagged"
    COMPLETE = "complete"
    FLAGGED = "flagged"

class MicrosoftGraphImportance(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"

class MicrosoftGraphInferenceClassificationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    FOCUSED = "focused"
    OTHER = "other"

class MicrosoftGraphMessageActionFlag(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ANY = "any"
    CALL = "call"
    DO_NOT_FORWARD = "doNotForward"
    FOLLOW_UP = "followUp"
    FYI = "fyi"
    FORWARD = "forward"
    NO_RESPONSE_NECESSARY = "noResponseNecessary"
    READ = "read"
    REPLY = "reply"
    REPLY_TO_ALL = "replyToAll"
    REVIEW = "review"

class MicrosoftGraphSensitivity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NORMAL = "normal"
    PERSONAL = "personal"
    PRIVATE = "private"
    CONFIDENTIAL = "confidential"
