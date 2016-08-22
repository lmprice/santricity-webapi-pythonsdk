# coding: utf-8

"""
ComponentBundle.py

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


class ComponentBundle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ComponentBundle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fan': 'list[Fan]',  # (required parameter)
            'battery': 'list[Battery]',  # (required parameter)
            'power_supply': 'list[PowerSupply]',  # (required parameter)
            'thermal_sensor': 'list[ThermalSensor]',  # (required parameter)
            'esm': 'list[Esm]',  # (required parameter)
            'ups': 'list[Ups]',  # (required parameter)
            'minihub': 'list[Minihub]',  # (required parameter)
            'gbic': 'list[Gbic]',  # (required parameter)
            'sfp': 'list[Sfp]',  # (required parameter)
            'interconnect_cru': 'list[InterconnectCRU]',  # (required parameter)
            'support_cru': 'list[SupportCRU]',  # (required parameter)
            'alarm': 'list[Alarm]',  # (required parameter)
            'host_board': 'list[HostBoard]',  # (required parameter)
            'sas_expander': 'list[SasExpander]',  # (required parameter)
            'cache_backup_device': 'list[CacheBackupDevice]',  # (required parameter)
            'cache_memory_dimm': 'list[CacheMemoryDimm]',  # (required parameter)
            'processor_memory_dimm': 'list[ProcessorMemoryDimm]',  # (required parameter)
            'drawer': 'list[Drawer]'
        }

        self.attribute_map = {
            'fan': 'fan',  # (required parameter)
            'battery': 'battery',  # (required parameter)
            'power_supply': 'powerSupply',  # (required parameter)
            'thermal_sensor': 'thermalSensor',  # (required parameter)
            'esm': 'esm',  # (required parameter)
            'ups': 'ups',  # (required parameter)
            'minihub': 'minihub',  # (required parameter)
            'gbic': 'gbic',  # (required parameter)
            'sfp': 'sfp',  # (required parameter)
            'interconnect_cru': 'interconnectCRU',  # (required parameter)
            'support_cru': 'supportCRU',  # (required parameter)
            'alarm': 'alarm',  # (required parameter)
            'host_board': 'hostBoard',  # (required parameter)
            'sas_expander': 'sasExpander',  # (required parameter)
            'cache_backup_device': 'cacheBackupDevice',  # (required parameter)
            'cache_memory_dimm': 'cacheMemoryDimm',  # (required parameter)
            'processor_memory_dimm': 'processorMemoryDimm',  # (required parameter)
            'drawer': 'drawer'
        }

        self._fan = None
        self._battery = None
        self._power_supply = None
        self._thermal_sensor = None
        self._esm = None
        self._ups = None
        self._minihub = None
        self._gbic = None
        self._sfp = None
        self._interconnect_cru = None
        self._support_cru = None
        self._alarm = None
        self._host_board = None
        self._sas_expander = None
        self._cache_backup_device = None
        self._cache_memory_dimm = None
        self._processor_memory_dimm = None
        self._drawer = None

    @property
    def fan(self):
        """
        Gets the fan of this ComponentBundle.
        The fan component.

        :return: The fan of this ComponentBundle.
        :rtype: list[Fan]
        :required/optional: required
        """
        return self._fan

    @fan.setter
    def fan(self, fan):
        """
        Sets the fan of this ComponentBundle.
        The fan component.

        :param fan: The fan of this ComponentBundle.
        :type: list[Fan]
        """
        self._fan = fan

    @property
    def battery(self):
        """
        Gets the battery of this ComponentBundle.
        The battery component.

        :return: The battery of this ComponentBundle.
        :rtype: list[Battery]
        :required/optional: required
        """
        return self._battery

    @battery.setter
    def battery(self, battery):
        """
        Sets the battery of this ComponentBundle.
        The battery component.

        :param battery: The battery of this ComponentBundle.
        :type: list[Battery]
        """
        self._battery = battery

    @property
    def power_supply(self):
        """
        Gets the power_supply of this ComponentBundle.
        The power supply component.

        :return: The power_supply of this ComponentBundle.
        :rtype: list[PowerSupply]
        :required/optional: required
        """
        return self._power_supply

    @power_supply.setter
    def power_supply(self, power_supply):
        """
        Sets the power_supply of this ComponentBundle.
        The power supply component.

        :param power_supply: The power_supply of this ComponentBundle.
        :type: list[PowerSupply]
        """
        self._power_supply = power_supply

    @property
    def thermal_sensor(self):
        """
        Gets the thermal_sensor of this ComponentBundle.
        The thermal sensor component.

        :return: The thermal_sensor of this ComponentBundle.
        :rtype: list[ThermalSensor]
        :required/optional: required
        """
        return self._thermal_sensor

    @thermal_sensor.setter
    def thermal_sensor(self, thermal_sensor):
        """
        Sets the thermal_sensor of this ComponentBundle.
        The thermal sensor component.

        :param thermal_sensor: The thermal_sensor of this ComponentBundle.
        :type: list[ThermalSensor]
        """
        self._thermal_sensor = thermal_sensor

    @property
    def esm(self):
        """
        Gets the esm of this ComponentBundle.
        The ESM component.

        :return: The esm of this ComponentBundle.
        :rtype: list[Esm]
        :required/optional: required
        """
        return self._esm

    @esm.setter
    def esm(self, esm):
        """
        Sets the esm of this ComponentBundle.
        The ESM component.

        :param esm: The esm of this ComponentBundle.
        :type: list[Esm]
        """
        self._esm = esm

    @property
    def ups(self):
        """
        Gets the ups of this ComponentBundle.
        The UPS component.

        :return: The ups of this ComponentBundle.
        :rtype: list[Ups]
        :required/optional: required
        """
        return self._ups

    @ups.setter
    def ups(self, ups):
        """
        Sets the ups of this ComponentBundle.
        The UPS component.

        :param ups: The ups of this ComponentBundle.
        :type: list[Ups]
        """
        self._ups = ups

    @property
    def minihub(self):
        """
        Gets the minihub of this ComponentBundle.
        The minihub component.

        :return: The minihub of this ComponentBundle.
        :rtype: list[Minihub]
        :required/optional: required
        """
        return self._minihub

    @minihub.setter
    def minihub(self, minihub):
        """
        Sets the minihub of this ComponentBundle.
        The minihub component.

        :param minihub: The minihub of this ComponentBundle.
        :type: list[Minihub]
        """
        self._minihub = minihub

    @property
    def gbic(self):
        """
        Gets the gbic of this ComponentBundle.
        The GBIC component.

        :return: The gbic of this ComponentBundle.
        :rtype: list[Gbic]
        :required/optional: required
        """
        return self._gbic

    @gbic.setter
    def gbic(self, gbic):
        """
        Sets the gbic of this ComponentBundle.
        The GBIC component.

        :param gbic: The gbic of this ComponentBundle.
        :type: list[Gbic]
        """
        self._gbic = gbic

    @property
    def sfp(self):
        """
        Gets the sfp of this ComponentBundle.
        The SFP component.

        :return: The sfp of this ComponentBundle.
        :rtype: list[Sfp]
        :required/optional: required
        """
        return self._sfp

    @sfp.setter
    def sfp(self, sfp):
        """
        Sets the sfp of this ComponentBundle.
        The SFP component.

        :param sfp: The sfp of this ComponentBundle.
        :type: list[Sfp]
        """
        self._sfp = sfp

    @property
    def interconnect_cru(self):
        """
        Gets the interconnect_cru of this ComponentBundle.
        The interconnect CRU.

        :return: The interconnect_cru of this ComponentBundle.
        :rtype: list[InterconnectCRU]
        :required/optional: required
        """
        return self._interconnect_cru

    @interconnect_cru.setter
    def interconnect_cru(self, interconnect_cru):
        """
        Sets the interconnect_cru of this ComponentBundle.
        The interconnect CRU.

        :param interconnect_cru: The interconnect_cru of this ComponentBundle.
        :type: list[InterconnectCRU]
        """
        self._interconnect_cru = interconnect_cru

    @property
    def support_cru(self):
        """
        Gets the support_cru of this ComponentBundle.
        The Support CRU.

        :return: The support_cru of this ComponentBundle.
        :rtype: list[SupportCRU]
        :required/optional: required
        """
        return self._support_cru

    @support_cru.setter
    def support_cru(self, support_cru):
        """
        Sets the support_cru of this ComponentBundle.
        The Support CRU.

        :param support_cru: The support_cru of this ComponentBundle.
        :type: list[SupportCRU]
        """
        self._support_cru = support_cru

    @property
    def alarm(self):
        """
        Gets the alarm of this ComponentBundle.
        The alarm.

        :return: The alarm of this ComponentBundle.
        :rtype: list[Alarm]
        :required/optional: required
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        """
        Sets the alarm of this ComponentBundle.
        The alarm.

        :param alarm: The alarm of this ComponentBundle.
        :type: list[Alarm]
        """
        self._alarm = alarm

    @property
    def host_board(self):
        """
        Gets the host_board of this ComponentBundle.
        The host board.

        :return: The host_board of this ComponentBundle.
        :rtype: list[HostBoard]
        :required/optional: required
        """
        return self._host_board

    @host_board.setter
    def host_board(self, host_board):
        """
        Sets the host_board of this ComponentBundle.
        The host board.

        :param host_board: The host_board of this ComponentBundle.
        :type: list[HostBoard]
        """
        self._host_board = host_board

    @property
    def sas_expander(self):
        """
        Gets the sas_expander of this ComponentBundle.
        The SAS expanders.

        :return: The sas_expander of this ComponentBundle.
        :rtype: list[SasExpander]
        :required/optional: required
        """
        return self._sas_expander

    @sas_expander.setter
    def sas_expander(self, sas_expander):
        """
        Sets the sas_expander of this ComponentBundle.
        The SAS expanders.

        :param sas_expander: The sas_expander of this ComponentBundle.
        :type: list[SasExpander]
        """
        self._sas_expander = sas_expander

    @property
    def cache_backup_device(self):
        """
        Gets the cache_backup_device of this ComponentBundle.
        The cache backup devices.

        :return: The cache_backup_device of this ComponentBundle.
        :rtype: list[CacheBackupDevice]
        :required/optional: required
        """
        return self._cache_backup_device

    @cache_backup_device.setter
    def cache_backup_device(self, cache_backup_device):
        """
        Sets the cache_backup_device of this ComponentBundle.
        The cache backup devices.

        :param cache_backup_device: The cache_backup_device of this ComponentBundle.
        :type: list[CacheBackupDevice]
        """
        self._cache_backup_device = cache_backup_device

    @property
    def cache_memory_dimm(self):
        """
        Gets the cache_memory_dimm of this ComponentBundle.
        List of field replaceable cache memory DIMM modules.

        :return: The cache_memory_dimm of this ComponentBundle.
        :rtype: list[CacheMemoryDimm]
        :required/optional: required
        """
        return self._cache_memory_dimm

    @cache_memory_dimm.setter
    def cache_memory_dimm(self, cache_memory_dimm):
        """
        Sets the cache_memory_dimm of this ComponentBundle.
        List of field replaceable cache memory DIMM modules.

        :param cache_memory_dimm: The cache_memory_dimm of this ComponentBundle.
        :type: list[CacheMemoryDimm]
        """
        self._cache_memory_dimm = cache_memory_dimm

    @property
    def processor_memory_dimm(self):
        """
        Gets the processor_memory_dimm of this ComponentBundle.
        List of field replaceable processor memory DIMMs.

        :return: The processor_memory_dimm of this ComponentBundle.
        :rtype: list[ProcessorMemoryDimm]
        :required/optional: required
        """
        return self._processor_memory_dimm

    @processor_memory_dimm.setter
    def processor_memory_dimm(self, processor_memory_dimm):
        """
        Sets the processor_memory_dimm of this ComponentBundle.
        List of field replaceable processor memory DIMMs.

        :param processor_memory_dimm: The processor_memory_dimm of this ComponentBundle.
        :type: list[ProcessorMemoryDimm]
        """
        self._processor_memory_dimm = processor_memory_dimm

    @property
    def drawer(self):
        """
        Gets the drawer of this ComponentBundle.
        List of drawers.

        :return: The drawer of this ComponentBundle.
        :rtype: list[Drawer]
        :required/optional: required
        """
        return self._drawer

    @drawer.setter
    def drawer(self, drawer):
        """
        Sets the drawer of this ComponentBundle.
        List of drawers.

        :param drawer: The drawer of this ComponentBundle.
        :type: list[Drawer]
        """
        self._drawer = drawer

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
