CREATE TABLE `info_table` (
  `userid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `age` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `info_table`
  ADD PRIMARY KEY (`userid`);