-- MySQL dump 10.14  Distrib 5.5.57-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: subscription_manager
-- ------------------------------------------------------
-- Server version	5.5.57-MariaDB
DROP SCHEMA IF EXISTS `subscription_manager`;
CREATE SCHEMA `subscription_manager`;
USE `subscription_manager`;

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
-- Temporary table structure for view `ability_to_review`
--

DROP TABLE IF EXISTS `ability_to_review`;
/*!50001 DROP VIEW IF EXISTS `ability_to_review`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `ability_to_review` (
  `service_name` tinyint NOT NULL,
  `user_id` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `all_support_tickets`
--

DROP TABLE IF EXISTS `all_support_tickets`;
/*!50001 DROP VIEW IF EXISTS `all_support_tickets`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `all_support_tickets` (
  `question` tinyint NOT NULL,
  `user_id` tinyint NOT NULL,
  `user_name` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `bundle`
--

DROP TABLE IF EXISTS `bundle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bundle` (
  `bundle_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `discount` float unsigned DEFAULT NULL,
  PRIMARY KEY (`bundle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bundle`
--

LOCK TABLES `bundle` WRITE;
/*!40000 ALTER TABLE `bundle` DISABLE KEYS */;
INSERT INTO `bundle` VALUES (1,12),(2,10),(3,31),(4,50),(5,50),(6,15),(7,40);
/*!40000 ALTER TABLE `bundle` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `subscription_manager`.`Bundle_BEFORE_INSERT` BEFORE INSERT ON `Bundle` FOR EACH ROW
BEGIN
	IF(NEW.discount<0 OR NEW.discount>100) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid data';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `subscription_manager`.`Bundle_BEFORE_UPDATE` BEFORE UPDATE ON `Bundle` FOR EACH ROW
BEGIN
	IF(NEW.discount<0 OR NEW.discount>100) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid data';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `bundle_contains_subscription_plan`
--

DROP TABLE IF EXISTS `bundle_contains_subscription_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bundle_contains_subscription_plan` (
  `bundle_id` int(10) unsigned NOT NULL,
  `plan_id` int(11) NOT NULL,
  `service_name` varchar(45) NOT NULL,
  PRIMARY KEY (`bundle_id`,`plan_id`,`service_name`),
  KEY `fk_Bundle_has_Subscription_plan_Subscription_plan1_idx` (`plan_id`,`service_name`),
  KEY `fk_Bundle_has_Subscription_plan_Bundle1_idx` (`bundle_id`),
  CONSTRAINT `fk_Bundle_has_Subscription_plan_Bundle1` FOREIGN KEY (`bundle_id`) REFERENCES `bundle` (`bundle_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bundle_has_Subscription_plan_Subscription_plan1` FOREIGN KEY (`plan_id`) REFERENCES `subscription_plan` (`plan_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bundle_contains_subscription_plan`
--

LOCK TABLES `bundle_contains_subscription_plan` WRITE;
/*!40000 ALTER TABLE `bundle_contains_subscription_plan` DISABLE KEYS */;
INSERT INTO `bundle_contains_subscription_plan` VALUES (1,2,'Nietflix'),(1,2,'TubeTuve'),(2,1,'Sportifu'),(2,2,'Nietflix'),(3,2,'WhoKnows+'),(3,3,'Diney--'),(4,2,'WhoKnows+'),(4,3,'Nietflix'),(5,1,'TheSportPlace'),(5,2,'TubeTuve'),(5,3,'Nietflix'),(6,2,'TubeTuve'),(6,3,'Nietflix'),(7,1,'Sportifu'),(7,1,'TheSportPlace'),(7,2,'TubeTuve'),(7,3,'Diney--');
/*!40000 ALTER TABLE `bundle_contains_subscription_plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `bundle_price`
--

DROP TABLE IF EXISTS `bundle_price`;
/*!50001 DROP VIEW IF EXISTS `bundle_price`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `bundle_price` (
  `bundle_id` tinyint NOT NULL,
  `total_bundle_price` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `global_plans`
--

DROP TABLE IF EXISTS `global_plans`;
/*!50001 DROP VIEW IF EXISTS `global_plans`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `global_plans` (
  `service_name` tinyint NOT NULL,
  `plan_id` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `movie_services`
--

DROP TABLE IF EXISTS `movie_services`;
/*!50001 DROP VIEW IF EXISTS `movie_services`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `movie_services` (
  `service_name` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `payment_method`
--

DROP TABLE IF EXISTS `payment_method`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment_method` (
  `payment_method` enum('Credit Card','Debit Card','Paypal','Paysafe') NOT NULL,
  `user_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`payment_method`,`user_id`),
  KEY `fk_Payment_method_Wallet1_idx` (`user_id`),
  CONSTRAINT `fk_Payment_method_Wallet1` FOREIGN KEY (`user_id`) REFERENCES `wallet` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_method`
--

LOCK TABLES `payment_method` WRITE;
/*!40000 ALTER TABLE `payment_method` DISABLE KEYS */;
INSERT INTO `payment_method` VALUES ('Credit Card',1),('Credit Card',2),('Credit Card',4),('Credit Card',7),('Credit Card',8),('Credit Card',9),('Credit Card',10),('Credit Card',11),('Credit Card',13),('Credit Card',16),('Credit Card',18),('Credit Card',19),('Debit Card',1),('Debit Card',3),('Debit Card',5),('Debit Card',6),('Debit Card',8),('Debit Card',9),('Debit Card',11),('Debit Card',12),('Debit Card',14),('Debit Card',15),('Debit Card',16),('Debit Card',17);
/*!40000 ALTER TABLE `payment_method` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `plan_payment`
--

DROP TABLE IF EXISTS `plan_payment`;
/*!50001 DROP VIEW IF EXISTS `plan_payment`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `plan_payment` (
  `user_id` tinyint NOT NULL,
  `total_plan_price` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `subscription_plan`
--

DROP TABLE IF EXISTS `subscription_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_plan` (
  `plan_id` int(11) NOT NULL AUTO_INCREMENT,
  `plan_price` float unsigned NOT NULL DEFAULT '0',
  `region` varchar(25) NOT NULL DEFAULT 'GLOBAL',
  `plan_type` enum('Basic','Family','Premium','Student') NOT NULL DEFAULT 'Basic',
  `service_name` varchar(25) NOT NULL,
  PRIMARY KEY (`plan_id`,`service_name`),
  KEY `fk_Subscription_plan_Subscription_Service1_idx` (`service_name`),
  CONSTRAINT `fk_Subscription_plan_Subscription_Service1` FOREIGN KEY (`service_name`) REFERENCES `subscription_service` (`service_name`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_plan`
--

LOCK TABLES `subscription_plan` WRITE;
/*!40000 ALTER TABLE `subscription_plan` DISABLE KEYS */;
INSERT INTO `subscription_plan` VALUES (1,6,'USA Only','Basic','Akalapataca'),(1,5,'USA Only','Basic','Amazoon Premium'),(1,10,'Europe Only','Basic','Diney--'),(1,10,'Russia Only','Basic','Nietflix'),(1,5,'Global','Basic','Sportifu'),(1,2,'Greece Only','Basic','SySolin'),(1,6,'Global','Basic','TheSportPlace'),(1,5,'Greece Only','Basic','TubeTuve'),(1,5,'Global','Premium','Twitch Prime'),(1,7,'Global','Basic','WhoKnows+'),(2,5,'USA Only','Student','Diney--'),(2,7.5,'Global','Student','Nietflix'),(2,14,'Africa+Asia','Family','Sportifu'),(2,12,'USA Only','Basic','TheSportPlace'),(2,3,'Global','Student','TubeTuve'),(2,9,'Global','Premium','WhoKnows+'),(3,12,'Global','Family','Diney--'),(3,13,'Global','Family','Nietflix'),(3,4.5,'USA Only','Basic','TubeTuve');
/*!40000 ALTER TABLE `subscription_plan` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `subscription_manager`.`Subscription_plan_BEFORE_INSERT` BEFORE INSERT ON `Subscription_plan` FOR EACH ROW
BEGIN
	IF(NEW.plan_price<0) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid data';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `subscription_manager`.`Subscription_plan_BEFORE_UPDATE` BEFORE UPDATE ON `Subscription_plan` FOR EACH ROW
BEGIN
	IF(NEW.plan_price<0) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid data';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `subscription_service`
--

DROP TABLE IF EXISTS `subscription_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_service` (
  `service_name` varchar(25) NOT NULL,
  `service_type` enum('Movies','Music','Games','Streaming','Sports') DEFAULT NULL,
  PRIMARY KEY (`service_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_service`
--

LOCK TABLES `subscription_service` WRITE;
/*!40000 ALTER TABLE `subscription_service` DISABLE KEYS */;
INSERT INTO `subscription_service` VALUES ('Akalapataca','Music'),('Amazoon Premium','Movies'),('Diney--','Movies'),('Nietflix','Movies'),('Sportifu','Sports'),('SySolin','Music'),('TheSportPlace','Streaming'),('TubeTuve','Sports'),('Twitch Prime','Streaming'),('WhoKnows+','Streaming');
/*!40000 ALTER TABLE `subscription_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `support_ticket`
--

DROP TABLE IF EXISTS `support_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `support_ticket` (
  `ticket_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `answer` varchar(1000) DEFAULT NULL,
  `question` varchar(1000) NOT NULL,
  `user_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`ticket_id`,`user_id`),
  KEY `fk_Support_Ticket_User1_idx` (`user_id`),
  CONSTRAINT `fk_Support_Ticket_User1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `support_ticket`
--

LOCK TABLES `support_ticket` WRITE;
/*!40000 ALTER TABLE `support_ticket` DISABLE KEYS */;
INSERT INTO `support_ticket` VALUES (1,'Trying reseting your router. If the problem insists, contact us again.','I have lag problems. What can I do??',1),(1,'Check if your account balance has enough credits for the subscription you want.','Payment is not accepted. Why does this happen?',2),(1,'We didn\'t get your question, try again.','fujawdawd na',4),(1,'You have to communicate with the **** service for more information','I want to have a passcode for my **** account so my underage child cannot use it',6),(1,'You have been hacked, we are trying our best to retrieve your account.','I can\'t access my subscription plans',12),(1,'We sent you an email for a new password','I forgot my password',13),(1,'Thank you for telling us. We will fix it soon!','Your app has a bug and it doesn\'t show the money.',15),(2,'We have a local problem with the server. We are trying to fix it.','The lag problem is insisting.',1),(2,'Please don\'t answer by sending another support ticket','Ok thank you',6),(3,'Unfortunately, you can cancel your subscriptions only when they are due to finish. Please wait until the new month.','I still have lag problems. I want to cancel my subscriptions.',1);
/*!40000 ALTER TABLE `support_ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_name` varchar(25) NOT NULL,
  `birth_date` date NOT NULL,
  `age` int(11) AS (2020-YEAR(birth_date)) VIRTUAL,
  `email` varchar(45) NOT NULL,
  `country` varchar(25) NOT NULL,
  `zip_code` char(10) NOT NULL,
  `street` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Ioannis Papas','1998-01-01',22,'ioannipapas@ece.auth.gr','Greece','54666','Kolokotroni 10'),(2,'Athanasios Sioppidis','1998-02-01',22,'athasiop@ece.auth.gr','Greece','10000','Atlantidas 23'),(3,'Dimitrios Papargyriou','1998-03-01',22,'dpapargy@ece.auth.gr','Greece','53780','Agiou Epameinonda 20'),(4,'Dimitris Papadopoulos','1983-07-04',37,'dpap@gmail.com','Cyprus','67810','Kipselis 10'),(5,'Jack Blackman','1950-12-19',70,'blackjack21@hotmail.com','USA','91000','Broadway 23'),(6,'Sakis Rouvas','1974-08-12',46,'sakiiiiiii@yahoo.gr','Greece','12145','Kerkyras 12'),(7,'Nick Calathes','1990-01-13',30,'nickTheQuick@barcabc.gr','Spain','92188','Tripontou 14'),(8,'Tom Holland','1996-01-12',24,'tomHolland@gmail.com','England','43828','Kingston 32'),(9,'Zac Efron','1987-05-13',33,'efronzacary@yahoo.com','America','17489','Pensylvania'),(10,'Dwayne Johnson','1972-07-01',48,'therock@hotmail.com','America','72819','3rd California Str.'),(11,'Sherlock Holmes','1920-04-02',100,'holmesdet@gmail.com','England','28184','Baker Street 3B'),(12,'Tom Felton','1987-08-03',33,'feltonidis@gmail.com','America','83281',''),(13,'Leonardo DiCaprio','1974-06-03',46,'leodc@windowslive.com','Italy','47729','Piazza di Spagna'),(14,'Chris Hemsworth','1983-10-08',37,'theThor@gmail.com','Iceland','21748','Reykjavik 45'),(15,'Ariana Grande','1993-08-31',27,'ariana@yahoo.com','Canada','38290','Toronto 3rd street 172'),(16,'Billie Eilish','2001-12-18',19,'eilish2001@hotmail.com','Ameriaca','21893','Broadway 2'),(17,'Shawn Mendes','1998-03-19',22,'senoritacallme@gmail.com','Mexico','72813','Guadalajara 32'),(18,'Walter White','1970-04-21',50,'heisenberg@yahoo.com','America','28184','Albaquerque'),(19,'Bruno Mars','1984-02-29',36,'marsb@gmail.com','Brazil','28194','Sao Paulo 32');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `subscription_manager`.`User_BEFORE_INSERT` BEFORE INSERT ON `User` FOR EACH ROW
BEGIN
	IF(YEAR(NEW.birth_date)<1900 OR YEAR(NEW.birth_date)>2002) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid data';
    END IF;
    
    
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `subscription_manager`.`User_BEFORE_UPDATE` BEFORE UPDATE ON `User` FOR EACH ROW
BEGIN
	IF(YEAR(NEW.birth_date)<1900 OR YEAR(NEW.birth_date)>2002) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid data';
    END IF;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `user_buys_bundle`
--

DROP TABLE IF EXISTS `user_buys_bundle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_buys_bundle` (
  `user_id` int(10) unsigned NOT NULL,
  `bundle_id` int(10) unsigned NOT NULL,
  `bundle_purchase_date` datetime NOT NULL,
  PRIMARY KEY (`user_id`,`bundle_id`),
  KEY `fk_User_has_Bundle_Bundle1_idx` (`bundle_id`),
  KEY `fk_User_has_Bundle_User1_idx` (`user_id`),
  CONSTRAINT `fk_User_has_Bundle_Bundle1` FOREIGN KEY (`bundle_id`) REFERENCES `bundle` (`bundle_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Bundle_User1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_buys_bundle`
--

LOCK TABLES `user_buys_bundle` WRITE;
/*!40000 ALTER TABLE `user_buys_bundle` DISABLE KEYS */;
INSERT INTO `user_buys_bundle` VALUES (1,1,'2020-12-10 00:00:00'),(1,2,'2020-09-01 00:00:00'),(4,2,'2020-10-29 00:00:00'),(7,4,'2020-12-01 00:00:00'),(10,6,'2020-11-08 00:00:00');
/*!40000 ALTER TABLE `user_buys_bundle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_buys_subscription_plan`
--

DROP TABLE IF EXISTS `user_buys_subscription_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_buys_subscription_plan` (
  `user_id` int(10) unsigned NOT NULL,
  `plan_id` int(11) NOT NULL,
  `service_name` varchar(25) NOT NULL,
  `plan_purchase_date` datetime NOT NULL,
  PRIMARY KEY (`user_id`,`plan_id`,`service_name`),
  KEY `fk_User_has_Subscription_plan_Subscription_plan1_idx` (`plan_id`,`service_name`),
  KEY `fk_User_has_Subscription_plan_User_idx` (`user_id`),
  CONSTRAINT `fk_User_has_Subscription_plan_Subscription_plan1` FOREIGN KEY (`plan_id`) REFERENCES `subscription_plan` (`plan_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Subscription_plan_User` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_buys_subscription_plan`
--

LOCK TABLES `user_buys_subscription_plan` WRITE;
/*!40000 ALTER TABLE `user_buys_subscription_plan` DISABLE KEYS */;
INSERT INTO `user_buys_subscription_plan` VALUES (1,1,'Amazoon Premium','2020-12-16 00:00:00'),(1,1,'Sportifu','2020-12-15 00:00:00'),(1,1,'Sysolin','2020-12-13 00:00:00'),(1,2,'Nietflix','2020-12-14 00:00:00'),(2,2,'Nietflix','2020-12-12 00:00:00'),(3,2,'Sportifu','2020-12-11 00:00:00'),(5,3,'Nietflix','2020-12-10 00:00:00'),(6,1,'WhoKnows +','2020-11-29 00:00:00'),(7,2,'TubeTuve','2020-12-20 00:00:00'),(8,1,'Twitch Prime','2020-12-06 00:00:00'),(8,2,'Diney--','2020-11-23 00:00:00'),(10,2,'TheSportPlace','2020-12-02 00:00:00'),(11,3,'TubeTuve','2020-12-01 00:00:00'),(12,1,'Sysolin','2020-12-17 00:00:00'),(13,2,'Nietflix','2020-12-12 00:00:00'),(15,1,'Sportifu','2020-12-19 00:00:00'),(18,1,'Akalapataca','2020-12-14 00:00:00');
/*!40000 ALTER TABLE `user_buys_subscription_plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_reviews_service`
--

DROP TABLE IF EXISTS `user_reviews_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_reviews_service` (
  `service_name` varchar(25) NOT NULL,
  `user_id` int(10) unsigned NOT NULL,
  `comment` varchar(45) DEFAULT NULL,
  `rating` tinyint(1) unsigned NOT NULL,
  `review_date` datetime NOT NULL,
  PRIMARY KEY (`service_name`,`user_id`),
  KEY `fk_Subscription_Service_has_User_User1_idx` (`user_id`),
  KEY `fk_Subscription_Service_has_User_Subscription_Service1_idx` (`service_name`),
  CONSTRAINT `fk_Subscription_Service_has_User_Subscription_Service1` FOREIGN KEY (`service_name`) REFERENCES `subscription_service` (`service_name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Subscription_Service_has_User_User1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_reviews_service`
--

LOCK TABLES `user_reviews_service` WRITE;
/*!40000 ALTER TABLE `user_reviews_service` DISABLE KEYS */;
INSERT INTO `user_reviews_service` VALUES ('Amazoon Premium',1,'Can be better',6,'2005-03-02 00:00:00'),('Nietflix',1,'Very good',10,'2020-11-10 00:00:00'),('Nietflix',2,'Not many films',7,'2018-04-29 00:00:00'),('Sportifu',1,'Actually good',8,'2018-10-01 00:00:00'),('Sportifu',2,'Too expensive,sparse content',8,'2010-04-04 00:00:00'),('SySolin',1,'Didn\'t work for new Year\'s Eve',5,'2015-01-01 00:00:00');
/*!40000 ALTER TABLE `user_reviews_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wallet`
--

DROP TABLE IF EXISTS `wallet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wallet` (
  `money` float NOT NULL,
  `user_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `fk_Wallet_User1_idx` (`user_id`),
  CONSTRAINT `fk_Wallet_User1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wallet`
--

LOCK TABLES `wallet` WRITE;
/*!40000 ALTER TABLE `wallet` DISABLE KEYS */;
INSERT INTO `wallet` VALUES (10,1),(14,2),(0,3),(231,4),(34.5,5),(100.08,6),(23.4,7),(12,8),(0,9),(11.24,10),(140.38,11),(13,12),(12,13),(56,14),(43.56,15),(453.45,16),(67,17),(0.12,18),(0,19);
/*!40000 ALTER TABLE `wallet` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `subscription_manager`.`Wallet_BEFORE_INSERT` BEFORE INSERT ON `Wallet` FOR EACH ROW
BEGIN
	IF(NEW.money<0) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid data';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `subscription_manager`.`Wallet_BEFORE_UPDATE` BEFORE UPDATE ON `Wallet` FOR EACH ROW
BEGIN
	IF(NEW.money<0) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='invalid data';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `ability_to_review`
--

/*!50001 DROP TABLE IF EXISTS `ability_to_review`*/;
/*!50001 DROP VIEW IF EXISTS `ability_to_review`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ability_to_review` AS select `user_buys_subscription_plan`.`service_name` AS `service_name`,`user_buys_subscription_plan`.`user_id` AS `user_id` from `user_buys_subscription_plan` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `all_support_tickets`
--

/*!50001 DROP TABLE IF EXISTS `all_support_tickets`*/;
/*!50001 DROP VIEW IF EXISTS `all_support_tickets`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `all_support_tickets` AS select `support_ticket`.`question` AS `question`,`user`.`user_id` AS `user_id`,`user`.`user_name` AS `user_name` from (`user` join `support_ticket` on((`user`.`user_id` = `support_ticket`.`user_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `bundle_price`
--

/*!50001 DROP TABLE IF EXISTS `bundle_price`*/;
/*!50001 DROP VIEW IF EXISTS `bundle_price`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `bundle_price` AS select `bundle`.`bundle_id` AS `bundle_id`,(sum(`subscription_plan`.`plan_price`) * (1 - (`bundle`.`discount` / 100))) AS `total_bundle_price` from ((`bundle` join `bundle_contains_subscription_plan` on((`bundle`.`bundle_id` = `bundle_contains_subscription_plan`.`bundle_id`))) join `subscription_plan` on(((`bundle_contains_subscription_plan`.`plan_id` = `subscription_plan`.`plan_id`) and (`bundle_contains_subscription_plan`.`service_name` = `subscription_plan`.`service_name`)))) group by `bundle`.`bundle_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `global_plans`
--

/*!50001 DROP TABLE IF EXISTS `global_plans`*/;
/*!50001 DROP VIEW IF EXISTS `global_plans`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `global_plans` AS select `subscription_plan`.`service_name` AS `service_name`,`subscription_plan`.`plan_id` AS `plan_id` from `subscription_plan` where (`subscription_plan`.`region` = 'Global') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `movie_services`
--

/*!50001 DROP TABLE IF EXISTS `movie_services`*/;
/*!50001 DROP VIEW IF EXISTS `movie_services`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `movie_services` AS select `subscription_service`.`service_name` AS `service_name` from `subscription_service` where (`subscription_service`.`service_type` = 'Movies') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `plan_payment`
--

/*!50001 DROP TABLE IF EXISTS `plan_payment`*/;
/*!50001 DROP VIEW IF EXISTS `plan_payment`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `plan_payment` AS select `user_buys_subscription_plan`.`user_id` AS `user_id`,sum(`subscription_plan`.`plan_price`) AS `total_plan_price` from (`user_buys_subscription_plan` join `subscription_plan` on(((`user_buys_subscription_plan`.`plan_id` = `subscription_plan`.`plan_id`) and (`user_buys_subscription_plan`.`service_name` = `subscription_plan`.`service_name`)))) group by `user_buys_subscription_plan`.`user_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-19 22:25:06
