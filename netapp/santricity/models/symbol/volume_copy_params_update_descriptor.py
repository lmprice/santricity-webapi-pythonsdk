# coding: utf-8

"""
VolumeCopyParamsUpdateDescriptor.py

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


class VolumeCopyParamsUpdateDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VolumeCopyParamsUpdateDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'vol_copy_ref': 'str',  # (required parameter)
            'copy_priority': 'str',  # (required parameter)
            'idle_target_write_prot': 'bool'
        }

        self.attribute_map = {
            'vol_copy_ref': 'volCopyRef',  # (required parameter)
            'copy_priority': 'copyPriority',  # (required parameter)
            'idle_target_write_prot': 'idleTargetWriteProt'
        }

        self._vol_copy_ref = None
        self._copy_priority = None
        self._idle_target_write_prot = None

    @property
    def vol_copy_ref(self):
        """
        Gets the vol_copy_ref of this VolumeCopyParamsUpdateDescriptor.
        The volume copy to be updated.

        :return: The vol_copy_ref of this VolumeCopyParamsUpdateDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._vol_copy_ref

    @vol_copy_ref.setter
    def vol_copy_ref(self, vol_copy_ref):
        """
        Sets the vol_copy_ref of this VolumeCopyParamsUpdateDescriptor.
        The volume copy to be updated.

        :param vol_copy_ref: The vol_copy_ref of this VolumeCopyParamsUpdateDescriptor.
        :type: str
        """
        self._vol_copy_ref = vol_copy_ref

    @property
    def copy_priority(self):
        """
        Gets the copy_priority of this VolumeCopyParamsUpdateDescriptor.
        Importance of copy operation.

        :return: The copy_priority of this VolumeCopyParamsUpdateDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._copy_priority

    @copy_priority.setter
    def copy_priority(self, copy_priority):
        """
        Sets the copy_priority of this VolumeCopyParamsUpdateDescriptor.
        Importance of copy operation.

        :param copy_priority: The copy_priority of this VolumeCopyParamsUpdateDescriptor.
        :type: str
        """
        allowed_values = ["priority0", "priority1", "priority2", "priority3", "priority4", "__UNDEFINED"]
        if copy_priority not in allowed_values:
            raise ValueError(
                "Invalid value for `copy_priority`, must be one of {0}"
                .format(allowed_values)
            )
        self._copy_priority = copy_priority

    @property
    def idle_target_write_prot(self):
        """
        Gets the idle_target_write_prot of this VolumeCopyParamsUpdateDescriptor.
        Apply write protection to target volume when copy is idle (true/false).

        :return: The idle_target_write_prot of this VolumeCopyParamsUpdateDescriptor.
        :rtype: bool
        :required/optional: required
        """
        return self._idle_target_write_prot

    @idle_target_write_prot.setter
    def idle_target_write_prot(self, idle_target_write_prot):
        """
        Sets the idle_target_write_prot of this VolumeCopyParamsUpdateDescriptor.
        Apply write protection to target volume when copy is idle (true/false).

        :param idle_target_write_prot: The idle_target_write_prot of this VolumeCopyParamsUpdateDescriptor.
        :type: bool
        """
        self._idle_target_write_prot = idle_target_write_prot

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
