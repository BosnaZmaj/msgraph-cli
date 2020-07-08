# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_bookings.generated._client_factory import cf_booking_business_booking_business
    bookings_booking_business_booking_business = CliCommandType(
        operations_tmpl='azext_bookings.vendored_sdks.bookings.operations._booking_business_booking_business_operations'
        '#BookingBusinessOperations.{}',
        client_factory=cf_booking_business_booking_business)
    with self.command_group('bookings booking-business-booking-business', bookings_booking_business_booking_business,
                            client_factory=cf_booking_business_booking_business, is_experimental=True) as g:
        g.custom_command('update', 'bookings_booking_business_booking_business_update')
        g.custom_command('delete', 'bookings_booking_business_booking_business_delete')
        g.custom_command('create-booking-business', 'bookings_booking_business_booking_business_create_booking_business'
                         '')
        g.custom_command('get-booking-business', 'bookings_booking_business_booking_business_get_booking_business')
        g.custom_command('list-booking-business', 'bookings_booking_business_booking_business_list_booking_business')

    from azext_bookings.generated._client_factory import cf_booking_business
    bookings_booking_business = CliCommandType(
        operations_tmpl='azext_bookings.vendored_sdks.bookings.operations._booking_business_operations#BookingBusinessO'
        'perations.{}',
        client_factory=cf_booking_business)
    with self.command_group('bookings booking-business', bookings_booking_business, client_factory=cf_booking_business,
                             is_experimental=True) as g:
        g.custom_command('update', 'bookings_booking_business_update')
        g.custom_command('create-appointment', 'bookings_booking_business_create_appointment')
        g.custom_command('create-calendar-view', 'bookings_booking_business_create_calendar_view')
        g.custom_command('create-customer', 'bookings_booking_business_create_customer')
        g.custom_command('create-service', 'bookings_booking_business_create_service')
        g.custom_command('create-staff-member', 'bookings_booking_business_create_staff_member')
        g.custom_command('get-appointment', 'bookings_booking_business_get_appointment')
        g.custom_command('get-calendar-view', 'bookings_booking_business_get_calendar_view')
        g.custom_command('get-customer', 'bookings_booking_business_get_customer')
        g.custom_command('get-service', 'bookings_booking_business_get_service')
        g.custom_command('get-staff-member', 'bookings_booking_business_get_staff_member')
        g.custom_command('list-appointment', 'bookings_booking_business_list_appointment')
        g.custom_command('list-calendar-view', 'bookings_booking_business_list_calendar_view')
        g.custom_command('list-customer', 'bookings_booking_business_list_customer')
        g.custom_command('list-service', 'bookings_booking_business_list_service')
        g.custom_command('list-staff-member', 'bookings_booking_business_list_staff_member')
        g.custom_command('publish', 'bookings_booking_business_publish')
        g.custom_command('unpublish', 'bookings_booking_business_unpublish')

    from azext_bookings.generated._client_factory import cf_booking_business_appointment
    bookings_booking_business_appointment = CliCommandType(
        operations_tmpl='azext_bookings.vendored_sdks.bookings.operations._booking_business_appointment_operations#Book'
        'ingBusinessAppointmentOperations.{}',
        client_factory=cf_booking_business_appointment)
    with self.command_group('bookings booking-business-appointment', bookings_booking_business_appointment,
                            client_factory=cf_booking_business_appointment, is_experimental=True) as g:
        g.custom_command('cancel', 'bookings_booking_business_appointment_cancel')

    from azext_bookings.generated._client_factory import cf_booking_business_calendar_view
    bookings_booking_business_calendar_view = CliCommandType(
        operations_tmpl='azext_bookings.vendored_sdks.bookings.operations._booking_business_calendar_view_operations#Bo'
        'okingBusinessCalendarViewOperations.{}',
        client_factory=cf_booking_business_calendar_view)
    with self.command_group('bookings booking-business-calendar-view', bookings_booking_business_calendar_view,
                            client_factory=cf_booking_business_calendar_view, is_experimental=True) as g:
        g.custom_command('cancel', 'bookings_booking_business_calendar_view_cancel')

    from azext_bookings.generated._client_factory import cf_booking_currency_booking_currency
    bookings_booking_currency_booking_currency = CliCommandType(
        operations_tmpl='azext_bookings.vendored_sdks.bookings.operations._booking_currency_booking_currency_operations'
        '#BookingCurrencyOperations.{}',
        client_factory=cf_booking_currency_booking_currency)
    with self.command_group('bookings booking-currency-booking-currency', bookings_booking_currency_booking_currency,
                            client_factory=cf_booking_currency_booking_currency, is_experimental=True) as g:
        g.custom_command('update', 'bookings_booking_currency_booking_currency_update')
        g.custom_command('delete', 'bookings_booking_currency_booking_currency_delete')
        g.custom_command('create-booking-currency', 'bookings_booking_currency_booking_currency_create_booking_currency'
                         '')
        g.custom_command('get-booking-currency', 'bookings_booking_currency_booking_currency_get_booking_currency')
        g.custom_command('list-booking-currency', 'bookings_booking_currency_booking_currency_list_booking_currency')
