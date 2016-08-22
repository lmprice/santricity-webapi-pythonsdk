# coding: utf-8

"""
AsyncMirrorGroupConnectivityTestResults.py

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


class AsyncMirrorGroupConnectivityTestResults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorGroupConnectivityTestResults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'test_type': 'str',  # (required parameter)
            'link_test_results': 'AsyncMirrorGroupLinkLatencyTestResults',  
            'bandwidth_test_results': 'AsyncMirrorGroupLinkBandwidthTestResults'
        }

        self.attribute_map = {
            'test_type': 'testType',  # (required parameter)
            'link_test_results': 'linkTestResults',  
            'bandwidth_test_results': 'bandwidthTestResults'
        }

        self._test_type = None
        self._link_test_results = None
        self._bandwidth_test_results = None

    @property
    def test_type(self):
        """
        Gets the test_type of this AsyncMirrorGroupConnectivityTestResults.
        Types of AMG connectivity tests.

        :return: The test_type of this AsyncMirrorGroupConnectivityTestResults.
        :rtype: str
        :required/optional: required
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """
        Sets the test_type of this AsyncMirrorGroupConnectivityTestResults.
        Types of AMG connectivity tests.

        :param test_type: The test_type of this AsyncMirrorGroupConnectivityTestResults.
        :type: str
        """
        allowed_values = ["connectivityTestUnknown", "basicConnectivityTest", "linkLatencyTest", "linkBandwidthTest", "__UNDEFINED"]
        if test_type not in allowed_values:
            raise ValueError(
                "Invalid value for `test_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._test_type = test_type

    @property
    def link_test_results(self):
        """
        Gets the link_test_results of this AsyncMirrorGroupConnectivityTestResults.
        This field is returned if the testType is equal to ASYNC_MIRROR_GROUP_LINK_LATENCY_TEST.

        :return: The link_test_results of this AsyncMirrorGroupConnectivityTestResults.
        :rtype: AsyncMirrorGroupLinkLatencyTestResults
        :required/optional: optional
        """
        return self._link_test_results

    @link_test_results.setter
    def link_test_results(self, link_test_results):
        """
        Sets the link_test_results of this AsyncMirrorGroupConnectivityTestResults.
        This field is returned if the testType is equal to ASYNC_MIRROR_GROUP_LINK_LATENCY_TEST.

        :param link_test_results: The link_test_results of this AsyncMirrorGroupConnectivityTestResults.
        :type: AsyncMirrorGroupLinkLatencyTestResults
        """
        self._link_test_results = link_test_results

    @property
    def bandwidth_test_results(self):
        """
        Gets the bandwidth_test_results of this AsyncMirrorGroupConnectivityTestResults.
        This field is returned if the testType is equal to ASYNC_MIRROR_GROUP_LINK_BANDWIDTH_TEST.

        :return: The bandwidth_test_results of this AsyncMirrorGroupConnectivityTestResults.
        :rtype: AsyncMirrorGroupLinkBandwidthTestResults
        :required/optional: optional
        """
        return self._bandwidth_test_results

    @bandwidth_test_results.setter
    def bandwidth_test_results(self, bandwidth_test_results):
        """
        Sets the bandwidth_test_results of this AsyncMirrorGroupConnectivityTestResults.
        This field is returned if the testType is equal to ASYNC_MIRROR_GROUP_LINK_BANDWIDTH_TEST.

        :param bandwidth_test_results: The bandwidth_test_results of this AsyncMirrorGroupConnectivityTestResults.
        :type: AsyncMirrorGroupLinkBandwidthTestResults
        """
        self._bandwidth_test_results = bandwidth_test_results

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
