HTMLPATH = ""
HELPPATH = ""

htmlfiles = [
         "maintain_troble_pingIpv4.html",
         "maintain_troble_pingIpv6.html",
         "maintain_troble_traceIpv4.html",
         "maintain_troble_traceIpv6.html",
         "route_arp_cache.html",
         "route_arp_conf.html",
         "route_arp_create.html",
         "route_arp_mgmt.html",
         "sec_acl_ipAceEdit.html",
         "sec_acl_ipAceExtEdit.html",
         "sec_acl_ipAce.html",
         "sec_acl_ipBind.html",
         "sec_acl_ipBindTable.html",
         "sec_acl_ipExtAce.html",
         "sec_acl_ip.html",
         "sec_acl_ipv6AceEdit.html",
         "sec_acl_ipv6Ace.html",
         "sec_acl_ipv6.html",
         "sec_acl_macAce.html",
         "sec_acl_macBind.html",
         "sec_acl_macBindTable.html",
         "sec_acl_mac.html",
         "sec_acl_vlanBindTable.html",
         "sec_acl_wizard.html",
         "sec_tc_privateVlanAssociation.html",
         "sec_tc_privateVlanHost.html",
         "sec_tc_privateVlanPortMode.html",
         "sec_tc_privateVlanPromiscuous.html",
         "sec_tc_privateVlanType.html",
         "sec_tc_protect.html",
         "switch_avoip_ouiBase.html",
         "switch_avoip_ouiBasePort.html",
         "switch_avoip_ouiBaseTable.html",
         "switch_avoip_protocolBasePort.html",
         "switch_avoip_status.html",
         "switch_loop_protection.html",
         "switch_vlan_conf.html",
         "switch_vlan_garp.html",
         "switch_vlan_garpPort.html",
         "switch_vlan_intf.html",
         "switch_vlan_macVlan.html",
         "switch_vlan_mbr.html",
         "switch_vlan_protoVlan.html",
         "switch_vlan_protoVlanMbrDetail.html",
         "switch_vlan_protoVlanMbr.html",
         "switch_vlan_status.html",
         "sys_mgmt_autoDos.html",
         "sys_mgmt_dayLightSaving.html",
         "sys_mgmt_dnsConf.html",
         "sys_mgmt_dosConf.html",
         "sys_mgmt_hostConf.html",
         "sys_mgmt_ipv6Neighbor.html",
         "sys_mgmt_sntp.html",
         "sys_mgmt_time.html",
         "sys_serv_daiAce.html",
         "sys_serv_daiAcl.html",
         "sys_serv_dai.html",
         "sys_serv_daiIntf.html",
         "sys_serv_daiStatistic.html",
         "sys_serv_daiVlan.html",
         "sys_serv_dsBind.html",
         "sys_serv_ds.html",
         "sys_serv_dsIntf.html",
         "sys_serv_dsPersist.html",
         "sys_serv_dsStatistic.html",
    ]

helpKey = [
         "ping",
         "pingIpv6",
         "traceroute",
         "traceroute",
         "tracerouteIpv6",
         "tracerouteIpv6",
         "vlan_arp_cache",
         "arpCache",
         "arpTableConfiguration",
         "arpCreate",
         "arpCache",
         "arpEntryManagement",
         "ipACLrulesConfiguration",
         "ipExACLrulesConfiguration",
         "ipRules",
         "ipRules",
         "ipBindingConfiguration",
         "ipInterfaceBindingStatus",
         "ipBindingTable",
         "ipERules",
         "ipRules",
         "ipACL",
         "ipACL",
         "ipv6ACLrulesConfiguration",
         "ipv6ACLrules",
         "ipv6ACLrulesTable",
         "ipACL",
         "ipACL",
         "macRules",
         "macRules",
         "macBindingConfiguration",
         "macBindingConfiguration",
         "macBindingTable",
         "macACL",
         "macACL",
         "aclIpv6VlanBindingTable",
         "aclWizardTypeSelection",
         "aclWizardRuleDmac",
         "aclWizardRuleSmac",
         "aclWizardRuleDipv4",
         "aclWizardRuleSipv4",
         "aclWizardRuleDipv6",
         "aclWizardRuleSipv6",
         "aclWizardRuleDportv4",
         "aclWizardRuleSportv4",
         "aclWizardRuleDportv6",
         "aclWizardRuleSportv6",
         "aclWizardRuleBinding",
         "pvlanasso",
         "pvlanhost",
         "pvlanpmode",
         "pvlanprom",
         "pvlantype",
         "protectedPort",
         "autoVoIPProp",
         "autoVoIPPortConf",
         "autoVoIPOUI",
         "autoGlobalVoIPConf",
         "autoVoIPConf",
         "autoVoIPstatus",
         "L2LoopGlobal",
         "L2LoopInterface",
         "basicVlanConfiguration",
         "resetVlan",
         "garpSwitchConfiguration",
         "garpPortConfiguration",
         "portPVIDConfiguration",
         "macVlanConfiguration",
         "vlanMembership",
         "groupConfiguration",
         "groupMembership",
         "vlanStatus",
         "voiceVlanGlobalCfg",
         "voiceVlanGlobalCfg",
         "autoDosConfiguration",
         "summerTimeConfig",
         "summerTimeStatus",
         "dnsConfiguration",
         "dnsServerConfiguration",
         "denialOfSerive",
         "greenLocalInfor",
         "greenRemoteInfor",
         "dnsHostConfiguration",
         "dnsDynamicHostConfiguration",
         "ipv6NeighborTbl",
         "sntpServerConfiguration",
         "sntpServerStatus",
         "TimeConfiguration",
         "sntpGlobalConfiguration",
         "sntpGlobalStatus",
         "daiRules",
         "daiRules",
         "daiAclCfg",
         "daiCfg",
         "daiInterfaceCfg",
         "daiStats",
         "daiVlanCfg",
         "dhcpSnoopingBindingCfg",
         "dhcpSnoopingdyBindingCfg",
         "dhcpSnoopingCfg",
         "dhcpSnoopingvlanCfg",
         "dhcpSnoopingIfCfg",
         "dhcpSnoopingPersistentCfg",
         "dhcpSnoopingStats",
]

htmlhelp = [
         "help_acl_wizard.html",
         "help_protectedport.html",
         "help_dhcp_snooping.html",
         "help_dai.html",
         "help_garp.html",
         "help_dos.html",
         "help_vlan.html",
         "help_dns.html",
         "help_sntp.html",
         "help_KeepALive.html",
         "help_switch_cfg.html",
         "help_pbvlan.html",
         "help_layer3ip.html",
         "help_mac_acl.html",
         "help_mac_vlan.html",
         "help_pvlan.html",
         "help_voip_vlan.html",
         "help_acl.html",
         ]

jshelp = [
         "help_acl_wizard.js",
         "help_protectedport.js",
         "help_dhcp_snooping.js",
         "help_dai.js",
         "help_garp.js",
         "help_dos.js",
         "help_vlan.js",
         "help_dns.js",
         "help_sntp.js",
         "help_KeepALive.js",
         "help_switch_cfg.js",
         "help_pbvlan.js",
         "help_layer3ip.js",
         "help_mac_acl.js",
         "help_mac_vlan.js",
         "help_pvlan.js",
         "help_voip_vlan.js",
         "help_acl.js",
         ]