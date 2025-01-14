# coding: utf-8

"""
    Tenants API

    Manage Tapis Tenants.  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: cicsupport@tacc.utexas.edu
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class LDAP(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ldap_id': 'str',
        'url': 'str',
        'port': 'int',
        'use_ssl': 'bool',
        'user_dn': 'str',
        'bind_dn': 'str',
        'bind_credential': 'str',
        'account_type': 'str',
        'create_time': 'str',
        'last_update_time': 'str'
    }

    attribute_map = {
        'ldap_id': 'ldap_id',
        'url': 'url',
        'port': 'port',
        'use_ssl': 'use_ssl',
        'user_dn': 'user_dn',
        'bind_dn': 'bind_dn',
        'bind_credential': 'bind_credential',
        'account_type': 'account_type',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time'
    }

    def __init__(self, ldap_id=None, url=None, port=None, use_ssl=None, user_dn=None, bind_dn=None, bind_credential=None, account_type=None, create_time=None, last_update_time=None):  # noqa: E501
        """LDAP - a model defined in OpenAPI"""  # noqa: E501

        self._ldap_id = None
        self._url = None
        self._port = None
        self._use_ssl = None
        self._user_dn = None
        self._bind_dn = None
        self._bind_credential = None
        self._account_type = None
        self._create_time = None
        self._last_update_time = None
        self.discriminator = None

        if ldap_id is not None:
            self.ldap_id = ldap_id
        if url is not None:
            self.url = url
        if port is not None:
            self.port = port
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if user_dn is not None:
            self.user_dn = user_dn
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_credential is not None:
            self.bind_credential = bind_credential
        if account_type is not None:
            self.account_type = account_type
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time

    @property
    def ldap_id(self):
        """Gets the ldap_id of this LDAP.  # noqa: E501

        Unique id for the LDAP object.  # noqa: E501

        :return: The ldap_id of this LDAP.  # noqa: E501
        :rtype: str
        """
        return self._ldap_id

    @ldap_id.setter
    def ldap_id(self, ldap_id):
        """Sets the ldap_id of this LDAP.

        Unique id for the LDAP object.  # noqa: E501

        :param ldap_id: The ldap_id of this LDAP.  # noqa: E501
        :type: str
        """

        self._ldap_id = ldap_id

    @property
    def url(self):
        """Gets the url of this LDAP.  # noqa: E501

        url to the LDAP  # noqa: E501

        :return: The url of this LDAP.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LDAP.

        url to the LDAP  # noqa: E501

        :param url: The url of this LDAP.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def port(self):
        """Gets the port of this LDAP.  # noqa: E501

        port for the LDAP  # noqa: E501

        :return: The port of this LDAP.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this LDAP.

        port for the LDAP  # noqa: E501

        :param port: The port of this LDAP.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def use_ssl(self):
        """Gets the use_ssl of this LDAP.  # noqa: E501

        Whether to use SSL with the LDAP  # noqa: E501

        :return: The use_ssl of this LDAP.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this LDAP.

        Whether to use SSL with the LDAP  # noqa: E501

        :param use_ssl: The use_ssl of this LDAP.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def user_dn(self):
        """Gets the user_dn of this LDAP.  # noqa: E501

        base DN for users  # noqa: E501

        :return: The user_dn of this LDAP.  # noqa: E501
        :rtype: str
        """
        return self._user_dn

    @user_dn.setter
    def user_dn(self, user_dn):
        """Sets the user_dn of this LDAP.

        base DN for users  # noqa: E501

        :param user_dn: The user_dn of this LDAP.  # noqa: E501
        :type: str
        """

        self._user_dn = user_dn

    @property
    def bind_dn(self):
        """Gets the bind_dn of this LDAP.  # noqa: E501

        DN used for binding to the LDAP.  # noqa: E501

        :return: The bind_dn of this LDAP.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this LDAP.

        DN used for binding to the LDAP.  # noqa: E501

        :param bind_dn: The bind_dn of this LDAP.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_credential(self):
        """Gets the bind_credential of this LDAP.  # noqa: E501

        Pointed to a Tapis credential for binding to the LDAP.  # noqa: E501

        :return: The bind_credential of this LDAP.  # noqa: E501
        :rtype: str
        """
        return self._bind_credential

    @bind_credential.setter
    def bind_credential(self, bind_credential):
        """Sets the bind_credential of this LDAP.

        Pointed to a Tapis credential for binding to the LDAP.  # noqa: E501

        :param bind_credential: The bind_credential of this LDAP.  # noqa: E501
        :type: str
        """

        self._bind_credential = bind_credential

    @property
    def account_type(self):
        """Gets the account_type of this LDAP.  # noqa: E501

        Whether this LDAP is used for service accounts or user accounts.  # noqa: E501

        :return: The account_type of this LDAP.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this LDAP.

        Whether this LDAP is used for service accounts or user accounts.  # noqa: E501

        :param account_type: The account_type of this LDAP.  # noqa: E501
        :type: str
        """
        allowed_values = ["service", "user"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def create_time(self):
        """Gets the create_time of this LDAP.  # noqa: E501

        The time the client was created.  # noqa: E501

        :return: The create_time of this LDAP.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this LDAP.

        The time the client was created.  # noqa: E501

        :param create_time: The create_time of this LDAP.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this LDAP.  # noqa: E501

        The time the client was last updated.  # noqa: E501

        :return: The last_update_time of this LDAP.  # noqa: E501
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this LDAP.

        The time the client was last updated.  # noqa: E501

        :param last_update_time: The last_update_time of this LDAP.  # noqa: E501
        :type: str
        """

        self._last_update_time = last_update_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LDAP):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
