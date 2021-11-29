-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_and_ninjas_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojos_and_ninjas_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_and_ninjas_schema` DEFAULT CHARACTER SET utf8 ;
USE `dojos_and_ninjas_schema` ;

-- -----------------------------------------------------
-- Table `dojos_and_ninjas_schema`.`Ninja`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_and_ninjas_schema`.`Ninja` (
  `id` INT GENERATED ALWAYS AS () VIRTUAL,
  `first_name` VARCHAR(64) NOT NULL,
  `last_name` VARCHAR(64) NOT NULL,
  `age` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_and_ninjas_schema`.`Dojo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_and_ninjas_schema`.`Dojo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `Ninja_id` INT NOT NULL,
  `Ninja_first_name` VARCHAR(64) NOT NULL,
  `Ninja_last_name` VARCHAR(64) NOT NULL,
  `Ninja_age` INT NOT NULL,
  `Ninja_created_at` DATETIME NOT NULL,
  `Ninja_updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`, `name`, `created_at`, `updated_at`),
  INDEX `fk_Dojo_Ninja_idx` (`Ninja_id` ASC, `Ninja_first_name` ASC, `Ninja_last_name` ASC, `Ninja_age` ASC, `Ninja_created_at` ASC, `Ninja_updated_at` ASC) VISIBLE,
  CONSTRAINT `fk_Dojo_Ninja`
    FOREIGN KEY (`Ninja_id` , `Ninja_first_name` , `Ninja_last_name` , `Ninja_age` , `Ninja_created_at` , `Ninja_updated_at`)
    REFERENCES `dojos_and_ninjas_schema`.`Ninja` (`id` , `first_name` , `last_name` , `age` , `created_at` , `updated_at`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
