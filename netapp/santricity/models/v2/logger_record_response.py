# coding: utf-8

"""
LoggerRecordResponse.py

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


class LoggerRecordResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LoggerRecordResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'record_type': 'str',  
            'log_records': 'list[LocalizedLogMessage]',  
            'time_stamps': 'dict(String, datetime)'
        }

        self.attribute_map = {
            'record_type': 'recordType',  
            'log_records': 'logRecords',  
            'time_stamps': 'timeStamps'
        }

        self._record_type = None
        self._log_records = None
        self._time_stamps = None

    @property
    def record_type(self):
        """
        Gets the record_type of this LoggerRecordResponse.
        Type of log records returned

        :return: The record_type of this LoggerRecordResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """
        Sets the record_type of this LoggerRecordResponse.
        Type of log records returned

        :param record_type: The record_type of this LoggerRecordResponse.
        :type: str
        """
        allowed_values = ["cfwUpgradeLogger", "driveUpgradeLogger", "iomServiceLogger", "cfwUpgradeTimestamp", "driveUpgradeTimestamp", "iomServiceTimestamp"]
        if record_type not in allowed_values:
            raise ValueError(
                "Invalid value for `record_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._record_type = record_type

    @property
    def log_records(self):
        """
        Gets the log_records of this LoggerRecordResponse.
        A Map of log records requested

        :return: The log_records of this LoggerRecordResponse.
        :rtype: list[LocalizedLogMessage]
        :required/optional: optional
        """
        return self._log_records

    @log_records.setter
    def log_records(self, log_records):
        """
        Sets the log_records of this LoggerRecordResponse.
        A Map of log records requested

        :param log_records: The log_records of this LoggerRecordResponse.
        :type: list[LocalizedLogMessage]
        """
        self._log_records = log_records

    @property
    def time_stamps(self):
        """
        Gets the time_stamps of this LoggerRecordResponse.
        A Map of timestamps for each logger type

        :return: The time_stamps of this LoggerRecordResponse.
        :rtype: dict(String, datetime)
        :required/optional: required
        """
        return self._time_stamps

    @time_stamps.setter
    def time_stamps(self, time_stamps):
        """
        Sets the time_stamps of this LoggerRecordResponse.
        A Map of timestamps for each logger type

        :param time_stamps: The time_stamps of this LoggerRecordResponse.
        :type: dict(String, datetime)
        """
        self._time_stamps = time_stamps

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
