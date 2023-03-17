# Auto generated from uco_vocabulary.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-17T20:22:15
# Schema: ucolink-vocabulary
#
# id: https://w3id.org/lmodel/ucolink-vocabulary
# description:
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = "1.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LM_CORE = CurieNamespace('lm_core', 'https://w3id.org/lmodel/core/')
SCHEMA_CORE = CurieNamespace('schema_core', 'https://w3id.org/lmodel/uco-core/schema/')
VOCABULARY = CurieNamespace('vocabulary', 'https://w3id.org/lmodel/uco-vocabulary/')
DEFAULT_ = VOCABULARY


# Types

# Class references




# Enumerations
class AccountTypeEnum(EnumDefinitionImpl):
    """
    "An account type represents the endpoint type where the account is located; for example, ADS for an
    ActiveDirectory endpoint type, or LDAP for an LDAP, etc."
    """
    ldap = PermissibleValue(text="ldap")
    nis = PermissibleValue(text="nis")
    openid = PermissibleValue(text="openid")
    radius = PermissibleValue(text="radius")
    tacacs = PermissibleValue(text="tacacs")
    unix = PermissibleValue(text="unix")
    windows_domain = PermissibleValue(text="windows_domain")
    windows_local = PermissibleValue(text="windows_local")

    _defn = EnumDefinition(
        name="AccountTypeEnum",
        description="\"An account type represents the endpoint type where the account is located; for example, ADS for an ActiveDirectory endpoint type, or LDAP for an LDAP, etc.\"",
    )

class ActionArgumentNameEnum(EnumDefinitionImpl):

    API = PermissibleValue(text="API")
    Command = PermissibleValue(text="Command")
    Flags = PermissibleValue(text="Flags")
    Hostname = PermissibleValue(text="Hostname")
    Options = PermissibleValue(text="Options")
    Password = PermissibleValue(text="Password")
    Protection = PermissibleValue(text="Protection")
    Reason = PermissibleValue(text="Reason")
    Server = PermissibleValue(text="Server")
    Username = PermissibleValue(text="Username")

    _defn = EnumDefinition(
        name="ActionArgumentNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "APC Address",
                PermissibleValue(text="APC Address") )
        setattr(cls, "APC Mode",
                PermissibleValue(text="APC Mode") )
        setattr(cls, "Access Mode",
                PermissibleValue(text="Access Mode") )
        setattr(cls, "Application Name",
                PermissibleValue(text="Application Name") )
        setattr(cls, "Base Address",
                PermissibleValue(text="Base Address") )
        setattr(cls, "Callback Address",
                PermissibleValue(text="Callback Address") )
        setattr(cls, "Code Address",
                PermissibleValue(text="Code Address") )
        setattr(cls, "Control Code",
                PermissibleValue(text="Control Code") )
        setattr(cls, "Control Parameter",
                PermissibleValue(text="Control Parameter") )
        setattr(cls, "Creation Flags",
                PermissibleValue(text="Creation Flags") )
        setattr(cls, "Database Name",
                PermissibleValue(text="Database Name") )
        setattr(cls, "Delay Time (ms)",
                PermissibleValue(text="Delay Time (ms)") )
        setattr(cls, "Destination Address",
                PermissibleValue(text="Destination Address") )
        setattr(cls, "Error Control",
                PermissibleValue(text="Error Control") )
        setattr(cls, "File Information Class",
                PermissibleValue(text="File Information Class") )
        setattr(cls, "Function Address",
                PermissibleValue(text="Function Address") )
        setattr(cls, "Function Name",
                PermissibleValue(text="Function Name") )
        setattr(cls, "Function Ordinal",
                PermissibleValue(text="Function Ordinal") )
        setattr(cls, "Hook Type",
                PermissibleValue(text="Hook Type") )
        setattr(cls, "Host Name",
                PermissibleValue(text="Host Name") )
        setattr(cls, "Initial Owner",
                PermissibleValue(text="Initial Owner") )
        setattr(cls, "Mapping Offset",
                PermissibleValue(text="Mapping Offset") )
        setattr(cls, "Number of Bytes Per Send",
                PermissibleValue(text="Number of Bytes Per Send") )
        setattr(cls, "Parameter Address",
                PermissibleValue(text="Parameter Address") )
        setattr(cls, "Privilege Name",
                PermissibleValue(text="Privilege Name") )
        setattr(cls, "Proxy Bypass",
                PermissibleValue(text="Proxy Bypass") )
        setattr(cls, "Proxy Name",
                PermissibleValue(text="Proxy Name") )
        setattr(cls, "Request Size",
                PermissibleValue(text="Request Size") )
        setattr(cls, "Requested Version",
                PermissibleValue(text="Requested Version") )
        setattr(cls, "Service Name",
                PermissibleValue(text="Service Name") )
        setattr(cls, "Service State",
                PermissibleValue(text="Service State") )
        setattr(cls, "Service Type",
                PermissibleValue(text="Service Type") )
        setattr(cls, "Share Mode",
                PermissibleValue(text="Share Mode") )
        setattr(cls, "Shutdown Flag",
                PermissibleValue(text="Shutdown Flag") )
        setattr(cls, "Size (bytes)",
                PermissibleValue(text="Size (bytes)") )
        setattr(cls, "Sleep Time (ms)",
                PermissibleValue(text="Sleep Time (ms)") )
        setattr(cls, "Source Address",
                PermissibleValue(text="Source Address") )
        setattr(cls, "Starting Address",
                PermissibleValue(text="Starting Address") )
        setattr(cls, "System Metric Index",
                PermissibleValue(text="System Metric Index") )
        setattr(cls, "Target PID",
                PermissibleValue(text="Target PID") )
        setattr(cls, "Transfer Flags",
                PermissibleValue(text="Transfer Flags") )

class ActionNameEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ActionNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Accept Socket Connection",
                PermissibleValue(text="Accept Socket Connection") )
        setattr(cls, "Add Connection to Network Share",
                PermissibleValue(text="Add Connection to Network Share") )
        setattr(cls, "Add Network Share",
                PermissibleValue(text="Add Network Share") )
        setattr(cls, "Add Scheduled Task",
                PermissibleValue(text="Add Scheduled Task") )
        setattr(cls, "Add System Call Hook",
                PermissibleValue(text="Add System Call Hook") )
        setattr(cls, "Add User",
                PermissibleValue(text="Add User") )
        setattr(cls, "Add Windows Hook",
                PermissibleValue(text="Add Windows Hook") )
        setattr(cls, "Allocate Virtual Memory in Process",
                PermissibleValue(text="Allocate Virtual Memory in Process") )
        setattr(cls, "Bind Address to Socket",
                PermissibleValue(text="Bind Address to Socket") )
        setattr(cls, "Change Service Configuration",
                PermissibleValue(text="Change Service Configuration") )
        setattr(cls, "Check for Remote Debugger",
                PermissibleValue(text="Check for Remote Debugger") )
        setattr(cls, "Close Port",
                PermissibleValue(text="Close Port") )
        setattr(cls, "Close Registry Key",
                PermissibleValue(text="Close Registry Key") )
        setattr(cls, "Close Socket",
                PermissibleValue(text="Close Socket") )
        setattr(cls, "Configure Service",
                PermissibleValue(text="Configure Service") )
        setattr(cls, "Connect to IP",
                PermissibleValue(text="Connect to IP") )
        setattr(cls, "Connect to Named Pipe",
                PermissibleValue(text="Connect to Named Pipe") )
        setattr(cls, "Connect to Network Share",
                PermissibleValue(text="Connect to Network Share") )
        setattr(cls, "Connect to Socket",
                PermissibleValue(text="Connect to Socket") )
        setattr(cls, "Connect to URL",
                PermissibleValue(text="Connect to URL") )
        setattr(cls, "Control Driver",
                PermissibleValue(text="Control Driver") )
        setattr(cls, "Control Service",
                PermissibleValue(text="Control Service") )
        setattr(cls, "Copy File",
                PermissibleValue(text="Copy File") )
        setattr(cls, "Create Dialog Box",
                PermissibleValue(text="Create Dialog Box") )
        setattr(cls, "Create Directory",
                PermissibleValue(text="Create Directory") )
        setattr(cls, "Create Event",
                PermissibleValue(text="Create Event") )
        setattr(cls, "Create File",
                PermissibleValue(text="Create File") )
        setattr(cls, "Create File Alternate Data Stream",
                PermissibleValue(text="Create File Alternate Data Stream") )
        setattr(cls, "Create File Mapping",
                PermissibleValue(text="Create File Mapping") )
        setattr(cls, "Create File Symbolic Link",
                PermissibleValue(text="Create File Symbolic Link") )
        setattr(cls, "Create Hidden File",
                PermissibleValue(text="Create Hidden File") )
        setattr(cls, "Create Mailslot",
                PermissibleValue(text="Create Mailslot") )
        setattr(cls, "Create Module",
                PermissibleValue(text="Create Module") )
        setattr(cls, "Create Mutex",
                PermissibleValue(text="Create Mutex") )
        setattr(cls, "Create Named Pipe",
                PermissibleValue(text="Create Named Pipe") )
        setattr(cls, "Create Process",
                PermissibleValue(text="Create Process") )
        setattr(cls, "Create Process as User",
                PermissibleValue(text="Create Process as User") )
        setattr(cls, "Create Registry Key",
                PermissibleValue(text="Create Registry Key") )
        setattr(cls, "Create Registry Key Value",
                PermissibleValue(text="Create Registry Key Value") )
        setattr(cls, "Create Remote Thread in Process",
                PermissibleValue(text="Create Remote Thread in Process") )
        setattr(cls, "Create Service",
                PermissibleValue(text="Create Service") )
        setattr(cls, "Create Socket",
                PermissibleValue(text="Create Socket") )
        setattr(cls, "Create Symbolic Link",
                PermissibleValue(text="Create Symbolic Link") )
        setattr(cls, "Create Thread",
                PermissibleValue(text="Create Thread") )
        setattr(cls, "Create Window",
                PermissibleValue(text="Create Window") )
        setattr(cls, "Delete Directory",
                PermissibleValue(text="Delete Directory") )
        setattr(cls, "Delete File",
                PermissibleValue(text="Delete File") )
        setattr(cls, "Delete Named Pipe",
                PermissibleValue(text="Delete Named Pipe") )
        setattr(cls, "Delete Network Share",
                PermissibleValue(text="Delete Network Share") )
        setattr(cls, "Delete Registry Key",
                PermissibleValue(text="Delete Registry Key") )
        setattr(cls, "Delete Registry Key Value",
                PermissibleValue(text="Delete Registry Key Value") )
        setattr(cls, "Delete Service",
                PermissibleValue(text="Delete Service") )
        setattr(cls, "Delete User",
                PermissibleValue(text="Delete User") )
        setattr(cls, "Disconnect from Named Pipe",
                PermissibleValue(text="Disconnect from Named Pipe") )
        setattr(cls, "Disconnect from Network Share",
                PermissibleValue(text="Disconnect from Network Share") )
        setattr(cls, "Disconnect from Socket",
                PermissibleValue(text="Disconnect from Socket") )
        setattr(cls, "Download File",
                PermissibleValue(text="Download File") )
        setattr(cls, "Enumerate DLLs",
                PermissibleValue(text="Enumerate DLLs") )
        setattr(cls, "Enumerate Network Shares",
                PermissibleValue(text="Enumerate Network Shares") )
        setattr(cls, "Enumerate Processes",
                PermissibleValue(text="Enumerate Processes") )
        setattr(cls, "Enumerate Protocols",
                PermissibleValue(text="Enumerate Protocols") )
        setattr(cls, "Enumerate Registry Key Subkeys",
                PermissibleValue(text="Enumerate Registry Key Subkeys") )
        setattr(cls, "Enumerate Registry Key Values",
                PermissibleValue(text="Enumerate Registry Key Values") )
        setattr(cls, "Enumerate Services",
                PermissibleValue(text="Enumerate Services") )
        setattr(cls, "Enumerate System Handles",
                PermissibleValue(text="Enumerate System Handles") )
        setattr(cls, "Enumerate Threads",
                PermissibleValue(text="Enumerate Threads") )
        setattr(cls, "Enumerate Threads in Process",
                PermissibleValue(text="Enumerate Threads in Process") )
        setattr(cls, "Enumerate Users",
                PermissibleValue(text="Enumerate Users") )
        setattr(cls, "Enumerate Windows",
                PermissibleValue(text="Enumerate Windows") )
        setattr(cls, "Find File",
                PermissibleValue(text="Find File") )
        setattr(cls, "Find Window",
                PermissibleValue(text="Find Window") )
        setattr(cls, "Flush Process Instruction Cache",
                PermissibleValue(text="Flush Process Instruction Cache") )
        setattr(cls, "Free Library",
                PermissibleValue(text="Free Library") )
        setattr(cls, "Free Process Virtual Memory",
                PermissibleValue(text="Free Process Virtual Memory") )
        setattr(cls, "Get Disk Free Space",
                PermissibleValue(text="Get Disk Free Space") )
        setattr(cls, "Get Disk Type",
                PermissibleValue(text="Get Disk Type") )
        setattr(cls, "Get Elapsed System Up Time",
                PermissibleValue(text="Get Elapsed System Up Time") )
        setattr(cls, "Get File Attributes",
                PermissibleValue(text="Get File Attributes") )
        setattr(cls, "Get Function Address",
                PermissibleValue(text="Get Function Address") )
        setattr(cls, "Get Host By Address",
                PermissibleValue(text="Get Host By Address") )
        setattr(cls, "Get Host By Name",
                PermissibleValue(text="Get Host By Name") )
        setattr(cls, "Get Host Name",
                PermissibleValue(text="Get Host Name") )
        setattr(cls, "Get Library File Name",
                PermissibleValue(text="Get Library File Name") )
        setattr(cls, "Get Library Handle",
                PermissibleValue(text="Get Library Handle") )
        setattr(cls, "Get NetBIOS Name",
                PermissibleValue(text="Get NetBIOS Name") )
        setattr(cls, "Get Process Current Directory",
                PermissibleValue(text="Get Process Current Directory") )
        setattr(cls, "Get Process Environment Variable",
                PermissibleValue(text="Get Process Environment Variable") )
        setattr(cls, "Get Process Startup Information",
                PermissibleValue(text="Get Process Startup Information") )
        setattr(cls, "Get Processes Snapshot",
                PermissibleValue(text="Get Processes Snapshot") )
        setattr(cls, "Get Registry Key Attributes",
                PermissibleValue(text="Get Registry Key Attributes") )
        setattr(cls, "Get Service Status",
                PermissibleValue(text="Get Service Status") )
        setattr(cls, "Get System Global Flags",
                PermissibleValue(text="Get System Global Flags") )
        setattr(cls, "Get System Host Name",
                PermissibleValue(text="Get System Host Name") )
        setattr(cls, "Get System Local Time",
                PermissibleValue(text="Get System Local Time") )
        setattr(cls, "Get System NetBIOS Name",
                PermissibleValue(text="Get System NetBIOS Name") )
        setattr(cls, "Get System Network Parameters",
                PermissibleValue(text="Get System Network Parameters") )
        setattr(cls, "Get System Time",
                PermissibleValue(text="Get System Time") )
        setattr(cls, "Get Thread Context",
                PermissibleValue(text="Get Thread Context") )
        setattr(cls, "Get Thread Username",
                PermissibleValue(text="Get Thread Username") )
        setattr(cls, "Get User Attributes",
                PermissibleValue(text="Get User Attributes") )
        setattr(cls, "Get Username",
                PermissibleValue(text="Get Username") )
        setattr(cls, "Get Windows Directory",
                PermissibleValue(text="Get Windows Directory") )
        setattr(cls, "Get Windows System Directory",
                PermissibleValue(text="Get Windows System Directory") )
        setattr(cls, "Get Windows Temporary Files Directory",
                PermissibleValue(text="Get Windows Temporary Files Directory") )
        setattr(cls, "Hide Window",
                PermissibleValue(text="Hide Window") )
        setattr(cls, "Impersonate Process",
                PermissibleValue(text="Impersonate Process") )
        setattr(cls, "Impersonate Thread",
                PermissibleValue(text="Impersonate Thread") )
        setattr(cls, "Inject Memory Page",
                PermissibleValue(text="Inject Memory Page") )
        setattr(cls, "Kill Process",
                PermissibleValue(text="Kill Process") )
        setattr(cls, "Kill Thread",
                PermissibleValue(text="Kill Thread") )
        setattr(cls, "Kill Window",
                PermissibleValue(text="Kill Window") )
        setattr(cls, "Listen on Port",
                PermissibleValue(text="Listen on Port") )
        setattr(cls, "Listen on Socket",
                PermissibleValue(text="Listen on Socket") )
        setattr(cls, "Load Driver",
                PermissibleValue(text="Load Driver") )
        setattr(cls, "Load Library",
                PermissibleValue(text="Load Library") )
        setattr(cls, "Load Module",
                PermissibleValue(text="Load Module") )
        setattr(cls, "Load and Call Driver",
                PermissibleValue(text="Load and Call Driver") )
        setattr(cls, "Lock File",
                PermissibleValue(text="Lock File") )
        setattr(cls, "Logon as User",
                PermissibleValue(text="Logon as User") )
        setattr(cls, "Map File",
                PermissibleValue(text="Map File") )
        setattr(cls, "Map Library",
                PermissibleValue(text="Map Library") )
        setattr(cls, "Map View of File",
                PermissibleValue(text="Map View of File") )
        setattr(cls, "Modify File",
                PermissibleValue(text="Modify File") )
        setattr(cls, "Modify Named Pipe",
                PermissibleValue(text="Modify Named Pipe") )
        setattr(cls, "Modify Process",
                PermissibleValue(text="Modify Process") )
        setattr(cls, "Modify Registry Key",
                PermissibleValue(text="Modify Registry Key") )
        setattr(cls, "Modify Registry Key Value",
                PermissibleValue(text="Modify Registry Key Value") )
        setattr(cls, "Modify Service",
                PermissibleValue(text="Modify Service") )
        setattr(cls, "Monitor Registry Key",
                PermissibleValue(text="Monitor Registry Key") )
        setattr(cls, "Move File",
                PermissibleValue(text="Move File") )
        setattr(cls, "Open File",
                PermissibleValue(text="Open File") )
        setattr(cls, "Open File Mapping",
                PermissibleValue(text="Open File Mapping") )
        setattr(cls, "Open Mutex",
                PermissibleValue(text="Open Mutex") )
        setattr(cls, "Open Port",
                PermissibleValue(text="Open Port") )
        setattr(cls, "Open Process",
                PermissibleValue(text="Open Process") )
        setattr(cls, "Open Registry Key",
                PermissibleValue(text="Open Registry Key") )
        setattr(cls, "Open Service",
                PermissibleValue(text="Open Service") )
        setattr(cls, "Open Service Control Manager",
                PermissibleValue(text="Open Service Control Manager") )
        setattr(cls, "Protect Virtual Memory",
                PermissibleValue(text="Protect Virtual Memory") )
        setattr(cls, "Query DNS",
                PermissibleValue(text="Query DNS") )
        setattr(cls, "Query Disk Attributes",
                PermissibleValue(text="Query Disk Attributes") )
        setattr(cls, "Query Process Virtual Memory",
                PermissibleValue(text="Query Process Virtual Memory") )
        setattr(cls, "Queue APC in Thread",
                PermissibleValue(text="Queue APC in Thread") )
        setattr(cls, "Read File",
                PermissibleValue(text="Read File") )
        setattr(cls, "Read From Named Pipe",
                PermissibleValue(text="Read From Named Pipe") )
        setattr(cls, "Read From Process Memory",
                PermissibleValue(text="Read From Process Memory") )
        setattr(cls, "Read Registry Key Value",
                PermissibleValue(text="Read Registry Key Value") )
        setattr(cls, "Receive Data on Socket",
                PermissibleValue(text="Receive Data on Socket") )
        setattr(cls, "Receive Email Message",
                PermissibleValue(text="Receive Email Message") )
        setattr(cls, "Release Mutex",
                PermissibleValue(text="Release Mutex") )
        setattr(cls, "Rename File",
                PermissibleValue(text="Rename File") )
        setattr(cls, "Revert Thread to Self",
                PermissibleValue(text="Revert Thread to Self") )
        setattr(cls, "Send Control Code to File",
                PermissibleValue(text="Send Control Code to File") )
        setattr(cls, "Send Control Code to Pipe",
                PermissibleValue(text="Send Control Code to Pipe") )
        setattr(cls, "Send Control Code to Service",
                PermissibleValue(text="Send Control Code to Service") )
        setattr(cls, "Send DNS Query",
                PermissibleValue(text="Send DNS Query") )
        setattr(cls, "Send Data on Socket",
                PermissibleValue(text="Send Data on Socket") )
        setattr(cls, "Send Data to Address on Socket",
                PermissibleValue(text="Send Data to Address on Socket") )
        setattr(cls, "Send Email Message",
                PermissibleValue(text="Send Email Message") )
        setattr(cls, "Send ICMP Request",
                PermissibleValue(text="Send ICMP Request") )
        setattr(cls, "Send Reverse DNS Query",
                PermissibleValue(text="Send Reverse DNS Query") )
        setattr(cls, "Set File Attributes",
                PermissibleValue(text="Set File Attributes") )
        setattr(cls, "Set NetBIOS Name",
                PermissibleValue(text="Set NetBIOS Name") )
        setattr(cls, "Set Process Current Directory",
                PermissibleValue(text="Set Process Current Directory") )
        setattr(cls, "Set Process Environment Variable",
                PermissibleValue(text="Set Process Environment Variable") )
        setattr(cls, "Set System Global Flags",
                PermissibleValue(text="Set System Global Flags") )
        setattr(cls, "Set System Host Name",
                PermissibleValue(text="Set System Host Name") )
        setattr(cls, "Set System Time",
                PermissibleValue(text="Set System Time") )
        setattr(cls, "Set Thread Context",
                PermissibleValue(text="Set Thread Context") )
        setattr(cls, "Show Window",
                PermissibleValue(text="Show Window") )
        setattr(cls, "Shutdown System",
                PermissibleValue(text="Shutdown System") )
        setattr(cls, "Sleep Process",
                PermissibleValue(text="Sleep Process") )
        setattr(cls, "Sleep System",
                PermissibleValue(text="Sleep System") )
        setattr(cls, "Start Service",
                PermissibleValue(text="Start Service") )
        setattr(cls, "Unload Driver",
                PermissibleValue(text="Unload Driver") )
        setattr(cls, "Unload Module",
                PermissibleValue(text="Unload Module") )
        setattr(cls, "Unlock File",
                PermissibleValue(text="Unlock File") )
        setattr(cls, "Unmap File",
                PermissibleValue(text="Unmap File") )
        setattr(cls, "Upload File",
                PermissibleValue(text="Upload File") )
        setattr(cls, "Write to File",
                PermissibleValue(text="Write to File") )
        setattr(cls, "Write to Process Virtual Memory",
                PermissibleValue(text="Write to Process Virtual Memory") )

class ActionRelationshipTypeEnum(EnumDefinitionImpl):

    Dependent_On = PermissibleValue(text="Dependent_On")
    Equivalent_To = PermissibleValue(text="Equivalent_To")
    Followed_By = PermissibleValue(text="Followed_By")
    Initiated = PermissibleValue(text="Initiated")
    Initiated_By = PermissibleValue(text="Initiated_By")
    Preceded_By = PermissibleValue(text="Preceded_By")
    Related_To = PermissibleValue(text="Related_To")

    _defn = EnumDefinition(
        name="ActionRelationshipTypeEnum",
    )

class ActionStatusTypeEnum(EnumDefinitionImpl):

    Error = PermissibleValue(text="Error")
    Fail = PermissibleValue(text="Fail")
    Ongoing = PermissibleValue(text="Ongoing")
    Pending = PermissibleValue(text="Pending")
    Success = PermissibleValue(text="Success")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="ActionStatusTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete/Finish",
                PermissibleValue(text="Complete/Finish") )

class ActionTypeEnum(EnumDefinitionImpl):

    Accept = PermissibleValue(text="Accept")
    Access = PermissibleValue(text="Access")
    Add = PermissibleValue(text="Add")
    Alert = PermissibleValue(text="Alert")
    Allocate = PermissibleValue(text="Allocate")
    Archive = PermissibleValue(text="Archive")
    Assign = PermissibleValue(text="Assign")
    Audit = PermissibleValue(text="Audit")
    Backup = PermissibleValue(text="Backup")
    Bind = PermissibleValue(text="Bind")
    Block = PermissibleValue(text="Block")
    Call = PermissibleValue(text="Call")
    Change = PermissibleValue(text="Change")
    Check = PermissibleValue(text="Check")
    Clean = PermissibleValue(text="Clean")
    Click = PermissibleValue(text="Click")
    Close = PermissibleValue(text="Close")
    Compare = PermissibleValue(text="Compare")
    Compress = PermissibleValue(text="Compress")
    Configure = PermissibleValue(text="Configure")
    Connect = PermissibleValue(text="Connect")
    Control = PermissibleValue(text="Control")
    Create = PermissibleValue(text="Create")
    Decode = PermissibleValue(text="Decode")
    Decompress = PermissibleValue(text="Decompress")
    Decrypt = PermissibleValue(text="Decrypt")
    Deny = PermissibleValue(text="Deny")
    Depress = PermissibleValue(text="Depress")
    Detect = PermissibleValue(text="Detect")
    Disconnect = PermissibleValue(text="Disconnect")
    Download = PermissibleValue(text="Download")
    Draw = PermissibleValue(text="Draw")
    Drop = PermissibleValue(text="Drop")
    Encode = PermissibleValue(text="Encode")
    Encrypt = PermissibleValue(text="Encrypt")
    Enumerate = PermissibleValue(text="Enumerate")
    Execute = PermissibleValue(text="Execute")
    Extract = PermissibleValue(text="Extract")
    Filter = PermissibleValue(text="Filter")
    Find = PermissibleValue(text="Find")
    Flush = PermissibleValue(text="Flush")
    Fork = PermissibleValue(text="Fork")
    Free = PermissibleValue(text="Free")
    Get = PermissibleValue(text="Get")
    Hide = PermissibleValue(text="Hide")
    Hook = PermissibleValue(text="Hook")
    Impersonate = PermissibleValue(text="Impersonate")
    Initialize = PermissibleValue(text="Initialize")
    Inject = PermissibleValue(text="Inject")
    Install = PermissibleValue(text="Install")
    Interleave = PermissibleValue(text="Interleave")
    Join = PermissibleValue(text="Join")
    Kill = PermissibleValue(text="Kill")
    Listen = PermissibleValue(text="Listen")
    Load = PermissibleValue(text="Load")
    Lock = PermissibleValue(text="Lock")
    Map = PermissibleValue(text="Map")
    Merge = PermissibleValue(text="Merge")
    Modify = PermissibleValue(text="Modify")
    Monitor = PermissibleValue(text="Monitor")
    Move = PermissibleValue(text="Move")
    Open = PermissibleValue(text="Open")
    Pack = PermissibleValue(text="Pack")
    Pause = PermissibleValue(text="Pause")
    Press = PermissibleValue(text="Press")
    Protect = PermissibleValue(text="Protect")
    Quarantine = PermissibleValue(text="Quarantine")
    Query = PermissibleValue(text="Query")
    Queue = PermissibleValue(text="Queue")
    Raise = PermissibleValue(text="Raise")
    Read = PermissibleValue(text="Read")
    Receive = PermissibleValue(text="Receive")
    Release = PermissibleValue(text="Release")
    Rename = PermissibleValue(text="Rename")
    Replicate = PermissibleValue(text="Replicate")
    Restore = PermissibleValue(text="Restore")
    Resume = PermissibleValue(text="Resume")
    Revert = PermissibleValue(text="Revert")
    Run = PermissibleValue(text="Run")
    Save = PermissibleValue(text="Save")
    Scan = PermissibleValue(text="Scan")
    Schedule = PermissibleValue(text="Schedule")
    Search = PermissibleValue(text="Search")
    Send = PermissibleValue(text="Send")
    Set = PermissibleValue(text="Set")
    Shutdown = PermissibleValue(text="Shutdown")
    Sleep = PermissibleValue(text="Sleep")
    Snapshot = PermissibleValue(text="Snapshot")
    Start = PermissibleValue(text="Start")
    Stop = PermissibleValue(text="Stop")
    Suspend = PermissibleValue(text="Suspend")
    Synchronize = PermissibleValue(text="Synchronize")
    Throw = PermissibleValue(text="Throw")
    Transmit = PermissibleValue(text="Transmit")
    Unblock = PermissibleValue(text="Unblock")
    Unhide = PermissibleValue(text="Unhide")
    Unhook = PermissibleValue(text="Unhook")
    Uninstall = PermissibleValue(text="Uninstall")
    Unload = PermissibleValue(text="Unload")
    Unlock = PermissibleValue(text="Unlock")
    Unmap = PermissibleValue(text="Unmap")
    Unpack = PermissibleValue(text="Unpack")
    Update = PermissibleValue(text="Update")
    Upgrade = PermissibleValue(text="Upgrade")
    Upload = PermissibleValue(text="Upload")
    Write = PermissibleValue(text="Write")

    _defn = EnumDefinition(
        name="ActionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Copy/Duplicate",
                PermissibleValue(text="Copy/Duplicate") )
        setattr(cls, "Login/Logon",
                PermissibleValue(text="Login/Logon") )
        setattr(cls, "Logout/Logoff",
                PermissibleValue(text="Logout/Logoff") )
        setattr(cls, "Remove/Delete",
                PermissibleValue(text="Remove/Delete") )
        setattr(cls, "Wipe/Destroy/Purge",
                PermissibleValue(text="Wipe/Destroy/Purge") )

class BitnessEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="BitnessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "32",
                PermissibleValue(text="32") )
        setattr(cls, "64",
                PermissibleValue(text="64") )

class CharacterEncodingEnum(EnumDefinitionImpl):

    ASCII = PermissibleValue(text="ASCII")

    _defn = EnumDefinition(
        name="CharacterEncodingEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "UTF-16",
                PermissibleValue(text="UTF-16") )
        setattr(cls, "UTF-32",
                PermissibleValue(text="UTF-32") )
        setattr(cls, "UTF-8",
                PermissibleValue(text="UTF-8") )
        setattr(cls, "Windows-1250",
                PermissibleValue(text="Windows-1250") )
        setattr(cls, "Windows-1251",
                PermissibleValue(text="Windows-1251") )
        setattr(cls, "Windows-1252",
                PermissibleValue(text="Windows-1252") )
        setattr(cls, "Windows-1253",
                PermissibleValue(text="Windows-1253") )
        setattr(cls, "Windows-1254",
                PermissibleValue(text="Windows-1254") )
        setattr(cls, "Windows-1255",
                PermissibleValue(text="Windows-1255") )
        setattr(cls, "Windows-1256",
                PermissibleValue(text="Windows-1256") )
        setattr(cls, "Windows-1257",
                PermissibleValue(text="Windows-1257") )
        setattr(cls, "Windows-1258",
                PermissibleValue(text="Windows-1258") )

class ContactAddressScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactAddressScopeEnum",
    )

class ContactEmailScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    cloud = PermissibleValue(text="cloud")

    _defn = EnumDefinition(
        name="ContactEmailScopeEnum",
    )

class ContactPhoneEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    mobile = PermissibleValue(text="mobile")
    main = PermissibleValue(text="main")
    pager = PermissibleValue(text="pager")

    _defn = EnumDefinition(
        name="ContactPhoneEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "home fax",
                PermissibleValue(text="home fax") )
        setattr(cls, "work fax",
                PermissibleValue(text="work fax") )

class ContactSIPScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactSIPScopeEnum",
    )

class ContactURLScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    homepage = PermissibleValue(text="homepage")

    _defn = EnumDefinition(
        name="ContactURLScopeEnum",
    )

class DiskTypeEnum(EnumDefinitionImpl):

    CDRom = PermissibleValue(text="CDRom")
    Fixed = PermissibleValue(text="Fixed")
    RAMDisk = PermissibleValue(text="RAMDisk")
    Remote = PermissibleValue(text="Remote")
    Removable = PermissibleValue(text="Removable")

    _defn = EnumDefinition(
        name="DiskTypeEnum",
    )

class EndiannessTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EndiannessTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Big-endian",
                PermissibleValue(text="Big-endian") )
        setattr(cls, "Little-endian",
                PermissibleValue(text="Little-endian") )
        setattr(cls, "Middle-endian",
                PermissibleValue(text="Middle-endian") )

class HashNameEnum(EnumDefinitionImpl):

    MD5 = PermissibleValue(text="MD5")
    MD6 = PermissibleValue(text="MD6")
    SHA1 = PermissibleValue(text="SHA1")
    SHA224 = PermissibleValue(text="SHA224")
    SHA256 = PermissibleValue(text="SHA256")
    SHA384 = PermissibleValue(text="SHA384")
    SHA512 = PermissibleValue(text="SHA512")
    SSDEEP = PermissibleValue(text="SSDEEP")

    _defn = EnumDefinition(
        name="HashNameEnum",
    )

class LibraryTypeEnum(EnumDefinitionImpl):

    Dynamic = PermissibleValue(text="Dynamic")
    Other = PermissibleValue(text="Other")
    Remote = PermissibleValue(text="Remote")
    Shared = PermissibleValue(text="Shared")
    Static = PermissibleValue(text="Static")

    _defn = EnumDefinition(
        name="LibraryTypeEnum",
    )

class MemoryBlockTypeEnum(EnumDefinitionImpl):

    Initialized = PermissibleValue(text="Initialized")
    Overlay = PermissibleValue(text="Overlay")
    Uninitialized = PermissibleValue(text="Uninitialized")

    _defn = EnumDefinition(
        name="MemoryBlockTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bit-mapped",
                PermissibleValue(text="Bit-mapped") )
        setattr(cls, "Byte-mapped",
                PermissibleValue(text="Byte-mapped") )

class ObservableObjectRelationshipEnum(EnumDefinitionImpl):

    Allocated = PermissibleValue(text="Allocated")
    Allocated_By = PermissibleValue(text="Allocated_By")
    Attachment_Of = PermissibleValue(text="Attachment_Of")
    Bound = PermissibleValue(text="Bound")
    Bound_By = PermissibleValue(text="Bound_By")
    Characterized_By = PermissibleValue(text="Characterized_By")
    Characterizes = PermissibleValue(text="Characterizes")
    Child_Of = PermissibleValue(text="Child_Of")
    Closed = PermissibleValue(text="Closed")
    Closed_By = PermissibleValue(text="Closed_By")
    Compressed = PermissibleValue(text="Compressed")
    Compressed_By = PermissibleValue(text="Compressed_By")
    Compressed_From = PermissibleValue(text="Compressed_From")
    Compressed_Into = PermissibleValue(text="Compressed_Into")
    Connected_From = PermissibleValue(text="Connected_From")
    Connected_To = PermissibleValue(text="Connected_To")
    Contained_Within = PermissibleValue(text="Contained_Within")
    Contains = PermissibleValue(text="Contains")
    Copied = PermissibleValue(text="Copied")
    Copied_By = PermissibleValue(text="Copied_By")
    Copied_From = PermissibleValue(text="Copied_From")
    Copied_To = PermissibleValue(text="Copied_To")
    Created = PermissibleValue(text="Created")
    Created_By = PermissibleValue(text="Created_By")
    Decoded = PermissibleValue(text="Decoded")
    Decoded_By = PermissibleValue(text="Decoded_By")
    Decompressed = PermissibleValue(text="Decompressed")
    Decompressed_By = PermissibleValue(text="Decompressed_By")
    Decrypted = PermissibleValue(text="Decrypted")
    Decrypted_By = PermissibleValue(text="Decrypted_By")
    Deleted = PermissibleValue(text="Deleted")
    Deleted_By = PermissibleValue(text="Deleted_By")
    Deleted_From = PermissibleValue(text="Deleted_From")
    Downloaded = PermissibleValue(text="Downloaded")
    Downloaded_By = PermissibleValue(text="Downloaded_By")
    Downloaded_From = PermissibleValue(text="Downloaded_From")
    Downloaded_To = PermissibleValue(text="Downloaded_To")
    Dropped = PermissibleValue(text="Dropped")
    Dropped_By = PermissibleValue(text="Dropped_By")
    Encoded = PermissibleValue(text="Encoded")
    Encoded_By = PermissibleValue(text="Encoded_By")
    Encrypted = PermissibleValue(text="Encrypted")
    Encrypted_By = PermissibleValue(text="Encrypted_By")
    Encrypted_From = PermissibleValue(text="Encrypted_From")
    Encrypted_To = PermissibleValue(text="Encrypted_To")
    Extracted_From = PermissibleValue(text="Extracted_From")
    FQDN_Of = PermissibleValue(text="FQDN_Of")
    Freed = PermissibleValue(text="Freed")
    Freed_By = PermissibleValue(text="Freed_By")
    Had_Attachment = PermissibleValue(text="Had_Attachment")
    Hooked = PermissibleValue(text="Hooked")
    Hooked_By = PermissibleValue(text="Hooked_By")
    Initialized_By = PermissibleValue(text="Initialized_By")
    Initialized_To = PermissibleValue(text="Initialized_To")
    Injected = PermissibleValue(text="Injected")
    Injected_As = PermissibleValue(text="Injected_As")
    Injected_By = PermissibleValue(text="Injected_By")
    Injected_Into = PermissibleValue(text="Injected_Into")
    Installed = PermissibleValue(text="Installed")
    Installed_By = PermissibleValue(text="Installed_By")
    Joined = PermissibleValue(text="Joined")
    Joined_By = PermissibleValue(text="Joined_By")
    Killed = PermissibleValue(text="Killed")
    Killed_By = PermissibleValue(text="Killed_By")
    Listened_On = PermissibleValue(text="Listened_On")
    Listened_On_By = PermissibleValue(text="Listened_On_By")
    Loaded_From = PermissibleValue(text="Loaded_From")
    Loaded_Into = PermissibleValue(text="Loaded_Into")
    Locked = PermissibleValue(text="Locked")
    Locked_By = PermissibleValue(text="Locked_By")
    Mapped_By = PermissibleValue(text="Mapped_By")
    Mapped_Into = PermissibleValue(text="Mapped_Into")
    Merged = PermissibleValue(text="Merged")
    Merged_By = PermissibleValue(text="Merged_By")
    Modified_Properties_Of = PermissibleValue(text="Modified_Properties_Of")
    Monitored = PermissibleValue(text="Monitored")
    Monitored_By = PermissibleValue(text="Monitored_By")
    Moved = PermissibleValue(text="Moved")
    Moved_By = PermissibleValue(text="Moved_By")
    Moved_From = PermissibleValue(text="Moved_From")
    Moved_To = PermissibleValue(text="Moved_To")
    Opened = PermissibleValue(text="Opened")
    Opened_By = PermissibleValue(text="Opened_By")
    Packed = PermissibleValue(text="Packed")
    Packed_By = PermissibleValue(text="Packed_By")
    Packed_From = PermissibleValue(text="Packed_From")
    Packed_Into = PermissibleValue(text="Packed_Into")
    Parent_Of = PermissibleValue(text="Parent_Of")
    Paused = PermissibleValue(text="Paused")
    Paused_By = PermissibleValue(text="Paused_By")
    Previously_Contained = PermissibleValue(text="Previously_Contained")
    Properties_Modified_By = PermissibleValue(text="Properties_Modified_By")
    Properties_Queried = PermissibleValue(text="Properties_Queried")
    Properties_Queried_By = PermissibleValue(text="Properties_Queried_By")
    Read_From = PermissibleValue(text="Read_From")
    Read_From_By = PermissibleValue(text="Read_From_By")
    Received = PermissibleValue(text="Received")
    Received_By = PermissibleValue(text="Received_By")
    Received_From = PermissibleValue(text="Received_From")
    Received_Via_Upload = PermissibleValue(text="Received_Via_Upload")
    Redirects_To = PermissibleValue(text="Redirects_To")
    Related_To = PermissibleValue(text="Related_To")
    Renamed = PermissibleValue(text="Renamed")
    Renamed_By = PermissibleValue(text="Renamed_By")
    Renamed_From = PermissibleValue(text="Renamed_From")
    Renamed_To = PermissibleValue(text="Renamed_To")
    Resolved_To = PermissibleValue(text="Resolved_To")
    Resumed = PermissibleValue(text="Resumed")
    Resumed_By = PermissibleValue(text="Resumed_By")
    Root_Domain_Of = PermissibleValue(text="Root_Domain_Of")
    Searched_For = PermissibleValue(text="Searched_For")
    Searched_For_By = PermissibleValue(text="Searched_For_By")
    Sent = PermissibleValue(text="Sent")
    Sent_By = PermissibleValue(text="Sent_By")
    Sent_To = PermissibleValue(text="Sent_To")
    Sent_Via_Upload = PermissibleValue(text="Sent_Via_Upload")
    Set_From = PermissibleValue(text="Set_From")
    Set_To = PermissibleValue(text="Set_To")
    Suspended = PermissibleValue(text="Suspended")
    Suspended_By = PermissibleValue(text="Suspended_By")
    Unhooked = PermissibleValue(text="Unhooked")
    Unhooked_By = PermissibleValue(text="Unhooked_By")
    Unlocked = PermissibleValue(text="Unlocked")
    Unlocked_By = PermissibleValue(text="Unlocked_By")
    Unpacked = PermissibleValue(text="Unpacked")
    Unpacked_By = PermissibleValue(text="Unpacked_By")
    Uploaded = PermissibleValue(text="Uploaded")
    Uploaded_By = PermissibleValue(text="Uploaded_By")
    Uploaded_From = PermissibleValue(text="Uploaded_From")
    Uploaded_To = PermissibleValue(text="Uploaded_To")
    Used = PermissibleValue(text="Used")
    Used_By = PermissibleValue(text="Used_By")
    Values_Enumerated = PermissibleValue(text="Values_Enumerated")
    Values_Enumerated_By = PermissibleValue(text="Values_Enumerated_By")
    Written_To_By = PermissibleValue(text="Written_To_By")
    Wrote_To = PermissibleValue(text="Wrote_To")

    _defn = EnumDefinition(
        name="ObservableObjectRelationshipEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Sub-domain_Of",
                PermissibleValue(text="Sub-domain_Of") )
        setattr(cls, "Supra-domain_Of",
                PermissibleValue(text="Supra-domain_Of") )

class ObservableObjectStateEnum(EnumDefinitionImpl):

    Active = PermissibleValue(text="Active")
    Closed = PermissibleValue(text="Closed")
    Exists = PermissibleValue(text="Exists")
    Inactive = PermissibleValue(text="Inactive")
    Locked = PermissibleValue(text="Locked")
    Open = PermissibleValue(text="Open")
    Started = PermissibleValue(text="Started")
    Stopped = PermissibleValue(text="Stopped")
    Unlocked = PermissibleValue(text="Unlocked")

    _defn = EnumDefinition(
        name="ObservableObjectStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Does Not Exist",
                PermissibleValue(text="Does Not Exist") )

class PartitionTypeEnum(EnumDefinitionImpl):

    PARTITION_ENTRY_UNUSED = PermissibleValue(text="PARTITION_ENTRY_UNUSED")
    PARTITION_EXTENDED = PermissibleValue(text="PARTITION_EXTENDED")
    PARTITION_FAT32 = PermissibleValue(text="PARTITION_FAT32")
    PARTITION_FAT32_XINT13 = PermissibleValue(text="PARTITION_FAT32_XINT13")
    PARTITION_FAT_12 = PermissibleValue(text="PARTITION_FAT_12")
    PARTITION_FAT_16 = PermissibleValue(text="PARTITION_FAT_16")
    PARTITION_HUGE = PermissibleValue(text="PARTITION_HUGE")
    PARTITION_IFS = PermissibleValue(text="PARTITION_IFS")
    PARTITION_LDM = PermissibleValue(text="PARTITION_LDM")
    PARTITION_NTFT = PermissibleValue(text="PARTITION_NTFT")
    PARTITION_OS2BOOTMGR = PermissibleValue(text="PARTITION_OS2BOOTMGR")
    PARTITION_PREP = PermissibleValue(text="PARTITION_PREP")
    PARTITION_UNIX = PermissibleValue(text="PARTITION_UNIX")
    PARTITION_XENIX_1 = PermissibleValue(text="PARTITION_XENIX_1")
    PARTITION_XENIX_2 = PermissibleValue(text="PARTITION_XENIX_2")
    PARTITION_XINT13 = PermissibleValue(text="PARTITION_XINT13")
    PARTITION_XINT13_EXTENDED = PermissibleValue(text="PARTITION_XINT13_EXTENDED")
    UNKNOWN = PermissibleValue(text="UNKNOWN")
    VALID_NTFT = PermissibleValue(text="VALID_NTFT")

    _defn = EnumDefinition(
        name="PartitionTypeEnum",
    )

class ProcessorArchEnum(EnumDefinitionImpl):

    ARM = PermissibleValue(text="ARM")
    Alpha = PermissibleValue(text="Alpha")
    MIPS = PermissibleValue(text="MIPS")
    Other = PermissibleValue(text="Other")
    PowerPC = PermissibleValue(text="PowerPC")
    SPARC = PermissibleValue(text="SPARC")

    _defn = EnumDefinition(
        name="ProcessorArchEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "IA-64",
                PermissibleValue(text="IA-64") )
        setattr(cls, "Motorola 68k",
                PermissibleValue(text="Motorola 68k") )
        setattr(cls, "eSi-RISC",
                PermissibleValue(text="eSi-RISC") )
        setattr(cls, "x86-32",
                PermissibleValue(text="x86-32") )
        setattr(cls, "x86-64",
                PermissibleValue(text="x86-64") )
        setattr(cls, "z/Architecture",
                PermissibleValue(text="z/Architecture") )

class RecoveredObjectStatusEnum(EnumDefinitionImpl):

    recovered = PermissibleValue(text="recovered")
    overwritten = PermissibleValue(text="overwritten")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="RecoveredObjectStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "partially recovered",
                PermissibleValue(text="partially recovered") )

class RegionalRegistryTypeEnum(EnumDefinitionImpl):

    APNIC = PermissibleValue(text="APNIC")
    ARIN = PermissibleValue(text="ARIN")
    AfriNIC = PermissibleValue(text="AfriNIC")
    LACNIC = PermissibleValue(text="LACNIC")

    _defn = EnumDefinition(
        name="RegionalRegistryTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RIPE NCC",
                PermissibleValue(text="RIPE NCC") )

class RegistryDatatypeEnum(EnumDefinitionImpl):
    """
    "From https //learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types, https
    //learn.microsoft.com/en-us/windows/win32/shell/hkey-type"
    """
    reg_binary = PermissibleValue(text="reg_binary",
                                           description=""Binary data in any form."")
    reg_dword = PermissibleValue(text="reg_dword",
                                         description=""A 32-bit number."")
    reg_dword_big_endian = PermissibleValue(text="reg_dword_big_endian",
                                                               description=""A 32-bit number in big-endian format. Some UNIX systems support big-endian architectures."")
    reg_expand_sz = PermissibleValue(text="reg_expand_sz",
                                                 description=""A null-terminated string that contains unexpanded references to environment Variables (for example, '%PATH%'). It will be a Unicode or ANSI string depending on wh ether you use the Unicode or ANSI functions. To expand the environment variable refere nces, use the ExpandEnvironmentStrings function."")
    reg_full_resource_descriptor = PermissibleValue(text="reg_full_resource_descriptor",
                                                                               description=""A list of hardware resources that a physical device is using, detected and written into the \HardwareDescription tree by the system."")
    reg_invalid_type = PermissibleValue(text="reg_invalid_type",
                                                       description=""Specifies an invalid key."")
    reg_link = PermissibleValue(text="reg_link",
                                       description=""A null-terminated Unicode string that contains the target path of a symboli c link that was created by calling the RegCreateKeyEx function with REG_OPTION_CREATE_ LINK."")
    reg_multi_sz = PermissibleValue(text="reg_multi_sz",
                                               description=""A sequence of null-terminated strings, terminated by an empty string (\0). The following is an example: String1\0String2\0String3\0LastString\0\0 The first \0 terminates the first string, the second to the last \0 terminates the last string, and the final \0 terminates the sequence. Note that the final terminator must be factored into the length of the string."")
    reg_none = PermissibleValue(text="reg_none",
                                       description=""No defined value type."")
    reg_qword = PermissibleValue(text="reg_qword",
                                         description=""A 64-bit number."")
    reg_resource_list = PermissibleValue(text="reg_resource_list",
                                                         description=""Device-driver resource list."")
    reg_resource_requirements_list = PermissibleValue(text="reg_resource_requirements_list",
                                                                                   description=""A device driver's list of possible hardware resources it or one of the physical devices it controls can use, from which the system writes a subset into the \ResourceMap tree"")
    reg_sz = PermissibleValue(text="reg_sz",
                                   description=""A null-terminated string. This will be either a Unicode or an ANSI string, depending on whether you use the Unicode or ANSI functions."")

    _defn = EnumDefinition(
        name="RegistryDatatypeEnum",
        description="\"From https //learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types, https //learn.microsoft.com/en-us/windows/win32/shell/hkey-type\"",
    )

class SIMFormEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SIMFormEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Full-size SIM",
                PermissibleValue(text="Full-size SIM") )
        setattr(cls, "Micro SIM",
                PermissibleValue(text="Micro SIM") )
        setattr(cls, "Nano SIM",
                PermissibleValue(text="Nano SIM") )

class SIMTypeEnum(EnumDefinitionImpl):

    SIM = PermissibleValue(text="SIM")
    UICC = PermissibleValue(text="UICC")
    USIM = PermissibleValue(text="USIM")

    _defn = EnumDefinition(
        name="SIMTypeEnum",
    )

class TaskActionTypeEnum(EnumDefinitionImpl):

    TASK_ACTION_COM_HANDLER = PermissibleValue(text="TASK_ACTION_COM_HANDLER")
    TASK_ACTION_EXEC = PermissibleValue(text="TASK_ACTION_EXEC")
    TASK_ACTION_SEND_EMAIL = PermissibleValue(text="TASK_ACTION_SEND_EMAIL")
    TASK_ACTION_SHOW_MESSAGE = PermissibleValue(text="TASK_ACTION_SHOW_MESSAGE")

    _defn = EnumDefinition(
        name="TaskActionTypeEnum",
    )

class TaskFlagEnum(EnumDefinitionImpl):

    TASK_FLAG_DELETE_WHEN_DONE = PermissibleValue(text="TASK_FLAG_DELETE_WHEN_DONE")
    TASK_FLAG_DISABLED = PermissibleValue(text="TASK_FLAG_DISABLED")
    TASK_FLAG_DONT_START_IF_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_DONT_START_IF_ON_BATTERIES")
    TASK_FLAG_HIDDEN = PermissibleValue(text="TASK_FLAG_HIDDEN")
    TASK_FLAG_INTERACTIVE = PermissibleValue(text="TASK_FLAG_INTERACTIVE")
    TASK_FLAG_KILL_IF_GOING_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_KILL_IF_GOING_ON_BATTERIES")
    TASK_FLAG_KILL_ON_IDLE_END = PermissibleValue(text="TASK_FLAG_KILL_ON_IDLE_END")
    TASK_FLAG_RESTART_ON_IDLE_RESUME = PermissibleValue(text="TASK_FLAG_RESTART_ON_IDLE_RESUME")
    TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET = PermissibleValue(text="TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET")
    TASK_FLAG_RUN_ONLY_IF_LOGGED_ON = PermissibleValue(text="TASK_FLAG_RUN_ONLY_IF_LOGGED_ON")
    TASK_FLAG_START_ONLY_IF_IDLE = PermissibleValue(text="TASK_FLAG_START_ONLY_IF_IDLE")
    TASK_FLAG_SYSTEM_REQUIRED = PermissibleValue(text="TASK_FLAG_SYSTEM_REQUIRED")
    TASK_FLAG_ZERO = PermissibleValue(text="TASK_FLAG_ZERO")

    _defn = EnumDefinition(
        name="TaskFlagEnum",
    )

class TaskPriorityEnum(EnumDefinitionImpl):

    ABOVE_NORMAL_PRIORITY_CLASS = PermissibleValue(text="ABOVE_NORMAL_PRIORITY_CLASS")
    BELOW_NORMAL_PRIORITY_CLASS = PermissibleValue(text="BELOW_NORMAL_PRIORITY_CLASS")
    HIGH_PRIORITY_CLASS = PermissibleValue(text="HIGH_PRIORITY_CLASS")
    IDLE_PRIORITY_CLASS = PermissibleValue(text="IDLE_PRIORITY_CLASS")
    NORMAL_PRIORITY_CLASS = PermissibleValue(text="NORMAL_PRIORITY_CLASS")
    REALTIME_PRIORITY_CLASS = PermissibleValue(text="REALTIME_PRIORITY_CLASS")

    _defn = EnumDefinition(
        name="TaskPriorityEnum",
    )

class TaskStatusEnum(EnumDefinitionImpl):

    SCHED_E_ACCOUNT_DBASE_CORRUPT = PermissibleValue(text="SCHED_E_ACCOUNT_DBASE_CORRUPT")
    SCHED_E_ACCOUNT_INFORMATION_NOT_SET = PermissibleValue(text="SCHED_E_ACCOUNT_INFORMATION_NOT_SET")
    SCHED_E_ACCOUNT_NAME_NOT_FOUND = PermissibleValue(text="SCHED_E_ACCOUNT_NAME_NOT_FOUND")
    SCHED_E_CANNOT_OPEN_TASK = PermissibleValue(text="SCHED_E_CANNOT_OPEN_TASK")
    SCHED_E_INVALID_TASK = PermissibleValue(text="SCHED_E_INVALID_TASK")
    SCHED_E_NO_SECURITY_SERVICES = PermissibleValue(text="SCHED_E_NO_SECURITY_SERVICES")
    SCHED_E_SERVICE_NOT_INSTALLED = PermissibleValue(text="SCHED_E_SERVICE_NOT_INSTALLED")
    SCHED_E_SERVICE_NOT_RUNNING = PermissibleValue(text="SCHED_E_SERVICE_NOT_RUNNING")
    SCHED_E_TASK_NOT_READY = PermissibleValue(text="SCHED_E_TASK_NOT_READY")
    SCHED_E_TASK_NOT_RUNNING = PermissibleValue(text="SCHED_E_TASK_NOT_RUNNING")
    SCHED_E_TRIGGER_NOT_FOUND = PermissibleValue(text="SCHED_E_TRIGGER_NOT_FOUND")
    SCHED_E_UNKNOWN_OBJECT_VERSION = PermissibleValue(text="SCHED_E_UNKNOWN_OBJECT_VERSION")
    SCHED_E_UNSUPPORTED_ACCOUNT_OPTION = PermissibleValue(text="SCHED_E_UNSUPPORTED_ACCOUNT_OPTION")
    SCHED_S_EVENT_TRIGGER = PermissibleValue(text="SCHED_S_EVENT_TRIGGER")
    SCHED_S_TASK_DISABLED = PermissibleValue(text="SCHED_S_TASK_DISABLED")
    SCHED_S_TASK_HAS_NOT_RUN = PermissibleValue(text="SCHED_S_TASK_HAS_NOT_RUN")
    SCHED_S_TASK_NOT_SCHEDULED = PermissibleValue(text="SCHED_S_TASK_NOT_SCHEDULED")
    SCHED_S_TASK_NO_MORE_RUNS = PermissibleValue(text="SCHED_S_TASK_NO_MORE_RUNS")
    SCHED_S_TASK_NO_VALID_TRIGGERS = PermissibleValue(text="SCHED_S_TASK_NO_VALID_TRIGGERS")
    SCHED_S_TASK_READY = PermissibleValue(text="SCHED_S_TASK_READY")
    SCHED_S_TASK_RUNNING = PermissibleValue(text="SCHED_S_TASK_RUNNING")
    SCHED_S_TASK_TERMINATED = PermissibleValue(text="SCHED_S_TASK_TERMINATED")
    TASK_STATE_QUEUED = PermissibleValue(text="TASK_STATE_QUEUED")
    TASK_STATE_UNKNOWN = PermissibleValue(text="TASK_STATE_UNKNOWN")

    _defn = EnumDefinition(
        name="TaskStatusEnum",
    )

class ThreadRunningStatusEnum(EnumDefinitionImpl):

    Initialized = PermissibleValue(text="Initialized")
    Ready = PermissibleValue(text="Ready")
    Running = PermissibleValue(text="Running")
    Standby = PermissibleValue(text="Standby")
    Terminated = PermissibleValue(text="Terminated")
    Transition = PermissibleValue(text="Transition")
    Unknown = PermissibleValue(text="Unknown")
    Waiting = PermissibleValue(text="Waiting")

    _defn = EnumDefinition(
        name="ThreadRunningStatusEnum",
    )

class TimestampPrecisionEnum(EnumDefinitionImpl):

    day = PermissibleValue(text="day")
    hour = PermissibleValue(text="hour")
    minute = PermissibleValue(text="minute")
    month = PermissibleValue(text="month")
    second = PermissibleValue(text="second")
    year = PermissibleValue(text="year")

    _defn = EnumDefinition(
        name="TimestampPrecisionEnum",
    )

class TrendEnum(EnumDefinitionImpl):

    Decreasing = PermissibleValue(text="Decreasing")
    Increasing = PermissibleValue(text="Increasing")

    _defn = EnumDefinition(
        name="TrendEnum",
    )

class TriggerFrequencyEnum(EnumDefinitionImpl):

    TASK_EVENT_TRIGGER_AT_LOGON = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_LOGON")
    TASK_EVENT_TRIGGER_AT_SYSTEMSTART = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_SYSTEMSTART")
    TASK_EVENT_TRIGGER_ON_IDLE = PermissibleValue(text="TASK_EVENT_TRIGGER_ON_IDLE")
    TASK_TIME_TRIGGER_DAILY = PermissibleValue(text="TASK_TIME_TRIGGER_DAILY")
    TASK_TIME_TRIGGER_MONTHLYDATE = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDATE")
    TASK_TIME_TRIGGER_MONTHLYDOW = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDOW")
    TASK_TIME_TRIGGER_ONCE = PermissibleValue(text="TASK_TIME_TRIGGER_ONCE")
    TASK_TIME_TRIGGER_WEEKLY = PermissibleValue(text="TASK_TIME_TRIGGER_WEEKLY")

    _defn = EnumDefinition(
        name="TriggerFrequencyEnum",
    )

class TriggerTypeEnum(EnumDefinitionImpl):

    TASK_TRIGGER_BOOT = PermissibleValue(text="TASK_TRIGGER_BOOT")
    TASK_TRIGGER_EVENT = PermissibleValue(text="TASK_TRIGGER_EVENT")
    TASK_TRIGGER_IDLE = PermissibleValue(text="TASK_TRIGGER_IDLE")
    TASK_TRIGGER_LOGON = PermissibleValue(text="TASK_TRIGGER_LOGON")
    TASK_TRIGGER_REGISTRATION = PermissibleValue(text="TASK_TRIGGER_REGISTRATION")
    TASK_TRIGGER_SESSION_STATE_CHANGE = PermissibleValue(text="TASK_TRIGGER_SESSION_STATE_CHANGE")
    TASK_TRIGGER_TIME = PermissibleValue(text="TASK_TRIGGER_TIME")

    _defn = EnumDefinition(
        name="TriggerTypeEnum",
    )

class URLTransitionTypeEnum(EnumDefinitionImpl):

    link = PermissibleValue(text="link")
    typed = PermissibleValue(text="typed")
    auto_bookmark = PermissibleValue(text="auto_bookmark")
    auto_subframe = PermissibleValue(text="auto_subframe")
    manual_subframe = PermissibleValue(text="manual_subframe")
    generated = PermissibleValue(text="generated")
    auto_toplevel = PermissibleValue(text="auto_toplevel")
    form_submit = PermissibleValue(text="form_submit")
    reload = PermissibleValue(text="reload")
    keyword = PermissibleValue(text="keyword")
    keyword_generated = PermissibleValue(text="keyword_generated")

    _defn = EnumDefinition(
        name="URLTransitionTypeEnum",
    )

class UnixProcessStateEnum(EnumDefinitionImpl):

    Dead = PermissibleValue(text="Dead")
    InterruptibleSleep = PermissibleValue(text="InterruptibleSleep")
    Paging = PermissibleValue(text="Paging")
    Running = PermissibleValue(text="Running")
    Stopped = PermissibleValue(text="Stopped")
    UninterruptibleSleep = PermissibleValue(text="UninterruptibleSleep")
    Zombie = PermissibleValue(text="Zombie")

    _defn = EnumDefinition(
        name="UnixProcessStateEnum",
    )

class WhoisContactTypeEnum(EnumDefinitionImpl):

    ADMIN = PermissibleValue(text="ADMIN")
    BILLING = PermissibleValue(text="BILLING")
    TECHNICAL = PermissibleValue(text="TECHNICAL")

    _defn = EnumDefinition(
        name="WhoisContactTypeEnum",
    )

class WhoisDNSSECTypeEnum(EnumDefinitionImpl):

    Signed = PermissibleValue(text="Signed")
    Unsigned = PermissibleValue(text="Unsigned")

    _defn = EnumDefinition(
        name="WhoisDNSSECTypeEnum",
    )

class WhoisStatusTypeEnum(EnumDefinitionImpl):

    ADD_PERIOD = PermissibleValue(text="ADD_PERIOD")
    AUTO_RENEW_PERIOD = PermissibleValue(text="AUTO_RENEW_PERIOD")
    CLIENT_DELETE_PROHIBITED = PermissibleValue(text="CLIENT_DELETE_PROHIBITED")
    CLIENT_HOLD = PermissibleValue(text="CLIENT_HOLD")
    CLIENT_RENEW_PROHIBITED = PermissibleValue(text="CLIENT_RENEW_PROHIBITED")
    CLIENT_TRANSFER_PROHIBITED = PermissibleValue(text="CLIENT_TRANSFER_PROHIBITED")
    CLIENT_UPDATE_PROHIBITED = PermissibleValue(text="CLIENT_UPDATE_PROHIBITED")
    DELETE_PROHIBITED = PermissibleValue(text="DELETE_PROHIBITED")
    HOLD = PermissibleValue(text="HOLD")
    INACTIVE = PermissibleValue(text="INACTIVE")
    OK = PermissibleValue(text="OK")
    PENDING_DELETE_RESTORABLE = PermissibleValue(text="PENDING_DELETE_RESTORABLE")
    PENDING_DELETE_SCHEDULED_FOR_RELEASE = PermissibleValue(text="PENDING_DELETE_SCHEDULED_FOR_RELEASE")
    PENDING_RESTORE = PermissibleValue(text="PENDING_RESTORE")
    RENEW_PERIOD = PermissibleValue(text="RENEW_PERIOD")
    RENEW_PROHIBITED = PermissibleValue(text="RENEW_PROHIBITED")
    TRANSFER_PERIOD = PermissibleValue(text="TRANSFER_PERIOD")
    TRANSFER_PROHIBITED = PermissibleValue(text="TRANSFER_PROHIBITED")
    UPDATE_PROHIBITED = PermissibleValue(text="UPDATE_PROHIBITED")

    _defn = EnumDefinition(
        name="WhoisStatusTypeEnum",
    )

class WindowsDriveTypeEnum(EnumDefinitionImpl):

    DRIVE_CDROM = PermissibleValue(text="DRIVE_CDROM")
    DRIVE_FIXED = PermissibleValue(text="DRIVE_FIXED")
    DRIVE_NO_ROOT_DIR = PermissibleValue(text="DRIVE_NO_ROOT_DIR")
    DRIVE_RAMDISK = PermissibleValue(text="DRIVE_RAMDISK")
    DRIVE_REMOTE = PermissibleValue(text="DRIVE_REMOTE")
    DRIVE_REMOVABLE = PermissibleValue(text="DRIVE_REMOVABLE")
    DRIVE_UNKNOWN = PermissibleValue(text="DRIVE_UNKNOWN")

    _defn = EnumDefinition(
        name="WindowsDriveTypeEnum",
    )

class WindowsVolumeAttributeEnum(EnumDefinitionImpl):

    Hidden = PermissibleValue(text="Hidden")
    NoDefaultDriveLetter = PermissibleValue(text="NoDefaultDriveLetter")
    ReadOnly = PermissibleValue(text="ReadOnly")
    ShadowCopy = PermissibleValue(text="ShadowCopy")

    _defn = EnumDefinition(
        name="WindowsVolumeAttributeEnum",
    )

class WirelessNetworkSecurityModeEnum(EnumDefinitionImpl):

    WEP = PermissibleValue(text="WEP")
    WPA = PermissibleValue(text="WPA")

    _defn = EnumDefinition(
        name="WirelessNetworkSecurityModeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
                PermissibleValue(text="None") )
        setattr(cls, "WPA2-PSK",
                PermissibleValue(text="WPA2-PSK") )
        setattr(cls, "WPA2-Enterprise",
                PermissibleValue(text="WPA2-Enterprise") )
        setattr(cls, "WPA3-PSK",
                PermissibleValue(text="WPA3-PSK") )
        setattr(cls, "WPA3-Enterprise",
                PermissibleValue(text="WPA3-Enterprise") )

# Slots
class slots:
    pass

slots.AccountTypeVocab = Slot(uri=VOCABULARY.AccountTypeVocab, name="AccountTypeVocab", curie=VOCABULARY.curie('AccountTypeVocab'),
                   model_uri=VOCABULARY.AccountTypeVocab, domain=None, range=Optional[Union[str, "AccountTypeEnum"]])

slots.ActionArgumentNameVocab = Slot(uri=VOCABULARY.ActionArgumentNameVocab, name="ActionArgumentNameVocab", curie=VOCABULARY.curie('ActionArgumentNameVocab'),
                   model_uri=VOCABULARY.ActionArgumentNameVocab, domain=None, range=Optional[Union[str, "ActionArgumentNameEnum"]])

slots.ActionNameVocab = Slot(uri=VOCABULARY.ActionNameVocab, name="ActionNameVocab", curie=VOCABULARY.curie('ActionNameVocab'),
                   model_uri=VOCABULARY.ActionNameVocab, domain=None, range=Optional[str])

slots.ActionRelationshipTypeVocab = Slot(uri=VOCABULARY.ActionRelationshipTypeVocab, name="ActionRelationshipTypeVocab", curie=VOCABULARY.curie('ActionRelationshipTypeVocab'),
                   model_uri=VOCABULARY.ActionRelationshipTypeVocab, domain=None, range=Optional[Union[str, "ActionRelationshipTypeEnum"]])

slots.ActionStatusTypeVocab = Slot(uri=VOCABULARY.ActionStatusTypeVocab, name="ActionStatusTypeVocab", curie=VOCABULARY.curie('ActionStatusTypeVocab'),
                   model_uri=VOCABULARY.ActionStatusTypeVocab, domain=None, range=Optional[Union[str, "ActionStatusTypeEnum"]])

slots.ActionTypeVocab = Slot(uri=VOCABULARY.ActionTypeVocab, name="ActionTypeVocab", curie=VOCABULARY.curie('ActionTypeVocab'),
                   model_uri=VOCABULARY.ActionTypeVocab, domain=None, range=Optional[Union[str, "ActionTypeEnum"]])

slots.BitnessVocab = Slot(uri=VOCABULARY.BitnessVocab, name="BitnessVocab", curie=VOCABULARY.curie('BitnessVocab'),
                   model_uri=VOCABULARY.BitnessVocab, domain=None, range=Optional[Union[str, "BitnessEnum"]])

slots.CharacterEncodingVocab = Slot(uri=VOCABULARY.CharacterEncodingVocab, name="CharacterEncodingVocab", curie=VOCABULARY.curie('CharacterEncodingVocab'),
                   model_uri=VOCABULARY.CharacterEncodingVocab, domain=None, range=Optional[Union[str, "CharacterEncodingEnum"]])

slots.ContactAddressScopeVocab = Slot(uri=VOCABULARY.ContactAddressScopeVocab, name="ContactAddressScopeVocab", curie=VOCABULARY.curie('ContactAddressScopeVocab'),
                   model_uri=VOCABULARY.ContactAddressScopeVocab, domain=None, range=Optional[Union[str, "ContactAddressScopeEnum"]])

slots.ContactEmailScopeVocab = Slot(uri=VOCABULARY.ContactEmailScopeVocab, name="ContactEmailScopeVocab", curie=VOCABULARY.curie('ContactEmailScopeVocab'),
                   model_uri=VOCABULARY.ContactEmailScopeVocab, domain=None, range=Optional[Union[str, "ContactEmailScopeEnum"]])

slots.ContactPhoneScopeVocab = Slot(uri=VOCABULARY.ContactPhoneScopeVocab, name="ContactPhoneScopeVocab", curie=VOCABULARY.curie('ContactPhoneScopeVocab'),
                   model_uri=VOCABULARY.ContactPhoneScopeVocab, domain=None, range=Optional[Union[str, "ContactPhoneEnum"]])

slots.ContactSIPScopeVocab = Slot(uri=VOCABULARY.ContactSIPScopeVocab, name="ContactSIPScopeVocab", curie=VOCABULARY.curie('ContactSIPScopeVocab'),
                   model_uri=VOCABULARY.ContactSIPScopeVocab, domain=None, range=Optional[Union[str, "ContactSIPScopeEnum"]])

slots.ContactURLScopeVocab = Slot(uri=VOCABULARY.ContactURLScopeVocab, name="ContactURLScopeVocab", curie=VOCABULARY.curie('ContactURLScopeVocab'),
                   model_uri=VOCABULARY.ContactURLScopeVocab, domain=None, range=Optional[Union[str, "ContactURLScopeEnum"]])

slots.DiskTypeVocab = Slot(uri=VOCABULARY.DiskTypeVocab, name="DiskTypeVocab", curie=VOCABULARY.curie('DiskTypeVocab'),
                   model_uri=VOCABULARY.DiskTypeVocab, domain=None, range=Optional[Union[str, "DiskTypeEnum"]])

slots.EndiannessTypeVocab = Slot(uri=VOCABULARY.EndiannessTypeVocab, name="EndiannessTypeVocab", curie=VOCABULARY.curie('EndiannessTypeVocab'),
                   model_uri=VOCABULARY.EndiannessTypeVocab, domain=None, range=Optional[Union[str, "EndiannessTypeEnum"]])

slots.HashNameVocab = Slot(uri=VOCABULARY.HashNameVocab, name="HashNameVocab", curie=VOCABULARY.curie('HashNameVocab'),
                   model_uri=VOCABULARY.HashNameVocab, domain=None, range=Optional[Union[str, "HashNameEnum"]])

slots.LibraryTypeVocab = Slot(uri=VOCABULARY.LibraryTypeVocab, name="LibraryTypeVocab", curie=VOCABULARY.curie('LibraryTypeVocab'),
                   model_uri=VOCABULARY.LibraryTypeVocab, domain=None, range=Optional[Union[str, "LibraryTypeEnum"]])

slots.MemoryBlockTypeVocab = Slot(uri=VOCABULARY.MemoryBlockTypeVocab, name="MemoryBlockTypeVocab", curie=VOCABULARY.curie('MemoryBlockTypeVocab'),
                   model_uri=VOCABULARY.MemoryBlockTypeVocab, domain=None, range=Optional[Union[str, "MemoryBlockTypeEnum"]])

slots.ObservableObjectRelationshipVocab = Slot(uri=VOCABULARY.ObservableObjectRelationshipVocab, name="ObservableObjectRelationshipVocab", curie=VOCABULARY.curie('ObservableObjectRelationshipVocab'),
                   model_uri=VOCABULARY.ObservableObjectRelationshipVocab, domain=None, range=Optional[Union[str, "ObservableObjectRelationshipEnum"]])

slots.ObservableObjectStateVocab = Slot(uri=VOCABULARY.ObservableObjectStateVocab, name="ObservableObjectStateVocab", curie=VOCABULARY.curie('ObservableObjectStateVocab'),
                   model_uri=VOCABULARY.ObservableObjectStateVocab, domain=None, range=Optional[Union[str, "ObservableObjectStateEnum"]])

slots.PartitionTypeVocab = Slot(uri=VOCABULARY.PartitionTypeVocab, name="PartitionTypeVocab", curie=VOCABULARY.curie('PartitionTypeVocab'),
                   model_uri=VOCABULARY.PartitionTypeVocab, domain=None, range=Optional[Union[str, "PartitionTypeEnum"]])

slots.ProcessorArchVocab = Slot(uri=VOCABULARY.ProcessorArchVocab, name="ProcessorArchVocab", curie=VOCABULARY.curie('ProcessorArchVocab'),
                   model_uri=VOCABULARY.ProcessorArchVocab, domain=None, range=Optional[Union[str, "ProcessorArchEnum"]])

slots.RecoveredObjectStatusVocab = Slot(uri=VOCABULARY.RecoveredObjectStatusVocab, name="RecoveredObjectStatusVocab", curie=VOCABULARY.curie('RecoveredObjectStatusVocab'),
                   model_uri=VOCABULARY.RecoveredObjectStatusVocab, domain=None, range=Optional[Union[str, "RecoveredObjectStatusEnum"]])

slots.RegionalRegistry_typeVocab = Slot(uri=VOCABULARY.RegionalRegistry_typeVocab, name="RegionalRegistry typeVocab", curie=VOCABULARY.curie('RegionalRegistry_typeVocab'),
                   model_uri=VOCABULARY.RegionalRegistry_typeVocab, domain=None, range=Optional[Union[str, "RegionalRegistryTypeEnum"]])

slots.RegistryDatatypeVocab = Slot(uri=VOCABULARY.RegistryDatatypeVocab, name="RegistryDatatypeVocab", curie=VOCABULARY.curie('RegistryDatatypeVocab'),
                   model_uri=VOCABULARY.RegistryDatatypeVocab, domain=None, range=Optional[Union[str, "RegistryDatatypeEnum"]])

slots.SIMFormVocab = Slot(uri=VOCABULARY.SIMFormVocab, name="SIMFormVocab", curie=VOCABULARY.curie('SIMFormVocab'),
                   model_uri=VOCABULARY.SIMFormVocab, domain=None, range=Optional[Union[str, "SIMFormEnum"]])

slots.SIMTypeVocab = Slot(uri=VOCABULARY.SIMTypeVocab, name="SIMTypeVocab", curie=VOCABULARY.curie('SIMTypeVocab'),
                   model_uri=VOCABULARY.SIMTypeVocab, domain=None, range=Optional[Union[str, "SIMTypeEnum"]])

slots.TaskActionTypeVocab = Slot(uri=VOCABULARY.TaskActionTypeVocab, name="TaskActionTypeVocab", curie=VOCABULARY.curie('TaskActionTypeVocab'),
                   model_uri=VOCABULARY.TaskActionTypeVocab, domain=None, range=Optional[Union[str, "TaskActionTypeEnum"]])

slots.TaskFlagVocab = Slot(uri=VOCABULARY.TaskFlagVocab, name="TaskFlagVocab", curie=VOCABULARY.curie('TaskFlagVocab'),
                   model_uri=VOCABULARY.TaskFlagVocab, domain=None, range=Optional[Union[str, "TaskFlagEnum"]])

slots.TaskPriorityVocab = Slot(uri=VOCABULARY.TaskPriorityVocab, name="TaskPriorityVocab", curie=VOCABULARY.curie('TaskPriorityVocab'),
                   model_uri=VOCABULARY.TaskPriorityVocab, domain=None, range=Optional[Union[str, "TaskPriorityEnum"]])

slots.TaskStatusVocab = Slot(uri=VOCABULARY.TaskStatusVocab, name="TaskStatusVocab", curie=VOCABULARY.curie('TaskStatusVocab'),
                   model_uri=VOCABULARY.TaskStatusVocab, domain=None, range=Optional[Union[str, "TaskStatusEnum"]])

slots.ThreadRunningStatusVocab = Slot(uri=VOCABULARY.ThreadRunningStatusVocab, name="ThreadRunningStatusVocab", curie=VOCABULARY.curie('ThreadRunningStatusVocab'),
                   model_uri=VOCABULARY.ThreadRunningStatusVocab, domain=None, range=Optional[Union[str, "ThreadRunningStatusEnum"]])

slots.TimestampPrecisionVocab = Slot(uri=VOCABULARY.TimestampPrecisionVocab, name="TimestampPrecisionVocab", curie=VOCABULARY.curie('TimestampPrecisionVocab'),
                   model_uri=VOCABULARY.TimestampPrecisionVocab, domain=None, range=Optional[Union[str, "TimestampPrecisionEnum"]])

slots.TrendVocab = Slot(uri=VOCABULARY.TrendVocab, name="TrendVocab", curie=VOCABULARY.curie('TrendVocab'),
                   model_uri=VOCABULARY.TrendVocab, domain=None, range=Optional[Union[str, "TrendEnum"]])

slots.TriggerFrequencyVocab = Slot(uri=VOCABULARY.TriggerFrequencyVocab, name="TriggerFrequencyVocab", curie=VOCABULARY.curie('TriggerFrequencyVocab'),
                   model_uri=VOCABULARY.TriggerFrequencyVocab, domain=None, range=Optional[Union[str, "TriggerFrequencyEnum"]])

slots.TriggerTypeVocab = Slot(uri=VOCABULARY.TriggerTypeVocab, name="TriggerTypeVocab", curie=VOCABULARY.curie('TriggerTypeVocab'),
                   model_uri=VOCABULARY.TriggerTypeVocab, domain=None, range=Optional[Union[str, "TriggerTypeEnum"]])

slots.URLTransitionTypeVocab = Slot(uri=VOCABULARY.URLTransitionTypeVocab, name="URLTransitionTypeVocab", curie=VOCABULARY.curie('URLTransitionTypeVocab'),
                   model_uri=VOCABULARY.URLTransitionTypeVocab, domain=None, range=Optional[Union[str, "URLTransitionTypeEnum"]])

slots.UnixProcessStateVocab = Slot(uri=VOCABULARY.UnixProcessStateVocab, name="UnixProcessStateVocab", curie=VOCABULARY.curie('UnixProcessStateVocab'),
                   model_uri=VOCABULARY.UnixProcessStateVocab, domain=None, range=Optional[Union[str, "UnixProcessStateEnum"]])

slots.WhoisContactTypeVocab = Slot(uri=VOCABULARY.WhoisContactTypeVocab, name="WhoisContactTypeVocab", curie=VOCABULARY.curie('WhoisContactTypeVocab'),
                   model_uri=VOCABULARY.WhoisContactTypeVocab, domain=None, range=Optional[Union[str, "WhoisContactTypeEnum"]])

slots.WhoisDNSSECTypeVocab = Slot(uri=VOCABULARY.WhoisDNSSECTypeVocab, name="WhoisDNSSECTypeVocab", curie=VOCABULARY.curie('WhoisDNSSECTypeVocab'),
                   model_uri=VOCABULARY.WhoisDNSSECTypeVocab, domain=None, range=Optional[Union[str, "WhoisDNSSECTypeEnum"]])

slots.WhoisStatusTypeVocab = Slot(uri=VOCABULARY.WhoisStatusTypeVocab, name="WhoisStatusTypeVocab", curie=VOCABULARY.curie('WhoisStatusTypeVocab'),
                   model_uri=VOCABULARY.WhoisStatusTypeVocab, domain=None, range=Optional[Union[str, "WhoisStatusTypeEnum"]])

slots.WindowsDriveTypeVocab = Slot(uri=VOCABULARY.WindowsDriveTypeVocab, name="WindowsDriveTypeVocab", curie=VOCABULARY.curie('WindowsDriveTypeVocab'),
                   model_uri=VOCABULARY.WindowsDriveTypeVocab, domain=None, range=Optional[Union[str, "WindowsDriveTypeEnum"]])

slots.WindowsVolumeAttributeVocab = Slot(uri=VOCABULARY.WindowsVolumeAttributeVocab, name="WindowsVolumeAttributeVocab", curie=VOCABULARY.curie('WindowsVolumeAttributeVocab'),
                   model_uri=VOCABULARY.WindowsVolumeAttributeVocab, domain=None, range=Optional[Union[str, "WindowsVolumeAttributeEnum"]])

slots.WirelessNetworkSecurityModeVocab = Slot(uri=VOCABULARY.WirelessNetworkSecurityModeVocab, name="WirelessNetworkSecurityModeVocab", curie=VOCABULARY.curie('WirelessNetworkSecurityModeVocab'),
                   model_uri=VOCABULARY.WirelessNetworkSecurityModeVocab, domain=None, range=Optional[Union[str, "WirelessNetworkSecurityModeEnum"]])