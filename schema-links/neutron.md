# Schema Links

- version: 0.0.2
- dialect: mysql
- database: neutron
- schema: neutron

## Inferred Links

### up
- inferred: agents.admin_state_up, healthmonitors.admin_state_up, lbaas_listeners.admin_state_up, lbaas_loadbalancers.admin_state_up, lbaas_members.admin_state_up, lbaas_members.weight, lbaas_pools.admin_state_up, members.admin_state_up, members.protocol_port, members.weight, ml2_gre_allocations.allocated, ml2_vlan_allocations.allocated, networks.admin_state_up, networksecuritybindings.port_security_enabled, pools.admin_state_up, ports.admin_state_up, portsecuritybindings.port_security_enabled, routers.admin_state_up, routers.enable_snat, securitygrouprules.port_range_max, securitygrouprules.port_range_min, subnets.enable_dhcp

### tenant
- inferred: default_security_group.tenant_id, floatingips.tenant_id, healthmonitors.tenant_id, lbaas_listeners.tenant_id, lbaas_loadbalancers.tenant_id, lbaas_members.tenant_id, lbaas_pools.tenant_id, members.tenant_id, networkrbacs.target_tenant, networkrbacs.tenant_id, networks.tenant_id, pools.tenant_id, ports.tenant_id, quotas.tenant_id, quotausages.tenant_id, routers.tenant_id, securitygrouprules.tenant_id, securitygroups.tenant_id, subnets.tenant_id, vips.tenant_id

### status
- inferred: floatingips.status, lbaas_listeners.provisioning_status, lbaas_loadbalancers.provisioning_status, lbaas_members.provisioning_status, lbaas_pools.provisioning_status, members.status, networks.status, pools.status, ports.status, routers.status

### poolstatisticss
- inferred: lbaas_loadbalancer_statistics.active_connections, lbaas_loadbalancer_statistics.bytes_out, poolstatisticss.active_connections, poolstatisticss.bytes_in, poolstatisticss.bytes_out, poolstatisticss.total_connections, quotausages.in_use

### host
- inferred: agents.host, ml2_gre_endpoints.host, ml2_port_binding_levels.host, ml2_port_bindings.host

### subnets.id
- inferred: lbaas_loadbalancers.vip_subnet_id, lbaas_members.subnet_id, pools.subnet_id
- declared: dnsnameservers.subnet_id, ipallocationpools.subnet_id, ipallocations.subnet_id, nuage_subnet_l2dom_mapping.subnet_id, subnetroutes.subnet_id, vpnservices.subnet_id

### ip
- inferred: ipallocationpools.first_ip, ipallocations.ip_address

### last
- inferred: ipallocationpools.last_ip, ipavailabilityranges.last_ip

### limit
- inferred: lbaas_listeners.connection_limit, quotas.limit

### physical
- inferred: ml2_network_segments.physical_network, ml2_vlan_allocations.physical_network

### networks.id
- inferred: floatingips.floating_network_id
- declared: auto_allocated_topologies.network_id, bgp_speaker_network_bindings.network_id, cisco_ml2_n1kv_network_bindings.network_id, externalnetworks.network_id, ha_router_networks.network_id, ha_router_vrid_allocations.network_id, ipallocations.network_id, ml2_network_segments.network_id, multi_provider_networks.network_id, networkconnections.network_id, networkdhcpagentbindings.network_id, networkdnsdomains.network_id, networkqueuemappings.network_id, networkrbacs.object_id, networksecuritybindings.network_id, neutron_nsx_network_mappings.neutron_id, nsxv_internal_networks.network_id, nsxv_spoofguard_policy_network_mappings.network_id, nsxv_tz_network_bindings.network_id, nuage_provider_net_bindings.network_id, ports.network_id, qos_network_policy_bindings.network_id, subnets.network_id, tz_network_bindings.network_id

### pools.id
- inferred: vips.pool_id
- declared: members.pool_id, nsxv_edge_pool_mappings.pool_id, nsxv_edge_vip_mappings.pool_id, poolloadbalanceragentbindings.pool_id, poolmonitorassociations.pool_id, poolstatisticss.pool_id

### routers.id
- inferred: floatingips.last_known_router_id
- declared: auto_allocated_topologies.router_id, cisco_ml2_apic_contracts.router_id, cisco_router_mappings.router_id, firewall_router_associations.router_id, floatingips.router_id, ha_router_agent_port_bindings.router_id, neutron_nsx_router_mappings.neutron_id, nsxv_router_ext_attributes.router_id, nuage_net_partition_router_mapping.router_id, router_extra_attributes.router_id, routerl3agentbindings.router_id, routerports.router_id, routerroutes.router_id, routerrules.router_id, vpnservices.router_id
