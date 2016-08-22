# coding: utf-8

"""
EnhEthFeaturesState.py

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


class EnhEthFeaturesState(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EnhEthFeaturesState - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fip_operational': 'bool',  # (required parameter)
            'fcoe_operational': 'bool',  # (required parameter)
            'pfc_operational': 'bool',  # (required parameter)
            'pg_operational': 'bool',  # (required parameter)
            'fcoe_bandwidth': 'bool',  # (required parameter)
            'iscsi_operational': 'bool',  # (required parameter)
            'fcoe_fip_mismatch': 'bool'
        }

        self.attribute_map = {
            'fip_operational': 'fipOperational',  # (required parameter)
            'fcoe_operational': 'fcoeOperational',  # (required parameter)
            'pfc_operational': 'pfcOperational',  # (required parameter)
            'pg_operational': 'pgOperational',  # (required parameter)
            'fcoe_bandwidth': 'fcoeBandwidth',  # (required parameter)
            'iscsi_operational': 'iscsiOperational',  # (required parameter)
            'fcoe_fip_mismatch': 'fcoeFipMismatch'
        }

        self._fip_operational = None
        self._fcoe_operational = None
        self._pfc_operational = None
        self._pg_operational = None
        self._fcoe_bandwidth = None
        self._iscsi_operational = None
        self._fcoe_fip_mismatch = None

    @property
    def fip_operational(self):
        """
        Gets the fip_operational of this EnhEthFeaturesState.
        This bool indicates the Operational mode of the FIP Application. .

        :return: The fip_operational of this EnhEthFeaturesState.
        :rtype: bool
        :required/optional: required
        """
        return self._fip_operational

    @fip_operational.setter
    def fip_operational(self, fip_operational):
        """
        Sets the fip_operational of this EnhEthFeaturesState.
        This bool indicates the Operational mode of the FIP Application. .

        :param fip_operational: The fip_operational of this EnhEthFeaturesState.
        :type: bool
        """
        self._fip_operational = fip_operational

    @property
    def fcoe_operational(self):
        """
        Gets the fcoe_operational of this EnhEthFeaturesState.
        This bool indicates the Operational mode of the FCoE Application.

        :return: The fcoe_operational of this EnhEthFeaturesState.
        :rtype: bool
        :required/optional: required
        """
        return self._fcoe_operational

    @fcoe_operational.setter
    def fcoe_operational(self, fcoe_operational):
        """
        Sets the fcoe_operational of this EnhEthFeaturesState.
        This bool indicates the Operational mode of the FCoE Application.

        :param fcoe_operational: The fcoe_operational of this EnhEthFeaturesState.
        :type: bool
        """
        self._fcoe_operational = fcoe_operational

    @property
    def pfc_operational(self):
        """
        Gets the pfc_operational of this EnhEthFeaturesState.
        This bool indicates the Operational mode of the PFC Feature.

        :return: The pfc_operational of this EnhEthFeaturesState.
        :rtype: bool
        :required/optional: required
        """
        return self._pfc_operational

    @pfc_operational.setter
    def pfc_operational(self, pfc_operational):
        """
        Sets the pfc_operational of this EnhEthFeaturesState.
        This bool indicates the Operational mode of the PFC Feature.

        :param pfc_operational: The pfc_operational of this EnhEthFeaturesState.
        :type: bool
        """
        self._pfc_operational = pfc_operational

    @property
    def pg_operational(self):
        """
        Gets the pg_operational of this EnhEthFeaturesState.
        The bool indicates the Operational mode of the PG Feature.

        :return: The pg_operational of this EnhEthFeaturesState.
        :rtype: bool
        :required/optional: required
        """
        return self._pg_operational

    @pg_operational.setter
    def pg_operational(self, pg_operational):
        """
        Sets the pg_operational of this EnhEthFeaturesState.
        The bool indicates the Operational mode of the PG Feature.

        :param pg_operational: The pg_operational of this EnhEthFeaturesState.
        :type: bool
        """
        self._pg_operational = pg_operational

    @property
    def fcoe_bandwidth(self):
        """
        Gets the fcoe_bandwidth of this EnhEthFeaturesState.
        This bool indicates if this interface has the FCoE bandwidth.

        :return: The fcoe_bandwidth of this EnhEthFeaturesState.
        :rtype: bool
        :required/optional: required
        """
        return self._fcoe_bandwidth

    @fcoe_bandwidth.setter
    def fcoe_bandwidth(self, fcoe_bandwidth):
        """
        Sets the fcoe_bandwidth of this EnhEthFeaturesState.
        This bool indicates if this interface has the FCoE bandwidth.

        :param fcoe_bandwidth: The fcoe_bandwidth of this EnhEthFeaturesState.
        :type: bool
        """
        self._fcoe_bandwidth = fcoe_bandwidth

    @property
    def iscsi_operational(self):
        """
        Gets the iscsi_operational of this EnhEthFeaturesState.
        This bool indicates the Operational Mode of the iSCSI Application.

        :return: The iscsi_operational of this EnhEthFeaturesState.
        :rtype: bool
        :required/optional: required
        """
        return self._iscsi_operational

    @iscsi_operational.setter
    def iscsi_operational(self, iscsi_operational):
        """
        Sets the iscsi_operational of this EnhEthFeaturesState.
        This bool indicates the Operational Mode of the iSCSI Application.

        :param iscsi_operational: The iscsi_operational of this EnhEthFeaturesState.
        :type: bool
        """
        self._iscsi_operational = iscsi_operational

    @property
    def fcoe_fip_mismatch(self):
        """
        Gets the fcoe_fip_mismatch of this EnhEthFeaturesState.
        This bool indicates if this interface has a FCoE/FIP Application Map Mismatch.

        :return: The fcoe_fip_mismatch of this EnhEthFeaturesState.
        :rtype: bool
        :required/optional: required
        """
        return self._fcoe_fip_mismatch

    @fcoe_fip_mismatch.setter
    def fcoe_fip_mismatch(self, fcoe_fip_mismatch):
        """
        Sets the fcoe_fip_mismatch of this EnhEthFeaturesState.
        This bool indicates if this interface has a FCoE/FIP Application Map Mismatch.

        :param fcoe_fip_mismatch: The fcoe_fip_mismatch of this EnhEthFeaturesState.
        :type: bool
        """
        self._fcoe_fip_mismatch = fcoe_fip_mismatch

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
