# coding: utf-8

"""
AsupEntry.py

 The Clear BSD License

 Copyright (c) – 2016, NetApp, Inc. All rights reserved.

 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

 * Neither the name of NetApp, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pprint import pformat
from six import iteritems


class AsupEntry(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsupEntry - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'file_name': 'str',  # (required parameter)
            'file_path': 'str',  
            'priority': 'int',  # (required parameter)
            'content_type': 'str',  # (required parameter)
            'description': 'str',  # (required parameter)
            'schedule': 'list[int]'
        }

        self.attribute_map = {
            'file_name': 'fileName',  # (required parameter)
            'file_path': 'filePath',  
            'priority': 'priority',  # (required parameter)
            'content_type': 'contentType',  # (required parameter)
            'description': 'description',  # (required parameter)
            'schedule': 'schedule'
        }

        self._file_name = None
        self._file_path = None
        self._priority = None
        self._content_type = None
        self._description = None
        self._schedule = None

    @property
    def file_name(self):
        """
        Gets the file_name of this AsupEntry.
        File name of the entry

        :return: The file_name of this AsupEntry.
        :rtype: str
        :required/optional: required
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this AsupEntry.
        File name of the entry

        :param file_name: The file_name of this AsupEntry.
        :type: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        """
        Gets the file_path of this AsupEntry.
        File path of the entry

        :return: The file_path of this AsupEntry.
        :rtype: str
        :required/optional: optional
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """
        Sets the file_path of this AsupEntry.
        File path of the entry

        :param file_path: The file_path of this AsupEntry.
        :type: str
        """
        self._file_path = file_path

    @property
    def priority(self):
        """
        Gets the priority of this AsupEntry.
        Priority of the entry

        :return: The priority of this AsupEntry.
        :rtype: int
        :required/optional: required
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this AsupEntry.
        Priority of the entry

        :param priority: The priority of this AsupEntry.
        :type: int
        """
        self._priority = priority

    @property
    def content_type(self):
        """
        Gets the content_type of this AsupEntry.
        Content type of the entry

        :return: The content_type of this AsupEntry.
        :rtype: str
        :required/optional: required
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this AsupEntry.
        Content type of the entry

        :param content_type: The content_type of this AsupEntry.
        :type: str
        """
        self._content_type = content_type

    @property
    def description(self):
        """
        Gets the description of this AsupEntry.
        Description of the entry

        :return: The description of this AsupEntry.
        :rtype: str
        :required/optional: required
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AsupEntry.
        Description of the entry

        :param description: The description of this AsupEntry.
        :type: str
        """
        self._description = description

    @property
    def schedule(self):
        """
        Gets the schedule of this AsupEntry.
        Scheduled dispatch of the entry

        :return: The schedule of this AsupEntry.
        :rtype: list[int]
        :required/optional: required
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this AsupEntry.
        Scheduled dispatch of the entry

        :param schedule: The schedule of this AsupEntry.
        :type: list[int]
        """
        self._schedule = schedule

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        if self is None:
           return None
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if self is None or other is None:
            return None
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

