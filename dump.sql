-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: etherscan_db
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.17.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `token_holders`
--

DROP TABLE IF EXISTS `token_holders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token_holders` (
  `id` int(10) DEFAULT NULL,
  `Token` varchar(255) DEFAULT NULL,
  `Rank` int(11) DEFAULT NULL,
  `Address` varchar(42) NOT NULL,
  `Quantity` varchar(255) DEFAULT NULL,
  `Percentage` varchar(255) DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `Since_ICO` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Address`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `token_info`
--

DROP TABLE IF EXISTS `token_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token_info` (
  `id` int(11) DEFAULT NULL,
  `token` varchar(255) NOT NULL,
  `total_supply` varchar(255) DEFAULT NULL,
  `ERC20_Contract` varchar(255) DEFAULT NULL,
  `value_per_token` varchar(255) DEFAULT NULL,
  `decimals` varchar(255) DEFAULT NULL,
  `token_holders` varchar(255) DEFAULT NULL,
  `NO_Of_Transfers` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`token`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `token_transfers`
--

DROP TABLE IF EXISTS `token_transfers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token_transfers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Token` varchar(1500) DEFAULT NULL,
  `Tx_Hash` varchar(255) DEFAULT NULL,
  `Age` datetime DEFAULT NULL,
  `From` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `To` varchar(255) DEFAULT NULL,
  `Quantity` varchar(255) DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2360 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tokens`
--

DROP TABLE IF EXISTS `tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tokens` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `c_index` int(11) DEFAULT NULL,
  `name_str` varchar(255) DEFAULT NULL,
  `name_simple` varchar(255) DEFAULT NULL,
  `icons` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `describes` varchar(1500) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `changes` varchar(255) DEFAULT NULL,
  `volume_24` varchar(255) DEFAULT NULL,
  `market_cap` varchar(255) DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-25 18:32:22
