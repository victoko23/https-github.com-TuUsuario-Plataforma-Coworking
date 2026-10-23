-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS coworking_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Crear el usuario (usamos 'root' sin contraseña porque es la configuración por defecto de WampServer)
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY '';

-- 3. Asignar todos los permisos al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON coworking_db.* TO 'root'@'localhost';

-- 4. Aplicar los cambios de privilegios
FLUSH PRIVILEGES;