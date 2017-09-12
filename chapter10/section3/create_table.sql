CREATE TABLE `hosts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` varchar(15) DEFAULT NULL,
  `groupname` varchar(15) DEFAULT NULL,
  `username` varchar(15) DEFAULT NULL,
  `port` int(11) DEFAULT '22',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;


