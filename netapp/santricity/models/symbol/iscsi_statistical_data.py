# coding: utf-8

"""
IscsiStatisticalData.py

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


class IscsiStatisticalData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IscsiStatisticalData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'controller': 'str',  # (required parameter)
            'time_data': 'StatisticalTimeData',  # (required parameter)
            'iscsi_interface_statistics': 'IscsiInterfaceStatistics',  # (required parameter)
            'iscsi_target_statistics': 'list[IscsiTargetStatistics]',  # (required parameter)
            'iscsi_initiator_statistics': 'list[IscsiInitiatorStatistics]'
        }

        self.attribute_map = {
            'controller': 'controller',  # (required parameter)
            'time_data': 'timeData',  # (required parameter)
            'iscsi_interface_statistics': 'iscsiInterfaceStatistics',  # (required parameter)
            'iscsi_target_statistics': 'iscsiTargetStatistics',  # (required parameter)
            'iscsi_initiator_statistics': 'iscsiInitiatorStatistics'
        }

        self._controller = None
        self._time_data = None
        self._iscsi_interface_statistics = None
        self._iscsi_target_statistics = None
        self._iscsi_initiator_statistics = None

    @property
    def controller(self):
        """
        Gets the controller of this IscsiStatisticalData.
        A reference to the controller that collected these statistics.

        :return: The controller of this IscsiStatisticalData.
        :rtype: str
        :required/optional: required
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this IscsiStatisticalData.
        A reference to the controller that collected these statistics.

        :param controller: The controller of this IscsiStatisticalData.
        :type: str
        """
        self._controller = controller

    @property
    def time_data(self):
        """
        Gets the time_data of this IscsiStatisticalData.
        The time data associated with this set of statistics.

        :return: The time_data of this IscsiStatisticalData.
        :rtype: StatisticalTimeData
        :required/optional: required
        """
        return self._time_data

    @time_data.setter
    def time_data(self, time_data):
        """
        Sets the time_data of this IscsiStatisticalData.
        The time data associated with this set of statistics.

        :param time_data: The time_data of this IscsiStatisticalData.
        :type: StatisticalTimeData
        """
        self._time_data = time_data

    @property
    def iscsi_interface_statistics(self):
        """
        Gets the iscsi_interface_statistics of this IscsiStatisticalData.
        iSCSI statistical data that pertain to the iSCSI interfaces for this controller. Each sub-structure of IscsiInterfaceStatistics has data identifying the iSCSI interface(s) with which the statistics are associated. Note that the data in any of the sub-structures may be associated with multiple interfaces. See the section on the IscsiInterfaceStatistics structure.

        :return: The iscsi_interface_statistics of this IscsiStatisticalData.
        :rtype: IscsiInterfaceStatistics
        :required/optional: required
        """
        return self._iscsi_interface_statistics

    @iscsi_interface_statistics.setter
    def iscsi_interface_statistics(self, iscsi_interface_statistics):
        """
        Sets the iscsi_interface_statistics of this IscsiStatisticalData.
        iSCSI statistical data that pertain to the iSCSI interfaces for this controller. Each sub-structure of IscsiInterfaceStatistics has data identifying the iSCSI interface(s) with which the statistics are associated. Note that the data in any of the sub-structures may be associated with multiple interfaces. See the section on the IscsiInterfaceStatistics structure.

        :param iscsi_interface_statistics: The iscsi_interface_statistics of this IscsiStatisticalData.
        :type: IscsiInterfaceStatistics
        """
        self._iscsi_interface_statistics = iscsi_interface_statistics

    @property
    def iscsi_target_statistics(self):
        """
        Gets the iscsi_target_statistics of this IscsiStatisticalData.
        iSCSI statistical data that pertain to the iSCSI targets. Each element of the array contains the statistics for one target that was collected by this controller. The counters from the two controllers, for a given target, must be added together by the client if a combined total for the target is desired.

        :return: The iscsi_target_statistics of this IscsiStatisticalData.
        :rtype: list[IscsiTargetStatistics]
        :required/optional: required
        """
        return self._iscsi_target_statistics

    @iscsi_target_statistics.setter
    def iscsi_target_statistics(self, iscsi_target_statistics):
        """
        Sets the iscsi_target_statistics of this IscsiStatisticalData.
        iSCSI statistical data that pertain to the iSCSI targets. Each element of the array contains the statistics for one target that was collected by this controller. The counters from the two controllers, for a given target, must be added together by the client if a combined total for the target is desired.

        :param iscsi_target_statistics: The iscsi_target_statistics of this IscsiStatisticalData.
        :type: list[IscsiTargetStatistics]
        """
        self._iscsi_target_statistics = iscsi_target_statistics

    @property
    def iscsi_initiator_statistics(self):
        """
        Gets the iscsi_initiator_statistics of this IscsiStatisticalData.
        iSCSI statistical data that pertain to the iSCSI initiator. Each element of the array contains the statistics for one initiator that was collected by this controller. The counters from the two controllers, for a given initiator, must be added together by the client if a combined total for the initiator is desired.

        :return: The iscsi_initiator_statistics of this IscsiStatisticalData.
        :rtype: list[IscsiInitiatorStatistics]
        :required/optional: required
        """
        return self._iscsi_initiator_statistics

    @iscsi_initiator_statistics.setter
    def iscsi_initiator_statistics(self, iscsi_initiator_statistics):
        """
        Sets the iscsi_initiator_statistics of this IscsiStatisticalData.
        iSCSI statistical data that pertain to the iSCSI initiator. Each element of the array contains the statistics for one initiator that was collected by this controller. The counters from the two controllers, for a given initiator, must be added together by the client if a combined total for the initiator is desired.

        :param iscsi_initiator_statistics: The iscsi_initiator_statistics of this IscsiStatisticalData.
        :type: list[IscsiInitiatorStatistics]
        """
        self._iscsi_initiator_statistics = iscsi_initiator_statistics

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
