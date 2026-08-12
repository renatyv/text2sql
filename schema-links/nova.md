# Schema Links

- version: 0.0.2
- dialect: mysql
- database: nova
- schema: nova

## Inferred Links

### shadow
- inferred: certificates.deleted, compute_nodes.disk_allocation_ratio, compute_nodes.local_gb_used, compute_nodes.vcpus_used, fixed_ips.allocated, fixed_ips.deleted, fixed_ips.leased, fixed_ips.reserved, floating_ips.auto_assigned, floating_ips.deleted, instance_actions.deleted, instance_actions_events.deleted, instance_types.disabled, instance_types.ephemeral_gb, instance_types.root_gb, instances.auto_disk_config, instances.ephemeral_gb, instances.root_gb, pci_devices.deleted, pci_devices.numa_node, quota_classes.deleted, quota_usages.deleted, quotas.deleted, s3_images.deleted, security_group_rules.deleted, services.disabled, services.forced_down, shadow_compute_nodes.current_workload, shadow_compute_nodes.local_gb_used, shadow_compute_nodes.running_vms, shadow_compute_nodes.vcpus_used, shadow_fixed_ips.allocated, shadow_fixed_ips.deleted, shadow_fixed_ips.leased, shadow_fixed_ips.reserved, shadow_migrations.deleted, shadow_migrations.disk_processed, shadow_migrations.disk_remaining, shadow_migrations.disk_total, shadow_pci_devices.numa_node, shadow_services.disabled, shadow_services.forced_down, shadow_services.version, volume_id_mappings.deleted

### project
- inferred: certificates.project_id, floating_ips.project_id, instance_actions.project_id, instance_groups.project_id, instance_type_projects.project_id, instances.project_id, quota_usages.project_id, quotas.project_id, reservations.project_id, security_groups.project_id, shadow_instance_type_projects.project_id, shadow_snapshots.project_id, snapshots.project_id

### user
- inferred: certificates.user_id, instance_actions.user_id, instance_groups.user_id, instances.user_id, key_pairs.user_id, quota_usages.user_id, reservations.user_id, security_groups.user_id, shadow_key_pairs.user_id, shadow_snapshots.user_id, snapshots.user_id

### host
- inferred: aggregate_hosts.host, compute_nodes.host, instance_faults.host, services.host, shadow_aggregate_hosts.host, shadow_migrations.source_compute

### instance_types.id
- inferred: instances.instance_type_id, shadow_instance_type_extra_specs.instance_type_id, shadow_instance_type_projects.instance_type_id, shadow_migrations.new_instance_type_id, shadow_migrations.old_instance_type_id
- declared: instance_type_extra_specs.instance_type_id, instance_type_projects.instance_type_id

### at
- inferred: instance_extra.deleted_at, instance_faults.deleted_at, instance_system_metadata.deleted_at, instances.updated_at

### device
- inferred: block_device_mapping.device_name, instances.default_ephemeral_device, instances.default_swap_device, instances.root_device_name

### mb
- inferred: instance_types.memory_mb, instances.memory_mb, shadow_compute_nodes.free_ram_mb, shadow_compute_nodes.memory_mb_used

### network
- inferred: fixed_ips.network_id, networks.id, shadow_fixed_ips.network_id, shadow_virtual_interfaces.network_id

### node
- inferred: compute_nodes.hypervisor_hostname, instances.node, shadow_migrations.dest_node, shadow_migrations.source_node

### instance
- inferred: instance_types.created_at, shadow_instance_type_extra_specs.deleted_at, shadow_instance_type_projects.deleted_at

### shadow
- inferred: pci_devices.extra_info, shadow_compute_nodes.stats, shadow_pci_devices.extra_info

### aggregates.id
- inferred: shadow_aggregate_hosts.aggregate_id, shadow_aggregate_metadata.aggregate_id
- declared: aggregate_hosts.aggregate_id, aggregate_metadata.aggregate_id

### host
- inferred: compute_nodes.host_ip, shadow_migrations.dest_host

### image
- inferred: block_device_mapping.image_id, instances.image_ref

### instance
- inferred: instance_actions.updated_at, instance_faults.created_at

### instance
- inferred: instance_extra.updated_at, instance_info_caches.deleted_at

### instance_groups.id
- inferred: shadow_security_group_rules.group_id, shadow_security_group_rules.parent_group_id
- declared: instance_group_member.group_id, instance_group_policy.group_id, security_group_instance_association.security_group_id, security_group_rules.group_id, security_group_rules.parent_group_id

### pci
- inferred: pci_devices.dev_id, shadow_pci_devices.dev_id

### product
- inferred: pci_devices.product_id, shadow_pci_devices.product_id

### shadow
- inferred: shadow_instance_group_member.group_id, shadow_instance_group_policy.group_id

### shared values
- inferred: compute_nodes.service_id, services.id

### shared values
- inferred: snapshot_id_mappings.uuid, snapshots.id

### shared values
- inferred: compute_nodes.deleted, instances.launch_index

### vendor
- inferred: pci_devices.vendor_id, shadow_pci_devices.vendor_id

### volume
- inferred: shadow_snapshots.volume_id, snapshots.volume_id

### compute_nodes.id
- inferred: shadow_pci_devices.compute_node_id
- declared: pci_devices.compute_node_id
