# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfPerson(msrest.serialization.Model):
    """Collection of person.

    :param value:
    :type value: list[~users_people.models.MicrosoftGraphPerson]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPerson]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfPerson, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class MicrosoftGraphEntity(msrest.serialization.Model):
    """entity.

    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class MicrosoftGraphLocation(msrest.serialization.Model):
    """location.

    :param display_name: The name associated with the location.
    :type display_name: str
    :param location_email_address: Optional email address of the location.
    :type location_email_address: str
    :param address: physicalAddress.
    :type address: ~users_people.models.MicrosoftGraphPhysicalAddress
    :param coordinates: outlookGeoCoordinates.
    :type coordinates: ~users_people.models.MicrosoftGraphOutlookGeoCoordinates
    :param location_uri: Optional URI representing the location.
    :type location_uri: str
    :param location_type: locationType. Possible values include: "default", "conferenceRoom",
     "homeAddress", "businessAddress", "geoCoordinates", "streetAddress", "hotel", "restaurant",
     "localBusiness", "postalAddress".
    :type location_type: str or ~users_people.models.MicrosoftGraphLocationType
    :param unique_id: For internal use only.
    :type unique_id: str
    :param unique_id_type: locationUniqueIdType. Possible values include: "unknown",
     "locationStore", "directory", "private", "bing".
    :type unique_id_type: str or ~users_people.models.MicrosoftGraphLocationUniqueIdType
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'location_email_address': {'key': 'locationEmailAddress', 'type': 'str'},
        'address': {'key': 'address', 'type': 'MicrosoftGraphPhysicalAddress'},
        'coordinates': {'key': 'coordinates', 'type': 'MicrosoftGraphOutlookGeoCoordinates'},
        'location_uri': {'key': 'locationUri', 'type': 'str'},
        'location_type': {'key': 'locationType', 'type': 'str'},
        'unique_id': {'key': 'uniqueId', 'type': 'str'},
        'unique_id_type': {'key': 'uniqueIdType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphLocation, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.location_email_address = kwargs.get('location_email_address', None)
        self.address = kwargs.get('address', None)
        self.coordinates = kwargs.get('coordinates', None)
        self.location_uri = kwargs.get('location_uri', None)
        self.location_type = kwargs.get('location_type', None)
        self.unique_id = kwargs.get('unique_id', None)
        self.unique_id_type = kwargs.get('unique_id_type', None)


class MicrosoftGraphOutlookGeoCoordinates(msrest.serialization.Model):
    """outlookGeoCoordinates.

    :param altitude: The altitude of the location.
    :type altitude: float
    :param latitude: The latitude of the location.
    :type latitude: float
    :param longitude: The longitude of the location.
    :type longitude: float
    :param accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be
     measured in meters, such as the latitude and longitude are accurate to within 50 meters.
    :type accuracy: float
    :param altitude_accuracy: The accuracy of the altitude.
    :type altitude_accuracy: float
    """

    _attribute_map = {
        'altitude': {'key': 'altitude', 'type': 'float'},
        'latitude': {'key': 'latitude', 'type': 'float'},
        'longitude': {'key': 'longitude', 'type': 'float'},
        'accuracy': {'key': 'accuracy', 'type': 'float'},
        'altitude_accuracy': {'key': 'altitudeAccuracy', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphOutlookGeoCoordinates, self).__init__(**kwargs)
        self.altitude = kwargs.get('altitude', None)
        self.latitude = kwargs.get('latitude', None)
        self.longitude = kwargs.get('longitude', None)
        self.accuracy = kwargs.get('accuracy', None)
        self.altitude_accuracy = kwargs.get('altitude_accuracy', None)


class MicrosoftGraphPerson(MicrosoftGraphEntity):
    """person.

    :param id: Read-only.
    :type id: str
    :param display_name: The person's display name.
    :type display_name: str
    :param given_name: The person's given name.
    :type given_name: str
    :param surname: The person's surname.
    :type surname: str
    :param birthday: The person's birthday.
    :type birthday: str
    :param person_notes: Free-form notes that the user has taken about this person.
    :type person_notes: str
    :param is_favorite: true if the user has flagged this person as a favorite.
    :type is_favorite: bool
    :param email_addresses:
    :type email_addresses: list[~users_people.models.MicrosoftGraphRankedEmailAddress]
    :param phones: The person's phone numbers.
    :type phones: list[~users_people.models.MicrosoftGraphPhone]
    :param postal_addresses: The person's addresses.
    :type postal_addresses: list[~users_people.models.MicrosoftGraphLocation]
    :param websites: The person's websites.
    :type websites: list[~users_people.models.MicrosoftGraphWebsite]
    :param title:
    :type title: str
    :param company_name: The name of the person's company.
    :type company_name: str
    :param yomi_company: The phonetic Japanese name of the person's company.
    :type yomi_company: str
    :param department: The person's department.
    :type department: str
    :param office_location: The location of the person's office.
    :type office_location: str
    :param profession: The person's profession.
    :type profession: str
    :param sources:
    :type sources: list[~users_people.models.MicrosoftGraphPersonDataSource]
    :param mailbox_type:
    :type mailbox_type: str
    :param person_type: The type of person.
    :type person_type: str
    :param user_principal_name: The user principal name (UPN) of the person. The UPN is an
     Internet-style login name for the person based on the Internet standard RFC 822. By convention,
     this should map to the person's email name. The general format is alias@domain.
    :type user_principal_name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'given_name': {'key': 'givenName', 'type': 'str'},
        'surname': {'key': 'surname', 'type': 'str'},
        'birthday': {'key': 'birthday', 'type': 'str'},
        'person_notes': {'key': 'personNotes', 'type': 'str'},
        'is_favorite': {'key': 'isFavorite', 'type': 'bool'},
        'email_addresses': {'key': 'emailAddresses', 'type': '[MicrosoftGraphRankedEmailAddress]'},
        'phones': {'key': 'phones', 'type': '[MicrosoftGraphPhone]'},
        'postal_addresses': {'key': 'postalAddresses', 'type': '[MicrosoftGraphLocation]'},
        'websites': {'key': 'websites', 'type': '[MicrosoftGraphWebsite]'},
        'title': {'key': 'title', 'type': 'str'},
        'company_name': {'key': 'companyName', 'type': 'str'},
        'yomi_company': {'key': 'yomiCompany', 'type': 'str'},
        'department': {'key': 'department', 'type': 'str'},
        'office_location': {'key': 'officeLocation', 'type': 'str'},
        'profession': {'key': 'profession', 'type': 'str'},
        'sources': {'key': 'sources', 'type': '[MicrosoftGraphPersonDataSource]'},
        'mailbox_type': {'key': 'mailboxType', 'type': 'str'},
        'person_type': {'key': 'personType', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphPerson, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.given_name = kwargs.get('given_name', None)
        self.surname = kwargs.get('surname', None)
        self.birthday = kwargs.get('birthday', None)
        self.person_notes = kwargs.get('person_notes', None)
        self.is_favorite = kwargs.get('is_favorite', None)
        self.email_addresses = kwargs.get('email_addresses', None)
        self.phones = kwargs.get('phones', None)
        self.postal_addresses = kwargs.get('postal_addresses', None)
        self.websites = kwargs.get('websites', None)
        self.title = kwargs.get('title', None)
        self.company_name = kwargs.get('company_name', None)
        self.yomi_company = kwargs.get('yomi_company', None)
        self.department = kwargs.get('department', None)
        self.office_location = kwargs.get('office_location', None)
        self.profession = kwargs.get('profession', None)
        self.sources = kwargs.get('sources', None)
        self.mailbox_type = kwargs.get('mailbox_type', None)
        self.person_type = kwargs.get('person_type', None)
        self.user_principal_name = kwargs.get('user_principal_name', None)


class MicrosoftGraphPersonDataSource(msrest.serialization.Model):
    """personDataSource.

    :param type:
    :type type: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphPersonDataSource, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)


class MicrosoftGraphPhone(msrest.serialization.Model):
    """phone.

    :param type: phoneType. Possible values include: "home", "business", "mobile", "other",
     "assistant", "homeFax", "businessFax", "otherFax", "pager", "radio".
    :type type: str or ~users_people.models.MicrosoftGraphPhoneType
    :param number: The phone number.
    :type number: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'number': {'key': 'number', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphPhone, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.number = kwargs.get('number', None)


class MicrosoftGraphPhysicalAddress(msrest.serialization.Model):
    """physicalAddress.

    :param type: physicalAddressType. Possible values include: "unknown", "home", "business",
     "other".
    :type type: str or ~users_people.models.MicrosoftGraphPhysicalAddressType
    :param post_office_box:
    :type post_office_box: str
    :param street: The street.
    :type street: str
    :param city: The city.
    :type city: str
    :param state: The state.
    :type state: str
    :param country_or_region: The country or region. It's a free-format string value, for example,
     'United States'.
    :type country_or_region: str
    :param postal_code: The postal code.
    :type postal_code: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'post_office_box': {'key': 'postOfficeBox', 'type': 'str'},
        'street': {'key': 'street', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'country_or_region': {'key': 'countryOrRegion', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphPhysicalAddress, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.post_office_box = kwargs.get('post_office_box', None)
        self.street = kwargs.get('street', None)
        self.city = kwargs.get('city', None)
        self.state = kwargs.get('state', None)
        self.country_or_region = kwargs.get('country_or_region', None)
        self.postal_code = kwargs.get('postal_code', None)


class MicrosoftGraphRankedEmailAddress(msrest.serialization.Model):
    """rankedEmailAddress.

    :param address:
    :type address: str
    :param rank:
    :type rank: float
    """

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'rank': {'key': 'rank', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphRankedEmailAddress, self).__init__(**kwargs)
        self.address = kwargs.get('address', None)
        self.rank = kwargs.get('rank', None)


class MicrosoftGraphWebsite(msrest.serialization.Model):
    """website.

    :param type: websiteType. Possible values include: "other", "home", "work", "blog", "profile".
    :type type: str or ~users_people.models.MicrosoftGraphWebsiteType
    :param address: The URL of the website.
    :type address: str
    :param display_name: The display name of the web site.
    :type display_name: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'address': {'key': 'address', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphWebsite, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.address = kwargs.get('address', None)
        self.display_name = kwargs.get('display_name', None)


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~users_people.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.error = kwargs['error']


class OdataErrorDetail(msrest.serialization.Model):
    """OdataErrorDetail.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)


class OdataErrorMain(msrest.serialization.Model):
    """OdataErrorMain.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~users_people.models.OdataErrorDetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[OdataErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)
