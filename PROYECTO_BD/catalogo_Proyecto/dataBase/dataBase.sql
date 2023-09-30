-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: fundacion
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrativosbd`
--

DROP TABLE IF EXISTS `administrativosbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrativosbd` (
  `Id_emp` int NOT NULL AUTO_INCREMENT,
  `Nombres_emp` varchar(20) NOT NULL,
  `Apellidos_emp` varchar(20) NOT NULL,
  `sexo_emp` varchar(1) NOT NULL,
  `telefono_emp` varchar(10) NOT NULL,
  `salario_emp` decimal(10,2) NOT NULL,
  `cargo_emp` varchar(40) NOT NULL,
  PRIMARY KEY (`Id_emp`),
  UNIQUE KEY `id_emp_UNIQUE` (`Id_emp`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrativosbd`
--

LOCK TABLES `administrativosbd` WRITE;
/*!40000 ALTER TABLE `administrativosbd` DISABLE KEYS */;
INSERT INTO `administrativosbd` VALUES (1,'CAMILO','VIEDMA','M','1234566',522222.00,'LIDER');
/*!40000 ALTER TABLE `administrativosbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comunidadesbd`
--

DROP TABLE IF EXISTS `comunidadesbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comunidadesbd` (
  `id_com` int NOT NULL AUTO_INCREMENT,
  `nombre_com` varchar(45) NOT NULL,
  `etnia_com` varchar(45) NOT NULL,
  `repre_com` int NOT NULL,
  PRIMARY KEY (`id_com`),
  UNIQUE KEY `id_com_UNIQUE` (`id_com`),
  UNIQUE KEY `repre_com_UNIQUE` (`repre_com`),
  CONSTRAINT `representanteid` FOREIGN KEY (`repre_com`) REFERENCES `representantesbd` (`id_Repre`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comunidadesbd`
--

LOCK TABLES `comunidadesbd` WRITE;
/*!40000 ALTER TABLE `comunidadesbd` DISABLE KEYS */;
INSERT INTO `comunidadesbd` VALUES (1,'UNIVALLE','EDU',1);
/*!40000 ALTER TABLE `comunidadesbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comunidadesbeneficiadasbd`
--

DROP TABLE IF EXISTS `comunidadesbeneficiadasbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comunidadesbeneficiadasbd` (
  `id_cb` int NOT NULL AUTO_INCREMENT,
  `comunidad_cb` int NOT NULL,
  `proyecto_cb` int NOT NULL,
  PRIMARY KEY (`id_cb`),
  UNIQUE KEY `id_cb_UNIQUE` (`id_cb`),
  KEY `comunidadcosa_idx` (`comunidad_cb`),
  KEY `proyectocosa_idx` (`proyecto_cb`),
  CONSTRAINT `comunidad12` FOREIGN KEY (`comunidad_cb`) REFERENCES `comunidadesbd` (`id_com`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `proyecto12` FOREIGN KEY (`proyecto_cb`) REFERENCES `proyectosbd` (`ID_Proy`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comunidadesbeneficiadasbd`
--

LOCK TABLES `comunidadesbeneficiadasbd` WRITE;
/*!40000 ALTER TABLE `comunidadesbeneficiadasbd` DISABLE KEYS */;
INSERT INTO `comunidadesbeneficiadasbd` VALUES (1,1,1);
/*!40000 ALTER TABLE `comunidadesbeneficiadasbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `niñosbd`
--

DROP TABLE IF EXISTS `niñosbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `niñosbd` (
  `ID_nin` int NOT NULL AUTO_INCREMENT,
  `nombre_nin` varchar(20) NOT NULL,
  `apellidos_nin` varchar(20) NOT NULL,
  `edad_nin` int NOT NULL,
  `genero_nin` varchar(1) NOT NULL,
  `com_nin` int NOT NULL,
  PRIMARY KEY (`ID_nin`),
  UNIQUE KEY `id_nin_UNIQUE` (`ID_nin`),
  KEY `id_com_idx` (`com_nin`),
  CONSTRAINT `id_com` FOREIGN KEY (`com_nin`) REFERENCES `comunidadesbd` (`id_com`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `niñosbd_chk_1` CHECK ((`edad_nin` between 0 and 18))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `niñosbd`
--

LOCK TABLES `niñosbd` WRITE;
/*!40000 ALTER TABLE `niñosbd` DISABLE KEYS */;
INSERT INTO `niñosbd` VALUES (1,'MILENA','MESA',2,'F',1);
/*!40000 ALTER TABLE `niñosbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objetivosbd`
--

DROP TABLE IF EXISTS `objetivosbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `objetivosbd` (
  `id_obj` int NOT NULL AUTO_INCREMENT,
  `descripcion_obj` varchar(45) NOT NULL,
  `tipo_obj` varchar(45) NOT NULL,
  PRIMARY KEY (`id_obj`),
  UNIQUE KEY `id_obj_UNIQUE` (`id_obj`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objetivosbd`
--

LOCK TABLES `objetivosbd` WRITE;
/*!40000 ALTER TABLE `objetivosbd` DISABLE KEYS */;
INSERT INTO `objetivosbd` VALUES (1,'GANAR','EL AÑO');
/*!40000 ALTER TABLE `objetivosbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objetivosproyectosbd`
--

DROP TABLE IF EXISTS `objetivosproyectosbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `objetivosproyectosbd` (
  `id_po` int NOT NULL AUTO_INCREMENT,
  `proyecto_po` int NOT NULL,
  `objetivo_po` int NOT NULL,
  `cumplimiento_po` int NOT NULL,
  PRIMARY KEY (`id_po`),
  UNIQUE KEY `id_po_UNIQUE` (`id_po`),
  KEY `proyectopo_idx` (`proyecto_po`),
  KEY `objetivospo_idx` (`objetivo_po`),
  CONSTRAINT `objetivospo` FOREIGN KEY (`objetivo_po`) REFERENCES `objetivosbd` (`id_obj`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `proyectopo` FOREIGN KEY (`proyecto_po`) REFERENCES `proyectosbd` (`ID_Proy`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `objetivosproyectosbd_chk_1` CHECK ((`cumplimiento_po` between 0 and 100))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objetivosproyectosbd`
--

LOCK TABLES `objetivosproyectosbd` WRITE;
/*!40000 ALTER TABLE `objetivosproyectosbd` DISABLE KEYS */;
INSERT INTO `objetivosproyectosbd` VALUES (1,1,1,100);
/*!40000 ALTER TABLE `objetivosproyectosbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `participantesproyectobd`
--

DROP TABLE IF EXISTS `participantesproyectobd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `participantesproyectobd` (
  `id_ppro` int NOT NULL AUTO_INCREMENT,
  `rol_ppro` varchar(45) NOT NULL,
  `tarea_ppro` varchar(45) NOT NULL,
  `tiempo_ppro` datetime NOT NULL,
  `pro_ppro` int NOT NULL,
  `proy_ppro` int NOT NULL,
  PRIMARY KEY (`id_ppro`),
  UNIQUE KEY `id_ppro_UNIQUE` (`id_ppro`),
  KEY `profesional_idx` (`pro_ppro`),
  KEY `proyecto_idx` (`proy_ppro`),
  CONSTRAINT `profesional` FOREIGN KEY (`pro_ppro`) REFERENCES `profesionalesbd` (`Id_emp`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `proyecto` FOREIGN KEY (`proy_ppro`) REFERENCES `proyectosbd` (`ID_Proy`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participantesproyectobd`
--

LOCK TABLES `participantesproyectobd` WRITE;
/*!40000 ALTER TABLE `participantesproyectobd` DISABLE KEYS */;
INSERT INTO `participantesproyectobd` VALUES (1,'ESTUDIAR','RESOLVER ECUACIONES','2023-08-04 00:00:00',1,1);
/*!40000 ALTER TABLE `participantesproyectobd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesionalesbd`
--

DROP TABLE IF EXISTS `profesionalesbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesionalesbd` (
  `Id_emp` int NOT NULL AUTO_INCREMENT,
  `Nombres_emp` varchar(20) NOT NULL,
  `Apellidos_emp` varchar(20) NOT NULL,
  `sexo_emp` varchar(1) NOT NULL,
  `telefono_emp` varchar(10) NOT NULL,
  `salario_emp` decimal(10,2) NOT NULL,
  `especia_emp` varchar(40) NOT NULL,
  PRIMARY KEY (`Id_emp`),
  UNIQUE KEY `id_emp_UNIQUE` (`Id_emp`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesionalesbd`
--

LOCK TABLES `profesionalesbd` WRITE;
/*!40000 ALTER TABLE `profesionalesbd` DISABLE KEYS */;
INSERT INTO `profesionalesbd` VALUES (1,'MARIA ','LEMUS','F','123456',2000000.00,'MATEMATICA');
/*!40000 ALTER TABLE `profesionalesbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectosbd`
--

DROP TABLE IF EXISTS `proyectosbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectosbd` (
  `ID_Proy` int NOT NULL AUTO_INCREMENT,
  `Titulo_proy` varchar(50) NOT NULL,
  `Descripcion_proy` varchar(100) NOT NULL,
  `Tema_proy` varchar(100) NOT NULL,
  `Alcance_proy` varchar(50) NOT NULL,
  `Presupuesto_proy` decimal(10,2) NOT NULL,
  `FechaInicio` date NOT NULL,
  `FechaFin` date NOT NULL,
  `Responsable_proy` int NOT NULL,
  PRIMARY KEY (`ID_Proy`),
  UNIQUE KEY `id_proy_UNIQUE` (`ID_Proy`),
  KEY `id_emp_idx` (`Responsable_proy`),
  CONSTRAINT `id_emp` FOREIGN KEY (`Responsable_proy`) REFERENCES `administrativosbd` (`Id_emp`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectosbd`
--

LOCK TABLES `proyectosbd` WRITE;
/*!40000 ALTER TABLE `proyectosbd` DISABLE KEYS */;
INSERT INTO `proyectosbd` VALUES (1,'MI ','ALMA','SE VA','DEL CUERPO',120000.00,'2022-05-08','2023-08-04',1);
/*!40000 ALTER TABLE `proyectosbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `representantesbd`
--

DROP TABLE IF EXISTS `representantesbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `representantesbd` (
  `id_Repre` int NOT NULL AUTO_INCREMENT,
  `nombres_repre` varchar(15) NOT NULL,
  `apellidos_repre` varchar(15) NOT NULL,
  `tel_repre` varchar(10) NOT NULL,
  `sexo_Repre` varchar(1) NOT NULL,
  `dir_ciudad_repre` varchar(15) NOT NULL,
  `dir_barrio_repre` varchar(15) NOT NULL,
  `dir_casa_Repre` varchar(15) NOT NULL,
  `dir_calle_repre` varchar(10) NOT NULL,
  PRIMARY KEY (`id_Repre`),
  UNIQUE KEY `id_Repre_UNIQUE` (`id_Repre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `representantesbd`
--

LOCK TABLES `representantesbd` WRITE;
/*!40000 ALTER TABLE `representantesbd` DISABLE KEYS */;
INSERT INTO `representantesbd` VALUES (1,'JANDI','RAMIREZ','3173575120','F','TULUA','SANTA TERESA','12','56');
/*!40000 ALTER TABLE `representantesbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vista1`
--

DROP TABLE IF EXISTS `vista1`;
/*!50001 DROP VIEW IF EXISTS `vista1`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vista1` AS SELECT 
 1 AS `ID_PROY`,
 1 AS `TITULO_PROY`,
 1 AS `AVG(OP.CUMPLIMIENTO_PO)`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vista2`
--

DROP TABLE IF EXISTS `vista2`;
/*!50001 DROP VIEW IF EXISTS `vista2`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vista2` AS SELECT 
 1 AS `ID_COM`,
 1 AS `NOMBRE_COM`,
 1 AS `COUNT(N.ID_NIN)`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vista1`
--

/*!50001 DROP VIEW IF EXISTS `vista1`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista1` AS select `p`.`ID_Proy` AS `ID_PROY`,`p`.`Titulo_proy` AS `TITULO_PROY`,avg(`op`.`cumplimiento_po`) AS `AVG(OP.CUMPLIMIENTO_PO)` from ((`proyectosbd` `p` join `objetivosproyectosbd` `op` on((`p`.`ID_Proy` = `op`.`proyecto_po`))) join `objetivosbd` `o` on((`op`.`objetivo_po` = `o`.`id_obj`))) group by `p`.`ID_Proy` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vista2`
--

/*!50001 DROP VIEW IF EXISTS `vista2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista2` AS select `c`.`id_com` AS `ID_COM`,`c`.`nombre_com` AS `NOMBRE_COM`,count(`n`.`ID_nin`) AS `COUNT(N.ID_NIN)` from (`comunidadesbd` `c` join `niñosbd` `n` on((`c`.`id_com` = `n`.`com_nin`))) group by `c`.`id_com` */;
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

-- Dump completed on 2023-07-10 20:08:27
