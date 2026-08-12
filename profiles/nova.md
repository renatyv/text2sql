---
generator: db-snooper
version: 0.0.27
generated_at_utc: 2026-08-12T09:51:16.892290Z
dialect: mysql
database: nova
schema: nova
skipped_technical_tables:
  - migrations
---

## Relationships

- aggregates.id ← aggregate_hosts.aggregate_id, aggregate_metadata.aggregate_id
- compute_nodes.id ← pci_devices.compute_node_id
- console_pools.id ← consoles.pool_id
- instance_actions.id ← instance_actions_events.action_id
- instance_groups.id ← instance_group_member.group_id, instance_group_policy.group_id
- instance_types.id ← instance_type_extra_specs.instance_type_id, instance_type_projects.instance_type_id
- instances.uuid ← block_device_mapping.instance_uuid, consoles.instance_uuid, fixed_ips.instance_uuid, instance_actions.instance_uuid, instance_extra.instance_uuid, instance_faults.instance_uuid, instance_info_caches.instance_uuid, instance_metadata.instance_uuid, instance_system_metadata.instance_uuid, security_group_instance_association.instance_uuid, virtual_interfaces.instance_uuid
- quota_usages.id ← reservations.usage_id
- security_groups.id ← security_group_instance_association.security_group_id, security_group_rules.group_id, security_group_rules.parent_group_id

# aggregate_hosts

```sql
CREATE TABLE `aggregate_hosts` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `host` varchar(255),
  `aggregate_id` int NOT NULL,
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`host`,`aggregate_id`,`deleted`),
  KEY (`aggregate_id`),
  CONSTRAINT `aggregate_hosts_ibfk_1` FOREIGN KEY (`aggregate_id`) REFERENCES `aggregates` (`id`)
) AUTO_INCREMENT=1252;
```

## Rows

- total=584

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-05-06T16:14:41 | 2018-11-05T04:53:23 | 2017-12-08T16:10:10 |
| updated_at | null | null | null |
| deleted_at | null | 2019-09-27T17:15:45 | 2017-12-08T16:20:57 |
| id | 1251 | 1057 | 947 |
| host | forge-23 | novae0-21 | helio1-2 |
| aggregate_id | 2 | 2 | 18 |
| deleted | 0 | 1057 | 947 |

## Columns

- created_at: all distinct, nulls=57
- updated_at: 2017-08-04 16:36:52=96, nulls=488
- deleted_at: 351 distinct, nulls=138
- id: unique identifier, int 1..1251
- host: 127 distinct
  - top_values: "spark9-96"=23, "forge-23"=22, "align-86"=16, "streak-26"=16, "ether-50"=15, "blitz1-32"=13, "ether-18"=13, "shine-94"=13, "nexis-43"=12, "space2-35"=12
- aggregate_id: 2=183, 18=86, 17=62, 1=57, 13=40, 4=32, 21=20, 5=19, 15=19, 6=17, 19=15, 20=12, 14=10, 11=8, 9=2, 10=2, int 1..21
- deleted: 352 distinct, int 0..1247
  - stats: average=571.7055, median=759.5000
  - top_values: 0=138, 1=96, 245=1, 516=1, 518=1, 519=1, 520=1, 521=1, 522=1, 523=1


# aggregate_metadata

```sql
CREATE TABLE `aggregate_metadata` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `aggregate_id` int NOT NULL,
  `key` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`aggregate_id`,`key`,`deleted`),
  KEY (`aggregate_id`),
  KEY (`key`),
  CONSTRAINT `aggregate_metadata_ibfk_1` FOREIGN KEY (`aggregate_id`) REFERENCES `aggregates` (`id`)
) AUTO_INCREMENT=43;
```

## Rows

- total=38

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-12-23T20:23:43 | 2019-12-23T20:23:33 | 2014-02-07T18:03:02 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 42 | 37 | 11 |
| aggregate_id | 20 | 21 | 5 |
| key | cpu_allocation_ratio | ram_allocation_ratio | ram_allocation_ratio |
| value | 8.0 | 3.5 | 1 |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 27 distinct
- updated_at: 2017-07-21 16:42:43=2, 2013-08-06 01:43:56=1, 2014-12-16 14:51:10=1, 2016-05-10 20:04:24=1, 2016-05-10 20:04:34=1, 2017-12-14 03:48:48=1, 2022-11-21 20:22:19=1, 2022-11-21 20:22:34=1, nulls=29
- deleted_at: 2018-09-25 22:29:45=1, nulls=37
- id: unique identifier, int 1..42
- aggregate_id: 2=5, 3=4, 4=4, 5=3, 6=3, 17=3, 19=3, 20=3, 21=3, 1=1, 9=1, 10=1, 11=1, 13=1, 14=1, 15=1, int 1..21
- key: "cpu_allocation_ratio"=9, "ram_allocation_ratio"=9, "switch"=6, "availability_zone"=3, "generation"=3, "overcommit"=2, "cpu_ratio"=1, "hi_mem_use"=1, "test"=1, "testing"=1, "tig"=1, "ups"=1
- value: 25 distinct
- deleted: 0=37, 22=1


# aggregates

```sql
CREATE TABLE `aggregates` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255),
  `deleted` int,
  `uuid` varchar(36),
  PRIMARY KEY (`id`),
  KEY (`uuid`)
) AUTO_INCREMENT=22;
```

## Rows

- total=21

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-12-23T19:47:47 | 2017-05-31T15:25:30 | 2016-08-03T13:47:04 |
| updated_at | null | null | 2016-10-13T15:03:15 |
| deleted_at | null | null | null |
| id | 21 | 17 | 10 |
| name | align-track | solar-2y-26 | delta-netix |
| deleted | 0 | 0 | 0 |
| uuid | 7ecfc17d-efad-4d26-a2d2-cc1b9a032a0c | c3ecbf5d-21e8-4c84-9cb3-810f99fd8aa1 | 1015ff87-4766-451b-867f-cc2f617e179b |

## Columns

- created_at: all distinct, nulls=1
- updated_at: 2016-10-13 15:03:15=10, 2016-10-13 15:03:16=3, 2014-12-04 20:18:55=1, 2017-08-04 16:29:22=1, nulls=6
- deleted_at: 2016-07-07 03:08:27=1, 2016-09-28 23:44:55=1, 2017-02-16 21:47:48=1, 2017-02-16 21:56:42=1, 2017-08-04 16:29:22=1, nulls=16
- id: unique identifier, int 1..21
- name: 20 distinct
- deleted: 0=16, 7=1, 8=1, 12=1, 13=1, 16=1, int 0..16
- uuid: "094d9b67-6185-4adf-84b0-133402c4f190"=1, "0cf382be-16ff-4622-b83c-5183bc990b1b"=1, "0db2e90b-ddf9-4044-87b7-3a864b5e4329"=1, "1015ff87-4766-451b-867f-cc2f617e179b"=1, "27f99211-b2c5-47cb-a1a5-e9e1dd1b8ace"=1, "51594b5b-0011-4568-8370-e3d188302040"=1, "5a914b0d-30f0-4a22-bf8a-c4eedbaca0e3"=1, "66806f0e-1afc-422e-8f83-464a9f6226c3"=1, "706bb206-a340-4144-85ba-b78ca38b018f"=1, "74703873-8ec4-4183-bc76-99bca4686fe1"=1, "7ecfc17d-efad-4d26-a2d2-cc1b9a032a0c"=1, "a2475632-4dca-41b9-b102-a28966002418"=1, "ae39debd-2ba7-4ac5-ab22-432669532571"=1, "bfdb2a6d-bba0-4fc4-8030-b3544843480e"=1, "c3ecbf5d-21e8-4c84-9cb3-810f99fd8aa1"=1, "c5c3b947-39b7-470e-8e97-2d07ec7f5997"=1, "cbe731e6-bb27-4f6c-b782-fed83ca7ed8f"=1, "e2097396-feb9-4727-92fd-58b53436287c"=1, "ec980ea8-57d5-4808-b914-cfad25f348d3"=1, nulls=2


# all_instances

```sql
CREATE VIEW nova.all_instances AS select `nova`.`instances`.`created_at` AS `created_at`,`nova`.`instances`.`updated_at` AS `updated_at`,`nova`.`instances`.`deleted_at` AS `deleted_at`,`nova`.`instances`.`id` AS `id`,`nova`.`instances`.`internal_id` AS `internal_id`,`nova`.`instances`.`user_id` AS `user_id`,`nova`.`instances`.`project_id` AS `project_id`,`nova`.`instances`.`image_ref` AS `image_ref`,`nova`.`instances`.`kernel_id` AS `kernel_id`,`nova`.`instances`.`ramdisk_id` AS `ramdisk_id`,`nova`.`instances`.`launch_index` AS `launch_index`,`nova`.`instances`.`key_name` AS `key_name`,`nova`.`instances`.`key_data` AS `key_data`,`nova`.`instances`.`power_state` AS `power_state`,`nova`.`instances`.`vm_state` AS `vm_state`,`nova`.`instances`.`memory_mb` AS `memory_mb`,`nova`.`instances`.`vcpus` AS `vcpus`,`nova`.`instances`.`hostname` AS `hostname`,`nova`.`instances`.`host` AS `host`,`nova`.`instances`.`user_data` AS `user_data`,`nova`.`instances`.`reservation_id` AS `reservation_id`,`nova`.`instances`.`scheduled_at` AS `scheduled_at`,`nova`.`instances`.`launched_at` AS `launched_at`,`nova`.`instances`.`terminated_at` AS `terminated_at`,`nova`.`instances`.`display_name` AS `display_name`,`nova`.`instances`.`display_description` AS `display_description`,`nova`.`instances`.`availability_zone` AS `availability_zone`,`nova`.`instances`.`locked` AS `locked`,`nova`.`instances`.`os_type` AS `os_type`,`nova`.`instances`.`launched_on` AS `launched_on`,`nova`.`instances`.`instance_type_id` AS `instance_type_id`,`nova`.`instances`.`vm_mode` AS `vm_mode`,`nova`.`instances`.`uuid` AS `uuid`,`nova`.`instances`.`architecture` AS `architecture`,`nova`.`instances`.`root_device_name` AS `root_device_name`,`nova`.`instances`.`access_ip_v4` AS `access_ip_v4`,`nova`.`instances`.`access_ip_v6` AS `access_ip_v6`,`nova`.`instances`.`config_drive` AS `config_drive`,`nova`.`instances`.`task_state` AS `task_state`,`nova`.`instances`.`default_ephemeral_device` AS `default_ephemeral_device`,`nova`.`instances`.`default_swap_device` AS `default_swap_device`,`nova`.`instances`.`progress` AS `progress`,`nova`.`instances`.`auto_disk_config` AS `auto_disk_config`,`nova`.`instances`.`shutdown_terminate` AS `shutdown_terminate`,`nova`.`instances`.`disable_terminate` AS `disable_terminate`,`nova`.`instances`.`root_gb` AS `root_gb`,`nova`.`instances`.`ephemeral_gb` AS `ephemeral_gb`,`nova`.`instances`.`cell_name` AS `cell_name`,`nova`.`instances`.`node` AS `node`,`nova`.`instances`.`deleted` AS `deleted`,`nova`.`instances`.`locked_by` AS `locked_by`,`nova`.`instances`.`cleaned` AS `cleaned`,`nova`.`instances`.`ephemeral_key_uuid` AS `ephemeral_key_uuid` from `nova`.`instances` union select `nova`.`shadow_instances`.`created_at` AS `created_at`,`nova`.`shadow_instances`.`updated_at` AS `updated_at`,`nova`.`shadow_instances`.`deleted_at` AS `deleted_at`,`nova`.`shadow_instances`.`id` AS `id`,`nova`.`shadow_instances`.`internal_id` AS `internal_id`,`nova`.`shadow_instances`.`user_id` AS `user_id`,`nova`.`shadow_instances`.`project_id` AS `project_id`,`nova`.`shadow_instances`.`image_ref` AS `image_ref`,`nova`.`shadow_instances`.`kernel_id` AS `kernel_id`,`nova`.`shadow_instances`.`ramdisk_id` AS `ramdisk_id`,`nova`.`shadow_instances`.`launch_index` AS `launch_index`,`nova`.`shadow_instances`.`key_name` AS `key_name`,`nova`.`shadow_instances`.`key_data` AS `key_data`,`nova`.`shadow_instances`.`power_state` AS `power_state`,`nova`.`shadow_instances`.`vm_state` AS `vm_state`,`nova`.`shadow_instances`.`memory_mb` AS `memory_mb`,`nova`.`shadow_instances`.`vcpus` AS `vcpus`,`nova`.`shadow_instances`.`hostname` AS `hostname`,`nova`.`shadow_instances`.`host` AS `host`,`nova`.`shadow_instances`.`user_data` AS `user_data`,`nova`.`shadow_instances`.`reservation_id` AS `reservation_id`,`nova`.`shadow_instances`.`scheduled_at` AS `scheduled_at`,`nova`.`shadow_instances`.`launched_at` AS `launched_at`,`nova`.`shadow_instances`.`terminated_at` AS `terminated_at`,`nova`.`shadow_instances`.`display_name` AS `display_name`,`nova`.`shadow_instances`.`display_description` AS `display_description`,`nova`.`shadow_instances`.`availability_zone` AS `availability_zone`,`nova`.`shadow_instances`.`locked` AS `locked`,`nova`.`shadow_instances`.`os_type` AS `os_type`,`nova`.`shadow_instances`.`launched_on` AS `launched_on`,`nova`.`shadow_instances`.`instance_type_id` AS `instance_type_id`,`nova`.`shadow_instances`.`vm_mode` AS `vm_mode`,`nova`.`shadow_instances`.`uuid` AS `uuid`,`nova`.`shadow_instances`.`architecture` AS `architecture`,`nova`.`shadow_instances`.`root_device_name` AS `root_device_name`,`nova`.`shadow_instances`.`access_ip_v4` AS `access_ip_v4`,`nova`.`shadow_instances`.`access_ip_v6` AS `access_ip_v6`,`nova`.`shadow_instances`.`config_drive` AS `config_drive`,`nova`.`shadow_instances`.`task_state` AS `task_state`,`nova`.`shadow_instances`.`default_ephemeral_device` AS `default_ephemeral_device`,`nova`.`shadow_instances`.`default_swap_device` AS `default_swap_device`,`nova`.`shadow_instances`.`progress` AS `progress`,`nova`.`shadow_instances`.`auto_disk_config` AS `auto_disk_config`,`nova`.`shadow_instances`.`shutdown_terminate` AS `shutdown_terminate`,`nova`.`shadow_instances`.`disable_terminate` AS `disable_terminate`,`nova`.`shadow_instances`.`root_gb` AS `root_gb`,`nova`.`shadow_instances`.`ephemeral_gb` AS `ephemeral_gb`,`nova`.`shadow_instances`.`cell_name` AS `cell_name`,`nova`.`shadow_instances`.`node` AS `node`,`nova`.`shadow_instances`.`deleted` AS `deleted`,`nova`.`shadow_instances`.`locked_by` AS `locked_by`,`nova`.`shadow_instances`.`cleaned` AS `cleaned`,`nova`.`shadow_instances`.`ephemeral_key_uuid` AS `ephemeral_key_uuid` from `nova`.`shadow_instances`;
```

## Rows

- total=717814

- (no rows sampled)

## Columns

- created_at: profile metrics skipped
- updated_at: nulls=84
- deleted_at: nulls=1485
- id: int 1..749387
- internal_id: all NULL
- user_id: profile metrics skipped
- project_id: profile metrics skipped
- image_ref: nulls=4110
- kernel_id: nulls=717695
- ramdisk_id: nulls=717695
- launch_index: int 0..511
  - stats: average=2.7386
- key_name: nulls=33056
- key_data: nulls=33061
- power_state: int 0..5
  - stats: average=0.7548
- vm_state: profile metrics skipped
- memory_mb: int 1..98304
  - stats: average=4388.6399
- vcpus: int 1..88
  - stats: average=2.4029
- hostname: profile metrics skipped
- host: profile metrics skipped
- user_data: nulls=369424
- reservation_id: profile metrics skipped
- scheduled_at: nulls=320813
- launched_at: nulls=173685
- terminated_at: nulls=142458
- display_name: profile metrics skipped
- display_description: nulls=434542
- availability_zone: nulls=685490
- locked: int 0..1
  - stats: average=0.0000
- os_type: all NULL
- launched_on: nulls=143559
- instance_type_id: int 1..196
- vm_mode: all NULL
- uuid: profile metrics skipped
- architecture: nulls=717620
- root_device_name: nulls=147834
- access_ip_v4: all NULL
- access_ip_v6: all NULL
- config_drive: nulls=717415
- task_state: nulls=575126
- default_ephemeral_device: nulls=409056
- default_swap_device: nulls=717260
- progress: int 0..0
  - stats: average=0.0000
- auto_disk_config: nulls=481255, int 0..1
  - stats: average=0.0039
- shutdown_terminate: int 0..1
  - stats: average=0.0269
- disable_terminate: int 0..0
  - stats: average=0.0000
- root_gb: int 0..100
  - stats: average=12.5595
- ephemeral_gb: int 0..360
  - stats: average=24.3553
- cell_name: all NULL
- node: nulls=472155
- deleted: int 0..749385
  - stats: average=359838.7599
- locked_by: nulls=717800
- cleaned: int 0..1
  - stats: average=0.9926
- ephemeral_key_uuid: all NULL


# block_device_mapping

```sql
CREATE TABLE `block_device_mapping` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `device_name` varchar(255),
  `delete_on_termination` tinyint(1),
  `snapshot_id` varchar(36),
  `volume_id` varchar(36),
  `volume_size` int,
  `no_device` tinyint(1),
  `connection_info` text,
  `instance_uuid` varchar(36),
  `deleted` int,
  `source_type` varchar(255),
  `destination_type` varchar(255),
  `guest_format` varchar(255),
  `device_type` varchar(255),
  `disk_bus` varchar(255),
  `boot_index` int,
  `image_id` varchar(36),
  PRIMARY KEY (`id`),
  KEY (`snapshot_id`),
  KEY (`volume_id`),
  KEY (`instance_uuid`),
  KEY (`instance_uuid`,`device_name`),
  KEY (`instance_uuid`,`volume_id`),
  CONSTRAINT `block_device_mapping_instance_uuid_fkey` FOREIGN KEY (`instance_uuid`) REFERENCES `instances` (`uuid`)
) AUTO_INCREMENT=281399;
```

## Rows

- total=16798

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-28T01:25:36 | 2022-09-25T23:02:15 | 2016-09-26T20:00:02 |
| updated_at | 2024-06-28T01:25:42 | 2022-09-25T23:02:20 | 2018-12-26T19:38:22 |
| deleted_at | 2024-06-28T01:37:05 | 2022-09-26T00:28:19 | 2022-12-09T18:13:33 |
| id | 281398 | 271808 | 226831 |
| device_name | /dev/vdb | /dev/vdj | /dev/vda |
| delete_on_termination | 0 | 0 | 0 |
| snapshot_id | null | null | null |
| volume_id | 7308377b-f688-4246-936b-5bd08a204982 | f4c4496d-a5d9-42b3-a0f7-9149b6567970 | 17e6b695-d6f5-417a-b78b-8273e94e6dae |
| volume_size | 5 | 5 | 800 |
| no_device | null | null | 0 |
| connection_info | {"driver_volume_type": "rbd", "connector": {"initiator": "iqn10.132.246.102/8-10.121.122.184/8org.debian:01:75848bb568e8", "ip": "10.165.53.177/8", "platform": "x86_64", "host": "cosmo3-23", "os_type": "linux2", "multipath": false}, "serial": "7308377b-f688-4246-936b-5bd08a204982", "data": {"secret_type": "ceph", "name": "volumes/volume-7308377b-f688-4246-936b-5bd08a204982", "encrypted": false, "secret_uuid": "cf58e08b-3c51-410f-b043-619c616c6f44", "qos_specs": null, "hosts": ["10.199.159.162/8", "10.21.63.238/8", "10.125.102.189/8", "10.236.77.110/8", "10.5.90.191/8"], "volume_id": "7308377b-f688-4246-936b-5bd08a204982", "auth_enabled": true, "access_mode": "rw", "auth_username": "openstack", "ports": ["6789", "6789", "6789", "6789", "6789"]}} | {"driver_volume_type": "rbd", "connector": {"initiator": "iqn10.132.246.102/8-10.121.122.184/8org.debian:01:423c708ae6dd", "ip": "10.18.36.134/8", "platform": "x86_64", "host": "spark9-96", "os_type": "linux2", "multipath": false}, "serial": "f4c4496d-a5d9-42b3-a0f7-9149b6567970", "data": {"secret_type": "ceph", "name": "volumes/volume-f4c4496d-a5d9-42b3-a0f7-9149b6567970", "encrypted": false, "secret_uuid": "cf58e08b-3c51-410f-b043-619c616c6f44", "qos_specs": null, "hosts": ["10.5.90.191/8", "10.236.77.110/8", "10.67.93.167/8", "10.125.102.189/8", "10.199.159.162/8"], "volume_id": "f4c4496d-a5d9-42b3-a0f7-9149b6567970", "auth_enabled": true, "access_mode": "rw", "auth_username": "openstack", "ports": ["6789", "6789", "6789", "6789", "6789"]}} | {"driver_volume_type": "rbd", "connector": {"initiator": "iqn10.132.246.102/8-10.121.122.184/8org.debian:01:3c1e61f0b28e", "ip": "10.235.253.224/8", "platform": "x86_64", "host": "ether-50", "os_type": "linux2", "multipath": false}, "serial": "17e6b695-d6f5-417a-b78b-8273e94e6dae", "data": {"secret_type": "ceph", "name": "volumes/volume-17e6b695-d6f5-417a-b78b-8273e94e6dae", "encrypted": false, "secret_uuid": "cf58e08b-3c51-410f-b043-619c616c6f44", "qos_specs": null, "hosts": ["10.201.239.86/8", "10.18.244.133/8", "10.188.237.136/8"], "volume_id": "17e6b695-d6f5-417a-b78b-8273e94e6dae", "auth_enabled": true, "access_mode": "rw", "auth_username": "openstack", "ports": ["6789", "6789", "6789"]}} |
| instance_uuid | 7fe281b6-5744-41ca-9f94-9d6f516b4e8b | 64d7cd79-6dc6-404c-b603-8cdd4f9263a0 | f37860ee-a76d-4df7-89bf-0d24b33281da |
| deleted | 281398 | 271808 | 226831 |
| source_type | volume | volume | image |
| destination_type | volume | volume | volume |
| guest_format | null | null | null |
| device_type | null | null | disk |
| disk_bus | null | null | virtio |
| boot_index | null | null | 0 |
| image_id | null | null | f54b8417-c104-438d-946c-ee31979bfa54 |

## Columns

- created_at: 15930 distinct
- updated_at: 15739 distinct, nulls=190
- deleted_at: 13825 distinct, nulls=1705
- id: unique identifier, int 28326..281398
- device_name: 29 distinct, nulls=115
  - top_values: "/dev/vda"=6027, "/dev/vdb"=1709, "/dev/vdd"=1524, "/dev/vdc"=1517, "/dev/vde"=1286, "/dev/vdf"=1058, "/dev/vdg"=854, "/dev/vdh"=597, "/dev/vdi"=488, "/dev/vdj"=368
- delete_on_termination: 0=11986, 1=4812
- snapshot_id: "f2548d6b-0503-424b-a724-f693164db5a5"=38, "77c31642-cd38-49f1-8699-866ad8d65ad9"=4, "912f4cde-2942-4ebd-b331-479d72026ff9"=4, "455c943a-6cef-45e5-a3c5-367efe6e24c7"=3, "5f88f17d-188c-4988-962f-5c709d235c24"=2, "0e4a03ca-ae1e-4cb6-bce3-7b5a8bbf786c"=1, "44bcca2f-4082-4898-89c0-d146d5b01645"=1, "56c5b012-d380-4694-99c9-455604b9a619"=1, "707161b4-048e-45ca-8bbf-df9175d2ef23"=1, "79d252e0-4d1c-4522-b8b6-7973d32b4eb3"=1, "7b43d435-da52-499b-86e0-f09d91cd6b13"=1, "810c3e0e-84c3-4799-8b6a-ed5b4fb2a8af"=1, "a0100981-2112-450c-acfa-98fc1031a550"=1, "acc984ab-7af5-4f09-b86c-a3d2d8920825"=1, "b21470a9-a635-40b9-93b2-b31da4606cfd"=1, "c4907106-3e73-49ce-8d94-8781a8f963bb"=1, "c5c0d411-12d2-4163-a2ce-5ac6762c032f"=1, "dedb5e1b-7d09-4110-b7be-ebaf06effff5"=1, nulls=16734
- volume_id: 1674 distinct, nulls=4776
  - top_values: "79ea9032-0141-45e4-af84-64796f14d4dd"=217, "19f6274f-e3cb-4700-bd16-a89f9574dffa"=162, "3b4d549a-85d6-4760-a04d-551d30bd8011"=161, "d152b1c5-c6ce-4599-8550-5a5a62961095"=155, "7c12e582-2dac-4904-a5ee-725ffb522ea6"=138, "d19b4658-ddd8-4ac6-bcb5-715c72785893"=134, "23b5f8b7-9de0-4102-9bff-2f7aa3cf3adf"=121, "cef71f67-0988-44e5-b08c-e0cfe4cbcd33"=119, "f16530a1-353b-40e9-a4b0-4fa793345446"=118, "71f8af57-2515-436e-afd3-80cd96888f86"=117
- volume_size: 74 distinct, nulls=4805, int 1..16384
  - stats: average=45.6010, median=5.0000
- no_device: 0=6240, nulls=10558
- connection_info: 2379 distinct, nulls=4860
- instance_uuid: 6143 distinct
  - top_values: "9b309acd-a62c-436e-b116-ff7554e6ec1e"=3313, "f651937a-8bcd-43f1-910e-f5b61fa358ac"=2338, "64d7cd79-6dc6-404c-b603-8cdd4f9263a0"=2014, "0b1e3819-6250-479d-9247-549549fcb712"=933, "501e65b0-b58f-4e7f-b015-30777efd0f31"=712, "c1852e78-3fbe-4cab-bb45-6712f15de351"=582, "c9a2d351-64b2-4b74-af4c-aa71269cad0d"=9, "bf46f261-9857-4915-b8fe-43d9e9cc3a40"=8, "d2836b5f-d5d6-4e04-980d-8f45882a19d2"=8, "d052d786-9b26-4439-ae6b-32a0505fdc12"=7
- deleted: 15094 distinct, int 0..281398
  - stats: average=243885.3779, median=272541.5000
- source_type: "volume"=11905, "image"=4677, "blank"=152, "snapshot"=64
- destination_type: "volume"=12023, "local"=4775
- guest_format: "swap"=57, nulls=16741
- device_type: "disk"=6604, "cdrom"=11, nulls=10183
- disk_bus: "virtio"=2037, "ide"=11, nulls=14750
- boot_index: 0=6143, -1=141, 1=65, nulls=10449, int -1..1
- image_id: 615 distinct, nulls=12121


# certificates

```sql
CREATE TABLE `certificates` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255),
  `project_id` varchar(255),
  `file_name` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`),
  KEY (`project_id`,`deleted`),
  KEY (`user_id`,`deleted`)
) AUTO_INCREMENT=128;
```

## Rows

- total=127

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2014-12-30T18:36:51 | 2013-02-25T03:49:35 | 2013-02-13T20:51:48 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 127 | 42 | 34 |
| user_id | a1ef823458d24a68955fec6f3d390019 | 92ece2ed533a4fd189ed2c269328b645 | 7f947163737b494a9cf8328780be0336 |
| project_id | bfd50153a2e9476f93e33e30e922cd06 | 3008a142e9524f7295b06ea811908f93 | 3008a142e9524f7295b06ea811908f93 |
| file_name | /var/lib/nova/CA/newcerts/8B.pem | /var/lib/nova/CA/newcerts/39.pem | /var/lib/nova/CA/newcerts/31.pem |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: all distinct
- updated_at: all NULL
- deleted_at: all NULL
- id: unique identifier, int 1..127
- user_id: 55 distinct
  - top_values: "3b484308cddd436a87471cd1dcfa53c7"=10, "6360caf9aaaa436c8deee7dbf094f726"=10, "a1ef823458d24a68955fec6f3d390019"=10, "c8490ee0863345f6919b5c63540efca1"=8, "78d8da36e7904928ad34c807390314f3"=7, "011e1ffb210245abbb2ba24be9b4f5be"=6, "d44a0e9978c347e288a218aa6266f38b"=5, "59a5934524c54089af8f35bed2ea7eaa"=4, "0df639d1cf6a48f7b9ddf6cf68772ca8"=3, "715323529b6e488d884944199f24b4c9"=3
- project_id: "3008a142e9524f7295b06ea811908f93"=77, "71322eb9ba804fc4ae74cefde3ad0742"=9, "98333a1a28e746fa8c629c83a818ad57"=9, "2a9b495932c64d80b1fac28d1416a921"=5, "97107d3284a848a4a4ea0345bd05cbef"=5, "70b2507b8cc44fcb917ddfb85f5079d9"=4, "b7188a889c6a4800893445d969673bab"=4, "bfd50153a2e9476f93e33e30e922cd06"=3, "dba6cc0fec6845a58f4dd5e84ef8dca5"=3, "4e101cf5264b4e739b7b5ebe0f6b5c68"=2, "1124c2b7959f4101a662875fd5581c19"=1, "1140b46602e84c47838f707b060d6fd2"=1, "6f5103a9ae434375a92a1de24a19ca56"=1, "d0ebc85936794a30b65bb6dae5687404"=1, "deecf4e22b4244ffa09aa8ce7748e976"=1, "fc1b446cad9e4849a41f9160664e3781"=1
- file_name: 124 distinct
- deleted: 0=127


# compute_nodes

```sql
CREATE TABLE `compute_nodes` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `service_id` int,
  `vcpus` int NOT NULL,
  `memory_mb` int NOT NULL,
  `local_gb` int NOT NULL,
  `vcpus_used` int NOT NULL,
  `memory_mb_used` int NOT NULL,
  `local_gb_used` int NOT NULL,
  `hypervisor_type` text NOT NULL,
  `hypervisor_version` int NOT NULL,
  `cpu_info` text NOT NULL,
  `disk_available_least` int,
  `free_ram_mb` int,
  `free_disk_gb` int,
  `current_workload` int,
  `running_vms` int,
  `hypervisor_hostname` varchar(255),
  `deleted` int,
  `host_ip` varchar(39),
  `supported_instances` text,
  `pci_stats` text,
  `metrics` text,
  `extra_resources` text,
  `stats` text,
  `numa_topology` text,
  `host` varchar(255),
  `ram_allocation_ratio` float,
  `cpu_allocation_ratio` float,
  `uuid` varchar(36),
  `disk_allocation_ratio` float,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`host`,`hypervisor_hostname`,`deleted`)
) AUTO_INCREMENT=150;
```

## Rows

- total=139

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-01-09T18:22:21 | 2014-12-03T07:53:17 | 2016-09-23T20:25:09 |
| updated_at | 2019-01-09T18:22:21 | 2017-12-12T20:22:29 | 2024-07-08T06:59:48 |
| deleted_at | null | 2018-11-05T19:06:48 | null |
| id | 149 | 85 | 91 |
| service_id | null | 178 | 243 |
| vcpus | 32 | 32 | 40 |
| memory_mb | 128893 | 193404 | 257720 |
| local_gb | 642559 | 376144 | 686780 |
| vcpus_used | 0 | 0 | 150 |
| memory_mb_used | 512 | 512 | 180736 |
| local_gb_used | 0 | 0 | 682 |
| hypervisor_type | QEMU | QEMU | QEMU |
| hypervisor_version | 2005000 | 2005000 | 2005000 |
| cpu_info | {"vendor": "Intel", "model": "Broadwell", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xtpr", "cmov", "hle", "smep", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "msr", "adx", "3dnowprefetch", "nx", "fxsr", "syscall", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "acpi", "fma", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "abm", "rdseed", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "avx2", "aes", "sse2", "ss", "ds_cpl", "bmi1", "bmi2", "pcid", "fpu", "cx16", "pse36", "mtrr", "movbe", "pdcm", "rdrand", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}} | {"vendor": "Intel", "model": "IvyBridge", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "fsgsbase", "xsave", "vmx", "erms", "xtpr", "cmov", "smep", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "acpi", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "aes", "sse2", "ss", "ds_cpl", "pcid", "fpu", "cx16", "pse36", "mtrr", "pdcm", "rdrand", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}} | {"vendor": "Intel", "model": "Broadwell-IBRS", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xtpr", "cmov", "hle", "smep", "spec-ctrl", "md-clear", "pat", "monitor", "smx", "pbe", "lm", "msr", "adx", "3dnowprefetch", "fpu", "fxsr", "syscall", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "ssbd", "pcid", "fma", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "abm", "est", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "nx", "aes", "sse2", "ss", "ds_cpl", "bmi1", "bmi2", "acpi", "ssse3", "rdseed", "cx16", "pse36", "mtrr", "movbe", "pdcm", "avx2", "rdrand", "x2apic"], "topology": {"cores": 10, "cells": 2, "threads": 2, "sockets": 1}} |
| disk_available_least | 364779 | 162479 | 229435 |
| free_ram_mb | 0 | 0 | 76984 |
| free_disk_gb | 642559 | 376144 | 686098 |
| current_workload | 0 | 0 | 0 |
| running_vms | 0 | 0 | 24 |
| hypervisor_hostname | cubic-10.yahoo.ca.com | vortex9-18.yahoo.ca.com | cosmo3-23.yahoo.ca.com |
| deleted | 0 | 85 | 0 |
| host_ip | 10.76.186.207/8 | 10.150.240.33/8 | 10.165.53.177/8 |
| supported_instances | [["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["aarch64", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "hvm"], ["microblaze", "qemu", "hvm"], ["microblazeel", "qemu", "hvm"], ["mips", "qemu", "hvm"], ["mipsel", "qemu", "hvm"], ["mips64", "qemu", "hvm"], ["mips64el", "qemu", "hvm"], ["openrisc", "qemu", "hvm"], ["ppc", "qemu", "hvm"], ["ppc64", "qemu", "hvm"], ["ppc64le", "qemu", "hvm"], ["ppcemb", "qemu", "hvm"], ["sh4", "qemu", "hvm"], ["sh4eb", "qemu", "hvm"], ["sparc", "qemu", "hvm"], ["sparc64", "qemu", "hvm"], ["unicore32", "qemu", "hvm"], ["x86_64", "qemu", "hvm"], ["x86_64", "kvm", "hvm"], ["xtensa", "qemu", "hvm"], ["xtensaeb", "qemu", "hvm"]] | [["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["aarch64", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "hvm"], ["microblaze", "qemu", "hvm"], ["microblazeel", "qemu", "hvm"], ["mips", "qemu", "hvm"], ["mipsel", "qemu", "hvm"], ["mips64", "qemu", "hvm"], ["mips64el", "qemu", "hvm"], ["openrisc", "qemu", "hvm"], ["ppc", "qemu", "hvm"], ["ppc64", "qemu", "hvm"], ["ppc64le", "qemu", "hvm"], ["ppcemb", "qemu", "hvm"], ["sh4", "qemu", "hvm"], ["sh4eb", "qemu", "hvm"], ["sparc", "qemu", "hvm"], ["sparc64", "qemu", "hvm"], ["unicore32", "qemu", "hvm"], ["x86_64", "qemu", "hvm"], ["x86_64", "kvm", "hvm"], ["xtensa", "qemu", "hvm"], ["xtensaeb", "qemu", "hvm"]] | [["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["aarch64", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "hvm"], ["microblaze", "qemu", "hvm"], ["microblazeel", "qemu", "hvm"], ["mips", "qemu", "hvm"], ["mipsel", "qemu", "hvm"], ["mips64", "qemu", "hvm"], ["mips64el", "qemu", "hvm"], ["openrisc", "qemu", "hvm"], ["ppc", "qemu", "hvm"], ["ppc64", "qemu", "hvm"], ["ppc64le", "qemu", "hvm"], ["ppcemb", "qemu", "hvm"], ["sh4", "qemu", "hvm"], ["sh4eb", "qemu", "hvm"], ["sparc", "qemu", "hvm"], ["sparc64", "qemu", "hvm"], ["unicore32", "qemu", "hvm"], ["x86_64", "qemu", "hvm"], ["x86_64", "kvm", "hvm"], ["xtensa", "qemu", "hvm"], ["xtensaeb", "qemu", "hvm"]] |
| pci_stats | {"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": [{"nova_object.version": "1.1", "nova_object.changes": ["count", "numa_node", "vendor_id", "product_id", "tags"], "nova_object.name": "PciDevicePool", "nova_object.data": {"count": 4, "numa_node": 0, "vendor_id": "10de", "product_id": "102d", "tags": {"dev_type": "type-PCI"}}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.1", "nova_object.changes": ["count", "numa_node", "vendor_id", "product_id", "tags"], "nova_object.name": "PciDevicePool", "nova_object.data": {"count": 4, "numa_node": 1, "vendor_id": "10de", "product_id": "102d", "tags": {"dev_type": "type-PCI"}}, "nova_object.namespace": "nova"}]}, "nova_object.namespace": "nova"} | {"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": []}, "nova_object.namespace": "nova"} | {"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": []}, "nova_object.namespace": "nova"} |
| metrics | [] | [] | [] |
| extra_resources | null | null | null |
| stats | {} | {} | {"num_task_None": "24", "num_proj_629cdb2191634719a8c97c8aaca2f5b1": "1", "io_workload": "0", "num_instances": "24", "num_proj_d5dea416238445dfa979e3abb838d4af": "1", "num_vm_active": "21", "num_proj_b3c6072810a24f67a7ac48e49a960e51": "1", "num_proj_9e2200862b674b3098afc897b0fbb977": "1", "num_proj_58034159195e4b77b18c2e20e44d4462": "1", "num_proj_c6d36b416dac49f193b4a209546ce370": "2", "num_proj_c182586b240f47ddb1a1bd6e0f41cc33": "1", "num_proj_e3fb2659584e436a832461dac02835f0": "5", "num_proj_5e35676c2c6947f29e1402b31c5b87a7": "1", "num_proj_5ae34f5a5ad843fbb8c370c99b66304b": "1", "num_vm_stopped": "3", "num_proj_62f1bd6e54e141f6abc0e78e51415269": "1", "num_proj_e7e8e8eca25741c8abc96fc07a103b94": "1", "num_proj_b1a541e6fa4e48e0aa7b20e347c8b436": "1", "num_os_type_None": "24", "num_proj_3be6c8b9f95842198466a9c673404768": "1", "num_proj_98333a1a28e746fa8c629c83a818ad57": "5"} |
| numa_topology | {"nova_object.version": "1.2", "nova_object.changes": ["cells"], "nova_object.name": "NUMATopology", "nova_object.data": {"cells": [{"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage", "memory_usage", "cpuset", "mempages", "pinned_cpus", "memory", "siblings", "id"], "nova_object.name": "NUMACell", "nova_object.data": {"cpu_usage": 0, "memory_usage": 0, "cpuset": [0, 1, 2, 3, 4, 5, 6, 7, 16, 17, 18, 19, 20, 21, 22, 23], "pinned_cpus": [], "siblings": [[2, 18], [1, 17], [0, 16], [19, 3], [22, 6], [20, 4], [23, 7], [5, 21]], "memory": 64383, "mempages": [{"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 16482241, "used": 0, "size_kb": 4}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 2048}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 1048576}, "nova_object.namespace": "nova"}], "id": 0}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage", "memory_usage", "cpuset", "mempages", "pinned_cpus", "memory", "siblings", "id"], "nova_object.name": "NUMACell", "nova_object.data": {"cpu_usage": 0, "memory_usage": 0, "cpuset": [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31], "pinned_cpus": [], "siblings": [[8, 24], [30, 14], [31, 15], [27, 11], [10, 26], [28, 12], [9, 25], [13, 29]], "memory": 64509, "mempages": [{"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 16514479, "used": 0, "size_kb": 4}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 2048}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 1048576}, "nova_object.namespace": "nova"}], "id": 1}, "nova_object.namespace": "nova"}]}, "nova_object.namespace": "nova"} | {"nova_object.version": "1.2", "nova_object.changes": ["cells"], "nova_object.name": "NUMATopology", "nova_object.data": {"cells": [{"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage", "memory_usage", "cpuset", "mempages", "pinned_cpus", "memory", "siblings", "id"], "nova_object.name": "NUMACell", "nova_object.data": {"cpu_usage": 0, "memory_usage": 0, "cpuset": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], "pinned_cpus": [], "siblings": [[8, 24], [2, 18], [10, 26], [0, 16], [28, 12], [22, 6], [30, 14], [20, 4]], "memory": 96640, "mempages": [{"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 24739915, "used": 0, "size_kb": 4}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 2048}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 1048576}, "nova_object.namespace": "nova"}], "id": 0}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage", "memory_usage", "cpuset", "mempages", "pinned_cpus", "memory", "siblings", "id"], "nova_object.name": "NUMACell", "nova_object.data": {"cpu_usage": 0, "memory_usage": 0, "cpuset": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], "pinned_cpus": [], "siblings": [[1, 17], [31, 15], [23, 7], [13, 29], [27, 11], [19, 3], [9, 25], [5, 21]], "memory": 96763, "mempages": [{"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 24771515, "used": 0, "size_kb": 4}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 2048}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 1048576}, "nova_object.namespace": "nova"}], "id": 1}, "nova_object.namespace": "nova"}]}, "nova_object.namespace": "nova"} | {"nova_object.version": "1.2", "nova_object.changes": ["cells"], "nova_object.name": "NUMATopology", "nova_object.data": {"cells": [{"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage", "memory_usage", "cpuset", "pinned_cpus", "siblings", "memory", "mempages", "id"], "nova_object.name": "NUMACell", "nova_object.data": {"cpu_usage": 0, "memory_usage": 0, "cpuset": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38], "pinned_cpus": [0, 2, 4, 8, 10, 12, 14, 16, 20, 22, 24, 28, 30, 32, 34, 36], "siblings": [[34, 14], [10, 30], [0, 20], [32, 12], [24, 4], [16, 36], [2, 22], [8, 28], [18, 38], [26, 6]], "memory": 128710, "mempages": [{"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 32949909, "used": 0, "size_kb": 4}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 2048}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 1048576}, "nova_object.namespace": "nova"}], "id": 0}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage", "memory_usage", "cpuset", "pinned_cpus", "siblings", "memory", "mempages", "id"], "nova_object.name": "NUMACell", "nova_object.data": {"cpu_usage": 0, "memory_usage": 0, "cpuset": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39], "pinned_cpus": [], "siblings": [[1, 21], [17, 37], [35, 15], [9, 29], [25, 5], [33, 13], [27, 7], [19, 39], [3, 23], [11, 31]], "memory": 129010, "mempages": [{"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 33026567, "used": 0, "size_kb": 4}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 2048}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.0", "nova_object.changes": ["total", "size_kb", "used"], "nova_object.name": "NUMAPagesTopology", "nova_object.data": {"total": 0, "used": 0, "size_kb": 1048576}, "nova_object.namespace": "nova"}], "id": 1}, "nova_object.namespace": "nova"}]}, "nova_object.namespace": "nova"} |
| host | cubic-10 | vortex9-18 | cosmo3-23 |
| ram_allocation_ratio | 0 | 0 | 0 |
| cpu_allocation_ratio | 0 | 0 | 0 |
| uuid | 5b0b8cb5-84e6-4cdf-9721-dffb37549727 | df67e717-c38f-47c6-91c3-83610de1f676 | 4b947532-ed33-47da-8ebe-0b74d0f39034 |
| disk_allocation_ratio | 0 | 0 | 0 |

## Columns

- created_at: all distinct
- updated_at: 126 distinct
- deleted_at: all distinct, nulls=43
- id: unique identifier, int 1..149
- service_id: 104 distinct, nulls=33, int 6..261
- vcpus: 24=66, 32=48, 40=20, 88=5, int 24..88
- memory_mb: 48292=48, 193403=21, 193404=20, 257720=19, 48294=6, 48295=5, 96676=5, 774004=5, 128893=2, 181307=2, 40228=1, 48164=1, 145019=1, 161147=1, 181308=1, 257719=1, int 40228..774004
- local_gb: 379868=61, 686780=33, 376144=11, 507931=8, 223452=5, 510310=5, 642559=5, 510717=4, 186210=3, 790=1, 916=1, 511508=1, 752475=1, int 790..752475
- vcpus_used: 45 distinct, int 0..585
  - stats: average=36.7770, median=0.0000
- memory_mb_used: 44 distinct, int 512..1912832
  - stats: average=76442.7050, median=512.0000
- local_gb_used: 44 distinct, int 0..3328
  - stats: average=190.1727, median=0.0000
- hypervisor_type: "QEMU"=139
- hypervisor_version: 2005000=128, 2000000=6, 2002000=3, 1005000=2, int 1005000..2005000
- cpu_info: "{"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["pge", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "acpi", "mmx", "cx8", "mce", "de", "rdtscp", "ht", "dca", "lahf_lm", "pdcm", "mca", "pdpe1gb", "apic", "sse", "pse", "ds", "invtsc", "pni", "tm2", "aes", "sse2", "ss", "ds_cpl", "pcid", "fpu", "cx16", "pse36", "mtrr", "popcnt"], "topology": {"cores": 6, "cells": 2, "threads": 2, "sockets": 1}}"=55, "{"vendor": "Intel", "model": "Broadwell-IBRS", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xtpr", "cmov", "hle", "smep", "spec-ctrl", "md-clear", "pat", "monitor", "smx", "pbe", "lm", "msr", "adx", "3dnowprefetch", "fpu", "fxsr", "syscall", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "ssbd", "pcid", "fma", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "abm", "est", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "nx", "aes", "sse2", "ss", "ds_cpl", "bmi1", "bmi2", "acpi", "ssse3", "rdseed", "cx16", "pse36", "mtrr", "movbe", "pdcm", "avx2", "rdrand", "x2apic"], "topology": {"cores": 10, "cells": 2, "threads": 2, "sockets": 1}}"=20, "{"vendor": "Intel", "model": "SandyBridge", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "xsave", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "acpi", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "pdcm", "mca", "pdpe1gb", "apic", "sse", "pse", "ds", "invtsc", "pni", "rdtscp", "aes", "sse2", "ss", "ds_cpl", "pcid", "fpu", "cx16", "pse36", "mtrr", "popcnt", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}}"=14, "{"vendor": "Intel", "model": "IvyBridge", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "fsgsbase", "xsave", "vmx", "erms", "xtpr", "cmov", "smep", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "acpi", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "aes", "sse2", "ss", "ds_cpl", "pcid", "fpu", "cx16", "pse36", "mtrr", "pdcm", "rdrand", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}}"=13, "{"vendor": "Intel", "model": "IvyBridge-IBRS", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "fsgsbase", "xsave", "vmx", "erms", "xtpr", "cmov", "smep", "ssse3", "md-clear", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "ssbd", "pcid", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "est", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "aes", "sse2", "ss", "ds_cpl", "acpi", "spec-ctrl", "fpu", "cx16", "pse36", "mtrr", "pdcm", "rdrand", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}}"=10, "{"vendor": "Intel", "model": "SandyBridge-IBRS", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "xsave", "vmx", "xtpr", "cmov", "ssse3", "md-clear", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "ssbd", "pcid", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "est", "pdcm", "mca", "pdpe1gb", "apic", "sse", "pse", "ds", "invtsc", "pni", "rdtscp", "aes", "sse2", "ss", "ds_cpl", "acpi", "spec-ctrl", "fpu", "cx16", "pse36", "mtrr", "popcnt", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}}"=6, "{"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["ssse3", "pge", "clflush", "sep", "syscall", "vme", "dtes64", "tsc", "vmx", "xtpr", "cmov", "pcid", "est", "pat", "monitor", "smx", "lm", "msr", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "acpi", "de", "mmx", "cx8", "mce", "mtrr", "tm2", "ht", "dca", "lahf_lm", "pdcm", "mca", "pdpe1gb", "apic", "sse", "pse", "ds", "pni", "rdtscp", "aes", "sse2", "ss", "pbe", "fpu", "cx16", "pse36", "ds_cpl", "popcnt"], "topology": {"cores": 6, "threads": 2, "sockets": 1}}"=6, "{"vendor": "Intel", "model": "Broadwell-IBRS", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xtpr", "cmov", "hle", "smep", "spec-ctrl", "md-clear", "pat", "monitor", "smx", "pbe", "lm", "msr", "adx", "3dnowprefetch", "fpu", "fxsr", "syscall", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "ssbd", "pcid", "fma", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "abm", "est", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "nx", "aes", "sse2", "ss", "ds_cpl", "bmi1", "bmi2", "acpi", "ssse3", "rdseed", "cx16", "pse36", "mtrr", "movbe", "pdcm", "avx2", "rdrand", "x2apic"], "topology": {"cores": 22, "cells": 2, "threads": 2, "sockets": 1}}"=5, "{"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["pge", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "acpi", "mmx", "cx8", "mce", "de", "rdtscp", "ht", "dca", "lahf_lm", "pdcm", "mca", "pdpe1gb", "apic", "sse", "pse", "ds", "invtsc", "pni", "tm2", "aes", "sse2", "ss", "ds_cpl", "pcid", "fpu", "cx16", "pse36", "mtrr", "popcnt"], "topology": {"cores": 6, "threads": 2, "sockets": 1}}"=3, "{"vendor": "Intel", "model": "Broadwell", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xtpr", "cmov", "hle", "smep", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "msr", "adx", "3dnowprefetch", "nx", "fxsr", "syscall", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "acpi", "fma", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "abm", "rdseed", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "avx2", "aes", "sse2", "ss", "ds_cpl", "bmi1", "bmi2", "pcid", "fpu", "cx16", "pse36", "mtrr", "movbe", "pdcm", "rdrand", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}}"=2, "{"vendor": "Intel", "model": "IvyBridge-IBRS", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "fsgsbase", "xsave", "vmx", "erms", "xtpr", "cmov", "smep", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "ssbd", "pcid", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "popcnt", "mca", "pdpe1gb", "apic", "sse", "f16c", "pse", "ds", "invtsc", "pni", "rdtscp", "aes", "sse2", "ss", "ds_cpl", "acpi", "spec-ctrl", "fpu", "cx16", "pse36", "mtrr", "pdcm", "rdrand", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}}"=2, "{"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["rdtscp", "pdpe1gb", "dca", "pcid", "pdcm", "xtpr", "tm2", "est", "smx", "vmx", "ds_cpl", "monitor", "dtes64", "pclmuldq", "pbe", "tm", "ht", "ss", "acpi", "ds", "vme"], "topology": {"cores": 6, "threads": 2, "sockets": 1}}"=2, "{"vendor": "Intel", "model": "SandyBridge-IBRS", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "xsave", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "monitor", "smx", "pbe", "lm", "tsc", "nx", "fxsr", "tm", "sse4.1", "pae", "sse4.2", "pclmuldq", "pcid", "tsc-deadline", "mmx", "osxsave", "cx8", "mce", "de", "tm2", "ht", "dca", "lahf_lm", "pdcm", "mca", "pdpe1gb", "apic", "sse", "pse", "ds", "invtsc", "pni", "rdtscp", "aes", "sse2", "ss", "ds_cpl", "acpi", "spec-ctrl", "fpu", "cx16", "pse36", "mtrr", "popcnt", "x2apic"], "topology": {"cores": 8, "cells": 2, "threads": 2, "sockets": 1}}"=1
- disk_available_least: 57 distinct, int 496..396651
  - stats: average=210288.3741, median=195844.0000
- free_ram_mb: 33 distinct, int 0..539508
  - stats: average=31066.6906, median=0.0000
- free_disk_gb: 58 distinct, int 620..752475
  - stats: average=465892.6475, median=379868.0000
- current_workload: 0=134, 1=4, 2=1, int 0..2
- running_vms: 26 distinct, int 0..55
  - stats: average=5.6475, median=0.0000
- hypervisor_hostname: 133 distinct
  - top_values: "blitz7-74.yahoo.ca.com"=2, "cubic-10.yahoo.ca.com"=2, "dash3-6.yahoo.ca.com"=2, "lumen4-89"=2, "quark-5.yahoo.ca.com"=2, "spike7-6.yahoo.ca.com"=2, "align-73.yahoo.ca.com"=1, "align-79.yahoo.ca.com"=1, "align-86.yahoo.ca.com"=1, "alpha-80.yahoo.ca.com"=1
- deleted: 97 distinct, int 0..144
  - stats: average=36.4892, median=28.0000
  - top_values: 0=43, 1=1, 2=1, 3=1, 4=1, 5=1, 6=1, 7=1, 8=1, 9=1
- host_ip: 125 distinct
- supported_instances: "[["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["aarch64", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "hvm"], ["microblaze", "qemu", "hvm"], ["microblazeel", "qemu", "hvm"], ["mips", "qemu", "hvm"], ["mipsel", "qemu", "hvm"], ["mips64", "qemu", "hvm"], ["mips64el", "qemu", "hvm"], ["openrisc", "qemu", "hvm"], ["ppc", "qemu", "hvm"], ["ppc64", "qemu", "hvm"], ["ppc64le", "qemu", "hvm"], ["ppcemb", "qemu", "hvm"], ["sh4", "qemu", "hvm"], ["sh4eb", "qemu", "hvm"], ["sparc", "qemu", "hvm"], ["sparc64", "qemu", "hvm"], ["unicore32", "qemu", "hvm"], ["x86_64", "qemu", "hvm"], ["x86_64", "kvm", "hvm"], ["xtensa", "qemu", "hvm"], ["xtensaeb", "qemu", "hvm"]]"=128, "[["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "hvm"], ["microblaze", "qemu", "hvm"], ["microblazeel", "qemu", "hvm"], ["mips", "qemu", "hvm"], ["mipsel", "qemu", "hvm"], ["mips64", "qemu", "hvm"], ["mips64el", "qemu", "hvm"], ["ppc", "qemu", "hvm"], ["ppc64", "qemu", "hvm"], ["ppcemb", "qemu", "hvm"], ["s390x", "qemu", "hvm"], ["sh4", "qemu", "hvm"], ["sh4eb", "qemu", "hvm"], ["sparc", "qemu", "hvm"], ["sparc64", "qemu", "hvm"], ["unicore32", "qemu", "hvm"], ["x86_64", "qemu", "hvm"], ["x86_64", "kvm", "hvm"], ["xtensa", "qemu", "hvm"], ["xtensaeb", "qemu", "hvm"]]"=7, "[["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["x86_64", "qemu", "hvm"], ["x86_64", "kvm", "hvm"]]"=4
- pci_stats: "{"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": []}, "nova_object.namespace": "nova"}"=130, "[]"=7, "{"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": [{"nova_object.version": "1.1", "nova_object.changes": ["count", "numa_node", "vendor_id", "product_id", "tags"], "nova_object.name": "PciDevicePool", "nova_object.data": {"count": 4, "numa_node": 0, "vendor_id": "10de", "product_id": "102d", "tags": {"dev_type": "type-PCI"}}, "nova_object.namespace": "nova"}, {"nova_object.version": "1.1", "nova_object.changes": ["count", "numa_node", "vendor_id", "product_id", "tags"], "nova_object.name": "PciDevicePool", "nova_object.data": {"count": 4, "numa_node": 1, "vendor_id": "10de", "product_id": "102d", "tags": {"dev_type": "type-PCI"}}, "nova_object.namespace": "nova"}]}, "nova_object.namespace": "nova"}"=2
- metrics: "[]"=131, "[{"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.user.percent", "value": 0.3661098901098901, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.kernel.time", "value": 319473170000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.iowait.percent", "value": 0.00018315018315018315, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.idle.time", "value": 205109180760000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.frequency", "value": 2268, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.iowait.time", "value": 29522840000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.percent", "value": 0.371018315018315, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.user.time", "value": 18704002500000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.idle.percent", "value": 0.6289816849816849, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.kernel.percent", "value": 0.0047252747252747255, "source": "libvirt.LibvirtDriver"}]"=1, "[{"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.user.percent", "value": 0.021698235158046565, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.kernel.time", "value": 326040000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.iowait.percent", "value": 0.0237903280673824, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.idle.time", "value": 5285800000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.frequency", "value": 2268, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.iowait.time", "value": 139870000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.percent", "value": 0.10094433331972623, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.user.time", "value": 127570000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.idle.percent", "value": 0.8990556666802738, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.kernel.percent", "value": 0.05545577009429726, "source": "libvirt.LibvirtDriver"}]"=1, "[{"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.user.percent", "value": 0.04069171794959948, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.kernel.time", "value": 318574840000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.iowait.percent", "value": 0.0001718980988070272, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.idle.time", "value": 287311841660000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.frequency", "value": 1600, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.iowait.time", "value": 54923410000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.percent", "value": 0.061525767525011175, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.user.time", "value": 737921510000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.idle.percent", "value": 0.9384742324749888, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.kernel.percent", "value": 0.02066215147660467, "source": "libvirt.LibvirtDriver"}]"=1, "[{"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.user.percent", "value": 0.26660726525017137, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.kernel.time", "value": 635416040000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.iowait.percent", "value": 0.00020562028786840302, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.idle.time", "value": 70595553200000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.frequency", "value": 1600, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.iowait.time", "value": 12200520000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.percent", "value": 0.2723029472241261, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.user.time", "value": 33129510930000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.idle.percent", "value": 0.7276970527758739, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.kernel.percent", "value": 0.0054900616860863605, "source": "libvirt.LibvirtDriver"}]"=1, "[{"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.user.percent", "value": 0.000685562334235875, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.kernel.time", "value": 872310000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.iowait.percent", "value": 0.00011079795300781819, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.idle.time", "value": 1144976300000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.frequency", "value": 1600, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.iowait.time", "value": 191540000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.percent", "value": 0.001142603890393125, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.user.time", "value": 1548090000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.idle.percent", "value": 0.9988573961096069, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.kernel.percent", "value": 0.0003462436031494318, "source": "libvirt.LibvirtDriver"}]"=1, "[{"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.user.percent", "value": 0.0007583611051199811, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.kernel.time", "value": 1700478940000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.iowait.percent", "value": 9.740417863926362e-05, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.idle.time", "value": 613884562510000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.frequency", "value": 1600, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.iowait.time", "value": 91440560000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.percent", "value": 0.0010992757303574037, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.user.time", "value": 30346972010000000, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.idle.percent", "value": 0.9989007242696426, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.kernel.percent", "value": 0.00024351044659815907, "source": "libvirt.LibvirtDriver"}]"=1, nulls=2
- extra_resources: all NULL
- stats: 49 distinct
- numa_topology: 50 distinct, nulls=5
- host: 126 distinct
  - top_values: ""=8, "lumen4-89"=3, "blitz7-74"=2, "cubic-10"=2, "quark-5"=2, "streak5-74"=2, "align-73"=1, "align-79"=1, "align-86"=1, "alpha-80"=1
- ram_allocation_ratio: 0=128, nulls=11
- cpu_allocation_ratio: 0=128, nulls=11
- uuid: all distinct, nulls=7
- disk_allocation_ratio: 0=128, nulls=11


# fixed_ips

```sql
CREATE TABLE `fixed_ips` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(39),
  `network_id` int,
  `allocated` tinyint(1),
  `leased` tinyint(1),
  `reserved` tinyint(1),
  `virtual_interface_id` int,
  `host` varchar(255),
  `instance_uuid` varchar(36),
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`address`,`deleted`),
  KEY (`virtual_interface_id`),
  KEY (`address`),
  KEY (`instance_uuid`),
  KEY (`host`),
  KEY (`network_id`,`host`,`deleted`),
  KEY (`address`,`reserved`,`network_id`,`deleted`),
  KEY (`address`,`deleted`,`allocated`),
  KEY (`deleted`,`allocated`,`updated_at`),
  CONSTRAINT `fixed_ips_instance_uuid_fkey` FOREIGN KEY (`instance_uuid`) REFERENCES `instances` (`uuid`)
) AUTO_INCREMENT=66305;
```

## Rows

- total=63724

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2012-09-07T13:52:47 | 2012-09-07T13:52:42 | 2012-09-07T13:52:19 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 66304 | 57258 | 11543 |
| address | 10.223.191.20/8 | 10.161.223.67/8 | 10.158.52.134/8 |
| network_id | 1 | 1 | 1 |
| allocated | 0 | 0 | 0 |
| leased | 0 | 0 | 0 |
| reserved | 1 | 0 | 0 |
| virtual_interface_id | null | null | null |
| host |  |  |  |
| instance_uuid | null | null | null |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 34 distinct
- updated_at: 531 distinct, nulls=62716
  - top_values: 2013-05-01 20:51:55=25, 2013-08-09 21:13:26=24, 2013-08-09 02:42:12=23, 2013-05-01 19:07:40=21, 2013-05-01 19:08:40=13, 2013-05-01 20:49:55=13, 2013-05-01 19:13:41=11, 2013-05-01 19:06:40=10, 2013-05-01 19:09:40=10, 2013-05-01 19:12:41=10
- deleted_at: all NULL
- id: unique identifier, int 769..66304
- address: all distinct
- network_id: 1=63724
- allocated: 0=63724
- leased: 0=63724
- reserved: 0=63721, 1=3
- virtual_interface_id: all NULL
- host: 62 distinct
  - top_values: ""=63663, "align-73"=1, "align-79"=1, "arrow-57"=1, "astro1-40"=1, "blaze1-11"=1, "blitz7-74"=1, "celes-28"=1, "dash3-6"=1, "drift-42"=1
- instance_uuid: all NULL
- deleted: 0=63724


# floating_ips

```sql
CREATE TABLE `floating_ips` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(39),
  `fixed_ip_id` int,
  `project_id` varchar(255),
  `host` varchar(255),
  `auto_assigned` tinyint(1),
  `pool` varchar(255),
  `interface` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`address`,`deleted`),
  KEY (`fixed_ip_id`),
  KEY (`host`),
  KEY (`project_id`),
  KEY (`pool`,`deleted`,`fixed_ip_id`,`project_id`)
) AUTO_INCREMENT=8191;
```

## Rows

- total=8190

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2012-07-05T19:22:43 | 2012-07-05T19:20:28 | 2012-07-05T19:20:33 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 8190 | 2839 | 3055 |
| address | 10.13.139.247/8 | 10.135.193.90/8 | 10.18.173.207/8 |
| fixed_ip_id | null | null | null |
| project_id | null | null | null |
| host | null | null | null |
| auto_assigned | 0 | 0 | 0 |
| pool | nova | nova | nova |
| interface | eth0 | eth0 | eth0 |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 208 distinct
- updated_at: 150 distinct, nulls=8019
- deleted_at: all NULL
- id: unique identifier, int 1..8190
- address: all distinct
- fixed_ip_id: all NULL
- project_id: 24 distinct, nulls=8020
  - top_values: "3008a142e9524f7295b06ea811908f93"=37, "292c70904ce7415c8626f801bbf1ed0c"=30, "6f5103a9ae434375a92a1de24a19ca56"=25, "98333a1a28e746fa8c629c83a818ad57"=11, "71322eb9ba804fc4ae74cefde3ad0742"=10, "956ae20bbb444a8c8f149729198aec63"=7, "4e101cf5264b4e739b7b5ebe0f6b5c68"=6, "34f87362758043a98ea19c5a5e9217c9"=5, "b7188a889c6a4800893445d969673bab"=5, "d0ebc85936794a30b65bb6dae5687404"=5
- host: all NULL
- auto_assigned: 0=8190
- pool: "nova"=8190
- interface: "eth0"=8190
- deleted: 0=8190


# instance_actions

```sql
CREATE TABLE `instance_actions` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `action` varchar(255),
  `instance_uuid` varchar(36),
  `request_id` varchar(255),
  `user_id` varchar(255),
  `project_id` varchar(255),
  `start_time` datetime,
  `finish_time` datetime,
  `message` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`),
  KEY (`instance_uuid`),
  KEY (`request_id`),
  CONSTRAINT `fk_instance_actions_instance_uuid` FOREIGN KEY (`instance_uuid`) REFERENCES `instances` (`uuid`)
) AUTO_INCREMENT=650158;
```

## Rows

- total=27472

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-07-05T20:28:18 | 2021-02-09T03:49:24 | 2020-02-10T19:31:12 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 650157 | 615489 | 602514 |
| action | stop | stop | delete |
| instance_uuid | 81606363-89ce-4172-93ff-63d26cdbd0b1 | d64d55ff-7efa-432a-a088-bbb18aa88d96 | b8149e21-b3ee-4a42-834a-1420a0c8de3a |
| request_id | req-6b9be970-4f72-48b2-ad39-a545b9506c41 | req-4b9121b8-e71e-4b42-aa7a-55919a8ffc78 | req-e7f917b0-76e6-4ec3-8249-aaa1a3c04c2f |
| user_id | 16d15017af6749c89af3cb547a3a28ff | 19095b2bd31a4f55bc7520e3a61556a2 | a1ef823458d24a68955fec6f3d390019 |
| project_id | a5c6a169183342b989557bb95c7b8e0b | 7202a43be6fa4aec8387216260a4fae7 | 98333a1a28e746fa8c629c83a818ad57 |
| start_time | 2024-07-05T20:28:17 | 2021-02-09T03:49:24 | 2020-02-10T19:31:11 |
| finish_time | null | null | null |
| message | null | null | null |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 23931 distinct
- updated_at: 884 distinct, nulls=26399
- deleted_at: all NULL
- id: unique identifier, int 115259..650157
- action: 23 distinct
- instance_uuid: 7218 distinct
  - top_values: "74334240-be67-4c1c-8295-9b6fcbbf8b9e"=196, "d2175cc8-2291-4575-bd91-6ad630003504"=104, "712a70cf-d00c-4c5b-8951-459012e56c08"=81, "3a428bb4-d4c2-4bd7-9433-b4b7a7ba9735"=60, "6869e646-0794-4207-8c16-cd196b535713"=52, "b78f7192-68f4-4cc1-a6a1-6a66692b612b"=50, "7cc17fdb-b107-4d13-ad5c-32c9dfec5abe"=49, "b8e529b0-87c9-4bb3-bdcb-9b83ceceea87"=45, "9b47723a-f295-451f-80ae-5d68e70fe9f7"=44, "a5b3463c-91c3-447a-b054-b89483e5ed75"=42
- request_id: 25464 distinct
  - top_values: "req-ba99e8ba-67eb-4893-a936-32e652f4f51f"=97, "req-255f06b8-f402-4698-b842-2f590902ab7e"=80, "req-bdafb6e5-08eb-481e-a088-04af324a2555"=40, "req-b653c71e-6dc3-4d24-a291-4bb8a75b1dfa"=28, "req-bf7e9a8c-1e78-4afa-baf3-c78709ed6368"=27, "req-29d94e17-61f2-4b59-af54-b6a2318bb521"=26, "req-0c18809b-a8a1-443e-a6a8-9d928458bbd8"=25, "req-0f3f7178-36fb-4a50-bc8e-fadf66bf03ad"=24, "req-2c261d80-529c-461b-b7be-a368686262a0"=22, "req-fc6fc800-1a62-43ef-a25a-401a7b7b65e6"=22
- user_id: 568 distinct, nulls=1701
- project_id: 481 distinct, nulls=1701
- start_time: 23719 distinct
- finish_time: all NULL
- message: "Error"=1073, nulls=26399
- deleted: 0=27472


# instance_actions_events

```sql
CREATE TABLE `instance_actions_events` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `event` varchar(255),
  `action_id` int,
  `start_time` datetime,
  `finish_time` datetime,
  `result` varchar(255),
  `traceback` text,
  `deleted` int,
  `host` varchar(255),
  `details` text,
  PRIMARY KEY (`id`),
  KEY (`action_id`),
  CONSTRAINT `instance_actions_events_ibfk_1` FOREIGN KEY (`action_id`) REFERENCES `instance_actions` (`id`)
) AUTO_INCREMENT=795648;
```

## Rows

- total=41690

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-07-05T20:28:18 | 2018-12-11T05:50:38 | 2022-03-03T15:16:14 |
| updated_at | 2024-07-05T20:28:25 | 2018-12-11T05:50:43 | 2022-03-03T15:16:18 |
| deleted_at | null | null | null |
| id | 795647 | 725780 | 783914 |
| event | compute_stop_instance | compute_check_can_live_migrate_source | compute_check_can_live_migrate_source |
| action_id | 650157 | 590091 | 641935 |
| start_time | 2024-07-05T20:28:18 | 2018-12-11T05:50:38 | 2022-03-03T15:16:14 |
| finish_time | 2024-07-05T20:28:25 | 2018-12-11T05:50:42 | 2022-03-03T15:16:18 |
| result | Success | Success | Success |
| traceback | null | null | null |
| deleted | 0 | 0 | 0 |
| host | null | null | null |
| details | null | null | null |

## Columns

- created_at: 33215 distinct
- updated_at: 32409 distinct, nulls=2522
- deleted_at: all NULL
- id: unique identifier, int 181740..795647
- event: 35 distinct
- action_id: 26251 distinct, int 115259..650157
  - top_values: 635476=27, 641794=27, 635226=23, 636850=15, 636904=15, 637012=15, 637015=15, 639025=15, 639027=15, 640039=15
- start_time: 33213 distinct
- finish_time: 32406 distinct, nulls=2522
- result: "Success"=38080, "Error"=1088, nulls=2522
- traceback: 167 distinct, nulls=40579
- deleted: 0=41690
- host: all NULL
- details: all NULL


# instance_extra

```sql
CREATE TABLE `instance_extra` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `deleted` int,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_uuid` varchar(36) NOT NULL,
  `numa_topology` text,
  `pci_requests` text,
  `flavor` text,
  `vcpu_model` text,
  `migration_context` text,
  PRIMARY KEY (`id`),
  KEY (`instance_uuid`),
  CONSTRAINT `instance_extra_instance_uuid_fkey` FOREIGN KEY (`instance_uuid`) REFERENCES `instances` (`uuid`)
) AUTO_INCREMENT=218600;
```

## Rows

- total=7253

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2020-05-29T00:11:01 | 2020-06-11T17:36:55 |
| updated_at | 2024-06-26T20:40:27 | 2020-05-29T00:14:02 | null |
| deleted_at | null | 2020-05-29T00:14:03 | 2020-06-11T17:36:55 |
| deleted | 0 | 213387 | 213521 |
| id | 218599 | 213387 | 213521 |
| instance_uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | 8d4b5645-2d99-48ce-b873-13a6bfc6a4d1 | 4fe5d618-3fa5-437d-afc5-ccff3124d601 |
| numa_topology | null | null | null |
| pci_requests | [] | [] | [] |
| flavor | {"new": null, "old": null, "cur": {"nova_object.version": "1.1", "nova_object.changes": ["extra_specs"], "nova_object.name": "Flavor", "nova_object.data": {"disabled": false, "root_gb": 32, "name": "lg.2core", "flavorid": "3100", "deleted": false, "created_at": "2013-08-15T19:20:04Z", "ephemeral_gb": 0, "updated_at": null, "memory_mb": 4096, "vcpus": 2, "extra_specs": {"overcommit": "default"}, "swap": 0, "rxtx_factor": 1.0, "is_public": true, "deleted_at": null, "vcpu_weight": 0, "id": 72}, "nova_object.namespace": "nova"}} | {"new": null, "old": null, "cur": {"nova_object.version": "1.1", "nova_object.changes": ["extra_specs"], "nova_object.name": "Flavor", "nova_object.data": {"disabled": false, "root_gb": 32, "name": "ups.2c2g", "flavorid": "ef2521ec-6368-43bf-bb63-9fe9d0b5527f", "deleted": false, "created_at": "2014-10-14T15:00:48Z", "ephemeral_gb": 0, "updated_at": null, "memory_mb": 2048, "vcpus": 2, "extra_specs": {"ups": "true"}, "swap": 0, "rxtx_factor": 1.0, "is_public": true, "deleted_at": null, "vcpu_weight": 0, "id": 130}, "nova_object.namespace": "nova"}} | {"new": null, "old": null, "cur": {"nova_object.version": "1.1", "nova_object.name": "Flavor", "nova_object.data": {"disabled": false, "root_gb": 32, "name": "tig.2c8g", "flavorid": "927d4ba8-26f8-4ea3-9451-699a430a7d87", "deleted": false, "created_at": "2015-04-10T15:23:12Z", "ephemeral_gb": 0, "updated_at": null, "memory_mb": 8192, "vcpus": 2, "extra_specs": {"tig": "true"}, "swap": 0, "rxtx_factor": 1.0, "is_public": false, "deleted_at": null, "vcpu_weight": 0, "id": 142}, "nova_object.namespace": "nova"}} |
| vcpu_model | {"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 2}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"} | {"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 2}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"} | null |
| migration_context | null | null | null |

## Columns

- created_at: 6330 distinct
- updated_at: 6480 distinct, nulls=9
- deleted_at: 4999 distinct, nulls=1512
- deleted: 5742 distinct, int 0..218597
  - stats: average=166267.5532, median=213320.0000
- id: unique identifier, int 1505..218599
- instance_uuid: 7226 distinct
  - top_values: "06eda471-651e-41bc-abb0-c332b6780a11"=2, "089aac34-c8c9-4228-89cb-e6d2d7b77e6f"=2, "274b1e63-823d-4bab-afb7-3db2f1df0896"=2, "3517d34c-81ba-4306-a98e-9a8cf509901b"=2, "3916f643-e660-486e-93ec-7f1ff3a88c90"=2, "411d757f-410d-4271-832a-31d451709dce"=2, "59ecc603-b6df-4c2c-aa81-51222e1e6b51"=2, "72a454ef-c141-4cc8-9ad2-c361aeedb462"=2, "7aac3e60-531c-4587-b764-dbb87f4065f5"=2, "7c2ad9e7-a631-4866-b30f-30eaa321f6cf"=2
- numa_topology: all distinct, nulls=7189
- pci_requests: "[]"=7171, "[{"count": 1, "request_id": null, "alias_name": "gpu", "spec": [{"vendor_id": "10de", "product_id": "102d"}], "is_new": false}]"=4, "[{"count": 2, "request_id": null, "alias_name": "gpu", "spec": [{"vendor_id": "10de", "product_id": "102d"}], "is_new": false}]"=1, nulls=77
- flavor: 199 distinct
- vcpu_model: "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 2}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=1780, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 1}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=1661, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 4}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=1418, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 8}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=957, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 24}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=497, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 16}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=235, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 12}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=225, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 8, "threads": 2, "sockets": 1}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=57, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 32}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=50, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 88}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=6, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 64}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=4, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 44}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=3, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 8, "threads": 1, "sockets": 1}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"}"=3, nulls=357
- migration_context: 214 distinct, nulls=7038


# instance_faults

```sql
CREATE TABLE `instance_faults` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_uuid` varchar(36),
  `code` int NOT NULL,
  `message` varchar(255),
  `details` text,
  `host` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`),
  KEY (`host`),
  KEY (`instance_uuid`,`deleted`,`created_at`),
  CONSTRAINT `fk_instance_faults_instance_uuid` FOREIGN KEY (`instance_uuid`) REFERENCES `instances` (`uuid`)
) AUTO_INCREMENT=209904;
```

## Rows

- total=5624

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-22T20:00:45 | 2021-05-10T21:13:46 | 2021-10-05T13:55:45 |
| updated_at | null | null | null |
| deleted_at | 2024-06-22T20:00:59 | 2021-05-12T21:46:50 | 2022-11-22T18:05:34 |
| id | 209903 | 206102 | 206705 |
| instance_uuid | 80ad4b7a-d2ff-46d2-b5e9-e88a357b6d74 | 917c0095-e1c4-4f4b-8e88-eafff054fec0 | 6d744cb3-d507-4e6f-a8ba-130ef74fb77c |
| code | 500 | 400 | 400 |
| message | 5ad43fc335ae8814d8ebe3345626860a | 4186c8343c8615354b6b88ffcb2914a0 | 2d0e15dab10de73df3952d60ba61741b |
| details | fb2141c5c0978bee9f87d0e1a0b4fe39 | null | null |
| host | cosmo3-23 | gamut-16 | galax4-70 |
| deleted | 209903 | 206102 | 206705 |

## Columns

- created_at: 4562 distinct
  - top_values: 2021-10-05 14:35:37=12, 2021-10-05 15:53:01=12, 2015-10-02 14:31:19=10, 2016-10-12 16:56:19=9, 2021-10-05 12:52:33=9, 2021-10-05 13:43:16=9, 2021-10-05 14:34:26=9, 2021-10-05 15:15:32=9, 2021-10-05 15:36:15=9, 2015-11-02 19:26:06=8
- updated_at: all NULL
- deleted_at: 822 distinct, nulls=1388
- id: unique identifier, int 175047..209903
- instance_uuid: 1252 distinct
  - top_values: "64d7cd79-6dc6-404c-b603-8cdd4f9263a0"=1010, "f651937a-8bcd-43f1-910e-f5b61fa358ac"=919, "075cd164-eac4-451d-9e8b-f88f96b20b41"=308, "e945b2b7-da17-4e24-ab43-de3c3360eea4"=295, "023de0aa-70a8-42f8-892c-be860e3f2890"=36, "3bc21419-2061-42eb-bc48-8417001cfbdc"=34, "5de2ff89-ff04-4cbe-8e00-3837479ba2f1"=29, "85aafec6-1b2e-423a-b834-d4a526068dec"=28, "ca7d8583-76b2-42f8-a8c6-102ce9ce56b1"=28, "7f7db4fc-3f92-4f90-9a34-7034fe0f3e90"=23
- code: 500=4004, 400=1610, 404=10, int 400..500
- message: 921 distinct
- details: 885 distinct, nulls=1670
- host: 121 distinct
  - top_values: "spark9-96"=1964, "gamut-16"=441, "shine-94"=415, "glint3-93"=308, "flare4-57"=130, "forge-23"=128, "blaze8-12"=111, "align-86"=98, "blitz1-32"=90, "beam8-22"=83
- deleted: 4237 distinct, int 0..209903
  - stats: average=155071.6981, median=206629.5000
  - top_values: 0=1388, 190215=1, 190246=1, 190248=1, 190249=1, 190252=1, 190262=1, 190263=1, 190424=1, 190501=1


# instance_group_member

```sql
CREATE TABLE `instance_group_member` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `deleted` int,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_id` varchar(255),
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY (`group_id`),
  KEY (`instance_id`),
  CONSTRAINT `instance_group_member_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `instance_groups` (`id`)
) AUTO_INCREMENT=4170;
```

## Rows

- total=4085

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-05-06T17:00:37 | 2019-05-17T22:06:14 | 2021-06-26T02:11:16 |
| updated_at | null | null | null |
| deleted_at | null | 2019-05-22T15:44:07 | 2021-07-01T02:47:22 |
| deleted | 0 | 2054 | 3909 |
| id | 4169 | 2054 | 3909 |
| instance_id | fe849f1d-bfa7-4b76-95fb-37e5b83920cf | d2b9fac0-40be-44e3-8bb6-67d848652ab3 | ba91257a-fc13-436d-a613-04cb6d994c82 |
| group_id | 216 | 70 | 187 |

## Columns

- created_at: 2866 distinct
- updated_at: all NULL
- deleted_at: 2210 distinct, nulls=56
- deleted: 4030 distinct, int 0..4167
  - stats: average=2100.1053, median=2110.0000
- id: unique identifier, int 1..4169
- instance_id: unique identifier
- group_id: 210 distinct, int 1..230
  - top_values: 32=228, 33=207, 1=200, 34=95, 99=90, 128=88, 39=79, 46=74, 41=60, 31=54


# instance_group_policy

```sql
CREATE TABLE `instance_group_policy` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `deleted` int,
  `id` int NOT NULL AUTO_INCREMENT,
  `policy` varchar(255),
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY (`group_id`),
  KEY (`policy`),
  CONSTRAINT `instance_group_policy_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `instance_groups` (`id`)
) AUTO_INCREMENT=231;
```

## Rows

- total=228

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2023-10-01T15:36:55 | 2018-12-11T21:35:30 | 2021-06-05T02:40:22 |
| updated_at | null | null | null |
| deleted_at | 2024-01-20T18:06:45 | 2019-02-04T21:02:39 | 2021-06-08T21:41:27 |
| deleted | 230 | 50 | 178 |
| id | 230 | 50 | 178 |
| policy | anti-affinity | anti-affinity | anti-affinity |
| group_id | 230 | 50 | 178 |

## Columns

- created_at: 151 distinct
- updated_at: all NULL
- deleted_at: 159 distinct, nulls=28
- deleted: 201 distinct, int 0..230
  - stats: average=103.7368, median=106.5000
- id: unique identifier, int 1..230
- policy: "anti-affinity"=225, "affinity"=3
- group_id: unique identifier, int 1..230


# instance_groups

```sql
CREATE TABLE `instance_groups` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `deleted` int,
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255),
  `project_id` varchar(255),
  `uuid` varchar(36) NOT NULL,
  `name` varchar(255),
  PRIMARY KEY (`id`),
  UNIQUE KEY (`uuid`,`deleted`)
) AUTO_INCREMENT=231;
```

## Rows

- total=230

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2023-10-01T15:36:55 | 2017-08-16T00:56:54 | 2021-06-05T02:40:22 |
| updated_at | null | null | null |
| deleted_at | 2024-01-20T18:06:45 | 2017-08-29T22:01:20 | 2021-06-08T21:41:08 |
| deleted | 230 | 32 | 180 |
| id | 230 | 32 | 180 |
| user_id | 77047e1a20db46b2b8d8daebb9e39fe8 | a1ef823458d24a68955fec6f3d390019 | a1ef823458d24a68955fec6f3d390019 |
| project_id | 5b92ec1146d04f9091ab48b6cdba3eff | 17ea94ad74b64b9d92f4888336a598c7 | 17ea94ad74b64b9d92f4888336a598c7 |
| uuid | 6857e997-f7b1-437c-b63b-2b93227f454d | 38bb5b5c-6ede-4a36-83d6-c95a73f3d668 | 13067039-1f7e-41f8-a065-2fcb2ad57474 |
| name | alpha4-glyph | vortx-beam | comet6-twist |

## Columns

- created_at: 154 distinct
- updated_at: all NULL
- deleted_at: 161 distinct, nulls=28
- deleted: 203 distinct, int 0..230
  - stats: average=102.9348, median=105.5000
  - top_values: 0=28, 1=1, 2=1, 3=1, 4=1, 11=1, 12=1, 13=1, 14=1, 15=1
- id: unique identifier, int 1..230
- user_id: "a1ef823458d24a68955fec6f3d390019"=187, "77047e1a20db46b2b8d8daebb9e39fe8"=25, "5302e30e168c4db283fc8e07009bb98f"=8, "c0a5d12d08874376a517eca2db78c3ca"=6, "7632ba71167341ff9697e116553c90f3"=2, "0be8fa0d641a4e778b9262bd2e5f40b5"=1, "ed22eaa324ea4dff812c57a199d3abd4"=1
- project_id: "17ea94ad74b64b9d92f4888336a598c7"=140, "98333a1a28e746fa8c629c83a818ad57"=48, "5b92ec1146d04f9091ab48b6cdba3eff"=25, "d7abb5f8e61a48e1a411b07aa2aeb152"=6, "47c0857cf5b5452a86f640fd44be1d40"=5, "bfd50153a2e9476f93e33e30e922cd06"=4, "09ad05432f914e26bc417bf58f1cb4d2"=2
- uuid: unique identifier
- name: 36 distinct


# instance_id_mappings

```sql
CREATE TABLE `instance_id_mappings` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `deleted` int,
  PRIMARY KEY (`id`),
  KEY (`uuid`)
) AUTO_INCREMENT=749370;
```

## Rows

- total=277653

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2015-03-04T02:30:58 | 2015-02-04T15:16:22 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 749369 | 551687 | 531967 |
| uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | ac807920-1f42-4b3c-ae98-971f2264c2d1 | 78fe30d4-95d2-420e-98d6-5359b59b1b84 |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: profile metrics skipped
- updated_at: all NULL
- deleted_at: all NULL
- id: unique identifier, int 446931..749369
- uuid: unique identifier
- deleted: int 0..0
  - stats: average=0.0000


# instance_info_caches

```sql
CREATE TABLE `instance_info_caches` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `network_info` text,
  `instance_uuid` varchar(36) NOT NULL,
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`instance_uuid`),
  CONSTRAINT `instance_info_caches_instance_uuid_fkey` FOREIGN KEY (`instance_uuid`) REFERENCES `instances` (`uuid`)
) AUTO_INCREMENT=749460;
```

## Rows

- total=7226

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2020-02-12T20:46:42 | 2020-02-13T19:01:24 |
| updated_at | 2024-07-08T06:17:59 | 2020-03-24T03:00:53 | 2020-02-13T19:59:59 |
| deleted_at | null | 2020-03-24T03:00:53 | 2020-02-13T19:59:59 |
| id | 749459 | 743280 | 743299 |
| network_info | [{"profile": {}, "ovs_interfaceid": "0639c4ce-dc51-4d07-baa5-109c5db4a609", "preserve_on_delete": false, "network": {"bridge": "br-int", "subnets": [{"ips": [{"meta": {}, "version": 4, "type": "fixed", "floating_ips": [], "address": "10.21.26.53/8"}], "version": 4, "meta": {"dhcp_server": "10.151.244.184/8"}, "dns": [{"meta": {}, "version": 4, "type": "dns", "address": "10.49.228.132/8"}, {"meta": {}, "version": 4, "type": "dns", "address": "10.67.40.40/8"}, {"meta": {}, "version": 4, "type": "dns", "address": "10.229.203.154/8"}], "routes": [{"interface": null, "cidr": "10.169.77.216/8", "meta": {}, "gateway": {"meta": {}, "version": 4, "type": "gateway", "address": "10.232.49.230/8"}}], "cidr": "10.37.117.235/8", "gateway": {"meta": {}, "version": 4, "type": "gateway", "address": "10.51.22.157/8"}}], "meta": {"injected": false, "tenant_id": "6f9adccbd03e4d2186756896957a14bf", "mtu": 9000}, "id": "0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d", "label": "inet"}, "devname": "tap0639c4ce-dc", "vnic_type": "normal", "qbh_params": null, "meta": {}, "details": {"port_filter": true, "ovs_hybrid_plug": true}, "address": "fa:16:3e:50:7a:7a", "active": true, "type": "ovs", "id": "0639c4ce-dc51-4d07-baa5-109c5db4a609", "qbg_params": null}] | [] | [] |
| instance_uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | a16f0f85-7f8e-44de-b987-18f7ac5bad5f | 2f4b8145-4406-4be5-82f2-c95e7ae1adea |
| deleted | 0 | 743280 | 743299 |

## Columns

- created_at: 6340 distinct
- updated_at: 6142 distinct, nulls=321
- deleted_at: 5021 distinct, nulls=1485
- id: unique identifier, int 509070..749459
- network_info: 1501 distinct
- instance_uuid: unique identifier
- deleted: 5742 distinct, int 0..749457
  - stats: average=588578.2690, median=744200.0000


# instance_metadata

```sql
CREATE TABLE `instance_metadata` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `key` varchar(255),
  `value` varchar(255),
  `instance_uuid` varchar(36),
  `deleted` int,
  PRIMARY KEY (`id`),
  KEY (`instance_uuid`),
  CONSTRAINT `instance_metadata_instance_uuid_fkey` FOREIGN KEY (`instance_uuid`) REFERENCES `instances` (`uuid`)
) AUTO_INCREMENT=574;
```

## Rows

- total=36

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2024-06-23T01:42:27 | 2024-06-22T22:53:48 |
| updated_at | null | null | null |
| deleted_at | null | 2024-06-26T20:37:18 | 2024-06-22T23:36:14 |
| id | 573 | 572 | 568 |
| key | csail | csail | csail |
| value | true | true | true |
| instance_uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | 11835f49-fb75-4acd-bd9a-9f3ab0bbed4e | f772c9a5-9a95-47f0-973a-4ea15eccf597 |
| deleted | 0 | 572 | 568 |

## Columns

- created_at: 35 distinct
- updated_at: 2022-10-21 13:55:20=1, nulls=35
- deleted_at: 29 distinct, nulls=5
- id: unique identifier, int 538..573
- key: "csail"=22, "hostname"=5, "sweep"=3, "image_version"=1, "release"=1, "RT"=1, "system"=1, "system_role"=1, "verified"=1
- value: "true"=22, "1"=2, "testy-mcansibleface-1"=2, "testy-mcansibleface-2"=2, "0"=1, "191716"=1, "2024-03-26"=1, "bionic"=1, "bionic_cloudimg"=1, "igorprod"=1, "igorprod_master"=1, "testy-mcansibleface-3"=1
- instance_uuid: 34 distinct
  - top_values: "942e264b-57c5-4f62-a21a-12f48401bdce"=2, "dfa40a23-a04c-4ca5-9b3b-e93a6a1c8b42"=2, "021a3b85-9932-4fd4-adbf-41d9645bfa72"=1, "03462f9f-d604-447d-99f2-50f7ab60204b"=1, "11199144-6f33-40ad-a81f-46e68a7a9d63"=1, "11835f49-fb75-4acd-bd9a-9f3ab0bbed4e"=1, "1d22482a-e321-4e41-a7a5-18d17cce998c"=1, "2aeb7403-595d-458b-97a2-9554bf844a8b"=1, "2d08a24d-cc48-4fea-8b84-1c39fa6c8cbd"=1, "3a782bc7-5d5c-48ec-95bb-2d9ff2997e80"=1
- deleted: 32 distinct, int 0..572
  - stats: average=479.5000, median=554.5000


# instance_system_metadata

```sql
CREATE TABLE `instance_system_metadata` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_uuid` varchar(36) NOT NULL,
  `key` varchar(255) NOT NULL,
  `value` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`),
  KEY (`instance_uuid`),
  CONSTRAINT `instance_system_metadata_ibfk_1` FOREIGN KEY (`instance_uuid`) REFERENCES `instances` (`uuid`)
) AUTO_INCREMENT=12281807;
```

## Rows

- total=76723

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2016-02-17T19:58:20 | 2024-01-26T16:34:15 |
| updated_at | null | null | null |
| deleted_at | null | null | 2024-01-26T16:37:39 |
| id | 12281805 | 11597161 | 12278466 |
| instance_uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | 2a6bd728-29be-482b-ab28-0fc35bec0dfd | 50695301-af65-4d64-aac0-29bfc9ae6a1b |
| key | image_base_image_ref | image_container_format | image_owner_specified.openstack.object |
| value | null | glint-shine | flare_radar |
| deleted | 0 | 0 | 12278466 |

## Columns

- created_at: 13321 distinct
- updated_at: 1424 distinct, nulls=75102
- deleted_at: 4997 distinct, nulls=17997
- id: unique identifier, int 8417981..12281805
- instance_uuid: 7226 distinct
  - top_values: "7aa0b283-fb49-4cc1-85aa-69e9c23bea62"=34, "f84c1ec8-cc70-49da-9955-88fbc44b1990"=30, "7711aa9b-492f-4620-8414-c5fc09c1f3fa"=29, "2be350ed-edab-4734-b721-7dd36ee03286"=28, "51e32669-00b1-4d79-a93b-05a92b2fa747"=28, "af938383-e6ff-4444-9f3b-3f6bcb118840"=28, "bd67d93a-c153-41b3-9ec9-64c8082fc8ed"=28, "f3d0b8e7-5867-4c4a-bdc0-c7eab1a1e713"=28, "047088e3-7e80-4e23-b33c-65ff168b35b9"=27, "0d1fe166-36ea-4f5d-926f-b8aa385e353f"=27
- key: 60 distinct
- value: 2598 distinct, nulls=2562
- deleted: 58727 distinct, int 0..12281803
  - stats: average=9327251.1266, median=12223005.0000


# instance_type_extra_specs

```sql
CREATE TABLE `instance_type_extra_specs` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_type_id` int NOT NULL,
  `key` varchar(255),
  `value` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`instance_type_id`,`key`,`deleted`),
  KEY (`instance_type_id`,`key`),
  CONSTRAINT `instance_type_extra_specs_ibfk_1` FOREIGN KEY (`instance_type_id`) REFERENCES `instance_types` (`id`)
) AUTO_INCREMENT=189;
```

## Rows

- total=135

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-02-23T14:18:22 | 2018-05-04T17:31:36 | 2014-02-07T20:03:56 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 188 | 145 | 66 |
| instance_type_id | 196 | 172 | 93 |
| key | generation | hw:numa_nodes | test |
| value | 5 | 2 | true |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 129 distinct
- updated_at: 2017-08-04 14:40:14=1, 2017-08-04 14:40:18=1, 2017-08-04 14:40:21=1, 2017-08-04 15:29:32=1, 2017-11-16 21:42:11=1, 2018-01-08 21:23:06=1, 2018-04-26 19:51:27=1, 2018-04-27 17:39:18=1, 2018-09-25 03:22:22=1, 2023-02-23 17:06:21=1, nulls=125
- deleted_at: 29 distinct, nulls=104
- id: unique identifier, int 29..188
- instance_type_id: 104 distinct, int 51..196
  - top_values: 192=6, 57=5, 172=5, 171=4, 173=4, 84=3, 175=3, 78=2, 79=2, 80=2
- key: "overcommit"=50, "generation"=22, "ups"=11, "tig"=10, "switch"=8, "test"=7, "hw:cpu_sockets"=4, "hw:numa_nodes"=4, "pci_passthrough:alias"=4, "hw:cpu_cores"=3, "hw:cpu_policy"=3, "is_public"=2, "pci_passthrough"=2, "RT"=1, "hi_mem_use"=1, "hw:mem_page_size"=1, "os-flavor-access:is_public"=1, "titan_xp"=1
- value: 22 distinct
- deleted: 32 distinct, int 0..184
  - stats: average=24.1037, median=0.0000
  - top_values: 0=104, 30=1, 31=1, 33=1, 34=1, 36=1, 57=1, 58=1, 59=1, 60=1


# instance_type_projects

```sql
CREATE TABLE `instance_type_projects` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_type_id` int NOT NULL,
  `project_id` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`instance_type_id`,`project_id`,`deleted`),
  KEY (`instance_type_id`),
  CONSTRAINT `instance_type_projects_ibfk_1` FOREIGN KEY (`instance_type_id`) REFERENCES `instance_types` (`id`)
) AUTO_INCREMENT=353;
```

## Rows

- total=232

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-02-23T14:18:22 | 2023-06-16T15:55:31 | 2019-06-25T18:05:37 |
| updated_at | null | null | null |
| deleted_at | null | null | 2019-07-01T14:22:28 |
| id | 352 | 348 | 316 |
| instance_type_id | 196 | 193 | 176 |
| project_id | ccf2065a88074df09526d5dd5c361845 | 7691c9955ce1444ab366d041f5bdf33c | 98333a1a28e746fa8c629c83a818ad57 |
| deleted | 0 | 0 | 316 |

## Columns

- created_at: 194 distinct
- updated_at: all NULL
- deleted_at: 61 distinct, nulls=140
- id: unique identifier, int 1..352
- instance_type_id: 71 distinct, int 9..196
  - top_values: 154=19, 155=12, 111=9, 125=8, 53=7, 51=6, 52=6, 55=6, 56=6, 139=6
- project_id: 39 distinct
  - top_values: "98333a1a28e746fa8c629c83a818ad57"=44, "6f9adccbd03e4d2186756896957a14bf"=32, "7691c9955ce1444ab366d041f5bdf33c"=26, "17ea94ad74b64b9d92f4888336a598c7"=18, "09ad05432f914e26bc417bf58f1cb4d2"=13, "717cc16840494e8795e2ee25c46fe797"=9, "0dc175871e05482b9aff22616534c199"=8, "47c0857cf5b5452a86f640fd44be1d40"=8, "292c70904ce7415c8626f801bbf1ed0c"=7, "3c0c9fa6bb85454784416297a250be7a"=7
- deleted: 93 distinct, int 0..337
  - stats: average=76.9828, median=0.0000
  - top_values: 0=140, 3=1, 4=1, 5=1, 8=1, 10=1, 11=1, 12=1, 15=1, 19=1


# instance_types

```sql
CREATE TABLE `instance_types` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `name` varchar(255),
  `id` int NOT NULL AUTO_INCREMENT,
  `memory_mb` int NOT NULL,
  `vcpus` int NOT NULL,
  `swap` int NOT NULL,
  `vcpu_weight` int,
  `flavorid` varchar(255),
  `rxtx_factor` float,
  `root_gb` int,
  `ephemeral_gb` int,
  `disabled` tinyint(1),
  `is_public` tinyint(1),
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`name`,`deleted`),
  UNIQUE KEY (`flavorid`,`deleted`)
) AUTO_INCREMENT=197;
```

## Rows

- total=190

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-02-23T14:18:22 | 2013-08-08T18:03:20 | 2014-04-27T20:03:53 |
| updated_at | null | null | 2018-09-24T16:17:02 |
| deleted_at | null | 2013-08-15T19:17:37 | 2018-09-24T16:17:02 |
| name | axiom.0mover | solar.6spark | astro.omni_quark |
| id | 196 | 37 | 111 |
| memory_mb | 90112 | 8192 | 2048 |
| vcpus | 88 | 2 | 1 |
| swap | 0 | 0 | 0 |
| vcpu_weight | null | null | null |
| flavorid | d20eaff8-d13b-44de-a65f-2cbe9a42ff8c | 4ca00095-28dc-4926-9c5b-72fbc4625ae7 | f4ce6c9e-f6e0-4edd-b83e-8269b5351c6b |
| rxtx_factor | 1 | 1 | 1 |
| root_gb | 32 | 64 | 32 |
| ephemeral_gb | 0 | 0 | 0 |
| disabled | 0 | 0 | 0 |
| is_public | 0 | 1 | 0 |
| deleted | 0 | 37 | 111 |

## Columns

- created_at: 172 distinct, nulls=5
- updated_at: all distinct, nulls=137
- deleted_at: 64 distinct, nulls=92
- name: 120 distinct
  - top_values: "spire.xenon_drive"=4, "zenta.3glint"=4, "alpha.aurum"=3, "blaze.5align"=3, "flare.0omega"=3, "flash.4flick"=3, "flash.layer"=3, "glyph.spind"=3, "shine.cubic_shift"=3, "solar.flux"=3
- id: unique identifier, int 1..196
- memory_mb: 30 distinct, int 1..98304
  - stats: average=17287.6947, median=8192.0000
- vcpus: 2=45, 1=33, 4=27, 8=21, 16=20, 24=16, 12=15, 32=5, 88=5, 44=2, 64=1, int 1..88
- swap: 0=167, 4=14, 2048=4, 1024=3, 4096=1, 16384=1, int 0..16384
- vcpu_weight: all NULL
- flavorid: 176 distinct
  - top_values: "901"=5, "6"=3, "bd48d209-4cdf-4fdd-a950-ea1b6adcb567"=3, "d00fa5cf-8cf9-45f3-aebe-f71c942ed3c1"=3, "000001"=2, "9"=2, "9016"=2, "f4ce6c9e-f6e0-4edd-b83e-8269b5351c6b"=2, "000000"=1, "00bf3c77-473e-4844-ae0b-f76164bf9667"=1
- rxtx_factor: 1=190
- root_gb: 32=88, 16=49, 10=23, 64=18, 0=10, 40=1, 100=1, int 0..100
- ephemeral_gb: 0=173, 160=5, 80=3, 8=2, 360=2, 16=1, 20=1, 40=1, 64=1, 200=1, int 0..360
- disabled: 0=190
- is_public: 1=104, 0=86
- deleted: 99 distinct, int 0..189
  - stats: average=37.2895, median=3.5000
  - top_values: 0=92, 1=1, 2=1, 3=1, 4=1, 5=1, 6=1, 7=1, 8=1, 9=1


# instances

```sql
CREATE TABLE `instances` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `internal_id` int,
  `user_id` varchar(255),
  `project_id` varchar(255),
  `image_ref` varchar(255),
  `kernel_id` varchar(255),
  `ramdisk_id` varchar(255),
  `launch_index` int,
  `key_name` varchar(255),
  `key_data` text,
  `power_state` int,
  `vm_state` varchar(255),
  `memory_mb` int,
  `vcpus` int,
  `hostname` varchar(255),
  `host` varchar(255),
  `user_data` text,
  `reservation_id` varchar(255),
  `scheduled_at` datetime,
  `launched_at` datetime,
  `terminated_at` datetime,
  `display_name` varchar(255),
  `display_description` varchar(255),
  `availability_zone` varchar(255),
  `locked` tinyint(1),
  `os_type` varchar(255),
  `launched_on` text,
  `instance_type_id` int,
  `vm_mode` varchar(255),
  `uuid` varchar(36) NOT NULL,
  `architecture` varchar(255),
  `root_device_name` varchar(255),
  `access_ip_v4` varchar(39),
  `access_ip_v6` varchar(39),
  `config_drive` varchar(255),
  `task_state` varchar(255),
  `default_ephemeral_device` varchar(255),
  `default_swap_device` varchar(255),
  `progress` int,
  `auto_disk_config` tinyint(1),
  `shutdown_terminate` tinyint(1),
  `disable_terminate` tinyint(1),
  `root_gb` int,
  `ephemeral_gb` int,
  `cell_name` varchar(255),
  `node` varchar(255),
  `deleted` int,
  `locked_by` enum('owner','admin'),
  `cleaned` int,
  `ephemeral_key_uuid` varchar(36),
  PRIMARY KEY (`id`),
  UNIQUE KEY (`uuid`),
  UNIQUE KEY (`uuid`),
  KEY (`reservation_id`),
  KEY (`terminated_at`,`launched_at`),
  KEY (`task_state`,`updated_at`),
  KEY (`uuid`,`deleted`),
  KEY (`host`,`node`,`deleted`),
  KEY (`host`,`deleted`,`cleaned`),
  KEY (`project_id`,`deleted`),
  KEY (`deleted`,`created_at`)
) AUTO_INCREMENT=749388;
```

## Rows

- total=7922

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2024-01-17T18:51:01 | 2017-07-18T16:42:40 |
| updated_at | 2024-06-26T20:40:27 | 2024-01-17T18:54:20 | 2022-12-13T16:16:46 |
| deleted_at | null | 2024-01-17T18:54:20 | 2022-12-13T16:16:46 |
| id | 749387 | 749047 | 714402 |
| internal_id | null | null | null |
| user_id | 64f64393530d486da6d548710ca2990c | 4e4f5c1f38554dd6b3f750ee6b9ca9d2 | 016a57c3112643b9be2a295e9d9c6e90 |
| project_id | b3c6072810a24f67a7ac48e49a960e51 | e3fb2659584e436a832461dac02835f0 | a3ccd76b29264bbe94415833015c9379 |
| image_ref | null | f50eb6cd-6af4-406d-85d6-0cc5e3c5d050 | null |
| kernel_id | null | null | null |
| ramdisk_id | null | null | null |
| launch_index | 0 | 1 | 0 |
| key_name | null | null | plane_khfu-keun-kgco-pxnp-bwiy |
| key_data | null | null | 838e73555b83f2fcb21ab361f576768d |
| power_state | 1 | 0 | 4 |
| vm_state | active | deleted | deleted |
| memory_mb | 4096 | 1024 | 2048 |
| vcpus | 2 | 2 | 2 |
| hostname | lumen-comet-axis | pulse-xenon-axiom | pico-align |
| host | cosmo3-23 | beam8-22 |  |
| user_data | replaced_user_data.749387 | replaced_user_data.749047 | replaced_user_data.714402 |
| reservation_id | r-as21013g | r-k3f0756t | r-0em5z24z |
| scheduled_at | null | null | null |
| launched_at | 2024-06-26T20:40:24 | 2024-01-17T18:52:54 | 2017-07-18T16:43:26 |
| terminated_at | null | 2024-01-17T18:55:34 | 2022-12-13T16:16:46 |
| display_name | lumen-comet-axis | pulse-xenon-axiom | pico-align |
| display_description | lumen-comet-axis | null | pico-align |
| availability_zone | null | null | flare3 |
| locked | 0 | 0 | 0 |
| os_type | null | null | null |
| launched_on | cosmo3-23 | beam8-22 | delta-67 |
| instance_type_id | 72 | 58 | 150 |
| vm_mode | null | null | null |
| uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | f0807394-05a7-41ca-ac03-6ef8a88e13ac | 9b58a47d-9764-4b13-864b-8cce7c226d8b |
| architecture | null | null | null |
| root_device_name | /dev/vda | /dev/vda | /dev/vda |
| access_ip_v4 | null | null | null |
| access_ip_v6 | null | null | null |
| config_drive | null | null | null |
| task_state | null | null | null |
| default_ephemeral_device | null | null | null |
| default_swap_device | null | null | /dev/vdb |
| progress | 0 | 0 | 0 |
| auto_disk_config | 0 | 0 | 0 |
| shutdown_terminate | 0 | 0 | 0 |
| disable_terminate | 0 | 0 | 0 |
| root_gb | 32 | 16 | 32 |
| ephemeral_gb | 0 | 0 | 0 |
| cell_name | null | null | null |
| node | cosmo3-23.yahoo.ca.com | beam8-22.yahoo.ca.com | null |
| deleted | 0 | 749047 | 714402 |
| locked_by | null | null | null |
| cleaned | 0 | 1 | 1 |
| ephemeral_key_uuid | null | null | null |

## Columns

- created_at: 6987 distinct
  - top_values: 2021-06-14 15:21:46=6, 2021-05-07 13:18:46=5, 2021-06-08 12:56:09=5, 2021-06-15 11:52:31=5, 2016-03-02 01:12:05=4, 2020-02-10 16:47:43=4, 2020-06-15 15:56:47=4, 2021-05-18 14:03:57=4, 2021-05-18 14:38:48=4, 2021-11-15 20:21:55=4
- updated_at: 7036 distinct, nulls=8
  - top_values: 2020-01-29 20:32:20=6, 2021-10-06 02:13:03=6, 2022-08-10 20:52:49=6, 2024-05-31 13:19:02=6, 2019-07-17 10:42:53=5, 2020-01-29 20:32:03=5, 2020-01-29 20:32:07=5, 2020-02-02 14:44:46=5, 2020-02-10 16:40:42=5, 2020-02-19 17:08:03=5
- deleted_at: 5580 distinct, nulls=1485
- id: unique identifier, int 509070..749387
- internal_id: all NULL
- user_id: 560 distinct
- project_id: 479 distinct
  - top_values: "98333a1a28e746fa8c629c83a818ad57"=1593, "34c8d5cd44cc4b179c27892ec7596364"=514, "dba6cc0fec6845a58f4dd5e84ef8dca5"=397, "3008a142e9524f7295b06ea811908f93"=319, "c6d36b416dac49f193b4a209546ce370"=250, "5b92ec1146d04f9091ab48b6cdba3eff"=229, "daa18fdafdf04b5eac18e04aa19ee214"=229, "e3fb2659584e436a832461dac02835f0"=229, "6f5103a9ae434375a92a1de24a19ca56"=148, "bfe6b439cb834e79a3d8adbf23b5a92d"=127
- image_ref: 672 distinct, nulls=1670
- kernel_id: all NULL
- ramdisk_id: all NULL
- launch_index: 97 distinct, int 0..96
  - stats: average=1.7492, median=0.0000
- key_name: 854 distinct, nulls=2083
- key_data: 1082 distinct, nulls=2087
- power_state: 0=6106, 4=1081, 1=731, 3=4, int 0..4
- vm_state: "deleted"=5899, "active"=722, "shelved_offloaded"=674, "error"=483, "stopped"=92, "building"=47, "suspended"=4, "paused"=1
- memory_mb: 1024=1369, 2048=1292, 8192=1291, 16384=962, 4096=874, 512=741, 32768=325, 98304=298, 49152=230, 65536=188, 6144=133, 24576=129, 12288=72, 90112=7, 15360=4, 32=3, 45056=3, 30720=1, int 32..98304
- vcpus: 2=2150, 1=1814, 4=1554, 8=1124, 24=576, 16=352, 12=284, 32=52, 88=9, 64=4, 44=3, int 1..88
- hostname: 3000 distinct
- host: 43 distinct
  - top_values: ""=1416, "blaze8-12"=355, "ether-18"=349, "shine-94"=336, "flare4-57"=316, "align-86"=308, "flux-60"=290, "blitz1-32"=289, "forge-23"=287, "prime3-77"=277
- user_data: all distinct
- reservation_id: 6793 distinct
  - top_values: "r-g3ha1q02"=97, "r-6ie9f5mn"=80, "r-y3hq11fm"=40, "r-bxc7dex6"=26, "r-80i9irgf"=25, "r-t8v9wyrj"=22, "r-6a4ozutv"=21, "r-b2cpy92b"=21, "r-cleywtkz"=21, "r-ix13jf0z"=21
- scheduled_at: 49 distinct, nulls=7872
- launched_at: 6982 distinct, nulls=486
  - top_values: 2022-08-04 15:36:07=11, 2022-08-10 20:54:51=8, 2022-08-10 20:59:08=8, 2020-02-10 19:21:48=7, 2022-10-04 13:22:46=7, 2020-02-10 19:21:25=6, 2022-08-04 11:58:54=6, 2022-08-10 21:17:50=6, 2020-02-10 19:30:34=5, 2020-02-10 19:31:14=5
- terminated_at: 5327 distinct, nulls=1963
  - top_values: 2024-05-31 13:18:18=6, 2019-07-17 10:42:53=5, 2020-01-29 20:32:03=5, 2020-02-10 16:40:42=5, 2020-03-16 23:54:26=5, 2020-06-25 19:56:24=5, 2022-08-04 15:26:52=5, 2019-05-28 13:52:09=4, 2019-05-28 14:18:03=4, 2019-05-28 15:29:34=4
- display_name: 2913 distinct
- display_description: 2361 distinct, nulls=286
- availability_zone: "flare3"=5218, "dash_plasm"=1, nulls=2703
- locked: 0=7916, 1=6
- os_type: all NULL
- launched_on: 126 distinct, nulls=145
- instance_type_id: 70 distinct, int 56..196
- vm_mode: all NULL
- uuid: unique identifier
- architecture: "amd64"=20, "x86_64"=16, nulls=7886
- root_device_name: "/dev/vda"=7749, "/dev/hda"=12, "/dev/sda"=1, nulls=160
- access_ip_v4: all NULL
- access_ip_v6: all NULL
- config_drive: "True"=54, nulls=7868
- task_state: "deleting"=470, "scheduling"=8, "shelving"=7, "image_snapshot_pending"=1, nulls=7436
- default_ephemeral_device: "/dev/vdb"=2, nulls=7920
- default_swap_device: "/dev/vdb"=62, "/dev/vdc"=15, nulls=7845
- progress: 0=7922
- auto_disk_config: 0=7507, 1=415
- shutdown_terminate: 0=7922
- disable_terminate: 0=7922
- root_gb: 32=2403, 16=2292, 64=1616, 10=1586, 0=25, int 0..64
- ephemeral_gb: 0=7812, 64=49, 8=46, 16=15, int 0..64
- cell_name: all NULL
- node: 42 distinct, nulls=1416
  - top_values: "blaze8-12.yahoo.ca.com"=355, "ether-18.yahoo.ca.com"=349, "shine-94.yahoo.ca.com"=336, "flare4-57.yahoo.ca.com"=316, "align-86.yahoo.ca.com"=308, "flux-60.yahoo.ca.com"=290, "blitz1-32.yahoo.ca.com"=289, "forge-23.yahoo.ca.com"=287, "prime3-77.yahoo.ca.com"=277, "prime5-78.yahoo.ca.com"=271
- deleted: 6438 distinct, int 0..749385
  - stats: average=601978.0746, median=743604.5000
  - top_values: 0=1485, 512376=1, 529835=1, 530624=1, 530679=1, 530923=1, 586957=1, 586976=1, 589919=1, 589939=1
- locked_by: "owner"=6, nulls=7916
- cleaned: 1=7098, 0=824
- ephemeral_key_uuid: all NULL


# key_pairs

```sql
CREATE TABLE `key_pairs` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `user_id` varchar(255),
  `fingerprint` varchar(255),
  `public_key` text,
  `deleted` int,
  `type` enum('ssh','x509') NOT NULL DEFAULT 'ssh',
  PRIMARY KEY (`id`),
  UNIQUE KEY (`user_id`,`name`,`deleted`)
) AUTO_INCREMENT=3392;
```

## Rows

- total=3132

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-24T16:09:39 | 2017-09-22T17:04:28 | 2021-08-18T20:24:02 |
| updated_at | null | null | null |
| deleted_at | null | 2017-09-22T17:05:46 | null |
| id | 3391 | 2016 | 2998 |
| name | plasm_helio.433cosmo | aurum_shine.380align | arrow_drive.549blaze |
| user_id | 7a6e4676819c4cd2bce6ae812f0fc6e9 | a1ef823458d24a68955fec6f3d390019 | 9f7e64db7ced403aab9d4633be86d8f7 |
| fingerprint | 63:f0:c8:48:3e:eb:d6:32:e6:f9:04:8c:a4:83:a5:e8 | 69:db:ed:72:16:75:52:64:c3:3b:bf:dd:8b:a5:c3:26 | 08:49:85:7f:df:7c:34:dd:fd:0a:13:f1:aa:4e:01:bb |
| public_key | xenon_twist.315alpha | gamma_pulse.839omni | plasm_delta.133solar |
| deleted | 0 | 2016 | 0 |
| type | ssh | ssh | ssh |

## Columns

- created_at: 2953 distinct
- updated_at: all NULL
- deleted_at: 1507 distinct, nulls=1423
- id: unique identifier, int 1..3391
- name: all distinct
- user_id: 764 distinct
  - top_values: "8dff92c968c94d8093e087d13565c1b1"=235, "a1ef823458d24a68955fec6f3d390019"=165, "526d71f9d9994362b701ecff70daa258"=162, "b39f00e75fd84e0d8c870222f9066dff"=144, "e34af343637941dc8603f36f279ba30c"=69, "0b2717d52e56454298168c59e6b006b7"=49, "77047e1a20db46b2b8d8daebb9e39fe8"=44, "5302e30e168c4db283fc8e07009bb98f"=26, "81d81f7f17834951a1dc5ee8aa8b4e49"=25, "540e6feab1bf4c4bafad1bb59daf3c31"=24
- fingerprint: 2809 distinct
- public_key: all distinct
- deleted: 1710 distinct, int 0..3386
  - stats: average=967.3024, median=525.0000
  - top_values: 0=1423, 22=1, 23=1, 34=1, 46=1, 50=1, 51=1, 101=1, 118=1, 141=1
- type: "ssh"=3132


# migrate_version

## All rows

| column | row 1 |
|---|---|
| repository_id | nova |
| repository_path | /usr/lib/python2.7/dist-packages/nova/db/sqlalchemy/migrate_repo |
| version | 319 |


# networks

## All rows

| column | row 1 |
|---|---|
| created_at | 2012-09-07T13:52:06 |
| updated_at | 2013-08-09T21:26:49 |
| deleted_at | null |
| id | 1 |
| injected | 0 |
| cidr | 10.116.184.94/8 |
| netmask | 255.255.0.0 |
| bridge | br100 |
| gateway | 10.0.0.1 |
| broadcast | 10.0.255.255 |
| dns1 | 128.30.2.23 |
| vlan | null |
| vpn_public_address | 10.36.62.183/8 |
| vpn_public_port | null |
| vpn_private_address | null |
| dhcp_start | 10.0.0.2 |
| project_id | null |
| host | neon-63 |
| cidr_v6 | null |
| gateway_v6 | null |
| label | private |
| netmask_v6 | null |
| bridge_interface | eth1 |
| multi_host | 1 |
| dns2 | 128.30.2.24 |
| uuid | 8d825f56-4836-43df-ae85-e5f376325441 |
| priority | null |
| rxtx_base | null |
| deleted | 0 |
| mtu | null |
| dhcp_server | null |
| enable_dhcp | 1 |
| share_address | 0 |


# pci_devices

```sql
CREATE TABLE `pci_devices` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `deleted` int,
  `id` int NOT NULL AUTO_INCREMENT,
  `compute_node_id` int NOT NULL,
  `address` varchar(12) NOT NULL,
  `product_id` varchar(4) NOT NULL,
  `vendor_id` varchar(4) NOT NULL,
  `dev_type` varchar(8) NOT NULL,
  `dev_id` varchar(255),
  `label` varchar(255) NOT NULL,
  `status` varchar(36) NOT NULL,
  `extra_info` text,
  `instance_uuid` varchar(36),
  `request_id` varchar(36),
  `numa_node` int,
  `parent_addr` varchar(12),
  PRIMARY KEY (`id`),
  UNIQUE KEY (`compute_node_id`,`address`,`deleted`),
  KEY (`compute_node_id`,`deleted`),
  KEY (`instance_uuid`,`deleted`),
  KEY (`compute_node_id`,`parent_addr`,`deleted`),
  CONSTRAINT `pci_devices_compute_node_id_fkey` FOREIGN KEY (`compute_node_id`) REFERENCES `compute_nodes` (`id`)
) AUTO_INCREMENT=25;
```

## Rows

- total=16

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-01-09T18:22:22 | 2016-10-18T18:01:35 | 2016-10-18T18:01:35 |
| updated_at | null | 2019-01-09T17:51:11 | 2019-01-09T17:51:12 |
| deleted_at | null | null | null |
| deleted | 0 | 0 | 0 |
| id | 24 | 11 | 13 |
| compute_node_id | 149 | 90 | 90 |
| address | 0000:43:32.0 | 0000:75:06.0 | 0000:04:56.0 |
| product_id | 102d | 102d | 102d |
| vendor_id | 10de | 10de | 10de |
| dev_type | type-PCI | type-PCI | type-PCI |
| dev_id | pci_0000_88_00_0 | pci_0000_08_00_0 | pci_0000_83_00_0 |
| label | label_10de_102d | label_10de_102d | label_10de_102d |
| status | available | available | available |
| extra_info | {} | {} | {} |
| instance_uuid | null | null | null |
| request_id | null | null | null |
| numa_node | 1 | 0 | 1 |
| parent_addr | null | null | null |

## Columns

- created_at: 2016-10-18 18:01:35=6, 2019-01-09 18:22:21=4, 2019-01-09 18:22:22=4, 2016-10-18 18:01:36=2
- updated_at: 2019-01-09 17:51:11=4, 2019-01-09 17:51:12=4, nulls=8
- deleted_at: all NULL
- deleted: 0=16
- id: unique identifier, int 9..24
- compute_node_id: 90=8, 149=8
- address: "0000:04:56.0"=2, "0000:06:33.0"=2, "0000:43:32.0"=2, "0000:54:12.0"=2, "0000:64:31.0"=2, "0000:75:06.0"=2, "0000:83:59.0"=2, "0000:93:95.0"=2
- product_id: "102d"=16
- vendor_id: "10de"=16
- dev_type: "type-PCI"=16
- dev_id: "pci_0000_04_00_0"=2, "pci_0000_05_00_0"=2, "pci_0000_08_00_0"=2, "pci_0000_09_00_0"=2, "pci_0000_83_00_0"=2, "pci_0000_84_00_0"=2, "pci_0000_87_00_0"=2, "pci_0000_88_00_0"=2
- label: "label_10de_102d"=16
- status: "available"=16
- extra_info: "{}"=16
- instance_uuid: all NULL
- request_id: all NULL
- numa_node: 0=8, 1=8
- parent_addr: all NULL


# quota_classes

```sql
CREATE TABLE `quota_classes` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255),
  `resource` varchar(255),
  `hard_limit` int,
  `deleted` int,
  PRIMARY KEY (`id`),
  KEY (`class_name`)
) AUTO_INCREMENT=14;
```

## Rows

- total=13

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2017-07-07T15:19:43 | 2015-02-13T15:48:10 | 2015-02-13T15:48:10 |
| updated_at | null | 2015-03-23T14:32:09 | 2015-03-23T14:32:09 |
| deleted_at | null | null | null |
| id | 13 | 6 | 5 |
| class_name | default | usersandbox | usersandbox |
| resource | server_group_members | cores | ram |
| hard_limit | 32 | 8 | 8192 |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 2017-07-07 15:19:43=4, 2013-09-23 01:46:15=3, 2015-02-13 15:48:10=3, 2015-02-13 15:49:46=3
- updated_at: 2015-03-23 14:32:09=3, nulls=10
- deleted_at: all NULL
- id: unique identifier, int 1..13
- class_name: "default"=7, "personal"=3, "usersandbox"=3
- resource: "cores"=3, "instances"=3, "ram"=3, "security_groups"=1, "security_group_rules"=1, "server_groups"=1, "server_group_members"=1
- hard_limit: 8=4, 32=3, 64=3, 8192=2, 131072=1, int 8..131072
- deleted: 0=13


# quota_usages

```sql
CREATE TABLE `quota_usages` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` varchar(255),
  `resource` varchar(255) NOT NULL,
  `in_use` int NOT NULL,
  `reserved` int NOT NULL,
  `until_refresh` int,
  `deleted` int,
  `user_id` varchar(255),
  PRIMARY KEY (`id`),
  KEY (`project_id`),
  KEY (`user_id`,`deleted`)
) AUTO_INCREMENT=3853;
```

## Rows

- total=3619

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-18T15:09:07 | 2014-08-04T20:40:15 | 2020-05-04T01:21:14 |
| updated_at | 2024-06-18T15:09:07 | 2017-03-17T19:39:08 | 2020-05-04T01:21:14 |
| deleted_at | null | null | null |
| id | 3852 | 602 | 3057 |
| project_id | 5e35676c2c6947f29e1402b31c5b87a7 | 97107d3284a848a4a4ea0345bd05cbef | cfcf7f3db6e34a93a3a79ab6b915920e |
| resource | cores | ram | security_groups |
| in_use | 2 | 0 | 1 |
| reserved | 0 | 0 | 0 |
| until_refresh | null | null | 0 |
| deleted | 0 | 0 | 0 |
| user_id | 3a1ff089c33740358d0ce80cc5f801f9 | d8a7bc18be1e4d6dbce5bc6dff6840f5 | 858a6f6ed6d54e63998d11bf28f78983 |

## Columns

- created_at: 1155 distinct
- updated_at: 1554 distinct
- deleted_at: all NULL
- id: unique identifier, int 7..3852
- project_id: 559 distinct, nulls=2
  - top_values: "3008a142e9524f7295b06ea811908f93"=365, "98333a1a28e746fa8c629c83a818ad57"=57, "70b2507b8cc44fcb917ddfb85f5079d9"=50, "190ad02e1faa494a8ab7153c6d2e56c1"=49, "97107d3284a848a4a4ea0345bd05cbef"=45, "09ad05432f914e26bc417bf58f1cb4d2"=41, "daa18fdafdf04b5eac18e04aa19ee214"=40, "dba6cc0fec6845a58f4dd5e84ef8dca5"=32, "d7d16dd7c387425b80c001832884b6de"=30, "47c0857cf5b5452a86f640fd44be1d40"=29
- resource: "cores"=1022, "instances"=1022, "ram"=1022, "security_groups"=494, "floating_ips"=26, "fixed_ips"=18, "server_groups"=11, "gigabytes"=2, "volumes"=2
- in_use: 174 distinct, int -512..1081344
  - stats: average=5862.5742, median=1.0000
- reserved: 0=3605, -2048=3, 2048=3, -2=2, 2=2, -35328=1, -15=1, -1=1, 1=1, int -35328..2048
- until_refresh: 0=330, nulls=3289
- deleted: 0=3619
- user_id: 739 distinct, nulls=48
  - top_values: "a1ef823458d24a68955fec6f3d390019"=101, "0be8fa0d641a4e778b9262bd2e5f40b5"=61, "ce3ea89d3bf34882b2666853f1474575"=50, "e1b9fa1bb2f44cc88f8a6fa63dc389a9"=28, "ed22eaa324ea4dff812c57a199d3abd4"=24, "016a57c3112643b9be2a295e9d9c6e90"=23, "36783874ab9946a18ee493f64443b2dc"=21, "5302e30e168c4db283fc8e07009bb98f"=20, "5c467be0707545338c91fc00d5a9914c"=17, "07d3187f379a4fe6a556c63c6131b2ac"=16


# quotas

```sql
CREATE TABLE `quotas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `project_id` varchar(255),
  `resource` varchar(255) NOT NULL,
  `hard_limit` int,
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`project_id`,`resource`,`deleted`)
) AUTO_INCREMENT=6260;
```

## Rows

- total=3579

| column | latest | sample | sample |
|---|---|---|---|
| id | 6259 | 1619 | 1842 |
| created_at | 2024-06-17T15:53:29 | 2015-09-22T19:54:40 | 2015-10-26T08:14:48 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| project_id | 7b3609decd234ec2852503d64e334e3f | ba36b1b9ecde479f92dc62fe0c0f49e9 | ad4b22ff76d74efcb23a0b7fcc6ddb0e |
| resource | cores | metadata_items | ram |
| hard_limit | 8 | 128 | 16384 |
| deleted | 0 | 0 | 0 |

## Columns

- id: unique identifier, int 1..6259
- created_at: 1078 distinct
- updated_at: 254 distinct, nulls=2581
- deleted_at: all NULL
- project_id: 941 distinct
  - top_values: "98333a1a28e746fa8c629c83a818ad57"=12, "17ea94ad74b64b9d92f4888336a598c7"=10, "9e2200862b674b3098afc897b0fbb977"=10, "02c3a636066b45faa84760bbaa76d8a8"=9, "0d16687ae70645678cbe037065831a32"=9, "292c70904ce7415c8626f801bbf1ed0c"=9, "2a9b495932c64d80b1fac28d1416a921"=9, "3008a142e9524f7295b06ea811908f93"=9, "347e25c219354db38c6662e4ab9a9c84"=9, "34f87362758043a98ea19c5a5e9217c9"=9
- resource: "cores"=940, "ram"=940, "instances"=937, "injected_files"=225, "injected_file_content_bytes"=225, "metadata_items"=225, "floating_ips"=25, "gigabytes"=23, "volumes"=23, "fixed_ips"=7, "security_groups"=3, "server_group_members"=3, "server_groups"=2, "security_group_rules"=1
- hard_limit: 91 distinct, int -1..50331648
  - stats: average=44392.4647, median=16.0000
- deleted: 0=3579


# reservations

```sql
CREATE TABLE `reservations` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `usage_id` int NOT NULL,
  `project_id` varchar(255),
  `resource` varchar(255),
  `delta` int NOT NULL,
  `expire` datetime,
  `deleted` int,
  `user_id` varchar(255),
  PRIMARY KEY (`id`),
  KEY (`usage_id`),
  KEY (`project_id`),
  KEY (`user_id`,`deleted`),
  KEY (`uuid`),
  KEY (`deleted`,`expire`),
  CONSTRAINT `reservations_ibfk_1` FOREIGN KEY (`usage_id`) REFERENCES `quota_usages` (`id`)
) AUTO_INCREMENT=1656703;
```

## Rows

- total=42003

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2023-05-03T19:41:23 | 2022-06-06T19:33:30 |
| updated_at | null | null | null |
| deleted_at | 2024-06-26T20:39:05 | 2023-05-03T19:41:27 | 2022-06-06T19:33:37 |
| id | 1656702 | 1650954 | 1645047 |
| uuid | 73ad8ef0-ffde-4057-a571-adbde829e0ee | 62abc27e-4e72-43c9-b928-8c6226576db3 | 48252533-d236-4d6a-bfe9-1e5937dde9f0 |
| usage_id | 2546 | 2592 | 2440 |
| project_id | b3c6072810a24f67a7ac48e49a960e51 | 8977ef5d45f74e7290c10832c324ab99 | d7d16dd7c387425b80c001832884b6de |
| resource | cores | cores | cores |
| delta | 2 | -12 | -2 |
| expire | 2024-06-27T20:39:03 | 2023-05-04T19:41:23 | 2022-06-07T19:33:30 |
| deleted | 1656702 | 1650954 | 1645047 |
| user_id | 64f64393530d486da6d548710ca2990c | d7ee5070593a4e71992ccce180b49a9d | ce3ea89d3bf34882b2666853f1474575 |

## Columns

- created_at: 12008 distinct
- updated_at: all NULL
- deleted_at: 12184 distinct
- id: unique identifier, int 1614700..1656702
- uuid: unique identifier
- usage_id: 1534 distinct, int 159..3852
  - top_values: 168=3271, 169=3271, 170=3271, 3285=1001, 3286=996, 3284=991, 163=890, 164=883, 162=877, 510=437
- project_id: 321 distinct
  - top_values: "17ea94ad74b64b9d92f4888336a598c7"=10016, "98333a1a28e746fa8c629c83a818ad57"=5879, "34c8d5cd44cc4b179c27892ec7596364"=3084, "dba6cc0fec6845a58f4dd5e84ef8dca5"=1602, "3008a142e9524f7295b06ea811908f93"=1527, "5b92ec1146d04f9091ab48b6cdba3eff"=1367, "daa18fdafdf04b5eac18e04aa19ee214"=1199, "e3fb2659584e436a832461dac02835f0"=850, "6f5103a9ae434375a92a1de24a19ca56"=732, "190ad02e1faa494a8ab7153c6d2e56c1"=585
- resource: "ram"=14051, "cores"=13968, "instances"=13702, "server_groups"=282
- delta: 132 distinct, int -98304..360448
  - stats: average=55.6183, median=-1.0000
- expire: 11918 distinct
  - top_values: 2020-02-20 18:09:04=30, 2021-05-13 16:53:07=30, 2020-02-20 18:09:15=27, 2020-03-10 18:38:44=27, 2020-05-31 03:48:18=27, 2021-05-13 16:46:32=27, 2021-05-13 16:46:46=27, 2021-05-13 16:53:41=27, 2020-03-10 18:38:55=24, 2021-05-02 20:46:43=24
- deleted: all distinct, int 1614700..1656702
  - stats: average=1635701.0000, median=1635701.0000
- user_id: 395 distinct
  - top_values: "a1ef823458d24a68955fec6f3d390019"=13187, "8dff92c968c94d8093e087d13565c1b1"=3099, "77047e1a20db46b2b8d8daebb9e39fe8"=1361, "5302e30e168c4db283fc8e07009bb98f"=1297, "08e9506592fc4819b2cd7a54d93fa8ae"=1098, "4e4f5c1f38554dd6b3f750ee6b9ca9d2"=813, "e1b9fa1bb2f44cc88f8a6fa63dc389a9"=620, "ce3ea89d3bf34882b2666853f1474575"=601, "016a57c3112643b9be2a295e9d9c6e90"=587, "0be8fa0d641a4e778b9262bd2e5f40b5"=492


# s3_images

```sql
CREATE TABLE `s3_images` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=2498;
```

## Rows

- total=2419

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-24T16:43:06 | 2020-03-05T15:29:58 | 2012-11-14T23:37:12 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 2497 | 2111 | 60 |
| uuid | 754667d2-7f09-4958-a2bf-505d410a99e5 | 8c6e1f82-67d8-47c8-8553-c7997340d657 | a39b25a1-f0b7-4971-92f9-37f6ca376769 |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 2305 distinct
- updated_at: all NULL
- deleted_at: all NULL
- id: unique identifier, int 1..2497
- uuid: 2410 distinct
- deleted: 0=2419


# security_group_rules

```sql
CREATE TABLE `security_group_rules` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `parent_group_id` int,
  `protocol` varchar(255),
  `from_port` int,
  `to_port` int,
  `cidr` varchar(43),
  `group_id` int,
  `deleted` int,
  PRIMARY KEY (`id`),
  KEY (`parent_group_id`),
  KEY (`group_id`),
  CONSTRAINT `security_group_rules_ibfk_1` FOREIGN KEY (`parent_group_id`) REFERENCES `security_groups` (`id`),
  CONSTRAINT `security_group_rules_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `security_groups` (`id`)
) AUTO_INCREMENT=193;
```

## Rows

- total=152

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2013-07-23T02:51:26 | 2013-05-16T01:18:27 | 2013-05-16T01:18:13 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 192 | 147 | 146 |
| parent_group_id | 64 | 62 | 62 |
| protocol | tcp | udp | udp |
| from_port | 1 | 9604 | 9603 |
| to_port | 65535 | 9604 | 9603 |
| cidr | 10.71.29.205/8 | 10.71.29.205/8 | 10.71.29.205/8 |
| group_id | null | null | null |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 151 distinct
- updated_at: all NULL
- deleted_at: all NULL
- id: unique identifier, int 1..192
- parent_group_id: 51 distinct, int 1..67
  - top_values: 62=20, 64=9, 54=8, 55=8, 45=7, 9=6, 23=6, 63=6, 22=4, 50=4
- protocol: "tcp"=115, "icmp"=19, "udp"=18
- from_port: 46 distinct, int -1..60000
  - stats: average=3598.9079, median=22.0000
- to_port: 49 distinct, int -1..65535
  - stats: average=12722.7434, median=654.0000
- cidr: "10.71.29.205/8"=135, "10.152.54.152/8"=3, "10.227.134.94/8"=3, "10.116.184.94/8"=2, "10.150.130.197/8"=2, "10.216.18.158/8"=1, nulls=6
- group_id: 23=3, 63=3, nulls=146
- deleted: 0=152


# security_groups

```sql
CREATE TABLE `security_groups` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255),
  `description` varchar(255),
  `user_id` varchar(255),
  `project_id` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`project_id`,`name`,`deleted`)
) AUTO_INCREMENT=622;
```

## Rows

- total=601

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-17T21:06:37 | 2016-09-07T15:25:48 | 2014-02-04T18:02:13 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 621 | 281 | 82 |
| name | aurum-xenon | aurum-xenon | aurum-xenon |
| description | c21f969b5f03d33d43e04f8f136e7682 | c21f969b5f03d33d43e04f8f136e7682 | c21f969b5f03d33d43e04f8f136e7682 |
| user_id | 7a6e4676819c4cd2bce6ae812f0fc6e9 | 9b62fba091b644f6aaa57e79492a8d24 | f34ef67977e942b992a214f18bef1a9d |
| project_id | 5e35676c2c6947f29e1402b31c5b87a7 | 4e7e31906cfd496b82a9ea5d2edb8dab | 3be6c8b9f95842198466a9c673404768 |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 600 distinct
- updated_at: all NULL
- deleted_at: 2012-07-09 15:38:51=1, 2012-09-13 02:28:33=1, 2012-11-09 18:54:54=1, 2012-11-20 01:59:21=1, 2012-11-29 17:18:11=1, 2012-11-29 17:19:41=1, 2012-12-25 01:15:01=1, 2013-01-10 16:27:00=1, 2013-01-23 01:35:49=1, nulls=592
- id: unique identifier, int 1..621
- name: 29 distinct
  - top_values: "aurum-xenon"=561, "helio-galax-solar"=9, "gamut"=4, "proto"=2, "align-mover"=1, "alpha-mover-meter"=1, "cosmo-novae"=1, "credo"=1, "cubic"=1, "dash"=1
- description: 39 distinct
- user_id: 488 distinct
- project_id: 561 distinct
  - top_values: "6f5103a9ae434375a92a1de24a19ca56"=7, "70b2507b8cc44fcb917ddfb85f5079d9"=6, "3008a142e9524f7295b06ea811908f93"=5, "98333a1a28e746fa8c629c83a818ad57"=4, "292c70904ce7415c8626f801bbf1ed0c"=3, "3a8a2c70884d474aa1d3aeebeb800f7e"=3, "4e101cf5264b4e739b7b5ebe0f6b5c68"=3, "6f9adccbd03e4d2186756896957a14bf"=3, "84d0ab8dd0b44f61981e4dc218daab3f"=3, "d0ebc85936794a30b65bb6dae5687404"=3
- deleted: 0=592, 7=1, 21=1, 24=1, 29=1, 35=1, 37=1, 38=1, 39=1, 41=1, int 0..41


# services

```sql
CREATE TABLE `services` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `host` varchar(255),
  `binary` varchar(255),
  `topic` varchar(255),
  `report_count` int NOT NULL,
  `disabled` tinyint(1),
  `deleted` int,
  `disabled_reason` varchar(255),
  `last_seen_up` datetime,
  `forced_down` tinyint(1),
  `version` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`host`,`topic`,`deleted`),
  UNIQUE KEY (`host`,`binary`,`deleted`)
) AUTO_INCREMENT=337;
```

## Rows

- total=149

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-01-09T18:22:20 | 2012-07-12T18:23:21 | 2018-01-09T16:20:23 |
| updated_at | 2019-01-09T18:22:30 | 2017-08-04T20:20:35 | 2024-07-08T07:00:01 |
| deleted_at | null | 2017-08-04T20:26:04 | null |
| id | 336 | 76 | 325 |
| host | cubic-10 | glint-54 | flux-60 |
| binary | nova-compute | nova-compute | nova-compute |
| topic | compute | compute | compute |
| report_count | 1 | 15609660 | 20374440 |
| disabled | 1 | 1 | 0 |
| deleted | 0 | 76 | 0 |
| disabled_reason | AUTO: Connection to libvirt lost: 0 | AUTO: Connection to libvirt lost: 0 | null |
| last_seen_up | 2019-01-09T18:22:27 | 2017-08-04T20:20:26 | 2024-07-08T07:00:01 |
| forced_down | 0 | 0 | 0 |
| version | 9 | 9 | 9 |

## Columns

- created_at: 146 distinct
- updated_at: 86 distinct, nulls=3
- deleted_at: all distinct, nulls=58
- id: unique identifier, int 6..336
- host: 142 distinct
  - top_values: "gamut-16"=4, "layer-19"=3, "cubic-10"=2, "lumen4-89"=2, "align-73"=1, "align-79"=1, "align-86"=1, "align-zenta-align"=1, "alpha-80"=1, "arrow-57"=1
- binary: "nova-compute"=129, "nova-conductor"=13, "nova-scheduler"=2, "nova-cert"=1, "nova-consoleauth"=1, "nova-ec2"=1, "nova-metadata"=1, "nova-osapi_compute"=1
- topic: "compute"=129, "conductor"=13, "scheduler"=2, "cert"=1, "consoleauth"=1, nulls=3
- report_count: 146 distinct, int 0..31320673
  - stats: average=14194824.7383, median=14297305.0000
- disabled: 0=92, 1=57
- deleted: 92 distinct, int 0..331
  - stats: average=74.2282, median=45.0000
  - top_values: 0=58, 6=1, 9=1, 12=1, 15=1, 19=1, 22=1, 23=1, 25=1, 28=1
- disabled_reason: "AUTO: Connection to libvirt lost: 0"=44, "retired"=11, "constantly rebooting"=1, nulls=93
- last_seen_up: 82 distinct, nulls=8
- forced_down: 0=149
- version: 9=143, 0=6


# shadow_aggregate_hosts

```sql
CREATE TABLE `shadow_aggregate_hosts` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `host` varchar(255),
  `aggregate_id` int NOT NULL,
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=743;
```

## Rows

- total=516

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2017-07-13T20:23:43 | 2014-12-11T18:55:21 | 2014-12-12T05:41:08 |
| updated_at | null | null | null |
| deleted_at | 2017-07-15T04:21:47 | 2014-12-11T18:58:13 | 2016-09-26T16:12:32 |
| id | 742 | 300 | 376 |
| host | grav9-5 | scope4-19 | pulse1-24 |
| aggregate_id | 18 | 2 | 2 |
| deleted | 742 | 300 | 376 |

## Columns

- created_at: 498 distinct, nulls=5
- updated_at: all NULL
- deleted_at: 494 distinct
- id: unique identifier, int 11..742
- host: 106 distinct
- aggregate_id: 2=258, 7=100, 4=41, 13=41, 3=18, 16=16, 12=11, 5=10, 6=9, 1=5, 17=5, 8=1, 18=1, int 1..18
- deleted: all distinct, int 11..742
  - stats: average=337.7345, median=318.5000


# shadow_aggregate_metadata

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| created_at | 2014-10-07T14:31:40 | 2014-10-07T14:31:40 | 2016-07-07T01:41:18 | 2016-08-03T13:47:15 |
| updated_at | null | null | null | null |
| deleted_at | 2016-09-28T23:44:55 | 2016-09-28T23:44:55 | 2016-07-07T03:08:27 | 2017-02-16T21:56:42 |
| id | 20 | 21 | 23 | 27 |
| aggregate_id | 7 | 7 | 8 | 12 |
| key | ram_allocation_ratio | cpu_allocation_ratio | ram_allocation_ratio | switch |
| value | 1 | 1 | 1.2 | os-1g-1 |
| deleted | 20 | 21 | 23 | 27 |


# shadow_block_device_mapping

```sql
CREATE TABLE `shadow_block_device_mapping` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `device_name` varchar(255),
  `delete_on_termination` tinyint(1),
  `snapshot_id` varchar(36),
  `volume_id` varchar(36),
  `volume_size` int,
  `no_device` tinyint(1),
  `connection_info` text,
  `instance_uuid` varchar(36),
  `deleted` int,
  `source_type` varchar(255),
  `destination_type` varchar(255),
  `guest_format` varchar(255),
  `device_type` varchar(255),
  `disk_bus` varchar(255),
  `boot_index` int,
  `image_id` varchar(36),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=263629;
```

## Rows

- total=212755

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:45:47 | 2015-12-07T03:52:33 | 2016-06-06T15:39:59 |
| updated_at | 2019-11-08T16:45:49 | 2015-12-07T03:52:38 | 2016-06-06T15:40:01 |
| deleted_at | 2019-11-08T16:49:58 | 2015-12-07T04:13:00 | 2016-06-06T16:40:04 |
| id | 263628 | 177586 | 217997 |
| device_name | /dev/vda | /dev/vda | /dev/vda |
| delete_on_termination | 1 | 1 | 1 |
| snapshot_id | null | null | null |
| volume_id | null | null | null |
| volume_size | null | null | null |
| no_device | 0 | 0 | 0 |
| connection_info | null | null | null |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | 8df2b216-eeb8-41db-819c-4bbbe4791d35 | ef78d4e4-744f-476a-bfb5-fabd863b7aae |
| deleted | 263628 | 177586 | 217997 |
| source_type | image | image | image |
| destination_type | local | local | local |
| guest_format | null | null | null |
| device_type | disk | disk | disk |
| disk_bus | null | null | null |
| boot_index | 0 | 0 | 0 |
| image_id | 0a4641df-191f-44d7-b79b-13d26e7c5218 | 42784945-58cb-4951-a23d-8ca5bc617257 | 30a14abe-e6fa-4ab7-b21a-5ddf6362f783 |

## Columns

- created_at: nulls=78
- updated_at: nulls=3960
- deleted_at: nulls=3210
- id: unique identifier, int 108..263628
- device_name: nulls=3553
- delete_on_termination: nulls=78, int 0..1
  - stats: average=0.9842
- snapshot_id: nulls=212311
- volume_id: nulls=209241
- volume_size: nulls=211417, int 0..16384
  - stats: average=258.0135
- no_device: nulls=156707, int 0..0
  - stats: average=0.0000
- connection_info: nulls=209606
- instance_uuid: profile metrics skipped
- deleted: nulls=78, int 0..263628
  - stats: average=110126.5061
- source_type: profile metrics skipped
- destination_type: nulls=24
- guest_format: nulls=212661
- device_type: nulls=1724
- disk_bus: nulls=210306
- boot_index: nulls=1516, int -1..1
  - stats: average=-0.0008
- image_id: nulls=3484


# shadow_compute_nodes

## All rows

| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| created_at | 2012-07-12T15:18:57 | 2012-12-14T18:18:23 | 2013-02-19T17:18:34 |
| updated_at | 2012-12-15T22:37:43 | 2012-12-14T18:36:10 | 2013-03-15T12:19:00 |
| deleted_at | 2013-04-29T16:11:57 | 2013-04-29T16:11:46 | 2013-04-29T16:12:15 |
| id | 11 | 45 | 61 |
| service_id | 30 | 96 | 129 |
| vcpus | 24 | 24 | 24 |
| memory_mb | 48295 | 48295 | 96679 |
| local_gb | 869 | 869 | 916 |
| vcpus_used | 0 | 0 | 0 |
| memory_mb_used | 512 | 512 | 512 |
| local_gb_used | 0 | 0 | 0 |
| hypervisor_type | QEMU | QEMU | QEMU |
| hypervisor_version | 1000000 | 1000000 | 1000000 |
| cpu_info | {"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["rdtscp", "pdpe1gb", "dca", "pdcm", "xtpr", "tm2", "est", "smx", "vmx", "ds_cpl", "monitor", "dtes64", "pclmuldq", "pbe", "tm", "ht", "ss", "acpi", "ds", "vme"], "topology": {"cores": 6, "threads": 2, "sockets": 1}} | {"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["rdtscp", "pdpe1gb", "dca", "pdcm", "xtpr", "tm2", "est", "smx", "vmx", "ds_cpl", "monitor", "dtes64", "pclmuldq", "pbe", "tm", "ht", "ss", "acpi", "ds", "vme"], "topology": {"cores": 6, "threads": 2, "sockets": 1}} | {"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["rdtscp", "pdpe1gb", "dca", "pdcm", "xtpr", "tm2", "est", "smx", "vmx", "ds_cpl", "monitor", "dtes64", "pclmuldq", "pbe", "tm", "ht", "ss", "acpi", "ds", "vme"], "topology": {"cores": 6, "threads": 2, "sockets": 1}} |
| disk_available_least | 839 | 867 | 786 |
| free_ram_mb | 47783 | 47783 | 96167 |
| free_disk_gb | 869 | 869 | 916 |
| current_workload | 0 | 0 | 0 |
| running_vms | 0 | 0 | 0 |
| hypervisor_hostname | flare-59.yahoo.ca.com | sonic4-45.yahoo.ca.com | shine-16.yahoo.ca.com |
| deleted | 11 | 45 | 61 |
| host_ip | null | null | null |
| supported_instances | null | null | null |
| pci_stats | null | null | null |
| metrics | null | null | null |
| extra_resources | null | null | null |
| stats | {} | {} | {} |
| numa_topology | null | null | null |
| host | null | null | null |
| ram_allocation_ratio | null | null | null |
| cpu_allocation_ratio | null | null | null |
| uuid | null | null | null |
| disk_allocation_ratio | null | null | null |


# shadow_fixed_ips

```sql
CREATE TABLE `shadow_fixed_ips` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(39),
  `network_id` int,
  `allocated` tinyint(1),
  `leased` tinyint(1),
  `reserved` tinyint(1),
  `virtual_interface_id` int,
  `host` varchar(255),
  `instance_uuid` varchar(36),
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1339;
```

## Rows

- total=15

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2012-09-07T13:52:14 | 2012-09-07T13:52:14 | 2012-09-07T13:52:14 |
| updated_at | 2013-09-17T02:45:25 | 2013-09-17T02:45:17 | 2013-09-17T02:37:24 |
| deleted_at | null | null | null |
| id | 1338 | 1311 | 1137 |
| address | 10.26.198.227/8 | 10.198.115.85/8 | 10.87.199.189/8 |
| network_id | 1 | 1 | 1 |
| allocated | 1 | 1 | 0 |
| leased | 1 | 1 | 0 |
| reserved | 0 | 0 | 0 |
| virtual_interface_id | 414194 | 414191 | null |
| host | null | null | null |
| instance_uuid | 6154483e-317a-43bc-9563-cd945f59a242 | cde72ffa-83d7-4758-ac76-d3fba5d6c5a4 | 566424cb-b7ec-45f7-aaf3-c8545c58a701 |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 2012-09-07 13:52:14=15
- updated_at: 2013-09-17 02:37:24=2, 2013-09-17 02:42:59=2, 2013-09-17 02:05:54=1, 2013-09-17 02:06:01=1, 2013-09-17 02:37:17=1, 2013-09-17 02:38:06=1, 2013-09-17 02:38:10=1, 2013-09-17 02:38:11=1, 2013-09-17 02:42:54=1, 2013-09-17 02:45:17=1, 2013-09-17 02:45:24=1, 2013-09-17 02:45:25=1, 2013-09-17 02:45:32=1
- deleted_at: all NULL
- id: unique identifier, int 901..1338
- address: "10.10.93.33/8"=1, "10.101.127.213/8"=1, "10.112.224.229/8"=1, "10.124.113.78/8"=1, "10.136.20.110/8"=1, "10.165.8.116/8"=1, "10.176.161.167/8"=1, "10.198.115.85/8"=1, "10.232.120.47/8"=1, "10.253.100.135/8"=1, "10.26.198.227/8"=1, "10.28.229.58/8"=1, "10.29.111.109/8"=1, "10.87.199.189/8"=1, "10.90.203.211/8"=1
- network_id: 1=15
- allocated: 0=11, 1=4
- leased: 0=11, 1=4
- reserved: 0=15
- virtual_interface_id: 414191=1, 414192=1, 414193=1, 414194=1, nulls=11, int 414191..414194
- host: all NULL
- instance_uuid: unique identifier
- deleted: 0=15


# shadow_instance_actions

```sql
CREATE TABLE `shadow_instance_actions` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `action` varchar(255),
  `instance_uuid` varchar(36),
  `request_id` varchar(255),
  `user_id` varchar(255),
  `project_id` varchar(255),
  `start_time` datetime,
  `finish_time` datetime,
  `message` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=600509;
```

## Rows

- total=523265

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:49:50 | 2015-04-18T06:48:46 | 2015-03-29T06:33:43 |
| updated_at | null | 2017-07-19T18:42:25 | 2017-07-19T18:42:25 |
| deleted_at | null | null | null |
| id | 600508 | 334643 | 267106 |
| action | delete | delete | create |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | 185c9ce1-cea1-4218-ae33-ae8806fdf4bf | d75a7f51-9517-4dbb-9507-bc3cd432a4f0 |
| request_id | req-56139ae9-20dc-4c93-a28b-d0b4f32fb85d | req-659e3dcc-ca8d-473b-9022-ca1cf1202ca3 | req-0ca40461-6a8b-4783-be5f-078b0e10dba4 |
| user_id | a1ef823458d24a68955fec6f3d390019 | ada9fad8c2394152af079258d13ca201 | ada9fad8c2394152af079258d13ca201 |
| project_id | bfd50153a2e9476f93e33e30e922cd06 | 3008a142e9524f7295b06ea811908f93 | 3008a142e9524f7295b06ea811908f93 |
| start_time | 2019-11-08T16:49:49 | 2015-04-18T06:48:46 | 2015-03-29T06:33:42 |
| finish_time | null | null | null |
| message | null | null | null |
| deleted | 0 | 334643 | 267106 |

## Columns

- created_at: profile metrics skipped
- updated_at: nulls=48354
- deleted_at: all NULL
- id: unique identifier, int 3978..600508
- action: profile metrics skipped
- instance_uuid: profile metrics skipped
- request_id: profile metrics skipped
- user_id: nulls=3886
- project_id: nulls=3886
- start_time: profile metrics skipped
- finish_time: all NULL
- message: nulls=514702
- deleted: int 0..539568
  - stats: average=227050.9764


# shadow_instance_actions_events

```sql
CREATE TABLE `shadow_instance_actions_events` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `event` varchar(255),
  `action_id` int,
  `start_time` datetime,
  `finish_time` datetime,
  `result` varchar(255),
  `traceback` text,
  `deleted` int,
  `host` varchar(255),
  `details` text,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=737364;
```

## Rows

- total=663442

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:49:50 | 2018-04-11T21:58:22 | 2015-02-27T04:59:18 |
| updated_at | 2019-11-08T16:49:59 | 2019-03-07T19:25:02 | 2017-07-19T16:30:42 |
| deleted_at | null | null | null |
| id | 737363 | 701948 | 284115 |
| event | compute_terminate_instance | compute_terminate_instance | compute__do_build_and_run_instance |
| action_id | 600508 | 567929 | 174501 |
| start_time | 2019-11-08T16:49:50 | 2018-04-11T21:58:22 | 2015-02-27T04:59:18 |
| finish_time | 2019-11-08T16:49:59 | 2018-04-11T21:58:31 | 2015-02-27T04:59:28 |
| result | Success | Success | Success |
| traceback | null | null | null |
| deleted | 0 | 701948 | 284115 |
| host | null | null | null |
| details | null | null | null |

## Columns

- created_at: profile metrics skipped
- updated_at: nulls=563
- deleted_at: all NULL
- id: unique identifier, int 5618..737363
- event: profile metrics skipped
- action_id: int 3978..600508
- start_time: profile metrics skipped
- finish_time: nulls=58400
- result: nulls=58400
- traceback: nulls=654508
- deleted: int 0..728497
  - stats: average=341353.9424
- host: all NULL
- details: all NULL


# shadow_instance_extra

```sql
CREATE TABLE `shadow_instance_extra` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `deleted` int,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_uuid` varchar(36) NOT NULL,
  `numa_topology` text,
  `pci_requests` text,
  `flavor` text,
  `vcpu_model` text,
  `migration_context` text,
  PRIMARY KEY (`id`),
  KEY (`instance_uuid`)
) AUTO_INCREMENT=211265;
```

## Rows

- total=179772

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:45:47 | 2015-03-02T03:04:42 | 2015-03-25T12:51:58 |
| updated_at | 2019-11-08T16:49:58 | 2015-03-02T03:05:04 | 2015-03-25T12:52:37 |
| deleted_at | 2019-11-08T16:49:58 | 2015-03-02T04:44:35 | 2015-03-25T16:34:43 |
| deleted | 211264 | 13869 | 41896 |
| id | 211264 | 13869 | 41896 |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | 12784651-bc34-4962-ad83-c3cb6d824bbb | 4d9f4c5c-9ce9-4c21-af3b-b2b6d09318e5 |
| numa_topology | null | null | null |
| pci_requests | [] | [] | [] |
| flavor | {"new": null, "old": null, "cur": {"nova_object.version": "1.1", "nova_object.changes": ["extra_specs"], "nova_object.name": "Flavor", "nova_object.data": {"disabled": false, "root_gb": 10, "name": "s1.2core", "flavorid": "1100", "deleted": false, "created_at": "2013-08-15T19:17:53Z", "ephemeral_gb": 0, "updated_at": null, "memory_mb": 1024, "vcpus": 2, "extra_specs": {"overcommit": "default"}, "swap": 0, "rxtx_factor": 1.0, "is_public": true, "deleted_at": null, "vcpu_weight": 0, "id": 58}, "nova_object.namespace": "nova"}} | null | null |
| vcpu_model | {"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "features": [], "mode": "host-passthrough", "model": null, "arch": null, "match": "exact", "topology": {"nova_object.version": "1.0", "nova_object.changes": ["cores", "threads", "sockets"], "nova_object.name": "VirtCPUTopology", "nova_object.data": {"cores": 1, "threads": 1, "sockets": 2}, "nova_object.namespace": "nova"}}, "nova_object.namespace": "nova"} | null | null |
| migration_context | null | null | null |

## Columns

- created_at: profile metrics skipped
- updated_at: nulls=53
- deleted_at: nulls=63
- deleted: int 0..211264
  - stats: average=98615.3022
- id: unique identifier, int 1..211264
- instance_uuid: 179720 distinct
- numa_topology: nulls=179754
- pci_requests: nulls=184
- flavor: nulls=105364
- vcpu_model: nulls=111869
- migration_context: nulls=179634


# shadow_instance_faults

```sql
CREATE TABLE `shadow_instance_faults` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_uuid` varchar(36),
  `code` int NOT NULL,
  `message` varchar(255),
  `details` text,
  `host` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=204829;
```

## Rows

- total=201285

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-07T16:55:40 | 2013-06-16T13:40:53 | 2013-04-05T22:11:49 |
| updated_at | null | null | null |
| deleted_at | 2019-11-07T18:28:41 | 2013-06-16T13:55:46 | 2013-04-05T22:13:43 |
| id | 204828 | 126354 | 26094 |
| instance_uuid | fe6c2d4d-d26d-4816-80cf-6baf2989203b | 6fd0d4c6-0963-406f-a591-c8bfcabb4e3f | 5aa68db2-877e-46dd-9e3a-cfa891de6b1f |
| code | 500 | 500 | 500 |
| message | 22c323b0493531e2b749b9918d7483da | 2f0ffe5e898249e3506367ee07ce4835 | 2f0ffe5e898249e3506367ee07ce4835 |
| details | 1d7bcac64380dd31e129a1fd15e3f795 | ee9f89f55405ff6ada25fefabe558dda | ee9f89f55405ff6ada25fefabe558dda |
| host | gamut-16 |  |  |
| deleted | 204828 | 430471 | 308946 |

## Columns

- created_at: profile metrics skipped
- updated_at: all NULL
- deleted_at: nulls=27912
- id: unique identifier, int 1..204828
- instance_uuid: profile metrics skipped
- code: int 400..500
  - stats: average=498.2082
- message: profile metrics skipped
- details: nulls=3281
- host: profile metrics skipped
- deleted: int 0..446923
  - stats: average=275318.1017


# shadow_instance_group_member

```sql
CREATE TABLE `shadow_instance_group_member` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `deleted` int,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_id` varchar(255),
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=333;
```

## Rows

- total=84

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2017-07-11T16:14:30 | 2017-06-28T13:27:24 | 2017-06-28T13:27:22 |
| updated_at | null | null | null |
| deleted_at | 2017-07-11T16:15:13 | 2017-07-06T20:47:05 | 2017-07-06T21:13:39 |
| deleted | 332 | 289 | 288 |
| id | 332 | 289 | 288 |
| instance_id | 9e7d58a9-2fae-45c3-b94f-68839d0fee21 | 9842f39a-f671-4e3d-bac7-3d505d7ab3c9 | fda1f27a-aeda-44f1-9a04-14d1d7c89910 |
| group_id | 14 | 11 | 11 |

## Columns

- created_at: 52 distinct
- updated_at: all NULL
- deleted_at: 67 distinct
- deleted: all distinct, int 241..332
  - stats: average=282.6905, median=282.5000
- id: unique identifier, int 241..332
- instance_id: unique identifier
- group_id: 11=81, 14=2, 12=1, int 11..14


# shadow_instance_group_policy

## All rows

| column | row 1 | row 2 |
|---|---|---|
| created_at | 2016-11-07T17:54:03 | 2016-11-07T20:59:35 |
| updated_at | null | null |
| deleted_at | 2017-07-06T23:18:19 | 2016-11-07T22:09:55 |
| deleted | 11 | 12 |
| id | 11 | 12 |
| policy | anti-affinity | anti-affinity |
| group_id | 11 | 12 |


# shadow_instance_info_caches

```sql
CREATE TABLE `shadow_instance_info_caches` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `network_info` text,
  `instance_uuid` varchar(36) NOT NULL,
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=742115;
```

## Rows

- total=263732

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:45:47 | 2014-04-25T00:55:25 | 2015-04-13T08:54:00 |
| updated_at | 2019-11-08T16:49:58 | 2014-04-25T00:55:32 | 2015-04-13T08:54:07 |
| deleted_at | 2019-11-08T16:49:58 | 2014-04-25T01:08:11 | 2015-04-13T09:04:46 |
| id | 742114 | 490861 | 596560 |
| network_info | [] | [{"ovs_interfaceid": "2d2b3b25-f630-4876-9a8c-5b7400d2c26b", "network": {"bridge": "br-int", "subnets": [{"ips": [{"meta": {}, "version": 4, "type": "fixed", "floating_ips": [], "address": "10.86.77.93/8"}], "version": 4, "meta": {}, "dns": [{"meta": {}, "version": 4, "type": "dns", "address": "10.67.40.40/8"}, {"meta": {}, "version": 4, "type": "dns", "address": "10.229.203.154/8"}, {"meta": {}, "version": 4, "type": "dns", "address": "10.49.228.132/8"}], "routes": [], "cidr": "10.37.117.235/8", "gateway": {"meta": {}, "version": 4, "type": "gateway", "address": "10.51.22.157/8"}}], "meta": {"injected": false, "tenant_id": "6f9adccbd03e4d2186756896957a14bf"}, "id": "0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d", "label": "inet"}, "devname": "tap2d2b3b25-f6", "qbh_params": null, "meta": {}, "address": "fa:16:3e:30:60:d8", "type": "ovs", "id": "2d2b3b25-f630-4876-9a8c-5b7400d2c26b", "qbg_params": null}] | [{"profile": {}, "ovs_interfaceid": "17850364-180c-413a-81c0-9c4cb7d66bf8", "network": {"bridge": "br-int", "subnets": [{"ips": [{"meta": {}, "version": 4, "type": "fixed", "floating_ips": [], "address": "10.98.127.27/8"}], "version": 4, "meta": {}, "dns": [{"meta": {}, "version": 4, "type": "dns", "address": "10.67.40.40/8"}, {"meta": {}, "version": 4, "type": "dns", "address": "10.229.203.154/8"}, {"meta": {}, "version": 4, "type": "dns", "address": "10.49.228.132/8"}], "routes": [{"interface": null, "cidr": "10.169.77.216/8", "meta": {}, "gateway": {"meta": {}, "version": 4, "type": "gateway", "address": "10.232.49.230/8"}}], "cidr": "10.37.117.235/8", "gateway": {"meta": {}, "version": 4, "type": "gateway", "address": "10.51.22.157/8"}}], "meta": {"injected": false, "tenant_id": "6f9adccbd03e4d2186756896957a14bf"}, "id": "0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d", "label": "inet"}, "devname": "tap17850364-18", "vnic_type": "normal", "qbh_params": null, "meta": {}, "details": {"port_filter": true, "ovs_hybrid_plug": true}, "address": "fa:16:3e:0e:40:9f", "active": false, "type": "ovs", "id": "17850364-180c-413a-81c0-9c4cb7d66bf8", "qbg_params": null}] |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | ef46d70d-6504-4376-878d-c1538fd33c7b | 792ef4fd-2762-4132-a43f-078266d82c12 |
| deleted | 742114 | 490861 | 596560 |

## Columns

- created_at: profile metrics skipped
- updated_at: nulls=26182
- deleted_at: nulls=5
- id: unique identifier, int 3084..742114
- network_info: profile metrics skipped
- instance_uuid: profile metrics skipped
- deleted: int 0..742114
  - stats: average=584619.6283


# shadow_instance_metadata

```sql
CREATE TABLE `shadow_instance_metadata` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `key` varchar(255),
  `value` varchar(255),
  `instance_uuid` varchar(36),
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=2029;
```

## Rows

- total=1554

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-05-25T02:48:30 | 2016-07-07T21:24:42 | 2017-12-18T12:10:57 |
| updated_at | null | null | null |
| deleted_at | 2019-05-27T05:30:33 | 2016-07-07T23:09:04 | 2018-02-02T05:08:00 |
| id | 2028 | 337 | 564 |
| key | role | jenkins-instance | system |
| value | theta_point | spind4 | layer2 |
| instance_uuid | 626ca30f-656f-4763-9de8-6927e9c23171 | 9991e66c-6195-41d3-b6f5-0be0abc02d6a | 02e70cce-74eb-4ad4-8489-c05438a08040 |
| deleted | 2028 | 337 | 564 |

## Columns

- created_at: 674 distinct
- updated_at: all NULL
- deleted_at: 464 distinct
- id: unique identifier, int 1..2028
- key: 21 distinct
- value: 76 distinct
- instance_uuid: 777 distinct
- deleted: all distinct, int 1..2028
  - stats: average=1077.1705, median=1251.5000


# shadow_instance_system_metadata

```sql
CREATE TABLE `shadow_instance_system_metadata` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_uuid` varchar(36) NOT NULL,
  `key` varchar(255) NOT NULL,
  `value` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=12204054;
```

## Rows

- total=4879813

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:49:56 | 2013-09-30T18:18:22 | 2014-06-10T19:29:48 |
| updated_at | null | null | 2014-06-10T19:29:48 |
| deleted_at | 2019-11-08T16:49:58 | null | 2014-06-10T19:29:48 |
| id | 12204053 | 7020804 | 8045452 |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | c1f32b3c-84fb-40e5-9273-8d0648df8b55 | f84852d0-8b86-4c6f-8111-07b50438492a |
| key | clean_attempts | instance_type_rxtx_factor | clean_attempts |
| value | comet-star-gamma | comet-star-gamma | comet-star-gamma |
| deleted | 12204053 | 0 | 8045452 |

## Columns

- created_at: profile metrics skipped
- updated_at: nulls=4819075
- deleted_at: nulls=4499466
- id: unique identifier, int 6918265..12204053
- instance_uuid: profile metrics skipped
- key: profile metrics skipped
- value: nulls=231539
- deleted: int 0..12204053


# shadow_instance_type_extra_specs

```sql
CREATE TABLE `shadow_instance_type_extra_specs` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_type_id` int NOT NULL,
  `key` varchar(255),
  `value` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=112;
```

## Rows

- total=53

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2015-08-17T18:40:38 | 2014-04-27T20:03:33 | 2015-08-17T18:39:11 |
| updated_at | null | null | null |
| deleted_at | 2015-08-17T18:41:58 | 2014-05-15T14:40:54 | 2015-08-17T18:40:38 |
| id | 111 | 77 | 110 |
| instance_type_id | 149 | 110 | 148 |
| key | tig | overcommit | tig |
| value | true | false | true |
| deleted | 111 | 77 | 110 |

## Columns

- created_at: 46 distinct
- updated_at: all NULL
- deleted_at: 28 distinct
- id: unique identifier, int 1..111
- instance_type_id: unique identifier, int 15..149
- key: "overcommit"=32, "tig"=11, "ups"=6, "test"=4
- value: "default"=28, "true"=21, "false"=4
- deleted: all distinct, int 1..111
  - stats: average=46.1887, median=27.0000


# shadow_instance_type_projects

```sql
CREATE TABLE `shadow_instance_type_projects` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `instance_type_id` int NOT NULL,
  `project_id` varchar(255),
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=221;
```

## Rows

- total=104

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2015-12-17T16:58:14 | 2014-02-08T02:30:15 | 2013-08-08T20:31:43 |
| updated_at | null | null | null |
| deleted_at | 2015-12-17T17:06:10 | 2015-04-10T15:20:56 | 2014-04-27T20:03:33 |
| id | 220 | 52 | 6 |
| instance_type_id | 152 | 101 | 54 |
| project_id | tig | 6f9adccbd03e4d2186756896957a14bf | 98333a1a28e746fa8c629c83a818ad57 |
| deleted | 220 | 52 | 6 |

## Columns

- created_at: 63 distinct
- updated_at: all NULL
- deleted_at: 40 distinct
- id: unique identifier, int 2..220
- instance_type_id: 37 distinct, int 50..152
- project_id: "6f9adccbd03e4d2186756896957a14bf"=27, "98333a1a28e746fa8c629c83a818ad57"=22, "17ea94ad74b64b9d92f4888336a598c7"=20, "717cc16840494e8795e2ee25c46fe797"=10, "7691c9955ce1444ab366d041f5bdf33c"=7, "292c70904ce7415c8626f801bbf1ed0c"=4, "47c0857cf5b5452a86f640fd44be1d40"=4, "09ad05432f914e26bc417bf58f1cb4d2"=3, "tig"=3, "a3ccd76b29264bbe94415833015c9379"=2, "4f5d702fa8674268be123e7df3eb9faa"=1, "e3fb2659584e436a832461dac02835f0"=1
- deleted: all distinct, int 2..220
  - stats: average=102.1827, median=103.5000


# shadow_instances

```sql
CREATE TABLE `shadow_instances` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `internal_id` int,
  `user_id` varchar(255),
  `project_id` varchar(255),
  `image_ref` varchar(255),
  `kernel_id` varchar(255),
  `ramdisk_id` varchar(255),
  `launch_index` int,
  `key_name` varchar(255),
  `key_data` text,
  `power_state` int,
  `vm_state` varchar(255),
  `memory_mb` int,
  `vcpus` int,
  `hostname` varchar(255),
  `host` varchar(255),
  `user_data` text,
  `reservation_id` varchar(255),
  `scheduled_at` datetime,
  `launched_at` datetime,
  `terminated_at` datetime,
  `display_name` varchar(255),
  `display_description` varchar(255),
  `availability_zone` varchar(255),
  `locked` tinyint(1),
  `os_type` varchar(255),
  `launched_on` text,
  `instance_type_id` int,
  `vm_mode` varchar(255),
  `uuid` varchar(36) NOT NULL,
  `architecture` varchar(255),
  `root_device_name` varchar(255),
  `access_ip_v4` varchar(39),
  `access_ip_v6` varchar(39),
  `config_drive` varchar(255),
  `task_state` varchar(255),
  `default_ephemeral_device` varchar(255),
  `default_swap_device` varchar(255),
  `progress` int,
  `auto_disk_config` tinyint(1),
  `shutdown_terminate` tinyint(1),
  `disable_terminate` tinyint(1),
  `root_gb` int,
  `ephemeral_gb` int,
  `cell_name` varchar(255),
  `node` varchar(255),
  `deleted` int,
  `locked_by` enum('owner','admin'),
  `cleaned` int,
  `ephemeral_key_uuid` varchar(36),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=741070;
```

## Rows

- total=709892

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-05-25T02:48:07 | 2012-11-16T23:06:34 | 2013-06-16T03:14:00 |
| updated_at | 2019-05-27T05:29:18 | 2012-11-16T23:14:06 | 2013-06-16T03:20:32 |
| deleted_at | 2019-05-27T05:29:18 | 2012-11-16T23:15:13 | 2013-06-16T03:20:32 |
| id | 741069 | 139275 | 427678 |
| internal_id | null | null | null |
| user_id | a1ef823458d24a68955fec6f3d390019 | c8490ee0863345f6919b5c63540efca1 | 7415306fc0b6459791760364709ee947 |
| project_id | 17ea94ad74b64b9d92f4888336a598c7 | 3008a142e9524f7295b06ea811908f93 | 3008a142e9524f7295b06ea811908f93 |
| image_ref | d74d6560-3a34-4ae6-bd89-ec4dc354b922 | 52a1451b-8311-4be2-b148-c7ee578a78eb | b1ca5c25-74f7-445c-9cd9-242c270ea069 |
| kernel_id | null | null | null |
| ramdisk_id | null | null | null |
| launch_index | 0 | 0 | 0 |
| key_name | null | flare_cvgr-feyl-nuws-tenn-pwyt | grav |
| key_data | null | 73e6cd4cbdc667c8e27bcf089ffda82a | b696dfa1d67cfac853c42b0d67f151e0 |
| power_state | 0 | 1 | 0 |
| vm_state | deleted | deleted | error |
| memory_mb | 4096 | 2048 | 8192 |
| vcpus | 8 | 1 | 4 |
| hostname | helix | helio | starx |
| host | beam8-22 | shift7-51 |  |
| user_data | 557863e33d149078ec6e1a03e609495d | 97df54dc2303b003bcb7a6c8c3490264 | null |
| reservation_id | r-92gre1nf | r-vrberaff | r-cyn2dwh4 |
| scheduled_at | null | 2012-11-16T23:07:15 | null |
| launched_at | 2019-05-25T02:48:59 | 2012-11-16T23:10:28 | null |
| terminated_at | 2019-05-27T05:29:29 | 2012-11-16T23:14:06 | null |
| display_name | helix | 10.143.195.81/8 | 10.110.201.179/8 |
| display_description | helix | null | null |
| availability_zone | null | null | null |
| locked | 0 | 0 | 0 |
| os_type | null | null | null |
| launched_on | beam8-22 | shift7-51 | null |
| instance_type_id | 60 | 5 | 3 |
| vm_mode | null | null | null |
| uuid | 5381e77a-b474-4f22-8729-3fdf0bfbcd18 | 6bba8332-2dd7-4dfb-a2a9-2dbb197fc2cc | e6790fbe-cf8f-45a5-bd59-a1b46fcf18c0 |
| architecture | null | null | null |
| root_device_name | /dev/vda | /dev/vda | null |
| access_ip_v4 | null | null | null |
| access_ip_v6 | null | null | null |
| config_drive | null | null | null |
| task_state | null | null | deleting |
| default_ephemeral_device | null | /dev/vdb | null |
| default_swap_device | null | null | null |
| progress | 0 | 0 | 0 |
| auto_disk_config | 0 | null | null |
| shutdown_terminate | 0 | 0 | 0 |
| disable_terminate | 0 | 0 | 0 |
| root_gb | 10 | 10 | 10 |
| ephemeral_gb | 0 | 20 | 80 |
| cell_name | null | null | null |
| node | beam8-22.yahoo.ca.com | null | null |
| deleted | 741069 | 139275 | 427678 |
| locked_by | null | null | null |
| cleaned | 1 | 1 | 1 |
| ephemeral_key_uuid | null | null | null |

## Columns

- created_at: profile metrics skipped
- updated_at: nulls=76
- deleted_at: profile metrics skipped
- id: unique identifier, int 1..741069
- internal_id: all NULL
- user_id: profile metrics skipped
- project_id: profile metrics skipped
- image_ref: nulls=2440
- kernel_id: nulls=709773
- ramdisk_id: nulls=709773
- launch_index: int 0..511
  - stats: average=2.7497
- key_name: nulls=30973
- key_data: nulls=30974
- power_state: int 0..5
  - stats: average=0.7561
- vm_state: profile metrics skipped
- memory_mb: int 1..98304
  - stats: average=4291.6139
- vcpus: int 1..32
  - stats: average=2.3635
- hostname: profile metrics skipped
- host: profile metrics skipped
- user_data: nulls=369424
- reservation_id: profile metrics skipped
- scheduled_at: nulls=312941
- launched_at: nulls=173199
- terminated_at: nulls=140495
- display_name: profile metrics skipped
- display_description: nulls=434256
- availability_zone: nulls=682787
- locked: int 0..1
  - stats: average=0.0000
- os_type: all NULL
- launched_on: nulls=143414
- instance_type_id: int 1..174
- vm_mode: all NULL
- uuid: profile metrics skipped
- architecture: nulls=709734
- root_device_name: nulls=147674
- access_ip_v4: all NULL
- access_ip_v6: all NULL
- config_drive: nulls=709547
- task_state: nulls=567690
- default_ephemeral_device: nulls=401136
- default_swap_device: nulls=709415
- progress: int 0..0
  - stats: average=0.0000
- auto_disk_config: nulls=481255, int 0..1
  - stats: average=0.0023
- shutdown_terminate: int 0..1
  - stats: average=0.0272
- disable_terminate: int 0..0
  - stats: average=0.0000
- root_gb: int 0..100
  - stats: average=12.3716
- ephemeral_gb: int 0..360
  - stats: average=24.6218
- cell_name: all NULL
- node: nulls=470739
- deleted: int 1..741069
  - stats: average=357136.6198
- locked_by: nulls=709884
- cleaned: int 0..1
  - stats: average=0.9936
- ephemeral_key_uuid: all NULL


# shadow_key_pairs

```sql
CREATE TABLE `shadow_key_pairs` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255),
  `user_id` varchar(255),
  `fingerprint` varchar(255),
  `public_key` text,
  `deleted` int,
  `type` enum('ssh','x509') NOT NULL DEFAULT 'ssh',
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=152;
```

## Rows

- total=51

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2013-07-29T21:03:17 | 2013-03-22T15:49:34 | 2013-02-04T22:26:09 |
| updated_at | 2013-07-29T21:03:34 | 2013-03-22T17:58:35 | 2013-02-20T22:07:41 |
| deleted_at | 2013-07-29T21:03:34 | 2013-03-22T17:58:35 | 2013-02-20T22:07:41 |
| id | 151 | 115 | 82 |
| name | axiom-dash | warp-warp | alpha0 |
| user_id | e754f357f72c43ad9301478cb2ccf3aa | 1fa83f177d0d41dab12c7d2ce6e5e6a0 | 0df639d1cf6a48f7b9ddf6cf68772ca8 |
| fingerprint | b1:9f:70:51:7f:b3:bd:7d:28:8d:cc:9d:ff:1a:10:71 | db:4a:93:83:8f:98:c1:c7:1c:78:10:a6:e8:ce:5a:77 | 2a:cf:85:d1:04:3c:85:a4:b3:1e:59:d0:fe:3d:68:4c |
| public_key | 63b3992a6ad94ee9a0c224d89dbd150e | a1e4933ce59c884ad93d282a5224dc15 | c2285738ba3ef312dc9400986c8df6ad |
| deleted | 151 | 115 | 82 |
| type | ssh | ssh | ssh |

## Columns

- created_at: all distinct
- updated_at: 48 distinct
- deleted_at: 48 distinct
- id: unique identifier, int 2..151
- name: 38 distinct
- user_id: 23 distinct
- fingerprint: all distinct
- public_key: all distinct
- deleted: all distinct, int 2..151
  - stats: average=73.6275, median=71.0000
- type: "ssh"=51


# shadow_migrations

```sql
CREATE TABLE `shadow_migrations` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `source_compute` varchar(255),
  `dest_compute` varchar(255),
  `dest_host` varchar(255),
  `status` varchar(255),
  `instance_uuid` varchar(36),
  `old_instance_type_id` int,
  `new_instance_type_id` int,
  `source_node` varchar(255),
  `dest_node` varchar(255),
  `deleted` int,
  `migration_type` enum('migration','resize','live-migration','evacuation'),
  `hidden` tinyint(1),
  `memory_total` bigint,
  `memory_processed` bigint,
  `memory_remaining` bigint,
  `disk_total` bigint,
  `disk_processed` bigint,
  `disk_remaining` bigint,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=4387;
```

## Rows

- total=2112

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-08-13T19:01:58 | 2017-08-14T17:49:40 | 2017-07-13T20:29:19 |
| updated_at | 2019-08-13T19:02:31 | 2017-08-14T17:49:45 | 2017-07-13T20:36:49 |
| deleted_at | null | 2018-09-06T14:55:17 | null |
| id | 4386 | 2531 | 1663 |
| source_compute | prime3-77 | pico6-23 | grav9-5 |
| dest_compute | cosmo3-23 | forge8-81 | spark9-96 |
| dest_host | 10.165.53.177/8 | null | null |
| status | confirmed | error | completed |
| instance_uuid | 19ae8899-9ed9-4880-bb19-f9e3a22354af | f774060e-18f1-44d3-a806-d7a535059ce0 | f3a45f31-4112-47b1-aa8f-5c9ecbeedd39 |
| old_instance_type_id | 66 | 81 | 66 |
| new_instance_type_id | 73 | 81 | 66 |
| source_node | prime3-77.yahoo.ca.com | null | null |
| dest_node | cosmo3-23.yahoo.ca.com | null | null |
| deleted | 0 | 1 | 0 |
| migration_type | resize | live-migration | live-migration |
| hidden | 0 | 0 | 0 |
| memory_total | null | 0 | 0 |
| memory_processed | null | 0 | 0 |
| memory_remaining | null | 0 | 0 |
| disk_total | null | 0 | 0 |
| disk_processed | null | 0 | 0 |
| disk_remaining | null | 0 | 0 |

## Columns

- created_at: 2093 distinct
- updated_at: 1965 distinct, nulls=109
- deleted_at: 2018-09-06 14:55:17=307, 2018-09-06 14:58:53=60, nulls=1745
- id: unique identifier, int 6..4386
- source_compute: 125 distinct
- dest_compute: 129 distinct, nulls=26
- dest_host: 115 distinct, nulls=1133
- status: "completed"=813, "confirmed"=580, "error"=400, "pre-migrating"=104, "failed"=93, "confirming"=31, "migrating"=26, "cancelled"=19, "preparing"=15, "reverted"=9, "finished"=7, "post-migrating"=7, "accepted"=5, "running"=2, "done"=1
- instance_uuid: 1253 distinct
- old_instance_type_id: 57 distinct, nulls=30, int 48..162
- new_instance_type_id: 55 distinct, nulls=30, int 48..172
- source_node: 120 distinct, nulls=1126
- dest_node: 117 distinct, nulls=1133
- deleted: 0=1745, 1=367
- migration_type: "live-migration"=1126, "resize"=306, "migration"=113, "evacuation"=30, nulls=537
- hidden: 0=2112
- memory_total: 31 distinct, nulls=1146, int 0..103088463872
  - stats: average=9420985833.7391, median=2156732416.0000
- memory_processed: 542 distinct, nulls=1146, int 0..317583106422
  - stats: average=6434959658.9255, median=391201103.5000
- memory_remaining: 541 distinct, nulls=1146, int 0..40323997696
  - stats: average=1056798669.1180, median=98648064.0000
- disk_total: 0=966, nulls=1146
- disk_processed: 0=966, nulls=1146
- disk_remaining: 0=966, nulls=1146


# shadow_pci_devices

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| created_at | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 |
| updated_at | 2016-10-18T15:08:41 | 2016-10-18T15:08:58 | 2016-10-18T15:11:34 | 2016-10-18T15:09:26 | 2016-10-13T14:12:40 | 2016-10-13T14:12:40 | 2016-10-13T14:12:40 | 2016-10-13T14:12:40 |
| deleted_at | 2016-10-13T21:02:54 | 2016-10-13T21:03:55 | 2016-10-13T21:02:54 | 2016-10-13T21:04:53 | 2016-10-13T21:02:54 | 2016-10-13T21:03:55 | 2016-10-13T21:02:54 | 2016-10-13T21:05:55 |
| deleted | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| id | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| compute_node_id | 90 | 90 | 90 | 90 | 90 | 90 | 90 | 90 |
| address | 0000:64:31.0 | 0000:06:33.0 | 0000:75:06.0 | 0000:54:12.0 | 0000:04:56.0 | 0000:93:95.0 | 0000:83:59.0 | 0000:43:32.0 |
| product_id | 102d | 102d | 102d | 102d | 102d | 102d | 102d | 102d |
| vendor_id | 10de | 10de | 10de | 10de | 10de | 10de | 10de | 10de |
| dev_type | type-PCI | type-PCI | type-PCI | type-PCI | type-PCI | type-PCI | type-PCI | type-PCI |
| dev_id | pci_0000_04_00_0 | pci_0000_05_00_0 | pci_0000_08_00_0 | pci_0000_09_00_0 | pci_0000_83_00_0 | pci_0000_84_00_0 | pci_0000_87_00_0 | pci_0000_88_00_0 |
| label | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d |
| status | allocated | allocated | available | allocated | available | available | available | available |
| extra_info | {} | {} | {} | {} | {} | {} | {} | {} |
| instance_uuid | 66fe2820-0a93-4e89-8575-650e1b18e037 | eb15a522-752f-4658-82bd-8521bed2c612 | null | 9269391a-4ce4-4c8d-993d-5ad7a9c3879b | null | null | null | null |
| request_id | null | null | null | null | null | null | null | null |
| numa_node | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| parent_addr | null | null | null | null | null | null | null | null |


# shadow_reservations

```sql
CREATE TABLE `shadow_reservations` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `usage_id` int NOT NULL,
  `project_id` varchar(255),
  `resource` varchar(255),
  `delta` int NOT NULL,
  `expire` datetime,
  `deleted` int,
  `user_id` varchar(255),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1614700;
```

## Rows

- total=1297676

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T18:16:30 | 2014-06-05T16:11:01 | 2014-01-12T05:18:41 |
| updated_at | null | null | null |
| deleted_at | 2019-11-08T18:16:31 | 2014-06-05T16:11:05 | 2014-01-12T05:18:46 |
| id | 1614699 | 236433 | 169561 |
| uuid | 7912a75e-ca94-42ed-9867-a1b451d02ac7 | 06e2cf92-d178-4806-998b-9222cb6bcaa9 | 9e4996d9-9418-408e-8139-9d71ad14bd90 |
| usage_id | 2879 | 211 | 168 |
| project_id | da4266d0e4f24017b0dc114ea64ad422 | 3008a142e9524f7295b06ea811908f93 | 17ea94ad74b64b9d92f4888336a598c7 |
| resource | ram | ram | instances |
| delta | 65536 | -2048 | -1 |
| expire | 2019-11-09T18:16:30 | 2014-06-06T16:11:01 | 2014-01-13T05:18:41 |
| deleted | 1614699 | 236433 | 169561 |
| user_id | 38fe63ea602f4200aa85186291d39df1 | 59a5934524c54089af8f35bed2ea7eaa | a1ef823458d24a68955fec6f3d390019 |

## Columns

- created_at: profile metrics skipped
- updated_at: all NULL
- deleted_at: profile metrics skipped
- id: unique identifier, int 1..1614699
- uuid: profile metrics skipped
- usage_id: int 1..2940
- project_id: profile metrics skipped
- resource: profile metrics skipped
- delta: int -98304..761856
- expire: profile metrics skipped
- deleted: int 1..1614699
- user_id: nulls=1176


# shadow_security_group_rules

```sql
CREATE TABLE `shadow_security_group_rules` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `parent_group_id` int,
  `protocol` varchar(255),
  `from_port` int,
  `to_port` int,
  `cidr` varchar(43),
  `group_id` int,
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=188;
```

## Rows

- total=40

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2013-06-12T22:05:18 | 2013-03-22T15:27:37 | 2013-06-12T21:09:23 |
| updated_at | 2013-06-12T22:06:40 | 2013-03-22T15:28:49 | 2013-06-12T21:34:43 |
| deleted_at | 2013-06-12T22:06:40 | 2013-03-22T15:28:49 | 2013-06-12T21:34:43 |
| id | 187 | 97 | 174 |
| parent_group_id | 66 | 55 | 64 |
| protocol | tcp | tcp | tcp |
| from_port | 446 | 22 | 445 |
| to_port | 446 | 22 | 445 |
| cidr | 10.71.29.205/8 | 10.71.29.205/8 | 10.71.29.205/8 |
| group_id | null | null | null |
| deleted | 187 | 97 | 174 |

## Columns

- created_at: all distinct
- updated_at: 33 distinct
- deleted_at: 33 distinct
- id: unique identifier, int 6..187
- parent_group_id: 64=13, 55=5, 63=4, 9=3, 5=2, 19=2, 66=2, 15=1, 21=1, 22=1, 39=1, 46=1, 47=1, 50=1, 51=1, 58=1, int 5..66
- protocol: "tcp"=26, "udp"=11, "icmp"=3
- from_port: 22=9, 1=6, 445=5, 9000=4, -1=2, 137=2, 139=2, 389=2, 8080=2, 8=1, 80=1, 123=1, 138=1, 446=1, 9010=1, int -1..9010
- to_port: 22=8, 65535=6, 445=5, 10000=4, 137=2, 139=2, 255=2, 389=2, 8080=2, -1=1, 23=1, 80=1, 138=1, 446=1, 456=1, 9020=1, int -1..65535
- cidr: "10.71.29.205/8"=29, "10.122.66.108/8"=4, "10.216.18.158/8"=3, "10.139.2.255/8"=1, nulls=3
- group_id: 22=1, 39=1, 58=1, nulls=37, int 22..58
- deleted: all distinct, int 6..187
  - stats: average=112.0500, median=111.0000


# shadow_services

```sql
CREATE TABLE `shadow_services` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `host` varchar(255),
  `binary` varchar(255),
  `topic` varchar(255),
  `report_count` int NOT NULL,
  `disabled` tinyint(1),
  `deleted` int,
  `disabled_reason` varchar(255),
  `last_seen_up` datetime,
  `forced_down` tinyint(1),
  `version` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=243;
```

## Rows

- total=110

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2016-08-11T15:47:19 | 2012-07-12T15:21:07 | 2013-02-19T17:18:25 |
| updated_at | 2016-08-11T15:57:05 | 2014-02-07T13:47:23 | 2014-02-07T13:48:11 |
| deleted_at | 2016-08-11T15:58:28 | null | null |
| id | 242 | 31 | 128 |
| host | blaze-shift | zenta1-8 | shine-16 |
| binary | nova-conductor | nova-network | nova-network |
| topic | conductor | network | network |
| report_count | 59 | 3345916 | 180103 |
| disabled | 0 | 1 | 1 |
| deleted | 242 | 1 | 1 |
| disabled_reason | null | null | null |
| last_seen_up | null | null | null |
| forced_down | 0 | 0 | 0 |
| version | 0 | 0 | 0 |

## Columns

- created_at: 105 distinct
- updated_at: 105 distinct
- deleted_at: 43 distinct, nulls=61
- id: unique identifier, int 1..242
- host: 94 distinct
- binary: "nova-network"=61, "nova-conductor"=33, "nova-compute"=8, "nova-volume"=5, "nova-cert"=1, "nova-consoleauth"=1, "nova-scheduler"=1
- topic: "network"=61, "conductor"=33, "compute"=8, "volume"=5, "cert"=1, "consoleauth"=1, "scheduler"=1
- report_count: 109 distinct, int 1..8648106
  - stats: average=2111383.1636, median=1700060.0000
- disabled: 1=76, 0=34
- deleted: 49 distinct, int 1..242
  - stats: average=59.4182, median=1.0000
- disabled_reason: "heat death"=1, "old-version"=1, nulls=108
- last_seen_up: all NULL
- forced_down: 0=110
- version: 0=110


# shadow_snapshots

## All rows

| column | row 1 |
|---|---|
| created_at | 2012-10-06T01:34:31 |
| updated_at | 2012-10-06T01:34:51 |
| deleted_at | 2012-10-06T01:34:57 |
| id | c5896a01-0f52-4d27-8e63-8b35f03ea197 |
| volume_id | 98ac28f5-77d8-476b-b3e1-c90a0fd3e880 |
| user_id | a1ef823458d24a68955fec6f3d390019 |
| project_id | 98333a1a28e746fa8c629c83a818ad57 |
| status | deleting |
| progress | 0% |
| volume_size | 32 |
| scheduled_at | null |
| display_name | celes-spark-gamma |
| display_description | null |
| deleted | c5896a01-0f52-4d27-8e63-8b35f03ea197 |


# shadow_virtual_interfaces

```sql
CREATE TABLE `shadow_virtual_interfaces` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(255),
  `network_id` int,
  `uuid` varchar(36),
  `instance_uuid` varchar(36),
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=414195;
```

## Rows

- total=742

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2013-09-17T02:44:27 | 2012-10-15T20:51:27 | 2012-09-18T13:41:20 |
| updated_at | null | null | null |
| deleted_at | null | 2012-10-22T11:23:39 | 2012-10-22T20:32:59 |
| id | 414194 | 30047 | 8126 |
| address | m1:c2:w7:oq:s5:sn | it:v5:wn:dk:9w:ct | ja:ks:8f:8e:3n:77 |
| network_id | 1 | 1 | 1 |
| uuid | 19495c14-0877-43c3-95db-af103f6d47a6 | 9a27e2db-7366-4514-9a69-3f2087627b04 | 32d399ea-6379-4e02-b795-854405d643bd |
| instance_uuid | 6154483e-317a-43bc-9563-cd945f59a242 | 49016342-3903-4a6c-9cc0-39358f66d336 | 5d6cb787-05df-4cdc-9af1-b048d9c1b67b |
| deleted | 0 | 27754 | 8140 |

## Columns

- created_at: 429 distinct
- updated_at: all NULL
- deleted_at: 455 distinct, nulls=4
- id: unique identifier, int 914..414194
- address: all distinct
- network_id: 1=742
- uuid: unique identifier
- instance_uuid: unique identifier
- deleted: 735 distinct, int 0..357436
  - stats: average=71492.8598, median=44084.0000


# snapshot_id_mappings

## All rows

| column | row 1 |
|---|---|
| created_at | null |
| updated_at | null |
| deleted_at | null |
| id | 1 |
| uuid | 1285e294-bece-489e-a40d-eb64b2f0ee7b |
| deleted | 0 |


# snapshots

## All rows

| column | row 1 |
|---|---|
| created_at | 2012-07-19T16:31:59 |
| updated_at | 2012-07-19T16:32:00 |
| deleted_at | null |
| id | 1285e294-bece-489e-a40d-eb64b2f0ee7b |
| volume_id | 98ac28f5-77d8-476b-b3e1-c90a0fd3e880 |
| user_id | 0be8fa0d641a4e778b9262bd2e5f40b5 |
| project_id | 6f9adccbd03e4d2186756896957a14bf |
| status | available |
| progress | 100% |
| volume_size | 32 |
| scheduled_at | null |
| display_name | novae-spear-flare |
| display_description | 3449069e92d320280a69b6f0a8175d55 |
| deleted | null |


# volume_id_mappings

```sql
CREATE TABLE `volume_id_mappings` (
  `created_at` datetime,
  `updated_at` datetime,
  `deleted_at` datetime,
  `id` int NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `deleted` int,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=66;
```

## Rows

- total=65

| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2014-12-08T21:45:04 | 2013-10-09T18:54:44 | 2012-12-17T20:48:21 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 65 | 40 | 32 |
| uuid | a62fdf5f-b89d-472e-aab3-8c0bf393c905 | 7d6a7600-58cd-4ab3-9543-85db5adda72d | 5f4795fe-fea3-4783-a078-b322cdea09dc |
| deleted | 0 | 0 | 0 |

## Columns

- created_at: 2014-12-08 21:45:01=6, 2014-12-08 21:45:02=6, 2014-05-29 13:53:00=4, 2012-11-11 02:08:44=3, 2013-10-09 18:54:44=3, 2014-12-08 21:45:03=3, 2013-09-26 01:41:18=2, 2013-10-17 20:41:25=2, 2014-05-29 13:53:01=2, 2012-12-17 20:48:21=1, 2013-09-25 22:25:09=1, 2013-10-03 22:42:14=1, 2013-10-03 22:43:33=1, 2013-10-18 04:41:06=1, 2014-12-08 21:45:04=1, nulls=28
- updated_at: all NULL
- deleted_at: all NULL
- id: unique identifier, int 1..65
- uuid: unique identifier
- deleted: 0=65


- Skipped 45 empty table(s): agent_builds, allocations, bw_usage_cache, cells, console_pools, consoles, dns_domains, inventories, project_user_quotas, provider_fw_rules, resource_provider_aggregates, resource_providers, security_group_default_rules, security_group_instance_association, shadow_agent_builds, shadow_aggregates, shadow_bw_usage_cache, shadow_cells, shadow_certificates, shadow_console_pools, shadow_consoles, shadow_dns_domains, shadow_floating_ips, shadow_instance_groups, shadow_instance_id_mappings, shadow_instance_types, shadow_migrate_version, shadow_networks, shadow_project_user_quotas, shadow_provider_fw_rules, shadow_quota_classes, shadow_quota_usages, shadow_quotas, shadow_s3_images, shadow_security_group_default_rules, shadow_security_group_instance_association, shadow_security_groups, shadow_snapshot_id_mappings, shadow_task_log, shadow_volume_id_mappings, shadow_volume_usage_cache, tags, task_log, virtual_interfaces, volume_usage_cache
