# coding: utf-8

"""
SCSIInterface.py

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


class SCSIInterface(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SCSIInterface - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channel': 'int',  # (required parameter)
            'scsi_id': 'int',  # (required parameter)
            'speed': 'int',  # (required parameter)
            'scsi_type': 'str',  # (required parameter)
            'width': 'int',  # (required parameter)
            'part': 'str',  # (required parameter)
            'revision': 'int',  # (required parameter)
            'reserved1': 'str',  
            'reserved2': 'str'
        }

        self.attribute_map = {
            'channel': 'channel',  # (required parameter)
            'scsi_id': 'scsiID',  # (required parameter)
            'speed': 'speed',  # (required parameter)
            'scsi_type': 'scsiType',  # (required parameter)
            'width': 'width',  # (required parameter)
            'part': 'part',  # (required parameter)
            'revision': 'revision',  # (required parameter)
            'reserved1': 'reserved1',  
            'reserved2': 'reserved2'
        }

        self._channel = None
        self._scsi_id = None
        self._speed = None
        self._scsi_type = None
        self._width = None
        self._part = None
        self._revision = None
        self._reserved1 = None
        self._reserved2 = None

    @property
    def channel(self):
        """
        Gets the channel of this SCSIInterface.
        The channel number of this interface.

        :return: The channel of this SCSIInterface.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this SCSIInterface.
        The channel number of this interface.

        :param channel: The channel of this SCSIInterface.
        :type: int
        """
        self._channel = channel

    @property
    def scsi_id(self):
        """
        Gets the scsi_id of this SCSIInterface.
        The SCSI ID value used by the controller on this interface.

        :return: The scsi_id of this SCSIInterface.
        :rtype: int
        :required/optional: required
        """
        return self._scsi_id

    @scsi_id.setter
    def scsi_id(self, scsi_id):
        """
        Sets the scsi_id of this SCSIInterface.
        The SCSI ID value used by the controller on this interface.

        :param scsi_id: The scsi_id of this SCSIInterface.
        :type: int
        """
        self._scsi_id = scsi_id

    @property
    def speed(self):
        """
        Gets the speed of this SCSIInterface.
        The speed of the interface in MB/sec.

        :return: The speed of this SCSIInterface.
        :rtype: int
        :required/optional: required
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """
        Sets the speed of this SCSIInterface.
        The speed of the interface in MB/sec.

        :param speed: The speed of this SCSIInterface.
        :type: int
        """
        self._speed = speed

    @property
    def scsi_type(self):
        """
        Gets the scsi_type of this SCSIInterface.
        The type of SCSI line driver (e.g. SE, LVD, etc.) being used.

        :return: The scsi_type of this SCSIInterface.
        :rtype: str
        :required/optional: required
        """
        return self._scsi_type

    @scsi_type.setter
    def scsi_type(self, scsi_type):
        """
        Sets the scsi_type of this SCSIInterface.
        The type of SCSI line driver (e.g. SE, LVD, etc.) being used.

        :param scsi_type: The scsi_type of this SCSIInterface.
        :type: str
        """
        allowed_values = ["se", "hvd", "lvd", "__UNDEFINED"]
        if scsi_type not in allowed_values:
            raise ValueError(
                "Invalid value for `scsi_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._scsi_type = scsi_type

    @property
    def width(self):
        """
        Gets the width of this SCSIInterface.
        The transfer width of the SCSI bus, in bits.

        :return: The width of this SCSIInterface.
        :rtype: int
        :required/optional: required
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this SCSIInterface.
        The transfer width of the SCSI bus, in bits.

        :param width: The width of this SCSIInterface.
        :type: int
        """
        self._width = width

    @property
    def part(self):
        """
        Gets the part of this SCSIInterface.
        An ASCII text string that describes the SCSI controller chip type.

        :return: The part of this SCSIInterface.
        :rtype: str
        :required/optional: required
        """
        return self._part

    @part.setter
    def part(self, part):
        """
        Sets the part of this SCSIInterface.
        An ASCII text string that describes the SCSI controller chip type.

        :param part: The part of this SCSIInterface.
        :type: str
        """
        self._part = part

    @property
    def revision(self):
        """
        Gets the revision of this SCSIInterface.
        The revision level of the SCSI controller chip.

        :return: The revision of this SCSIInterface.
        :rtype: int
        :required/optional: required
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this SCSIInterface.
        The revision level of the SCSI controller chip.

        :param revision: The revision of this SCSIInterface.
        :type: int
        """
        self._revision = revision

    @property
    def reserved1(self):
        """
        Gets the reserved1 of this SCSIInterface.


        :return: The reserved1 of this SCSIInterface.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved1

    @reserved1.setter
    def reserved1(self, reserved1):
        """
        Sets the reserved1 of this SCSIInterface.


        :param reserved1: The reserved1 of this SCSIInterface.
        :type: str
        """
        self._reserved1 = reserved1

    @property
    def reserved2(self):
        """
        Gets the reserved2 of this SCSIInterface.


        :return: The reserved2 of this SCSIInterface.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """
        Sets the reserved2 of this SCSIInterface.


        :param reserved2: The reserved2 of this SCSIInterface.
        :type: str
        """
        self._reserved2 = reserved2

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
