
CREATE TABLE `transporter_geo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `transporter_id` bigint(20) DEFAULT 0 comment '骑士ID',
  `lat` decimal(30, 6) DEFAULT NULL comment '纬度',
  `lng` decimal(30, 6) DEFAULT NULL comment '经度',
  `time` bigint(20) DEFAULT 0 comment '导入时间',
  `createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP comment '创建时间',
  `updateTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' comment '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 comment '骑士经纬度表';