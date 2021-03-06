# coding: utf-8

"""
DriveCounterGroup.py

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


class DriveCounterGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DriveCounterGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'controller_ref': 'str',  # (required parameter)
            'base_time': 'int',  # (required parameter)
            'read_ops': 'int',  # (required parameter)
            'read_bytes': 'int',  # (required parameter)
            'read_time_total': 'int',  # (required parameter)
            'read_time_max': 'int',  # (required parameter)
            'write_ops': 'int',  # (required parameter)
            'write_bytes': 'int',  # (required parameter)
            'write_time_total': 'int',  # (required parameter)
            'write_time_max': 'int',  # (required parameter)
            'other_ops': 'int',  # (required parameter)
            'other_time_total': 'int',  # (required parameter)
            'other_time_max': 'int',  # (required parameter)
            'idle_time': 'int',  # (required parameter)
            'recovered_errors': 'int',  # (required parameter)
            'unrecovered_errors': 'int',  # (required parameter)
            'timeouts': 'int',  # (required parameter)
            'retried_ios': 'int',  # (required parameter)
            'read_time_total_sq': 'int',  # (required parameter)
            'write_time_total_sq': 'int',  # (required parameter)
            'other_time_total_sq': 'int',  # (required parameter)
            'start_time': 'int',  # (required parameter)
            'observed_time': 'int',  # (required parameter)
            'queue_depth_total': 'int',  # (required parameter)
            'queue_depth_max': 'int',  # (required parameter)
            'random_ios_total': 'int',  # (required parameter)
            'random_bytes_total': 'int',  # (required parameter)
            'cumulative_lba': 'int',  # (required parameter)
            'cumulative_delta_lba': 'int'
        }

        self.attribute_map = {
            'controller_ref': 'controllerRef',  # (required parameter)
            'base_time': 'baseTime',  # (required parameter)
            'read_ops': 'readOps',  # (required parameter)
            'read_bytes': 'readBytes',  # (required parameter)
            'read_time_total': 'readTimeTotal',  # (required parameter)
            'read_time_max': 'readTimeMax',  # (required parameter)
            'write_ops': 'writeOps',  # (required parameter)
            'write_bytes': 'writeBytes',  # (required parameter)
            'write_time_total': 'writeTimeTotal',  # (required parameter)
            'write_time_max': 'writeTimeMax',  # (required parameter)
            'other_ops': 'otherOps',  # (required parameter)
            'other_time_total': 'otherTimeTotal',  # (required parameter)
            'other_time_max': 'otherTimeMax',  # (required parameter)
            'idle_time': 'idleTime',  # (required parameter)
            'recovered_errors': 'recoveredErrors',  # (required parameter)
            'unrecovered_errors': 'unrecoveredErrors',  # (required parameter)
            'timeouts': 'timeouts',  # (required parameter)
            'retried_ios': 'retriedIos',  # (required parameter)
            'read_time_total_sq': 'readTimeTotalSq',  # (required parameter)
            'write_time_total_sq': 'writeTimeTotalSq',  # (required parameter)
            'other_time_total_sq': 'otherTimeTotalSq',  # (required parameter)
            'start_time': 'startTime',  # (required parameter)
            'observed_time': 'observedTime',  # (required parameter)
            'queue_depth_total': 'queueDepthTotal',  # (required parameter)
            'queue_depth_max': 'queueDepthMax',  # (required parameter)
            'random_ios_total': 'randomIosTotal',  # (required parameter)
            'random_bytes_total': 'randomBytesTotal',  # (required parameter)
            'cumulative_lba': 'cumulativeLBA',  # (required parameter)
            'cumulative_delta_lba': 'cumulativeDeltaLBA'
        }

        self._controller_ref = None
        self._base_time = None
        self._read_ops = None
        self._read_bytes = None
        self._read_time_total = None
        self._read_time_max = None
        self._write_ops = None
        self._write_bytes = None
        self._write_time_total = None
        self._write_time_max = None
        self._other_ops = None
        self._other_time_total = None
        self._other_time_max = None
        self._idle_time = None
        self._recovered_errors = None
        self._unrecovered_errors = None
        self._timeouts = None
        self._retried_ios = None
        self._read_time_total_sq = None
        self._write_time_total_sq = None
        self._other_time_total_sq = None
        self._start_time = None
        self._observed_time = None
        self._queue_depth_total = None
        self._queue_depth_max = None
        self._random_ios_total = None
        self._random_bytes_total = None
        self._cumulative_lba = None
        self._cumulative_delta_lba = None

    @property
    def controller_ref(self):
        """
        Gets the controller_ref of this DriveCounterGroup.
        A reference to the controller that accumulated the counters for this group.

        :return: The controller_ref of this DriveCounterGroup.
        :rtype: str
        :required/optional: required
        """
        return self._controller_ref

    @controller_ref.setter
    def controller_ref(self, controller_ref):
        """
        Sets the controller_ref of this DriveCounterGroup.
        A reference to the controller that accumulated the counters for this group.

        :param controller_ref: The controller_ref of this DriveCounterGroup.
        :type: str
        """
        self._controller_ref = controller_ref

    @property
    def base_time(self):
        """
        Gets the base_time of this DriveCounterGroup.
        The time that the counters were last reset. Time is the number of seconds since midnight, January 1, 1970.

        :return: The base_time of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._base_time

    @base_time.setter
    def base_time(self, base_time):
        """
        Sets the base_time of this DriveCounterGroup.
        The time that the counters were last reset. Time is the number of seconds since midnight, January 1, 1970.

        :param base_time: The base_time of this DriveCounterGroup.
        :type: int
        """
        self._base_time = base_time

    @property
    def read_ops(self):
        """
        Gets the read_ops of this DriveCounterGroup.
        The number of read operations.

        :return: The read_ops of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._read_ops

    @read_ops.setter
    def read_ops(self, read_ops):
        """
        Sets the read_ops of this DriveCounterGroup.
        The number of read operations.

        :param read_ops: The read_ops of this DriveCounterGroup.
        :type: int
        """
        self._read_ops = read_ops

    @property
    def read_bytes(self):
        """
        Gets the read_bytes of this DriveCounterGroup.
        The number of bytes read.

        :return: The read_bytes of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._read_bytes

    @read_bytes.setter
    def read_bytes(self, read_bytes):
        """
        Sets the read_bytes of this DriveCounterGroup.
        The number of bytes read.

        :param read_bytes: The read_bytes of this DriveCounterGroup.
        :type: int
        """
        self._read_bytes = read_bytes

    @property
    def read_time_total(self):
        """
        Gets the read_time_total of this DriveCounterGroup.
        The total time in microseconds spent in read operations.

        :return: The read_time_total of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._read_time_total

    @read_time_total.setter
    def read_time_total(self, read_time_total):
        """
        Sets the read_time_total of this DriveCounterGroup.
        The total time in microseconds spent in read operations.

        :param read_time_total: The read_time_total of this DriveCounterGroup.
        :type: int
        """
        self._read_time_total = read_time_total

    @property
    def read_time_max(self):
        """
        Gets the read_time_max of this DriveCounterGroup.
        The maximum time in microseconds spent in any one read operation.

        :return: The read_time_max of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._read_time_max

    @read_time_max.setter
    def read_time_max(self, read_time_max):
        """
        Sets the read_time_max of this DriveCounterGroup.
        The maximum time in microseconds spent in any one read operation.

        :param read_time_max: The read_time_max of this DriveCounterGroup.
        :type: int
        """
        self._read_time_max = read_time_max

    @property
    def write_ops(self):
        """
        Gets the write_ops of this DriveCounterGroup.
        The number of write operations.

        :return: The write_ops of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._write_ops

    @write_ops.setter
    def write_ops(self, write_ops):
        """
        Sets the write_ops of this DriveCounterGroup.
        The number of write operations.

        :param write_ops: The write_ops of this DriveCounterGroup.
        :type: int
        """
        self._write_ops = write_ops

    @property
    def write_bytes(self):
        """
        Gets the write_bytes of this DriveCounterGroup.
        The number of bytes written.

        :return: The write_bytes of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._write_bytes

    @write_bytes.setter
    def write_bytes(self, write_bytes):
        """
        Sets the write_bytes of this DriveCounterGroup.
        The number of bytes written.

        :param write_bytes: The write_bytes of this DriveCounterGroup.
        :type: int
        """
        self._write_bytes = write_bytes

    @property
    def write_time_total(self):
        """
        Gets the write_time_total of this DriveCounterGroup.
        The total time in microseconds spent in write operations.

        :return: The write_time_total of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._write_time_total

    @write_time_total.setter
    def write_time_total(self, write_time_total):
        """
        Sets the write_time_total of this DriveCounterGroup.
        The total time in microseconds spent in write operations.

        :param write_time_total: The write_time_total of this DriveCounterGroup.
        :type: int
        """
        self._write_time_total = write_time_total

    @property
    def write_time_max(self):
        """
        Gets the write_time_max of this DriveCounterGroup.
        The maximum time in microseconds spent in any one write operation.

        :return: The write_time_max of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._write_time_max

    @write_time_max.setter
    def write_time_max(self, write_time_max):
        """
        Sets the write_time_max of this DriveCounterGroup.
        The maximum time in microseconds spent in any one write operation.

        :param write_time_max: The write_time_max of this DriveCounterGroup.
        :type: int
        """
        self._write_time_max = write_time_max

    @property
    def other_ops(self):
        """
        Gets the other_ops of this DriveCounterGroup.
        The number of non-read-write operations.

        :return: The other_ops of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._other_ops

    @other_ops.setter
    def other_ops(self, other_ops):
        """
        Sets the other_ops of this DriveCounterGroup.
        The number of non-read-write operations.

        :param other_ops: The other_ops of this DriveCounterGroup.
        :type: int
        """
        self._other_ops = other_ops

    @property
    def other_time_total(self):
        """
        Gets the other_time_total of this DriveCounterGroup.
        The total time in microseconds spent in non-read-write operations.

        :return: The other_time_total of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._other_time_total

    @other_time_total.setter
    def other_time_total(self, other_time_total):
        """
        Sets the other_time_total of this DriveCounterGroup.
        The total time in microseconds spent in non-read-write operations.

        :param other_time_total: The other_time_total of this DriveCounterGroup.
        :type: int
        """
        self._other_time_total = other_time_total

    @property
    def other_time_max(self):
        """
        Gets the other_time_max of this DriveCounterGroup.
        The maximum time in microseconds spent in any one non-read-write operation.

        :return: The other_time_max of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._other_time_max

    @other_time_max.setter
    def other_time_max(self, other_time_max):
        """
        Sets the other_time_max of this DriveCounterGroup.
        The maximum time in microseconds spent in any one non-read-write operation.

        :param other_time_max: The other_time_max of this DriveCounterGroup.
        :type: int
        """
        self._other_time_max = other_time_max

    @property
    def idle_time(self):
        """
        Gets the idle_time of this DriveCounterGroup.
        The total time in microseconds spent idle since baseTime.

        :return: The idle_time of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._idle_time

    @idle_time.setter
    def idle_time(self, idle_time):
        """
        Sets the idle_time of this DriveCounterGroup.
        The total time in microseconds spent idle since baseTime.

        :param idle_time: The idle_time of this DriveCounterGroup.
        :type: int
        """
        self._idle_time = idle_time

    @property
    def recovered_errors(self):
        """
        Gets the recovered_errors of this DriveCounterGroup.
        The number of recovered errors.

        :return: The recovered_errors of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._recovered_errors

    @recovered_errors.setter
    def recovered_errors(self, recovered_errors):
        """
        Sets the recovered_errors of this DriveCounterGroup.
        The number of recovered errors.

        :param recovered_errors: The recovered_errors of this DriveCounterGroup.
        :type: int
        """
        self._recovered_errors = recovered_errors

    @property
    def unrecovered_errors(self):
        """
        Gets the unrecovered_errors of this DriveCounterGroup.
        The number of unrecovered errors.

        :return: The unrecovered_errors of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._unrecovered_errors

    @unrecovered_errors.setter
    def unrecovered_errors(self, unrecovered_errors):
        """
        Sets the unrecovered_errors of this DriveCounterGroup.
        The number of unrecovered errors.

        :param unrecovered_errors: The unrecovered_errors of this DriveCounterGroup.
        :type: int
        """
        self._unrecovered_errors = unrecovered_errors

    @property
    def timeouts(self):
        """
        Gets the timeouts of this DriveCounterGroup.
        The number of timeouts.

        :return: The timeouts of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._timeouts

    @timeouts.setter
    def timeouts(self, timeouts):
        """
        Sets the timeouts of this DriveCounterGroup.
        The number of timeouts.

        :param timeouts: The timeouts of this DriveCounterGroup.
        :type: int
        """
        self._timeouts = timeouts

    @property
    def retried_ios(self):
        """
        Gets the retried_ios of this DriveCounterGroup.
        The number of retried I/O operations.

        :return: The retried_ios of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._retried_ios

    @retried_ios.setter
    def retried_ios(self, retried_ios):
        """
        Sets the retried_ios of this DriveCounterGroup.
        The number of retried I/O operations.

        :param retried_ios: The retried_ios of this DriveCounterGroup.
        :type: int
        """
        self._retried_ios = retried_ios

    @property
    def read_time_total_sq(self):
        """
        Gets the read_time_total_sq of this DriveCounterGroup.
        The sum of the squares of microseconds spent in read operations.

        :return: The read_time_total_sq of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._read_time_total_sq

    @read_time_total_sq.setter
    def read_time_total_sq(self, read_time_total_sq):
        """
        Sets the read_time_total_sq of this DriveCounterGroup.
        The sum of the squares of microseconds spent in read operations.

        :param read_time_total_sq: The read_time_total_sq of this DriveCounterGroup.
        :type: int
        """
        self._read_time_total_sq = read_time_total_sq

    @property
    def write_time_total_sq(self):
        """
        Gets the write_time_total_sq of this DriveCounterGroup.
        The sum of the squares of microseconds spent in write operations.

        :return: The write_time_total_sq of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._write_time_total_sq

    @write_time_total_sq.setter
    def write_time_total_sq(self, write_time_total_sq):
        """
        Sets the write_time_total_sq of this DriveCounterGroup.
        The sum of the squares of microseconds spent in write operations.

        :param write_time_total_sq: The write_time_total_sq of this DriveCounterGroup.
        :type: int
        """
        self._write_time_total_sq = write_time_total_sq

    @property
    def other_time_total_sq(self):
        """
        Gets the other_time_total_sq of this DriveCounterGroup.
        The sum of the squares of microseconds spent in non read-write operations.

        :return: The other_time_total_sq of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._other_time_total_sq

    @other_time_total_sq.setter
    def other_time_total_sq(self, other_time_total_sq):
        """
        Sets the other_time_total_sq of this DriveCounterGroup.
        The sum of the squares of microseconds spent in non read-write operations.

        :param other_time_total_sq: The other_time_total_sq of this DriveCounterGroup.
        :type: int
        """
        self._other_time_total_sq = other_time_total_sq

    @property
    def start_time(self):
        """
        Gets the start_time of this DriveCounterGroup.
        Start time for this collection as measured by the number of seconds since baseTime.

        :return: The start_time of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this DriveCounterGroup.
        Start time for this collection as measured by the number of seconds since baseTime.

        :param start_time: The start_time of this DriveCounterGroup.
        :type: int
        """
        self._start_time = start_time

    @property
    def observed_time(self):
        """
        Gets the observed_time of this DriveCounterGroup.
        End time for this collection as measured by the number of seconds since baseTime.

        :return: The observed_time of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._observed_time

    @observed_time.setter
    def observed_time(self, observed_time):
        """
        Sets the observed_time of this DriveCounterGroup.
        End time for this collection as measured by the number of seconds since baseTime.

        :param observed_time: The observed_time of this DriveCounterGroup.
        :type: int
        """
        self._observed_time = observed_time

    @property
    def queue_depth_total(self):
        """
        Gets the queue_depth_total of this DriveCounterGroup.
        Total drive queue depth.

        :return: The queue_depth_total of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._queue_depth_total

    @queue_depth_total.setter
    def queue_depth_total(self, queue_depth_total):
        """
        Sets the queue_depth_total of this DriveCounterGroup.
        Total drive queue depth.

        :param queue_depth_total: The queue_depth_total of this DriveCounterGroup.
        :type: int
        """
        self._queue_depth_total = queue_depth_total

    @property
    def queue_depth_max(self):
        """
        Gets the queue_depth_max of this DriveCounterGroup.
        Maximum queue depth.

        :return: The queue_depth_max of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._queue_depth_max

    @queue_depth_max.setter
    def queue_depth_max(self, queue_depth_max):
        """
        Sets the queue_depth_max of this DriveCounterGroup.
        Maximum queue depth.

        :param queue_depth_max: The queue_depth_max of this DriveCounterGroup.
        :type: int
        """
        self._queue_depth_max = queue_depth_max

    @property
    def random_ios_total(self):
        """
        Gets the random_ios_total of this DriveCounterGroup.
        Total number of IOs that are categorized as random.

        :return: The random_ios_total of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._random_ios_total

    @random_ios_total.setter
    def random_ios_total(self, random_ios_total):
        """
        Sets the random_ios_total of this DriveCounterGroup.
        Total number of IOs that are categorized as random.

        :param random_ios_total: The random_ios_total of this DriveCounterGroup.
        :type: int
        """
        self._random_ios_total = random_ios_total

    @property
    def random_bytes_total(self):
        """
        Gets the random_bytes_total of this DriveCounterGroup.
        Total number of Bytes that are categorized as random.

        :return: The random_bytes_total of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._random_bytes_total

    @random_bytes_total.setter
    def random_bytes_total(self, random_bytes_total):
        """
        Sets the random_bytes_total of this DriveCounterGroup.
        Total number of Bytes that are categorized as random.

        :param random_bytes_total: The random_bytes_total of this DriveCounterGroup.
        :type: int
        """
        self._random_bytes_total = random_bytes_total

    @property
    def cumulative_lba(self):
        """
        Gets the cumulative_lba of this DriveCounterGroup.
        Sum of LBA's accessed from the drive within an observation interval.

        :return: The cumulative_lba of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._cumulative_lba

    @cumulative_lba.setter
    def cumulative_lba(self, cumulative_lba):
        """
        Sets the cumulative_lba of this DriveCounterGroup.
        Sum of LBA's accessed from the drive within an observation interval.

        :param cumulative_lba: The cumulative_lba of this DriveCounterGroup.
        :type: int
        """
        self._cumulative_lba = cumulative_lba

    @property
    def cumulative_delta_lba(self):
        """
        Gets the cumulative_delta_lba of this DriveCounterGroup.
        Sum of LBA shifts accessed from the drive within an observation interval.

        :return: The cumulative_delta_lba of this DriveCounterGroup.
        :rtype: int
        :required/optional: required
        """
        return self._cumulative_delta_lba

    @cumulative_delta_lba.setter
    def cumulative_delta_lba(self, cumulative_delta_lba):
        """
        Sets the cumulative_delta_lba of this DriveCounterGroup.
        Sum of LBA shifts accessed from the drive within an observation interval.

        :param cumulative_delta_lba: The cumulative_delta_lba of this DriveCounterGroup.
        :type: int
        """
        self._cumulative_delta_lba = cumulative_delta_lba

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

