--This is bank database to import using xampp applications.
-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2021 at 04:24 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Table structure for table `accdetail`
--

CREATE TABLE `accdetail` (
  `aid` int(11) NOT NULL,
  `rid` int(11) NOT NULL,
  `AccNo` varchar(1000) NOT NULL,
  `balance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accdetail`
--

INSERT INTO `accdetail` (`aid`, `rid`, `AccNo`, `balance`) VALUES
(1, 1, '123', 67000),
(2, 2, '1221', 454545),
(3, 3, '147', 700000),
(4, 4, '258', 32632),
(5, 5, '9878', 321459);

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `fname` varchar(1000) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `uname` varchar(1000) NOT NULL,
  `pno` varchar(1000) NOT NULL,
  `pan` varchar(1000) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `adhar` varchar(1000) NOT NULL,
  `pas` varchar(1000) NOT NULL,
  `rid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`fname`, `email`, `uname`, `pno`, `pan`, `address`, `adhar`, `pas`, `rid`) VALUES
('Ashish Phadtare', 'ashish2020@gamil.com', 'ashish', '7774877280', 'EBC093P', 'Pune', '380247482888', '789', 1),
('Nitin', 'nitni@gamil.com', 'nitni', '4548785', 'DVDF58D', 'Mumbai', '656454545', '456', 2),
('Vishal Jadhav', 'vishal@gamil.com', 'vishal', '8989898989', 'UPOA787P', 'Kolhapur', '78799986455', '123', 3),
('Aniket Phadtare', 'aniket2020@gmail.com', 'aniket', '989775454', 'PIEJ045W', 'Pune', '78797454585', '147', 4),
('vikas', 'vikas78@gamil.com', 'vikas', '787945456', 'ADF2828P', 'Pune', '78745545556', '258', 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accdetail`
--
ALTER TABLE `accdetail`
  ADD PRIMARY KEY (`aid`),
  ADD KEY `rid` (`rid`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`rid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accdetail`
--
ALTER TABLE `accdetail`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accdetail`
--
ALTER TABLE `accdetail`
  ADD CONSTRAINT `accdetail_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `register` (`rid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
