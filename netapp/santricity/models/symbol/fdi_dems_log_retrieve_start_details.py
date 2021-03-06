# coding: utf-8

"""
FdiDemsLogRetrieveStartDetails.py

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


class FdiDemsLogRetrieveStartDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FdiDemsLogRetrieveStartDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'all_log_entries': 'bool',  # (required parameter)
            'oldest_entry_timestamp': 'int',  # (required parameter)
            'all_drives': 'bool',  # (required parameter)
            'drive_refs': 'DriveRefList'
        }

        self.attribute_map = {
            'all_log_entries': 'allLogEntries',  # (required parameter)
            'oldest_entry_timestamp': 'oldestEntryTimestamp',  # (required parameter)
            'all_drives': 'allDrives',  # (required parameter)
            'drive_refs': 'driveRefs'
        }

        self._all_log_entries = None
        self._oldest_entry_timestamp = None
        self._all_drives = None
        self._drive_refs = None

    @property
    def all_log_entries(self):
        """
        Gets the all_log_entries of this FdiDemsLogRetrieveStartDetails.
        If true, all log entries will be retrieved and the value of oldestEntryTimestamp will be ignored.

        :return: The all_log_entries of this FdiDemsLogRetrieveStartDetails.
        :rtype: bool
        :required/optional: required
        """
        return self._all_log_entries

    @all_log_entries.setter
    def all_log_entries(self, all_log_entries):
        """
        Sets the all_log_entries of this FdiDemsLogRetrieveStartDetails.
        If true, all log entries will be retrieved and the value of oldestEntryTimestamp will be ignored.

        :param all_log_entries: The all_log_entries of this FdiDemsLogRetrieveStartDetails.
        :type: bool
        """
        self._all_log_entries = all_log_entries

    @property
    def oldest_entry_timestamp(self):
        """
        Gets the oldest_entry_timestamp of this FdiDemsLogRetrieveStartDetails.
        If allLogEntries is false, log entries will be retrieved if their timestamp is equal to or more recent than this value (measured in seconds since midnight January 1, 1970).

        :return: The oldest_entry_timestamp of this FdiDemsLogRetrieveStartDetails.
        :rtype: int
        :required/optional: required
        """
        return self._oldest_entry_timestamp

    @oldest_entry_timestamp.setter
    def oldest_entry_timestamp(self, oldest_entry_timestamp):
        """
        Sets the oldest_entry_timestamp of this FdiDemsLogRetrieveStartDetails.
        If allLogEntries is false, log entries will be retrieved if their timestamp is equal to or more recent than this value (measured in seconds since midnight January 1, 1970).

        :param oldest_entry_timestamp: The oldest_entry_timestamp of this FdiDemsLogRetrieveStartDetails.
        :type: int
        """
        self._oldest_entry_timestamp = oldest_entry_timestamp

    @property
    def all_drives(self):
        """
        Gets the all_drives of this FdiDemsLogRetrieveStartDetails.
        If true, log entries will be retrieved for all drives and the values in driveRefs will be ignored.

        :return: The all_drives of this FdiDemsLogRetrieveStartDetails.
        :rtype: bool
        :required/optional: required
        """
        return self._all_drives

    @all_drives.setter
    def all_drives(self, all_drives):
        """
        Sets the all_drives of this FdiDemsLogRetrieveStartDetails.
        If true, log entries will be retrieved for all drives and the values in driveRefs will be ignored.

        :param all_drives: The all_drives of this FdiDemsLogRetrieveStartDetails.
        :type: bool
        """
        self._all_drives = all_drives

    @property
    def drive_refs(self):
        """
        Gets the drive_refs of this FdiDemsLogRetrieveStartDetails.
        If allDrives is false, log entries will be retrieved only for the drives in this list.

        :return: The drive_refs of this FdiDemsLogRetrieveStartDetails.
        :rtype: DriveRefList
        :required/optional: required
        """
        return self._drive_refs

    @drive_refs.setter
    def drive_refs(self, drive_refs):
        """
        Sets the drive_refs of this FdiDemsLogRetrieveStartDetails.
        If allDrives is false, log entries will be retrieved only for the drives in this list.

        :param drive_refs: The drive_refs of this FdiDemsLogRetrieveStartDetails.
        :type: DriveRefList
        """
        self._drive_refs = drive_refs

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

