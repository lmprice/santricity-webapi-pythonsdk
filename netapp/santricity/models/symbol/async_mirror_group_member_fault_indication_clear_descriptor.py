# coding: utf-8

"""
AsyncMirrorGroupMemberFaultIndicationClearDescriptor.py

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


class AsyncMirrorGroupMemberFaultIndicationClearDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorGroupMemberFaultIndicationClearDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'member': 'str',  # (required parameter)
            'indication': 'str'
        }

        self.attribute_map = {
            'member': 'member',  # (required parameter)
            'indication': 'indication'
        }

        self._member = None
        self._indication = None

    @property
    def member(self):
        """
        Gets the member of this AsyncMirrorGroupMemberFaultIndicationClearDescriptor.
        The AMG member with condition to be cleared / acknowledged.

        :return: The member of this AsyncMirrorGroupMemberFaultIndicationClearDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this AsyncMirrorGroupMemberFaultIndicationClearDescriptor.
        The AMG member with condition to be cleared / acknowledged.

        :param member: The member of this AsyncMirrorGroupMemberFaultIndicationClearDescriptor.
        :type: str
        """
        self._member = member

    @property
    def indication(self):
        """
        Gets the indication of this AsyncMirrorGroupMemberFaultIndicationClearDescriptor.
        The type of indication to clear.

        :return: The indication of this AsyncMirrorGroupMemberFaultIndicationClearDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._indication

    @indication.setter
    def indication(self, indication):
        """
        Sets the indication of this AsyncMirrorGroupMemberFaultIndicationClearDescriptor.
        The type of indication to clear.

        :param indication: The indication of this AsyncMirrorGroupMemberFaultIndicationClearDescriptor.
        :type: str
        """
        allowed_values = ["unknownFailure", "failedFan", "failedPowerSupply", "failedMinihub", "failedEsm", "batteryNearExpiration", "failedBattery", "nominalTempExceeded", "maxTempExceeded", "upsOnBattery", "nonPreferredPath", "memParityError", "failedDriveScsiChannel", "degradedVolume", "failedVolumeInterruptedWrite", "failedModifyingVolume", "failedModifyingMultiRaid", "failedVolume", "failedVolumeMultiRaid", "impairedVolume", "failedVolumeAwaitingInit", "volumeHotSpareInUse", "offlineVolumeGroup", "failedDrive", "impendingDriveFailureRiskHigh", "impendingDriveFailureRiskMed", "impendingDriveFailureRiskLow", "uncertifiedDrive", "offlineCtl", "passiveCtl", "partitionsNotCompliant", "esmCodeVersionMismatch", "lostRedundancyDrive", "lostRedundancyTray", "lostRedundancyEsm", "trayidMismatch", "trayidConflict", "failedTransceiverModule", "channelMiswire", "nonFruBatteryNearExpiration", "nonFruFailedBattery", "rpaErrCtl", "repositoryOverThreshold", "repositoryFull", "snapshotFailed", "unsupportedMinihub", "esmMiswire", "ghostVolume", "snapshotNotCompliant", "rvmNotCompliant", "metadataOffline", "mirrorDualPrimary", "mirrorDualSecondary", "mirrorUnsynchronized", "remoteNoLun", "remoteNoArray", "remoteNoFabric", "remoteWwnChangeFailed", "fanUnknownStat", "powerSupplyUnknownStat", "esmUnknownStat", "tempSensorUnknownStat", "transModUnknownStat", "driveBypassedSpeedMismatch", "driveBypassedCauseUnknown", "minihubSpeedMismatch", "removedEsm", "removedBattery", "nonFruRemovedBattery", "volcopyFailed", "volcopyNotCompliant", "channelDegraded", "unsupportedTray", "speedNegError", "usmDatabaseFull", "usmUnreadableSectorsExist", "pathDegraded", "netSetupError", "mismatchedDriveType", "ctlMismatch", "failedDiscreteLine", "channelFailed", "linkSpeedDetectionMismatch", "uncertifiedEsm", "removedFan", "removedPowerSupply", "removedTempSensor", "removedIccCru", "removedSupportCru", "failedIccCru", "failedSupportCru", "batteryUnknownStat", "driveTraysNotGroupedTogether", "goldKeyNotCompliant", "mismatchedMdtSettings", "mismatchedGoldKeySettings", "ctlMiswire", "supportCruNoinput", "submodelNotSupported", "submodelNotSet", "submodelMismatch", "failedBatterySystem", "removedBatteryPack", "batteryConfigMismatch", "esmHardwareMismatch", "hostBoardFault", "ddcAvailable", "replacedDriveWrongType", "redundantPsRequired", "driveTraysNotCompliant", "sasDeviceLimitExceeded", "sasPortMiswired", "sasPortDegraded", "sasPortFailed", "corruptVpdEeprom", "failedI2cBus", "enclosureMisconfigured", "featureBundleNotCompliant", "driveBypassedSinglePort", "esmFactoryDefaultsMismatch", "hostBoardUnknownStat", "failedHostIoCard", "batteryWarn", "volumeGroupPartiallyComplete", "volumeGroupIncomplete", "volumeGroupMissing", "hotspareDriveMissing", "driveIncompatibleUprevDacstore", "driveIncompatibleDownrevDacstore", "iccCruUnknownStat", "removedAlarm", "supportCruUnknownStat", "performanceTierNotCompliant", "raid6NotCompliant", "driveIncompatibleSectorSize", "foreignDriveInconsistent", "foreignDriveRefersToNativeDrive", "nativeVgRefersToForeignDrive", "nativeVgForeignDriveMutualRef", "vgCloned", "foreignDriveHasInconsistentRole", "vgDrivePartOfMultipleVgs", "incompatibleFailedLegacyDrive", "unsupportedCacheMemorySize", "dedicatedMirrorChannelFailed", "vgHasDrivePartOfMultipleVgs", "ddfDriveOtherVendor", "multipleConfigDatabasesDetected", "adoptionFailedRaidLevelUnsupported", "dbAdoptionHardLimitExceeded", "legacyVgNotOptimal", "cacheMemSizeMismatch", "altCtlrBoardIdUnreadable", "cacheBackupDeviceFailed", "cacheBackupDeviceWriteProtected", "cacheBackupDeviceInsufficientCapacity", "expiredBattery", "expiredIntegratedBattery", "procMemTooSmallForCache", "batteryOvertemp", "invalidHostTypeIndex", "insufficientProcMemory", "ctlFailedCacheBackupDev", "removedController", "degradedHostIoCard", "ldFwVersionMismatch", "ldIncompatibleDatabase", "hostBoardIdMismatch", "iccMissing", "linkSpeedMismatch", "unsupportedHostBoard", "writebackCachingDisabled", "securityGetKey", "securityKeyInconsistent", "securityNotCompliant", "mixedDriveEnclosureMiswire", "unsuccessIsolationRedunMismatch", "thresExcdedMismatchCorrected", "inactiveHostPort", "inactiveInitiator", "protectionInformationNotCompliant", "protectionInformationNotSupported", "replacedInsufficientDriveCapacity", "drawerFailed", "drawerOpened", "ssdNotCompliant", "ssdAtEndOfLife", "fibreTrunkMiswire", "fibreTrunkIncompatibleEsm", "driveSlotLimitNotCompliant", "securityGetNewKey", "externalKmsNotCompliant", "sbbValidationFailure", "invalidPowerSupply", "enclosureThermalShutdown", "wbCachingForciblyDisabled", "driveUnsupportedProtocolConnection", "failedTwiBus", "mismatchedMidplaneEeproms", "driveUnsupportedCapacity", "evaluationLicenseExpirationImminent", "externalKmsKeyInvalid", "multipleMismatchedKeyIdsFound", "securityKeyValidationLock", "cacheDataLoss", "baseControllerDiagFailed", "featureNotCompliant", "driveIncompatiblePiType", "drawerDegraded", "offlineCtlIocFail", "invalidSataFlashConfiguration", "iocDiagFail", "sasPhyDisabledLocalWidePortDegraded", "sasPhyDisabledSharedWidePortDegraded", "drawerInvalid", "drawerRemoved", "driveUnsupportedInterposerFwVersion", "redundancyGroupNotConsistentDuringReconfig", "snapshotRollbackPaused", "pitRollbackPaused", "pitGroupRepositoryOverThreshold", "pitViewRepositoryOverThreshold", "pitGroupRepositoryFull", "pitViewRepositoryFull", "pitGroupFailed", "pitViewFailed", "pitPurged", "arvmDegradedMirrorGroup", "arvmFailedMirror", "arvmSyncIntervalTimeOverThreshold", "arvmRepositoryOverWarnThreshold", "arvmMirrorGroupRoleConflict", "incompatibleVolumeGroupSecurity", "arvmOrphanGroup", "arvmOrphanMember", "arvmMirrorGroupRecoveryPointLost", "diskPoolPartiallyPresent", "diskPoolIncomplete", "diskPoolMissing", "diskPoolReconstructionDriveCountBelowThreshold", "diskPoolUtilizationWarning", "diskPoolUtilizationCritical", "pendingPitCreationFailed", "pendingCgpitCreationFailed", "tpvRepositoryOverThreshold", "tpvRepositoryFull", "tpvFailed", "arvmSecondaryRepositoryFull", "arvmSyncInternallySuspended", "databaseRecoveryMode", "arvmPrimaryRepositoryFull", "incompatibleSataDrive", "diskPoolCapacityDepleted", "driveIncompatibleModelNumberUnsupported", "flashCacheNonOptimalDrives", "flashCacheHotSpareInUse", "allDrivesBypassedIncompatibleNvsram", "diskPoolDriveFailure", "diskPoolInsufficientMemory", "arvmOrphanIncompleteMember", "arvmSyncPausedAltState", "arvmRoleChangePaused", "driveIncompatibleAlignmentForEmulationDrive", "lossOfExternalRedundancy", "rvmWriteModeInconsistent", "sasHostMiswire", "sasCrossMiswire", "sasLoopMiswire", "copyThenFailWaitingOnHotSpare", "missingDriveLockdown", "hicConfigurationOoc", "copyThenFailWaitingOnDdpCapacity", "piErrorServiceMode", "piErrorLockdown", "sasPortDiscoveryError", "netNtpResolutionFail", "netNtpQueryFail", "netNtpServiceUnavailable", "multipathConfigurationError", "hostRedundancyLost", "excessiveRebootsDetected", "cacheNotFlushedOnOnlyCtlr", "__UNDEFINED"]
        if indication not in allowed_values:
            raise ValueError(
                "Invalid value for `indication`, must be one of {0}"
                .format(allowed_values)
            )
        self._indication = indication

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
