# coding: utf-8

"""
RemoteVolumeMirrorCreateRequest.py

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


class RemoteVolumeMirrorCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RemoteVolumeMirrorCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'src_vol_id': 'str',  # (required parameter)
            'tgt_vol_wwn': 'str',  # (required parameter)
            'remote_array_id': 'str',  # (required parameter)
            'copy_type': 'int',  # (required parameter)
            'priority': 'int',  # (required parameter)
            'auto_resync': 'bool'
        }

        self.attribute_map = {
            'src_vol_id': 'srcVolID',  # (required parameter)
            'tgt_vol_wwn': 'tgtVolWWN',  # (required parameter)
            'remote_array_id': 'remoteArrayId',  # (required parameter)
            'copy_type': 'copyType',  # (required parameter)
            'priority': 'priority',  # (required parameter)
            'auto_resync': 'autoResync'
        }

        self._src_vol_id = None
        self._tgt_vol_wwn = None
        self._remote_array_id = None
        self._copy_type = None
        self._priority = None
        self._auto_resync = None

    @property
    def src_vol_id(self):
        """
        Gets the src_vol_id of this RemoteVolumeMirrorCreateRequest.
        Remote Volume Mirror source volume ID.

        :return: The src_vol_id of this RemoteVolumeMirrorCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._src_vol_id

    @src_vol_id.setter
    def src_vol_id(self, src_vol_id):
        """
        Sets the src_vol_id of this RemoteVolumeMirrorCreateRequest.
        Remote Volume Mirror source volume ID.

        :param src_vol_id: The src_vol_id of this RemoteVolumeMirrorCreateRequest.
        :type: str
        """
        self._src_vol_id = src_vol_id

    @property
    def tgt_vol_wwn(self):
        """
        Gets the tgt_vol_wwn of this RemoteVolumeMirrorCreateRequest.


        :return: The tgt_vol_wwn of this RemoteVolumeMirrorCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._tgt_vol_wwn

    @tgt_vol_wwn.setter
    def tgt_vol_wwn(self, tgt_vol_wwn):
        """
        Sets the tgt_vol_wwn of this RemoteVolumeMirrorCreateRequest.


        :param tgt_vol_wwn: The tgt_vol_wwn of this RemoteVolumeMirrorCreateRequest.
        :type: str
        """
        self._tgt_vol_wwn = tgt_vol_wwn

    @property
    def remote_array_id(self):
        """
        Gets the remote_array_id of this RemoteVolumeMirrorCreateRequest.


        :return: The remote_array_id of this RemoteVolumeMirrorCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._remote_array_id

    @remote_array_id.setter
    def remote_array_id(self, remote_array_id):
        """
        Sets the remote_array_id of this RemoteVolumeMirrorCreateRequest.


        :param remote_array_id: The remote_array_id of this RemoteVolumeMirrorCreateRequest.
        :type: str
        """
        self._remote_array_id = remote_array_id

    @property
    def copy_type(self):
        """
        Gets the copy_type of this RemoteVolumeMirrorCreateRequest.


        :return: The copy_type of this RemoteVolumeMirrorCreateRequest.
        :rtype: int
        :required/optional: required
        """
        return self._copy_type

    @copy_type.setter
    def copy_type(self, copy_type):
        """
        Sets the copy_type of this RemoteVolumeMirrorCreateRequest.


        :param copy_type: The copy_type of this RemoteVolumeMirrorCreateRequest.
        :type: int
        """
        self._copy_type = copy_type

    @property
    def priority(self):
        """
        Gets the priority of this RemoteVolumeMirrorCreateRequest.


        :return: The priority of this RemoteVolumeMirrorCreateRequest.
        :rtype: int
        :required/optional: required
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this RemoteVolumeMirrorCreateRequest.


        :param priority: The priority of this RemoteVolumeMirrorCreateRequest.
        :type: int
        """
        self._priority = priority

    @property
    def auto_resync(self):
        """
        Gets the auto_resync of this RemoteVolumeMirrorCreateRequest.


        :return: The auto_resync of this RemoteVolumeMirrorCreateRequest.
        :rtype: bool
        :required/optional: required
        """
        return self._auto_resync

    @auto_resync.setter
    def auto_resync(self, auto_resync):
        """
        Sets the auto_resync of this RemoteVolumeMirrorCreateRequest.


        :param auto_resync: The auto_resync of this RemoteVolumeMirrorCreateRequest.
        :type: bool
        """
        self._auto_resync = auto_resync

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

