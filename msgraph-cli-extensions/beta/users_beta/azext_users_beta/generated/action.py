# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddServicePlans(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddServicePlans, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'applies-to':
                d['applies_to'] = v[0]
            elif kl == 'provisioning-status':
                d['provisioning_status'] = v[0]
            elif kl == 'service-plan-id':
                d['service_plan_id'] = v[0]
            elif kl == 'service-plan-name':
                d['service_plan_name'] = v[0]
        return d


class AddTargetPolicy(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.target_policy = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'platform-types':
                d['platform_types'] = v
        return d


class AddPayloadVisualContent(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.payload_visual_content = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'body':
                d['body'] = v[0]
            elif kl == 'title':
                d['title'] = v[0]
        return d


class AddMasterCategories(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMasterCategories, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'color':
                d['color'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddShiftPreferencesLastModifiedByApplication(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.shift_preferences_last_modified_by_application = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddRegionalAndLanguageSettingsAuthoringLanguages(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddRegionalAndLanguageSettingsAuthoringLanguages, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'locale':
                d['locale'] = v[0]
        return d


class AddRegionalAndLanguageSettingsDefaultDisplayLanguage(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.regional_and_language_settings_default_display_language = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'locale':
                d['locale'] = v[0]
        return d


class AddRegionalAndLanguageSettingsRegionalFormatOverrides(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.regional_and_language_settings_regional_format_overrides = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'calendar':
                d['calendar'] = v[0]
            elif kl == 'first-day-of-week':
                d['first_day_of_week'] = v[0]
            elif kl == 'long-date-format':
                d['long_date_format'] = v[0]
            elif kl == 'long-time-format':
                d['long_time_format'] = v[0]
            elif kl == 'short-date-format':
                d['short_date_format'] = v[0]
            elif kl == 'short-time-format':
                d['short_time_format'] = v[0]
            elif kl == 'time-zone':
                d['time_zone'] = v[0]
        return d


class AddBody(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.body = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'content':
                d['content'] = v[0]
            elif kl == 'content-type':
                d['content_type'] = v[0]
        return d


class AddCompletedDateTime(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.completed_date_time = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'date-time':
                d['date_time'] = v[0]
            elif kl == 'time-zone':
                d['time_zone'] = v[0]
        return d


class AddAttachments(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAttachments, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'content-type':
                d['content_type'] = v[0]
            elif kl == 'is-inline':
                d['is_inline'] = v[0]
            elif kl == 'last-modified-date-time':
                d['last_modified_date_time'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            elif kl == 'size':
                d['size'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddUsersCreateTaskMultiValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddUsersCreateTaskMultiValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'value':
                d['value'] = v
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddUsersCreateTaskSingleValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddUsersCreateTaskSingleValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'value':
                d['value'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddRecurrencePattern(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.recurrence_pattern = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'day-of-month':
                d['day_of_month'] = v[0]
            elif kl == 'days-of-week':
                d['days_of_week'] = v
            elif kl == 'first-day-of-week':
                d['first_day_of_week'] = v[0]
            elif kl == 'index':
                d['index'] = v[0]
            elif kl == 'interval':
                d['interval'] = v[0]
            elif kl == 'month':
                d['month'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
        return d


class AddRecurrenceRange(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.recurrence_range = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'end-date':
                d['end_date'] = v[0]
            elif kl == 'number-of-occurrences':
                d['number_of_occurrences'] = v[0]
            elif kl == 'recurrence-time-zone':
                d['recurrence_time_zone'] = v[0]
            elif kl == 'start-date':
                d['start_date'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
        return d


class AddUsersCreateTaskFolderMultiValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddUsersCreateTaskFolderMultiValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'value':
                d['value'] = v
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddUsersCreateTaskFolderSingleValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddUsersCreateTaskFolderSingleValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'value':
                d['value'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddUsersTodoExtensions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddUsersTodoExtensions, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'id':
                d['id'] = v[0]
        return d


class AddUsersTodoListsExtensions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddUsersTodoListsExtensions, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'id':
                d['id'] = v[0]
        return d


class AddLinkedResources(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddLinkedResources, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'application-name':
                d['application_name'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'external-id':
                d['external_id'] = v[0]
            elif kl == 'web-url':
                d['web_url'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d