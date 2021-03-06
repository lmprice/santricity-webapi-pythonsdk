# coding: utf-8

"""
MetadataVolCreationDescriptor.py

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


class MetadataVolCreationDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MetadataVolCreationDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metadata_vol_type': 'str',  # (required parameter)
            'ctl0_label': 'str',  # (required parameter)
            'ctl1_label': 'str',  # (required parameter)
            'candidate': 'VolumeCandidate',  # (required parameter)
            'volume_group_label': 'str',  # (required parameter)
            'protection_type': 'str'
        }

        self.attribute_map = {
            'metadata_vol_type': 'metadataVolType',  # (required parameter)
            'ctl0_label': 'ctl0Label',  # (required parameter)
            'ctl1_label': 'ctl1Label',  # (required parameter)
            'candidate': 'candidate',  # (required parameter)
            'volume_group_label': 'volumeGroupLabel',  # (required parameter)
            'protection_type': 'protectionType'
        }

        self._metadata_vol_type = None
        self._ctl0_label = None
        self._ctl1_label = None
        self._candidate = None
        self._volume_group_label = None
        self._protection_type = None

    @property
    def metadata_vol_type(self):
        """
        Gets the metadata_vol_type of this MetadataVolCreationDescriptor.
        The metadata volume type to create.

        :return: The metadata_vol_type of this MetadataVolCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._metadata_vol_type

    @metadata_vol_type.setter
    def metadata_vol_type(self, metadata_vol_type):
        """
        Sets the metadata_vol_type of this MetadataVolCreationDescriptor.
        The metadata volume type to create.

        :param metadata_vol_type: The metadata_vol_type of this MetadataVolCreationDescriptor.
        :type: str
        """
        allowed_values = ["allMdatTypes", "remoteMirror", "__UNDEFINED"]
        if metadata_vol_type not in allowed_values:
            raise ValueError(
                "Invalid value for `metadata_vol_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._metadata_vol_type = metadata_vol_type

    @property
    def ctl0_label(self):
        """
        Gets the ctl0_label of this MetadataVolCreationDescriptor.
        The user assigned label, as assigned by the firmware, for controller 0 volume.

        :return: The ctl0_label of this MetadataVolCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._ctl0_label

    @ctl0_label.setter
    def ctl0_label(self, ctl0_label):
        """
        Sets the ctl0_label of this MetadataVolCreationDescriptor.
        The user assigned label, as assigned by the firmware, for controller 0 volume.

        :param ctl0_label: The ctl0_label of this MetadataVolCreationDescriptor.
        :type: str
        """
        self._ctl0_label = ctl0_label

    @property
    def ctl1_label(self):
        """
        Gets the ctl1_label of this MetadataVolCreationDescriptor.
        The user assigned label, as assigned by the firmware, for controller 1 volume.

        :return: The ctl1_label of this MetadataVolCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._ctl1_label

    @ctl1_label.setter
    def ctl1_label(self, ctl1_label):
        """
        Sets the ctl1_label of this MetadataVolCreationDescriptor.
        The user assigned label, as assigned by the firmware, for controller 1 volume.

        :param ctl1_label: The ctl1_label of this MetadataVolCreationDescriptor.
        :type: str
        """
        self._ctl1_label = ctl1_label

    @property
    def candidate(self):
        """
        Gets the candidate of this MetadataVolCreationDescriptor.
        The volume candidate for the repository.

        :return: The candidate of this MetadataVolCreationDescriptor.
        :rtype: VolumeCandidate
        :required/optional: required
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """
        Sets the candidate of this MetadataVolCreationDescriptor.
        The volume candidate for the repository.

        :param candidate: The candidate of this MetadataVolCreationDescriptor.
        :type: VolumeCandidate
        """
        self._candidate = candidate

    @property
    def volume_group_label(self):
        """
        Gets the volume_group_label of this MetadataVolCreationDescriptor.
        The label to assign to the new volume group for the repository, if any. This field is only used when the repository candidate selection type is CANDIDATE_SEL_MANUAL or CANDIDATE_SEL_COUNT.

        :return: The volume_group_label of this MetadataVolCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._volume_group_label

    @volume_group_label.setter
    def volume_group_label(self, volume_group_label):
        """
        Sets the volume_group_label of this MetadataVolCreationDescriptor.
        The label to assign to the new volume group for the repository, if any. This field is only used when the repository candidate selection type is CANDIDATE_SEL_MANUAL or CANDIDATE_SEL_COUNT.

        :param volume_group_label: The volume_group_label of this MetadataVolCreationDescriptor.
        :type: str
        """
        self._volume_group_label = volume_group_label

    @property
    def protection_type(self):
        """
        Gets the protection_type of this MetadataVolCreationDescriptor.
        The protection type that should be used for the metadata volume being created

        :return: The protection_type of this MetadataVolCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """
        Sets the protection_type of this MetadataVolCreationDescriptor.
        The protection type that should be used for the metadata volume being created

        :param protection_type: The protection_type of this MetadataVolCreationDescriptor.
        :type: str
        """
        allowed_values = ["type0Protection", "type1Protection", "type2Protection", "type3Protection", "__UNDEFINED"]
        if protection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `protection_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._protection_type = protection_type

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

