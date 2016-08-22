# coding: utf-8

"""
VolumeGroupTypeData.py

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


class VolumeGroupTypeData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VolumeGroupTypeData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',  # (required parameter)
            'disk_pool_data': 'DiskPoolData'
        }

        self.attribute_map = {
            'type': 'type',  # (required parameter)
            'disk_pool_data': 'diskPoolData'
        }

        self._type = None
        self._disk_pool_data = None

    @property
    def type(self):
        """
        Gets the type of this VolumeGroupTypeData.
        This enumeration is used to indicate the type of the volume group.

        :return: The type of this VolumeGroupTypeData.
        :rtype: str
        :required/optional: required
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VolumeGroupTypeData.
        This enumeration is used to indicate the type of the volume group.

        :param type: The type of this VolumeGroupTypeData.
        :type: str
        """
        allowed_values = ["unknown", "traditional", "diskPool", "__UNDEFINED"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def disk_pool_data(self):
        """
        Gets the disk_pool_data of this VolumeGroupTypeData.
        This field is present only if the value of type is equal to VG_TYPE_DISK_POOL.

        :return: The disk_pool_data of this VolumeGroupTypeData.
        :rtype: DiskPoolData
        :required/optional: optional
        """
        return self._disk_pool_data

    @disk_pool_data.setter
    def disk_pool_data(self, disk_pool_data):
        """
        Sets the disk_pool_data of this VolumeGroupTypeData.
        This field is present only if the value of type is equal to VG_TYPE_DISK_POOL.

        :param disk_pool_data: The disk_pool_data of this VolumeGroupTypeData.
        :type: DiskPoolData
        """
        self._disk_pool_data = disk_pool_data

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
