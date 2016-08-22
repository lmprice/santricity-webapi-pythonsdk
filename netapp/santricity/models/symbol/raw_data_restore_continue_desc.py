# coding: utf-8

"""
RawDataRestoreContinueDesc.py

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


class RawDataRestoreContinueDesc(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RawDataRestoreContinueDesc - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',  # (required parameter)
            'final_sequence_number': 'int',  # (required parameter)
            'this_sequence_number': 'int',  # (required parameter)
            'details': 'RawDataRestoreChunkDetails',  # (required parameter)
            'controller_ref': 'str'
        }

        self.attribute_map = {
            'type': 'type',  # (required parameter)
            'final_sequence_number': 'finalSequenceNumber',  # (required parameter)
            'this_sequence_number': 'thisSequenceNumber',  # (required parameter)
            'details': 'details',  # (required parameter)
            'controller_ref': 'controllerRef'
        }

        self._type = None
        self._final_sequence_number = None
        self._this_sequence_number = None
        self._details = None
        self._controller_ref = None

    @property
    def type(self):
        """
        Gets the type of this RawDataRestoreContinueDesc.
        The type of transfer

        :return: The type of this RawDataRestoreContinueDesc.
        :rtype: str
        :required/optional: required
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RawDataRestoreContinueDesc.
        The type of transfer

        :param type: The type of this RawDataRestoreContinueDesc.
        :type: str
        """
        allowed_values = ["unknown", "dq", "dbmblk", "dbmrec", "dbmCheck", "enclosureStateCapture", "dplCoreDumpBundle", "ioStatistics", "fdiDemsLogs", "drivePerformanceHistory", "iocDump", "driveHealthLogs", "ctrlPerfLogs", "dom0SupportData", "retrieveWlcAnalytics", "autoLoadBalanceStatisticsLog", "__UNDEFINED"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def final_sequence_number(self):
        """
        Gets the final_sequence_number of this RawDataRestoreContinueDesc.
        Indicates the sequence number of the last chunk that will be delivered to the controller.

        :return: The final_sequence_number of this RawDataRestoreContinueDesc.
        :rtype: int
        :required/optional: required
        """
        return self._final_sequence_number

    @final_sequence_number.setter
    def final_sequence_number(self, final_sequence_number):
        """
        Sets the final_sequence_number of this RawDataRestoreContinueDesc.
        Indicates the sequence number of the last chunk that will be delivered to the controller.

        :param final_sequence_number: The final_sequence_number of this RawDataRestoreContinueDesc.
        :type: int
        """
        self._final_sequence_number = final_sequence_number

    @property
    def this_sequence_number(self):
        """
        Gets the this_sequence_number of this RawDataRestoreContinueDesc.
        The sequence number of the current chunk of data being delivered to the controller.

        :return: The this_sequence_number of this RawDataRestoreContinueDesc.
        :rtype: int
        :required/optional: required
        """
        return self._this_sequence_number

    @this_sequence_number.setter
    def this_sequence_number(self, this_sequence_number):
        """
        Sets the this_sequence_number of this RawDataRestoreContinueDesc.
        The sequence number of the current chunk of data being delivered to the controller.

        :param this_sequence_number: The this_sequence_number of this RawDataRestoreContinueDesc.
        :type: int
        """
        self._this_sequence_number = this_sequence_number

    @property
    def details(self):
        """
        Gets the details of this RawDataRestoreContinueDesc.
        The transfer type-specific details.

        :return: The details of this RawDataRestoreContinueDesc.
        :rtype: RawDataRestoreChunkDetails
        :required/optional: required
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this RawDataRestoreContinueDesc.
        The transfer type-specific details.

        :param details: The details of this RawDataRestoreContinueDesc.
        :type: RawDataRestoreChunkDetails
        """
        self._details = details

    @property
    def controller_ref(self):
        """
        Gets the controller_ref of this RawDataRestoreContinueDesc.
        The controller running the retrieve.

        :return: The controller_ref of this RawDataRestoreContinueDesc.
        :rtype: str
        :required/optional: required
        """
        return self._controller_ref

    @controller_ref.setter
    def controller_ref(self, controller_ref):
        """
        Sets the controller_ref of this RawDataRestoreContinueDesc.
        The controller running the retrieve.

        :param controller_ref: The controller_ref of this RawDataRestoreContinueDesc.
        :type: str
        """
        self._controller_ref = controller_ref

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
