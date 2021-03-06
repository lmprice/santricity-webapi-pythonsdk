# coding: utf-8

"""
AsyncMirrorGroupLinkBandwidthTestResults.py

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


class AsyncMirrorGroupLinkBandwidthTestResults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorGroupLinkBandwidthTestResults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'latency_measures': 'AsyncMirrorGroupLinkLatencyTestResults',  # (required parameter)
            'min_bandwidth_bits_per_second': 'int',  # (required parameter)
            'max_bandwidth_bits_per_second': 'int',  # (required parameter)
            'avg_bandwidth_bits_per_second': 'int',  # (required parameter)
            'negotiated_link_speed_bits_per_second': 'int'
        }

        self.attribute_map = {
            'latency_measures': 'latencyMeasures',  # (required parameter)
            'min_bandwidth_bits_per_second': 'minBandwidthBitsPerSecond',  # (required parameter)
            'max_bandwidth_bits_per_second': 'maxBandwidthBitsPerSecond',  # (required parameter)
            'avg_bandwidth_bits_per_second': 'avgBandwidthBitsPerSecond',  # (required parameter)
            'negotiated_link_speed_bits_per_second': 'negotiatedLinkSpeedBitsPerSecond'
        }

        self._latency_measures = None
        self._min_bandwidth_bits_per_second = None
        self._max_bandwidth_bits_per_second = None
        self._avg_bandwidth_bits_per_second = None
        self._negotiated_link_speed_bits_per_second = None

    @property
    def latency_measures(self):
        """
        Gets the latency_measures of this AsyncMirrorGroupLinkBandwidthTestResults.
        The bandwidth test also returns latency values since latency numbers are measured in order to factor them out of the bandwidth calculations.

        :return: The latency_measures of this AsyncMirrorGroupLinkBandwidthTestResults.
        :rtype: AsyncMirrorGroupLinkLatencyTestResults
        :required/optional: required
        """
        return self._latency_measures

    @latency_measures.setter
    def latency_measures(self, latency_measures):
        """
        Sets the latency_measures of this AsyncMirrorGroupLinkBandwidthTestResults.
        The bandwidth test also returns latency values since latency numbers are measured in order to factor them out of the bandwidth calculations.

        :param latency_measures: The latency_measures of this AsyncMirrorGroupLinkBandwidthTestResults.
        :type: AsyncMirrorGroupLinkLatencyTestResults
        """
        self._latency_measures = latency_measures

    @property
    def min_bandwidth_bits_per_second(self):
        """
        Gets the min_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        The minimum bandwidth measured in bits per second.

        :return: The min_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        :rtype: int
        :required/optional: required
        """
        return self._min_bandwidth_bits_per_second

    @min_bandwidth_bits_per_second.setter
    def min_bandwidth_bits_per_second(self, min_bandwidth_bits_per_second):
        """
        Sets the min_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        The minimum bandwidth measured in bits per second.

        :param min_bandwidth_bits_per_second: The min_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        :type: int
        """
        self._min_bandwidth_bits_per_second = min_bandwidth_bits_per_second

    @property
    def max_bandwidth_bits_per_second(self):
        """
        Gets the max_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        The maximum bandwidth measured in bits per second.

        :return: The max_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        :rtype: int
        :required/optional: required
        """
        return self._max_bandwidth_bits_per_second

    @max_bandwidth_bits_per_second.setter
    def max_bandwidth_bits_per_second(self, max_bandwidth_bits_per_second):
        """
        Sets the max_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        The maximum bandwidth measured in bits per second.

        :param max_bandwidth_bits_per_second: The max_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        :type: int
        """
        self._max_bandwidth_bits_per_second = max_bandwidth_bits_per_second

    @property
    def avg_bandwidth_bits_per_second(self):
        """
        Gets the avg_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        The average bandwidth measured in bits per second.

        :return: The avg_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        :rtype: int
        :required/optional: required
        """
        return self._avg_bandwidth_bits_per_second

    @avg_bandwidth_bits_per_second.setter
    def avg_bandwidth_bits_per_second(self, avg_bandwidth_bits_per_second):
        """
        Sets the avg_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        The average bandwidth measured in bits per second.

        :param avg_bandwidth_bits_per_second: The avg_bandwidth_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        :type: int
        """
        self._avg_bandwidth_bits_per_second = avg_bandwidth_bits_per_second

    @property
    def negotiated_link_speed_bits_per_second(self):
        """
        Gets the negotiated_link_speed_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        The negotiated link speed measured in bits per second.

        :return: The negotiated_link_speed_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        :rtype: int
        :required/optional: required
        """
        return self._negotiated_link_speed_bits_per_second

    @negotiated_link_speed_bits_per_second.setter
    def negotiated_link_speed_bits_per_second(self, negotiated_link_speed_bits_per_second):
        """
        Sets the negotiated_link_speed_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        The negotiated link speed measured in bits per second.

        :param negotiated_link_speed_bits_per_second: The negotiated_link_speed_bits_per_second of this AsyncMirrorGroupLinkBandwidthTestResults.
        :type: int
        """
        self._negotiated_link_speed_bits_per_second = negotiated_link_speed_bits_per_second

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

