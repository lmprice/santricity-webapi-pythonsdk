# coding: utf-8

"""
EnhancedEthernetStatistics.py

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


class EnhancedEthernetStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EnhancedEthernetStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interfaces': 'list[str]',  # (required parameter)
            'enhanced_ethernet_flow_control_status': 'str',  # (required parameter)
            'enh_eth_features_state': 'EnhEthFeaturesState',  # (required parameter)
            'local_tl_vs': 'EnhEthTLVSet',  # (required parameter)
            'operational_tl_vs': 'EnhEthTLVSet',  # (required parameter)
            'remote_tl_vs': 'EnhEthTLVSet'
        }

        self.attribute_map = {
            'interfaces': 'interfaces',  # (required parameter)
            'enhanced_ethernet_flow_control_status': 'enhancedEthernetFlowControlStatus',  # (required parameter)
            'enh_eth_features_state': 'enhEthFeaturesState',  # (required parameter)
            'local_tl_vs': 'localTLVs',  # (required parameter)
            'operational_tl_vs': 'operationalTLVs',  # (required parameter)
            'remote_tl_vs': 'remoteTLVs'
        }

        self._interfaces = None
        self._enhanced_ethernet_flow_control_status = None
        self._enh_eth_features_state = None
        self._local_tl_vs = None
        self._operational_tl_vs = None
        self._remote_tl_vs = None

    @property
    def interfaces(self):
        """
        Gets the interfaces of this EnhancedEthernetStatistics.
        This is the Interface(s) to which the Enhanced Ethernet Statistics apply. Even though this is shown as an array, it will only be a single instance.

        :return: The interfaces of this EnhancedEthernetStatistics.
        :rtype: list[str]
        :required/optional: required
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this EnhancedEthernetStatistics.
        This is the Interface(s) to which the Enhanced Ethernet Statistics apply. Even though this is shown as an array, it will only be a single instance.

        :param interfaces: The interfaces of this EnhancedEthernetStatistics.
        :type: list[str]
        """
        self._interfaces = interfaces

    @property
    def enhanced_ethernet_flow_control_status(self):
        """
        Gets the enhanced_ethernet_flow_control_status of this EnhancedEthernetStatistics.
        This is the port/interface priority-based flow control state

        :return: The enhanced_ethernet_flow_control_status of this EnhancedEthernetStatistics.
        :rtype: str
        :required/optional: required
        """
        return self._enhanced_ethernet_flow_control_status

    @enhanced_ethernet_flow_control_status.setter
    def enhanced_ethernet_flow_control_status(self, enhanced_ethernet_flow_control_status):
        """
        Sets the enhanced_ethernet_flow_control_status of this EnhancedEthernetStatistics.
        This is the port/interface priority-based flow control state

        :param enhanced_ethernet_flow_control_status: The enhanced_ethernet_flow_control_status of this EnhancedEthernetStatistics.
        :type: str
        """
        allowed_values = ["unk", "disabled", "standard", "perPriority", "__UNDEFINED"]
        if enhanced_ethernet_flow_control_status not in allowed_values:
            raise ValueError(
                "Invalid value for `enhanced_ethernet_flow_control_status`, must be one of {0}"
                .format(allowed_values)
            )
        self._enhanced_ethernet_flow_control_status = enhanced_ethernet_flow_control_status

    @property
    def enh_eth_features_state(self):
        """
        Gets the enh_eth_features_state of this EnhancedEthernetStatistics.
        This structure contains the operational state of the given DCBX features for Enhanced Ethernet.

        :return: The enh_eth_features_state of this EnhancedEthernetStatistics.
        :rtype: EnhEthFeaturesState
        :required/optional: required
        """
        return self._enh_eth_features_state

    @enh_eth_features_state.setter
    def enh_eth_features_state(self, enh_eth_features_state):
        """
        Sets the enh_eth_features_state of this EnhancedEthernetStatistics.
        This structure contains the operational state of the given DCBX features for Enhanced Ethernet.

        :param enh_eth_features_state: The enh_eth_features_state of this EnhancedEthernetStatistics.
        :type: EnhEthFeaturesState
        """
        self._enh_eth_features_state = enh_eth_features_state

    @property
    def local_tl_vs(self):
        """
        Gets the local_tl_vs of this EnhancedEthernetStatistics.
        This structure contains the TLV set for the Local Node.

        :return: The local_tl_vs of this EnhancedEthernetStatistics.
        :rtype: EnhEthTLVSet
        :required/optional: required
        """
        return self._local_tl_vs

    @local_tl_vs.setter
    def local_tl_vs(self, local_tl_vs):
        """
        Sets the local_tl_vs of this EnhancedEthernetStatistics.
        This structure contains the TLV set for the Local Node.

        :param local_tl_vs: The local_tl_vs of this EnhancedEthernetStatistics.
        :type: EnhEthTLVSet
        """
        self._local_tl_vs = local_tl_vs

    @property
    def operational_tl_vs(self):
        """
        Gets the operational_tl_vs of this EnhancedEthernetStatistics.
        This structure contains the Operational (Negotiated) TLV set.

        :return: The operational_tl_vs of this EnhancedEthernetStatistics.
        :rtype: EnhEthTLVSet
        :required/optional: required
        """
        return self._operational_tl_vs

    @operational_tl_vs.setter
    def operational_tl_vs(self, operational_tl_vs):
        """
        Sets the operational_tl_vs of this EnhancedEthernetStatistics.
        This structure contains the Operational (Negotiated) TLV set.

        :param operational_tl_vs: The operational_tl_vs of this EnhancedEthernetStatistics.
        :type: EnhEthTLVSet
        """
        self._operational_tl_vs = operational_tl_vs

    @property
    def remote_tl_vs(self):
        """
        Gets the remote_tl_vs of this EnhancedEthernetStatistics.
        This structure contains the TLVs sent from the Remote Node.

        :return: The remote_tl_vs of this EnhancedEthernetStatistics.
        :rtype: EnhEthTLVSet
        :required/optional: required
        """
        return self._remote_tl_vs

    @remote_tl_vs.setter
    def remote_tl_vs(self, remote_tl_vs):
        """
        Sets the remote_tl_vs of this EnhancedEthernetStatistics.
        This structure contains the TLVs sent from the Remote Node.

        :param remote_tl_vs: The remote_tl_vs of this EnhancedEthernetStatistics.
        :type: EnhEthTLVSet
        """
        self._remote_tl_vs = remote_tl_vs

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

