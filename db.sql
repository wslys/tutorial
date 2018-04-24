-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: etherscan_db
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.17.10.1

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
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Token` varchar(255) DEFAULT NULL,
  `Rank` int(11) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Quantity` varchar(255) DEFAULT NULL,
  `Percentage` varchar(255) DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `Since_ICO` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_holders`
--

LOCK TABLES `token_holders` WRITE;
/*!40000 ALTER TABLE `token_holders` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_holders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_info`
--

DROP TABLE IF EXISTS `token_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `token` varchar(255) DEFAULT NULL,
  `total_supply` varchar(255) DEFAULT NULL,
  `ERC20_Contract` varchar(255) DEFAULT NULL,
  `value_per_token` varchar(255) DEFAULT NULL,
  `decimals` varchar(255) DEFAULT NULL,
  `token_holders` varchar(255) DEFAULT NULL,
  `NO_Of_Transfers` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_info`
--

LOCK TABLES `token_info` WRITE;
/*!40000 ALTER TABLE `token_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_transfers`
--

DROP TABLE IF EXISTS `token_transfers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token_transfers` (
  `id` int(11) NOT NULL,
  `Token` varchar(255) DEFAULT NULL,
  `Tx_Hash` varchar(255) DEFAULT NULL,
  `Age` datetime DEFAULT NULL,
  `From` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `To` varchar(255) DEFAULT NULL,
  `Quantity` varchar(255) DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_transfers`
--

LOCK TABLES `token_transfers` WRITE;
/*!40000 ALTER TABLE `token_transfers` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_transfers` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tokens`
--

LOCK TABLES `tokens` WRITE;
/*!40000 ALTER TABLE `tokens` DISABLE KEYS */;
INSERT INTO `tokens` VALUES (1,51,'Cortex Coin ','CTXC','/token/images/cortex_28.png','0xea11755ae41d889ceec39a63e6ff75a02bc1c00d','Decentralized AI autonomous system.','$1.8553','35.49%','$63,187,100','$151,627,855','2018-04-24 14:50:44'),(2,52,'MATRIX AI Network ','MAN','/token/images/matrix_ai_28.png','0xe25bcec5d3801ce3a794079bf94adf1b8ccd802d','Aims to be an open source public intelligent blockchain platform','$1.0084','13.78%','$1,989,730','$151,252,500','2018-04-24 14:50:44'),(3,53,'Fusion ','FSN','/token/images/fusion_28.png','0xd0352a019e9ab9d757776f532377aaebd36fd541','FUSION is a public blockchain devoting itself to creating an inclusive cryptofinancial platform by providing cross-chain, cross-organization, and cross-datasource smart contracts.','$5.0608','0.71%','$4,004,020','$150,225,870','2018-04-24 14:50:44'),(4,54,'DENT ','DENT','/token/images/dentcoin.png','0x3597bfd533a99c9aa083587b074434e61eb0a258','Aims to disrupt the mobile operator industry by creating an open marketplace for buying and selling of mobile data.','$0.0136','-6.98%','$7,751,810','$144,635,671','2018-04-24 14:50:44'),(5,55,'Civic ','CVC','/token/images/civic_28.png','0x41e5560054824ea6b0732e656e3ad64e20e94e45','Giving businesses and individuals the tools to control and protect identities','$0.4211','-0.50%','$8,572,130','$144,301,017','2018-04-24 14:50:44'),(6,56,'Game.com Token ','GTC','/token/images/gameico_28.png','0xB70835D7822eBB9426B56543E391846C107bd32C','Game.com is focused on creating a global gaming platform for blockchain digital currencies.','$0.2372','-19.78%','$194,293,000','$141,792,445','2018-04-24 14:50:44'),(7,57,'Loom ','LOOM','/token/images/loom_28.png','0xa4e8c3ec456107ea67d3075bf9e3df3a75823db0','Online game & social apps','$0.2769','2.00%','$1,797,700','$141,637,058','2018-04-24 14:50:44'),(8,58,'Po.et ','POE','/token/images/poet_28.png','0x0e0989b1f9b8a38983c2ba8053269ca62ec9b195','Po.et aims to reclaim value for content creators, publishers and consumers.','$0.0562','6.13%','$9,874,100','$126,838,913','2018-04-24 14:50:44'),(9,59,'SAN ','SAN','/token/images/san_28.png','0x7c5a0ce9267ed19b22f8cae653f198e3e8daf098','A Better Way to Trade Crypto-Markets - Market Datafeeds, Newswires, and Crowd Sentiment Insights for the Blockchain World','$2.0168','8.76%','$3,757,820','$126,375,316','2018-04-24 14:50:44'),(10,60,'Nuls ','NULS','/token/images/nuls28.png','0xb91318f35bdb262e9423bc7c7c2a3a93dd93c92c','NULS is a global blockchain open-source project which is a highly customizable modular blockchain infrastructure consisting of a microkernel and functional modules.','$3.1572','5.86%','$17,606,900','$126,287,600','2018-04-24 14:50:44'),(11,61,'Quantstamp ','QSP','/token/images/quantstamp28.png','0x99ea4db9ee77acd40b119bd1dc4e33e1c070b80d','Quantstamp u2013 the Protocol for Securing Smart Contracts. We believe in the future of smart contracts and are building a foundational technology to protect users and investors u2013 with scalable proofs-of-audit.','$0.2039','1.95%','$10,970,000','$125,844,432','2018-04-24 14:50:44'),(12,62,'Gifto ','GTO','/token/images/gifto28.png','0xc5bbae50781be1669306b9e001eff57a2957b09d','Decentralized Universal Gifting Protocol.','$0.3650','9.73%','$13,284,600','$123,540,447','2018-04-24 14:50:44'),(13,63,'Polymath ','POLY','/token/images/polymath_28.png','0x9992ec3cf6a55b00978cddf2b27bc6882d88d1ec','Polymath aims to enable securities to migrate to the blockchain.','$0.5125','-1.71%','$3,820,990','$123,007,552','2018-04-24 14:50:44'),(14,64,'Gnosis ','GNO','/token/images/gnosis.png','0x6810e776880c02933d47db1b9fc05908e5386b96','Crowd Sourced Wisdom - The next generation blockchain network. Speculate on anything with an easy-to-use prediction market','$110.2690','2.74%','$942,168','$121,802,035','2018-04-24 14:50:44'),(15,65,'RLC ','RLC','/token/images/iexec_28.png','0x607F4C5BB672230e8672085532f7e901544a7375','Blockchain Based distributed cloud computing','$1.5098','-0.02%','$2,654,350','$120,893,286','2018-04-24 14:50:44'),(16,66,'SingularityNET ','AGI','/token/images/singularitynet_28.png','0x8eb24319393716668d768dcec29356ae9cffe285','Decentralized Marketplace for AI.','$0.2218','0.54%','$597,960','$119,681,720','2018-04-24 14:50:44'),(17,67,'Metal ','MTL','/token/images/metalpay_28.png','0xF433089366899D83a9f26A773D59ec7eCF30355e','Transfer money instantly around the globe with nothing more than a phone number. Earn rewards every time you spend or make a purchase. Ditch the bank and go digital.','$4.8573','3.13%','$19,377,200','$117,607,462','2018-04-24 14:50:44'),(18,68,'ArcBlock ','ABT','/token/images/arcblock_28.png','0xb98d4c97425d9908e66e53a6fdf673acca0be986','An open source protocol that provides an abstract layer for accessing underlying blockchains, enabling your application to work on different blockchains.','$1.2367','4.62%','$53,464,900','$115,115,734','2018-04-24 14:50:44'),(19,69,'EnjinCoin ','ENJ','/token/images/enjincoin_28.jpg','0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c','Customizable cryptocurrency and virtual goods platform for gaming.','$0.1521','6.79%','$13,008,800','$115,039,570','2018-04-24 14:50:44'),(20,70,'Aragon ','ANT','/token/images/aragon_28.png','0x960b236A07cf122663c4303350609A66A7B288C0','Create and manage unstoppable organizations. Aragon lets you manage entire organizations using the blockchain. This makes Aragon organizations more efficient than their traditional counterparties.','$4.3207','5.40%','$1,169,970','$113,934,706','2018-04-24 14:50:44'),(21,71,'PayPie ','PPP','/token/images/paypie_28.png','0xc42209aCcC14029c1012fB5680D95fBd6036E2a0','PayPie platform brings ultimate trust and transparency to the financial markets by introducing the worldu2019s first risk score algorithm based on business accounting.','$1.3714','9.63%','$116,144','$113,136,375','2018-04-24 14:50:44'),(22,72,'HPBCoin ','HPB','/token/images/hpbcoin_28.png','0x38c6a68304cdefb9bec48bbfaaba5c5b47818bb2','HPB (High-Performance Blockchain) is a new kind of block chain hardware and software architecture, which includes a chip acceleration engine and the blockchain platform, aiming to realize the performance extension of distributed applications','$3.7557','2.45%','$8,306,690','$111,554,472','2018-04-24 14:50:44'),(23,73,'Raiden ','RDN','/token/images/raiden28.png','0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6','The Raiden Network is an off-chain scaling solution, enabling near-instant, low-fee and scalable payments. Itu2019s complementary to the Ethereum blockchain and works with any ERC20 compatible token.','$2.1679','2.71%','$8,676,840','$108,762,741','2018-04-24 14:50:44'),(24,74,'CyberMiles ','CMT','/token/images/5miles_28.png','0xf85feea2fdd81d51177f6b8f35f0e6734ce45f5f','Empowering the Decentralization of Online Marketplaces.','$0.1704','12.57%','$45,271,400','$107,981,419','2018-04-24 14:50:44'),(25,75,'Genaro X ','GNX','/token/images/genaroX_28.png','0x6ec8a24cabdc339a06a172f8223ea557055adaa5','Blockchain 3.0 Ecosystem Built on a Turing-Complete Public Chain with Decentralized Storage.','$0.4297','-2.69%','$5,314,820','$103,201,479','2018-04-24 14:50:44'),(26,76,'CUBE ','AUTO','/token/images/cube_28.png','0x622dFfCc4e83C64ba959530A5a5580687a57581b','CUBE is an autonomous car security platform backed by blockchain technology.','$0.0160','-2.72%','$8,787,020','$100,480,614','2018-04-24 14:50:44'),(27,77,'Bluzelle ','BLZ','/token/images/bluzelle28.png','0x5732046a883704404f284ce41ffadd5b007fd668','Aims to be the next-gen database protocol for the decentralized internet.','$0.6029','9.95%','$7,478,790','$99,485,265','2018-04-24 14:50:44'),(28,78,'SPHTX ','SPHTX','/token/images/sophiatx_28.png','0x3833dda0aeb6947b98ce454d89366cba8cc55528','Integrating Blockchain with Enterprise Applications.','$0.5150','8.07%','$1,740,110','$98,847,472','2018-04-24 14:50:44'),(29,79,'CREDITS ','CS','/token/images/credits2_28.png','0x46b9ad944d1059450da1163511069c718f699d31','CREDITS is an open blockchain platform with autonomous smart contracts and the internal cryptocurrency. The platform is designed to create services for blockchain systems using self-executing smart contracts and a public data registry.','$0.7140','16.28%','$5,897,090','$98,141,509','2018-04-24 14:50:44'),(30,80,'Amber ','AMB','/token/images/ambrosus_28.png','0x4dc3643dbc642b72c158e7f3d2ff232df61cb6ce','Combining high-tech sensors, blockchain protocol and smart contracts, we are building a universally verifiable, community-driven ecosystem to assure the quality, safety & origins of products.','$0.6636','24.68%','$22,536,400','$95,956,933','2018-04-24 14:50:44'),(31,81,'BLOCKv ','VEE','/token/images/blockv_28.png','0x340d2bde5eb28c1eed91b2f790723e3b160613b7','Create and Public Digital virtual goods on the blockchain','$0.0624','15.39%','$8,146,250','$95,574,647','2018-04-24 14:50:44'),(32,82,'SIRIN ','SRN','/token/images/sirin_28.png','0x68d57c9a1c35f63e2c83ee8e49a64e9d70528d25','SIRIN LABSu2019 aims to become the worldu2019s leader in secure open source consumer electronics, bridging the gap between the mass market and the blockchain econom','$0.4137','7.34%','$24,648,500','$94,842,900','2018-04-24 14:50:44'),(33,83,'Theta Token ','THETA','/token/images/theta_28.png','0x3883f5e181fccaf8410fa61e12b59bad963fb645','A decentralized peer-to-peer network that aims to offer improved video delivery at lower costs.','$0.1545','1.90%','$12,956,200','$94,749,143','2018-04-24 14:50:44'),(34,84,'RUFF ','RUFF','/token/images/ruffchain_28.png','0xf278c1ca969095ffddded020290cf8b5c424ace2','Decentralized open source blockchain architecture for high efficiency Internet of Things application development','$0.1057','3.71%','$11,413,400','$92,188,491','2018-04-24 14:50:44'),(35,85,'AirSwap ','AST','/token/images/airswap_28.png','0x27054b13b1b798b345b591a4d22e6562d47ea75a','AirSwap is based on the Swap protocol, a peer-to-peer protocol for trading Ethereum tokens','$0.6048','19.07%','$12,521,000','$90,718,200','2018-04-24 14:50:44'),(36,86,'Genesis Vision ','GVT','/token/images/genesisvision_28.png','0x103c3A209da59d3E7C4A89307e66521e081CFDF0','A platform for the private trust management market, built on Blockchain technology and Smart Contracts.','$23.7801','3.05%','$12,178,100','$88,623,222','2018-04-24 14:50:44'),(37,87,'EthLend ','LEND','/token/images/ethlend_28.png','0x80fB784B7eD66730e8b1DBd9820aFD29931aab03','Decentralized and secure financial marketplace for peer to peer lending agreements using Blockchain and Smart Contracts.','$0.0792','2.64%','$3,882,610','$86,078,689','2018-04-24 14:50:44'),(38,88,'PILLAR ','PLR','/token/images/pillar-wallet_28.png','0xe3818504c1b32bf1557b16c238b2e01fd3149c17','Building the a cryptocurrency and token wallet that aims to become the dashboard for your digital life.','$0.3607','11.65%','$104,341','$82,025,428','2018-04-24 14:50:44'),(39,89,'DATAcoin ','DATA','/token/images/streamr_28.png','0x0cf0ee63788a0849fe5297f3407f701e122cc023','Streamr tokenizes streaming data to enable a new way for machines & people to trade it on a decentralised P2P network.','$0.1174','12.56%','$961,426','$79,494,554','2018-04-24 14:50:44'),(40,90,'Simple Token ','ST','/token/images/simpletoken_28.png','0x2c4e8f2d746113d0696ce89b35f0d8bf88e0aeca','OST KIT gives you all the tools you need to run your blockchain-powered economy on open scalable sidechains.','$0.2582','2.56%','$5,190,930','$78,958,265','2018-04-24 14:50:44'),(41,91,'SONM ','SNM','/token/images/sonm_28.png','0x983f6d60db79ea8ca4eb9968c6aff8cfa04b3c63','SONM\'s aims to be a secure and cost-effective fog supercomputer for general-purpose computing, from mobile app hosting to video rendering to DNA analysis.','$0.2175','5.58%','$1,766,720','$78,204,010','2018-04-24 14:50:44'),(42,92,'BIX Token ','BIX','/token/images/bix_28.png','0xb3104b4b9da82025e8b9f8fb28b3553ce2f67069','AI Enhanced Encrypted Digital Asset Exchange.','$0.7357','11.84%','$37,429,700','$76,766,109','2018-04-24 14:50:44'),(43,93,'IOT Chain ','ITC','/token/images/iotchain28.png','0x5e6b6d9abad9093fdc861ea1600eba1b355cd940','IoT Chain aims to be a A High Security Lite IoT OS','$1.5698','-0.68%','$13,475,300','$76,296,597','2018-04-24 14:50:44'),(44,94,'Crypterium ','CRPT','/token/images/crypterium_28_2.png','0x80a7e048f37a50500351c204cb407766fa3bae7f','Cryptobank for Cryptopeople.','$0.9531','0.61%','$563,447','$74,820,929','2018-04-24 14:50:44'),(45,95,'AdEx ','ADX','/token/images/adex_28.png','0x4470BB87d77b963A013DB939BE332f927f2b992e','Decentralized Ad Network','$1.0149','-2.61%','$12,783,000','$74,524,084','2018-04-24 14:50:44'),(46,96,'RipioCreditNetwork ','RCN','/token/images/ripio_28.png','0xf970b8e36e23f7fc3fd752eea86f8be8d83375a6','Ripio Credit Network is a global credit network based on cosigned smart contracts and blockchain technology that connects lenders and borrowers located anywhere in the world and on any currency','$0.1510','2.97%','$13,496,500','$73,919,489','2018-04-24 14:50:44'),(47,97,'Telcoin ','TEL','/token/images/telcoin_28.png','0x85e076361cc813a908ff672f9bad1541474402b2','A cryptocurrency distributed by your mobile operator and accepted everywhere.','$0.0025','-2.36%','$1,080,480','$71,876,247','2018-04-24 14:50:44'),(48,98,'Eidoo ','EDO','/token/images/eidoo_28.png','0xced4e93198734ddaff8492d525bd258d49eb388e','Aims to be a Fast, easy, and not only a Multicurrency Wallet and Hybrid Exchange.','$2.3896','4.64%','$9,977,860','$69,924,358','2018-04-24 14:50:44'),(49,99,'Crypto20 ','C20','/token/images/crypto20_28.png','0x26e75307fc0c021472feb8f727839531f112f317','Tokenized Crypto Index Fund.','$1.7457','7.13%','$1,613,160','$69,177,416','2018-04-24 14:50:44'),(50,100,'Internet Node Token ','INT','/token/images/intchain_28.png','0x0b76544f6c413a555f309bf76260d1e02377c02a','IOT applications','$0.4595','16.14%','$30,000,200','$68,923,950','2018-04-24 14:50:44');
/*!40000 ALTER TABLE `tokens` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-24 18:42:41
