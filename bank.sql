-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 16, 2019 at 02:03 AM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('ayush', 'ayush');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `sno` int(100) NOT NULL,
  `from` bigint(10) NOT NULL,
  `to` bigint(10) NOT NULL,
  `date` datetime NOT NULL,
  `deposit` float DEFAULT NULL,
  `withdrawl` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`sno`, `from`, `to`, `date`, `deposit`, `withdrawl`) VALUES
(1, 199802259035480119, 199802259035480119, '2019-04-14 19:43:21', 100000, NULL),
(2, 199802259035480119, 199802259035480119, '2019-04-14 19:59:42', 5000, NULL),
(3, 199802259035480119, 199802259035480119, '2019-04-14 21:04:24', NULL, 5000),
(6, 198505234567891231, 198505234567891231, '2019-04-14 23:21:08', 200, NULL),
(7, 198505234567891231, 198505234567891231, '2019-04-14 23:44:44', NULL, 100),
(8, 199802259035480119, 198505234567891231, '2019-04-14 23:51:21', NULL, 500),
(9, 199802259035480119, 198505234567891231, '2019-04-15 12:20:40', NULL, 100),
(10, 198505234567891231, 199802259035480119, '2019-04-15 12:22:20', NULL, 20),
(11, 199802259035480119, 199802259035480119, '2019-04-15 15:48:19', 4000, NULL),
(12, 199802259035480119, 199802259035480119, '2019-04-15 15:53:40', 4000, NULL),
(13, 199802259035480119, 199802259035480119, '2019-04-15 15:53:46', NULL, 2000);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `acct_no` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `first_name` text NOT NULL,
  `last_name` text NOT NULL,
  `dob` date NOT NULL,
  `address` text NOT NULL,
  `account_type` text NOT NULL,
  `email` varchar(20) NOT NULL,
  `contact_no` bigint(10) NOT NULL,
  `balance` float NOT NULL,
  `date` datetime NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`acct_no`, `password`, `first_name`, `last_name`, `dob`, `address`, `account_type`, `email`, `contact_no`, `balance`, `date`, `status`) VALUES
('199802259035480119', 'ayush', 'ayush', 'shekhar', '1998-02-25', 'patna', 'current', 'cadet4049@gmail.com', 9035480119, 101400, '2019-04-14 00:00:00', 'open'),
('198505234567891231', '19850523', 'abc', 'abc', '1985-05-23', 'bangalore', 'savings', 'ca@ajdba.com', 4567891231, 80, '2019-04-14 23:21:08', 'open');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `sno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
