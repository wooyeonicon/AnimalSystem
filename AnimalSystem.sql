/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 8.0.17 : Database - animalsystem
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`animalsystem` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `animalsystem`;

/*Table structure for table `features` */

DROP TABLE IF EXISTS `features`;

CREATE TABLE `features` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feature` varchar(50) DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

/*Data for the table `features` */

insert  into `features`(`id`,`feature`) values (1,'有毛'),(2,'产奶'),(3,'有羽毛'),(4,'会飞'),(5,'会下蛋'),(6,'吃肉'),(7,'有犬齿'),(8,'有爪子'),(9,'眼睛盯前面'),(10,'有蹄'),(11,'反刍'),(12,'黄褐色'),(13,'有斑点'),(14,'有黑色条纹'),(15,'长脖'),(16,'长腿'),(17,'不会飞'),(18,'会游泳'),(19,'黑白两色'),(20,'善飞'),(21,'哺乳类'),(22,'鸟类'),(23,'肉食类'),(24,'蹄类'),(25,'企鹅'),(26,'海燕'),(27,'鸵鸟'),(28,'斑马'),(29,'长颈鹿'),(30,'虎'),(31,'金钱豹'),(32,'大象'),(33,'狮子'),(34,'黑豹'),(35,'猫咪'),(36,'小狗');

/*Table structure for table `relu` */

DROP TABLE IF EXISTS `relu`;

CREATE TABLE `relu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `f1` int(11) DEFAULT NULL,
  `f2` int(11) DEFAULT NULL,
  `f3` int(11) DEFAULT NULL,
  `f4` int(11) DEFAULT NULL,
  `console` int(11) DEFAULT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `relu` */

insert  into `relu`(`id`,`f1`,`f2`,`f3`,`f4`,`console`) values (1,1,0,0,0,21),(2,21,9,0,0,24),(3,23,12,13,0,31),(4,4,5,0,0,22),(5,7,8,9,0,23),(6,24,15,16,13,29),(7,22,15,16,17,27),(8,21,10,0,0,24),(9,23,12,14,0,30),(10,22,18,19,17,25),(11,24,14,0,0,28),(12,22,20,0,0,26),(13,2,0,0,0,21),(14,3,0,0,0,22);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
