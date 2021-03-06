# coding: utf-8

"""
IbRdmaChannelStatistics.py

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


class IbRdmaChannelStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IbRdmaChannelStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'endpoints': 'IbRdmaChannelEndpoints',  # (required parameter)
            'active_messages': 'int',  # (required parameter)
            'queued_messages': 'int',  # (required parameter)
            'tx_messages': 'int',  # (required parameter)
            'rx_messages': 'int',  # (required parameter)
            'rdma_ops_started': 'int',  # (required parameter)
            'rdma_ops_completed': 'int',  # (required parameter)
            'messages_completed_with_error': 'int',  # (required parameter)
            'maximum_observed_message_size': 'int',  # (required parameter)
            'maximum_observed_queue_depth': 'int'
        }

        self.attribute_map = {
            'endpoints': 'endpoints',  # (required parameter)
            'active_messages': 'activeMessages',  # (required parameter)
            'queued_messages': 'queuedMessages',  # (required parameter)
            'tx_messages': 'txMessages',  # (required parameter)
            'rx_messages': 'rxMessages',  # (required parameter)
            'rdma_ops_started': 'rdmaOpsStarted',  # (required parameter)
            'rdma_ops_completed': 'rdmaOpsCompleted',  # (required parameter)
            'messages_completed_with_error': 'messagesCompletedWithError',  # (required parameter)
            'maximum_observed_message_size': 'maximumObservedMessageSize',  # (required parameter)
            'maximum_observed_queue_depth': 'maximumObservedQueueDepth'
        }

        self._endpoints = None
        self._active_messages = None
        self._queued_messages = None
        self._tx_messages = None
        self._rx_messages = None
        self._rdma_ops_started = None
        self._rdma_ops_completed = None
        self._messages_completed_with_error = None
        self._maximum_observed_message_size = None
        self._maximum_observed_queue_depth = None

    @property
    def endpoints(self):
        """
        Gets the endpoints of this IbRdmaChannelStatistics.
        A structure that identifies the RDMA channel by identifying its endpoints.

        :return: The endpoints of this IbRdmaChannelStatistics.
        :rtype: IbRdmaChannelEndpoints
        :required/optional: required
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this IbRdmaChannelStatistics.
        A structure that identifies the RDMA channel by identifying its endpoints.

        :param endpoints: The endpoints of this IbRdmaChannelStatistics.
        :type: IbRdmaChannelEndpoints
        """
        self._endpoints = endpoints

    @property
    def active_messages(self):
        """
        Gets the active_messages of this IbRdmaChannelStatistics.
        The number of messages in-flight on the channel.

        :return: The active_messages of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._active_messages

    @active_messages.setter
    def active_messages(self, active_messages):
        """
        Sets the active_messages of this IbRdmaChannelStatistics.
        The number of messages in-flight on the channel.

        :param active_messages: The active_messages of this IbRdmaChannelStatistics.
        :type: int
        """
        self._active_messages = active_messages

    @property
    def queued_messages(self):
        """
        Gets the queued_messages of this IbRdmaChannelStatistics.
        The number of messages queued on the channel.

        :return: The queued_messages of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._queued_messages

    @queued_messages.setter
    def queued_messages(self, queued_messages):
        """
        Sets the queued_messages of this IbRdmaChannelStatistics.
        The number of messages queued on the channel.

        :param queued_messages: The queued_messages of this IbRdmaChannelStatistics.
        :type: int
        """
        self._queued_messages = queued_messages

    @property
    def tx_messages(self):
        """
        Gets the tx_messages of this IbRdmaChannelStatistics.
        The number of messages transmitted on the channel.

        :return: The tx_messages of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_messages

    @tx_messages.setter
    def tx_messages(self, tx_messages):
        """
        Sets the tx_messages of this IbRdmaChannelStatistics.
        The number of messages transmitted on the channel.

        :param tx_messages: The tx_messages of this IbRdmaChannelStatistics.
        :type: int
        """
        self._tx_messages = tx_messages

    @property
    def rx_messages(self):
        """
        Gets the rx_messages of this IbRdmaChannelStatistics.
        The number of messages received on the channel.

        :return: The rx_messages of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_messages

    @rx_messages.setter
    def rx_messages(self, rx_messages):
        """
        Sets the rx_messages of this IbRdmaChannelStatistics.
        The number of messages received on the channel.

        :param rx_messages: The rx_messages of this IbRdmaChannelStatistics.
        :type: int
        """
        self._rx_messages = rx_messages

    @property
    def rdma_ops_started(self):
        """
        Gets the rdma_ops_started of this IbRdmaChannelStatistics.
        The number of RDMA operations started on the channel.

        :return: The rdma_ops_started of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rdma_ops_started

    @rdma_ops_started.setter
    def rdma_ops_started(self, rdma_ops_started):
        """
        Sets the rdma_ops_started of this IbRdmaChannelStatistics.
        The number of RDMA operations started on the channel.

        :param rdma_ops_started: The rdma_ops_started of this IbRdmaChannelStatistics.
        :type: int
        """
        self._rdma_ops_started = rdma_ops_started

    @property
    def rdma_ops_completed(self):
        """
        Gets the rdma_ops_completed of this IbRdmaChannelStatistics.
        The number of RDMA operations completed on the channel.

        :return: The rdma_ops_completed of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rdma_ops_completed

    @rdma_ops_completed.setter
    def rdma_ops_completed(self, rdma_ops_completed):
        """
        Sets the rdma_ops_completed of this IbRdmaChannelStatistics.
        The number of RDMA operations completed on the channel.

        :param rdma_ops_completed: The rdma_ops_completed of this IbRdmaChannelStatistics.
        :type: int
        """
        self._rdma_ops_completed = rdma_ops_completed

    @property
    def messages_completed_with_error(self):
        """
        Gets the messages_completed_with_error of this IbRdmaChannelStatistics.
        The number of RDMA completed with error on the channel.

        :return: The messages_completed_with_error of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._messages_completed_with_error

    @messages_completed_with_error.setter
    def messages_completed_with_error(self, messages_completed_with_error):
        """
        Sets the messages_completed_with_error of this IbRdmaChannelStatistics.
        The number of RDMA completed with error on the channel.

        :param messages_completed_with_error: The messages_completed_with_error of this IbRdmaChannelStatistics.
        :type: int
        """
        self._messages_completed_with_error = messages_completed_with_error

    @property
    def maximum_observed_message_size(self):
        """
        Gets the maximum_observed_message_size of this IbRdmaChannelStatistics.
        The maximum message size observed since the baseline time.

        :return: The maximum_observed_message_size of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._maximum_observed_message_size

    @maximum_observed_message_size.setter
    def maximum_observed_message_size(self, maximum_observed_message_size):
        """
        Sets the maximum_observed_message_size of this IbRdmaChannelStatistics.
        The maximum message size observed since the baseline time.

        :param maximum_observed_message_size: The maximum_observed_message_size of this IbRdmaChannelStatistics.
        :type: int
        """
        self._maximum_observed_message_size = maximum_observed_message_size

    @property
    def maximum_observed_queue_depth(self):
        """
        Gets the maximum_observed_queue_depth of this IbRdmaChannelStatistics.
        The maximum queue depth observed since the baseline time.

        :return: The maximum_observed_queue_depth of this IbRdmaChannelStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._maximum_observed_queue_depth

    @maximum_observed_queue_depth.setter
    def maximum_observed_queue_depth(self, maximum_observed_queue_depth):
        """
        Sets the maximum_observed_queue_depth of this IbRdmaChannelStatistics.
        The maximum queue depth observed since the baseline time.

        :param maximum_observed_queue_depth: The maximum_observed_queue_depth of this IbRdmaChannelStatistics.
        :type: int
        """
        self._maximum_observed_queue_depth = maximum_observed_queue_depth

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

