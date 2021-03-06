# coding: utf-8

"""
AsyncMirrorRepositoryUtilization.py

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


class AsyncMirrorRepositoryUtilization(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorRepositoryUtilization - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pit_data_bytes': 'int',  # (required parameter)
            'delta_log_bytes': 'int',  # (required parameter)
            'bytes_available': 'int',  # (required parameter)
            'mirror_ref': 'str',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'pit_data_bytes': 'pitDataBytes',  # (required parameter)
            'delta_log_bytes': 'deltaLogBytes',  # (required parameter)
            'bytes_available': 'bytesAvailable',  # (required parameter)
            'mirror_ref': 'mirrorRef',  # (required parameter)
            'id': 'id'
        }

        self._pit_data_bytes = None
        self._delta_log_bytes = None
        self._bytes_available = None
        self._mirror_ref = None
        self._id = None

    @property
    def pit_data_bytes(self):
        """
        Gets the pit_data_bytes of this AsyncMirrorRepositoryUtilization.
        The total number of bytes used in the repository for copy-on-write data and related metadata.

        :return: The pit_data_bytes of this AsyncMirrorRepositoryUtilization.
        :rtype: int
        :required/optional: required
        """
        return self._pit_data_bytes

    @pit_data_bytes.setter
    def pit_data_bytes(self, pit_data_bytes):
        """
        Sets the pit_data_bytes of this AsyncMirrorRepositoryUtilization.
        The total number of bytes used in the repository for copy-on-write data and related metadata.

        :param pit_data_bytes: The pit_data_bytes of this AsyncMirrorRepositoryUtilization.
        :type: int
        """
        self._pit_data_bytes = pit_data_bytes

    @property
    def delta_log_bytes(self):
        """
        Gets the delta_log_bytes of this AsyncMirrorRepositoryUtilization.
        The total number of bytes used for the delta logs (bitmaps).

        :return: The delta_log_bytes of this AsyncMirrorRepositoryUtilization.
        :rtype: int
        :required/optional: required
        """
        return self._delta_log_bytes

    @delta_log_bytes.setter
    def delta_log_bytes(self, delta_log_bytes):
        """
        Sets the delta_log_bytes of this AsyncMirrorRepositoryUtilization.
        The total number of bytes used for the delta logs (bitmaps).

        :param delta_log_bytes: The delta_log_bytes of this AsyncMirrorRepositoryUtilization.
        :type: int
        """
        self._delta_log_bytes = delta_log_bytes

    @property
    def bytes_available(self):
        """
        Gets the bytes_available of this AsyncMirrorRepositoryUtilization.
        The total number of bytes available for ongoing copy-on-write operations.

        :return: The bytes_available of this AsyncMirrorRepositoryUtilization.
        :rtype: int
        :required/optional: required
        """
        return self._bytes_available

    @bytes_available.setter
    def bytes_available(self, bytes_available):
        """
        Sets the bytes_available of this AsyncMirrorRepositoryUtilization.
        The total number of bytes available for ongoing copy-on-write operations.

        :param bytes_available: The bytes_available of this AsyncMirrorRepositoryUtilization.
        :type: int
        """
        self._bytes_available = bytes_available

    @property
    def mirror_ref(self):
        """
        Gets the mirror_ref of this AsyncMirrorRepositoryUtilization.
        The mirror group member for which this utilization information applies.

        :return: The mirror_ref of this AsyncMirrorRepositoryUtilization.
        :rtype: str
        :required/optional: required
        """
        return self._mirror_ref

    @mirror_ref.setter
    def mirror_ref(self, mirror_ref):
        """
        Sets the mirror_ref of this AsyncMirrorRepositoryUtilization.
        The mirror group member for which this utilization information applies.

        :param mirror_ref: The mirror_ref of this AsyncMirrorRepositoryUtilization.
        :type: str
        """
        self._mirror_ref = mirror_ref

    @property
    def id(self):
        """
        Gets the id of this AsyncMirrorRepositoryUtilization.


        :return: The id of this AsyncMirrorRepositoryUtilization.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AsyncMirrorRepositoryUtilization.


        :param id: The id of this AsyncMirrorRepositoryUtilization.
        :type: str
        """
        self._id = id

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

