# coding: utf-8

"""
AmgIncompleteMember.py

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


class AmgIncompleteMember(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AmgIncompleteMember - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'member_ref': 'str',  # (required parameter)
            'group_ref': 'str',  # (required parameter)
            'primary_vol_wwn': 'str',  # (required parameter)
            'primary_vol_capacity': 'int',  # (required parameter)
            'primary_vol_raid_level': 'str',  # (required parameter)
            'primary_vol_protection_type': 'str',  # (required parameter)
            'primary_vol_security_type': 'str',  # (required parameter)
            'primary_vol_user_label': 'str',  # (required parameter)
            'orphan_incomplete_member': 'bool',  # (required parameter)
            'primary_volume_parameters': 'VolumeTypeParameters',  # (required parameter)
            'primary_vol_security_level': 'str',  # (required parameter)
            'remote_target_wwn': 'str',  
            'remote_target_name': 'str',  
            'remote_target_id': 'str',  
            'id': 'str'
        }

        self.attribute_map = {
            'member_ref': 'memberRef',  # (required parameter)
            'group_ref': 'groupRef',  # (required parameter)
            'primary_vol_wwn': 'primaryVolWWN',  # (required parameter)
            'primary_vol_capacity': 'primaryVolCapacity',  # (required parameter)
            'primary_vol_raid_level': 'primaryVolRAIDLevel',  # (required parameter)
            'primary_vol_protection_type': 'primaryVolProtectionType',  # (required parameter)
            'primary_vol_security_type': 'primaryVolSecurityType',  # (required parameter)
            'primary_vol_user_label': 'primaryVolUserLabel',  # (required parameter)
            'orphan_incomplete_member': 'orphanIncompleteMember',  # (required parameter)
            'primary_volume_parameters': 'primaryVolumeParameters',  # (required parameter)
            'primary_vol_security_level': 'primaryVolSecurityLevel',  # (required parameter)
            'remote_target_wwn': 'remoteTargetWwn',  
            'remote_target_name': 'remoteTargetName',  
            'remote_target_id': 'remoteTargetId',  
            'id': 'id'
        }

        self._member_ref = None
        self._group_ref = None
        self._primary_vol_wwn = None
        self._primary_vol_capacity = None
        self._primary_vol_raid_level = None
        self._primary_vol_protection_type = None
        self._primary_vol_security_type = None
        self._primary_vol_user_label = None
        self._orphan_incomplete_member = None
        self._primary_volume_parameters = None
        self._primary_vol_security_level = None
        self._remote_target_wwn = None
        self._remote_target_name = None
        self._remote_target_id = None
        self._id = None

    @property
    def member_ref(self):
        """
        Gets the member_ref of this AmgIncompleteMember.
        The reference (key) for the group member.

        :return: The member_ref of this AmgIncompleteMember.
        :rtype: str
        :required/optional: required
        """
        return self._member_ref

    @member_ref.setter
    def member_ref(self, member_ref):
        """
        Sets the member_ref of this AmgIncompleteMember.
        The reference (key) for the group member.

        :param member_ref: The member_ref of this AmgIncompleteMember.
        :type: str
        """
        self._member_ref = member_ref

    @property
    def group_ref(self):
        """
        Gets the group_ref of this AmgIncompleteMember.
        The associated Async Mirror Group.

        :return: The group_ref of this AmgIncompleteMember.
        :rtype: str
        :required/optional: required
        """
        return self._group_ref

    @group_ref.setter
    def group_ref(self, group_ref):
        """
        Sets the group_ref of this AmgIncompleteMember.
        The associated Async Mirror Group.

        :param group_ref: The group_ref of this AmgIncompleteMember.
        :type: str
        """
        self._group_ref = group_ref

    @property
    def primary_vol_wwn(self):
        """
        Gets the primary_vol_wwn of this AmgIncompleteMember.
        The WWN of the primary volume on the remote array.

        :return: The primary_vol_wwn of this AmgIncompleteMember.
        :rtype: str
        :required/optional: required
        """
        return self._primary_vol_wwn

    @primary_vol_wwn.setter
    def primary_vol_wwn(self, primary_vol_wwn):
        """
        Sets the primary_vol_wwn of this AmgIncompleteMember.
        The WWN of the primary volume on the remote array.

        :param primary_vol_wwn: The primary_vol_wwn of this AmgIncompleteMember.
        :type: str
        """
        self._primary_vol_wwn = primary_vol_wwn

    @property
    def primary_vol_capacity(self):
        """
        Gets the primary_vol_capacity of this AmgIncompleteMember.
        Capacity of the primary (used to aid in selection of mirror secondary volume).

        :return: The primary_vol_capacity of this AmgIncompleteMember.
        :rtype: int
        :required/optional: required
        """
        return self._primary_vol_capacity

    @primary_vol_capacity.setter
    def primary_vol_capacity(self, primary_vol_capacity):
        """
        Sets the primary_vol_capacity of this AmgIncompleteMember.
        Capacity of the primary (used to aid in selection of mirror secondary volume).

        :param primary_vol_capacity: The primary_vol_capacity of this AmgIncompleteMember.
        :type: int
        """
        self._primary_vol_capacity = primary_vol_capacity

    @property
    def primary_vol_raid_level(self):
        """
        Gets the primary_vol_raid_level of this AmgIncompleteMember.
        RAID level of the primary volume.

        :return: The primary_vol_raid_level of this AmgIncompleteMember.
        :rtype: str
        :required/optional: required
        """
        return self._primary_vol_raid_level

    @primary_vol_raid_level.setter
    def primary_vol_raid_level(self, primary_vol_raid_level):
        """
        Sets the primary_vol_raid_level of this AmgIncompleteMember.
        RAID level of the primary volume.

        :param primary_vol_raid_level: The primary_vol_raid_level of this AmgIncompleteMember.
        :type: str
        """
        allowed_values = ["raidUnsupported", "raidAll", "raid0", "raid1", "raid3", "raid5", "raid6", "raidDiskPool", "__UNDEFINED"]
        if primary_vol_raid_level not in allowed_values:
            raise ValueError(
                "Invalid value for `primary_vol_raid_level`, must be one of {0}"
                .format(allowed_values)
            )
        self._primary_vol_raid_level = primary_vol_raid_level

    @property
    def primary_vol_protection_type(self):
        """
        Gets the primary_vol_protection_type of this AmgIncompleteMember.
        The protection type of the primary volume.

        :return: The primary_vol_protection_type of this AmgIncompleteMember.
        :rtype: str
        :required/optional: required
        """
        return self._primary_vol_protection_type

    @primary_vol_protection_type.setter
    def primary_vol_protection_type(self, primary_vol_protection_type):
        """
        Sets the primary_vol_protection_type of this AmgIncompleteMember.
        The protection type of the primary volume.

        :param primary_vol_protection_type: The primary_vol_protection_type of this AmgIncompleteMember.
        :type: str
        """
        allowed_values = ["type0Protection", "type1Protection", "type2Protection", "type3Protection", "__UNDEFINED"]
        if primary_vol_protection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `primary_vol_protection_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._primary_vol_protection_type = primary_vol_protection_type

    @property
    def primary_vol_security_type(self):
        """
        Gets the primary_vol_security_type of this AmgIncompleteMember.
        Security type of the primary volume.

        :return: The primary_vol_security_type of this AmgIncompleteMember.
        :rtype: str
        :required/optional: required
        """
        return self._primary_vol_security_type

    @primary_vol_security_type.setter
    def primary_vol_security_type(self, primary_vol_security_type):
        """
        Sets the primary_vol_security_type of this AmgIncompleteMember.
        Security type of the primary volume.

        :param primary_vol_security_type: The primary_vol_security_type of this AmgIncompleteMember.
        :type: str
        """
        allowed_values = ["unknown", "none", "capable", "enabled", "__UNDEFINED"]
        if primary_vol_security_type not in allowed_values:
            raise ValueError(
                "Invalid value for `primary_vol_security_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._primary_vol_security_type = primary_vol_security_type

    @property
    def primary_vol_user_label(self):
        """
        Gets the primary_vol_user_label of this AmgIncompleteMember.
        User label of the primary volume.

        :return: The primary_vol_user_label of this AmgIncompleteMember.
        :rtype: str
        :required/optional: required
        """
        return self._primary_vol_user_label

    @primary_vol_user_label.setter
    def primary_vol_user_label(self, primary_vol_user_label):
        """
        Sets the primary_vol_user_label of this AmgIncompleteMember.
        User label of the primary volume.

        :param primary_vol_user_label: The primary_vol_user_label of this AmgIncompleteMember.
        :type: str
        """
        self._primary_vol_user_label = primary_vol_user_label

    @property
    def orphan_incomplete_member(self):
        """
        Gets the orphan_incomplete_member of this AmgIncompleteMember.
        If true, the incomplete member is an orphan.

        :return: The orphan_incomplete_member of this AmgIncompleteMember.
        :rtype: bool
        :required/optional: required
        """
        return self._orphan_incomplete_member

    @orphan_incomplete_member.setter
    def orphan_incomplete_member(self, orphan_incomplete_member):
        """
        Sets the orphan_incomplete_member of this AmgIncompleteMember.
        If true, the incomplete member is an orphan.

        :param orphan_incomplete_member: The orphan_incomplete_member of this AmgIncompleteMember.
        :type: bool
        """
        self._orphan_incomplete_member = orphan_incomplete_member

    @property
    def primary_volume_parameters(self):
        """
        Gets the primary_volume_parameters of this AmgIncompleteMember.
        The capacity provisioning parameters for the primary volume.

        :return: The primary_volume_parameters of this AmgIncompleteMember.
        :rtype: VolumeTypeParameters
        :required/optional: required
        """
        return self._primary_volume_parameters

    @primary_volume_parameters.setter
    def primary_volume_parameters(self, primary_volume_parameters):
        """
        Sets the primary_volume_parameters of this AmgIncompleteMember.
        The capacity provisioning parameters for the primary volume.

        :param primary_volume_parameters: The primary_volume_parameters of this AmgIncompleteMember.
        :type: VolumeTypeParameters
        """
        self._primary_volume_parameters = primary_volume_parameters

    @property
    def primary_vol_security_level(self):
        """
        Gets the primary_vol_security_level of this AmgIncompleteMember.
        Refines the information in the securityType field to describe the set of drives.

        :return: The primary_vol_security_level of this AmgIncompleteMember.
        :rtype: str
        :required/optional: required
        """
        return self._primary_vol_security_level

    @primary_vol_security_level.setter
    def primary_vol_security_level(self, primary_vol_security_level):
        """
        Sets the primary_vol_security_level of this AmgIncompleteMember.
        Refines the information in the securityType field to describe the set of drives.

        :param primary_vol_security_level: The primary_vol_security_level of this AmgIncompleteMember.
        :type: str
        """
        allowed_values = ["unknown", "none", "mixed", "fde", "fips", "__UNDEFINED"]
        if primary_vol_security_level not in allowed_values:
            raise ValueError(
                "Invalid value for `primary_vol_security_level`, must be one of {0}"
                .format(allowed_values)
            )
        self._primary_vol_security_level = primary_vol_security_level

    @property
    def remote_target_wwn(self):
        """
        Gets the remote_target_wwn of this AmgIncompleteMember.
        The WWN of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created.

        :return: The remote_target_wwn of this AmgIncompleteMember.
        :rtype: str
        :required/optional: optional
        """
        return self._remote_target_wwn

    @remote_target_wwn.setter
    def remote_target_wwn(self, remote_target_wwn):
        """
        Sets the remote_target_wwn of this AmgIncompleteMember.
        The WWN of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created.

        :param remote_target_wwn: The remote_target_wwn of this AmgIncompleteMember.
        :type: str
        """
        self._remote_target_wwn = remote_target_wwn

    @property
    def remote_target_name(self):
        """
        Gets the remote_target_name of this AmgIncompleteMember.
        The user label of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created, and will not be available in embedded mode.

        :return: The remote_target_name of this AmgIncompleteMember.
        :rtype: str
        :required/optional: optional
        """
        return self._remote_target_name

    @remote_target_name.setter
    def remote_target_name(self, remote_target_name):
        """
        Sets the remote_target_name of this AmgIncompleteMember.
        The user label of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created, and will not be available in embedded mode.

        :param remote_target_name: The remote_target_name of this AmgIncompleteMember.
        :type: str
        """
        self._remote_target_name = remote_target_name

    @property
    def remote_target_id(self):
        """
        Gets the remote_target_id of this AmgIncompleteMember.
        The id of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created, and will not be available in embedded mode.

        :return: The remote_target_id of this AmgIncompleteMember.
        :rtype: str
        :required/optional: optional
        """
        return self._remote_target_id

    @remote_target_id.setter
    def remote_target_id(self, remote_target_id):
        """
        Sets the remote_target_id of this AmgIncompleteMember.
        The id of the target array in the mirroring relationship. This field may not be immediately available after an AMG is created, and will not be available in embedded mode.

        :param remote_target_id: The remote_target_id of this AmgIncompleteMember.
        :type: str
        """
        self._remote_target_id = remote_target_id

    @property
    def id(self):
        """
        Gets the id of this AmgIncompleteMember.


        :return: The id of this AmgIncompleteMember.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AmgIncompleteMember.


        :param id: The id of this AmgIncompleteMember.
        :type: str
        """
        self._id = id

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

