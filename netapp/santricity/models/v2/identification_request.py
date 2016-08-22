# coding: utf-8

"""
IdentificationRequest.py

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


class IdentificationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IdentificationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channels': 'list[int]',  
            'trays': 'list[str]',  
            'drives': 'list[str]',  
            'pools': 'list[str]',  
            'volumes': 'list[str]',  
            'storage_system': 'bool'
        }

        self.attribute_map = {
            'channels': 'channels',  
            'trays': 'trays',  
            'drives': 'drives',  
            'pools': 'pools',  
            'volumes': 'volumes',  
            'storage_system': 'storageSystem'
        }

        self._channels = None
        self._trays = None
        self._drives = None
        self._pools = None
        self._volumes = None
        self._storage_system = None

    @property
    def channels(self):
        """
        Gets the channels of this IdentificationRequest.
        A list of channel ids.

        :return: The channels of this IdentificationRequest.
        :rtype: list[int]
        :required/optional: optional
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """
        Sets the channels of this IdentificationRequest.
        A list of channel ids.

        :param channels: The channels of this IdentificationRequest.
        :type: list[int]
        """
        self._channels = channels

    @property
    def trays(self):
        """
        Gets the trays of this IdentificationRequest.
        A list of tray ids.

        :return: The trays of this IdentificationRequest.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._trays

    @trays.setter
    def trays(self, trays):
        """
        Sets the trays of this IdentificationRequest.
        A list of tray ids.

        :param trays: The trays of this IdentificationRequest.
        :type: list[str]
        """
        self._trays = trays

    @property
    def drives(self):
        """
        Gets the drives of this IdentificationRequest.
        A list of drive ids.

        :return: The drives of this IdentificationRequest.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """
        Sets the drives of this IdentificationRequest.
        A list of drive ids.

        :param drives: The drives of this IdentificationRequest.
        :type: list[str]
        """
        self._drives = drives

    @property
    def pools(self):
        """
        Gets the pools of this IdentificationRequest.
        A list of storage pool ids. Associated, optimal drives will be identified.

        :return: The pools of this IdentificationRequest.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """
        Sets the pools of this IdentificationRequest.
        A list of storage pool ids. Associated, optimal drives will be identified.

        :param pools: The pools of this IdentificationRequest.
        :type: list[str]
        """
        self._pools = pools

    @property
    def volumes(self):
        """
        Gets the volumes of this IdentificationRequest.
        A list of volume ids. Associated, optimal drives will be identified.

        :return: The volumes of this IdentificationRequest.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this IdentificationRequest.
        A list of volume ids. Associated, optimal drives will be identified.

        :param volumes: The volumes of this IdentificationRequest.
        :type: list[str]
        """
        self._volumes = volumes

    @property
    def storage_system(self):
        """
        Gets the storage_system of this IdentificationRequest.
        Set to \"true\" to identify the StorageSystem.

        :return: The storage_system of this IdentificationRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._storage_system

    @storage_system.setter
    def storage_system(self, storage_system):
        """
        Sets the storage_system of this IdentificationRequest.
        Set to \"true\" to identify the StorageSystem.

        :param storage_system: The storage_system of this IdentificationRequest.
        :type: bool
        """
        self._storage_system = storage_system

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
