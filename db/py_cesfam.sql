-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 17-01-2026 a las 17:02:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `py_cesfam`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas_medicas`
--

CREATE TABLE `citas_medicas` (
  `id` int(11) NOT NULL,
  `id_medico` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `fecha_hora` datetime NOT NULL,
  `estado_cita` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_cita`
--

CREATE TABLE `detalle_cita` (
  `id` int(11) NOT NULL,
  `id_cita` int(11) NOT NULL,
  `motivo_cita` varchar(100) NOT NULL,
  `observaciones` varchar(100) DEFAULT NULL,
  `indicaciones` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagnostico`
--

CREATE TABLE `diagnostico` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `diagnostico`
--

INSERT INTO `diagnostico` (`id`, `nombre`) VALUES
(1, 'Hipertensión Arterial'),
(2, 'Diabetes Mellitus Tipo 2'),
(3, 'Infección Respiratoria Aguda (Resfrío)'),
(4, 'Lumbago Mecánico'),
(5, 'Depresión Leve'),
(6, 'Hipotiroidismo'),
(7, 'Asma Bronquial'),
(8, 'Gastroenteritis Aguda'),
(9, 'Otitis Media'),
(10, 'Obesidad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagnosticos_atencion`
--

CREATE TABLE `diagnosticos_atencion` (
  `id` int(11) NOT NULL,
  `detalle_cita_id` int(11) NOT NULL,
  `diagnostico_id` int(11) NOT NULL,
  `tipo_diagnostico` int(11) NOT NULL,
  `observaciones` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidad`
--

CREATE TABLE `especialidad` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `especialidad`
--

INSERT INTO `especialidad` (`id`, `nombre`) VALUES
(1, 'Medicina General'),
(2, 'Nutrición'),
(3, 'Pediatría'),
(4, 'Obstetricia'),
(5, 'Medicina Familiar'),
(6, 'Medicina Interna'),
(7, 'Psicología'),
(8, 'Kinesiología');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidad_usuario`
--

CREATE TABLE `especialidad_usuario` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `especialidad_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_cita`
--

CREATE TABLE `estado_cita` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estado_cita`
--

INSERT INTO `estado_cita` (`id`, `nombre`) VALUES
(1, 'Agendada'),
(2, 'Cancelada'),
(3, 'Finalizada'),
(4, 'No Se Presentó');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_entrega`
--

CREATE TABLE `estado_entrega` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estado_entrega`
--

INSERT INTO `estado_entrega` (`id`, `nombre`) VALUES
(1, 'Pendiente'),
(2, 'Entregada'),
(3, 'Rechazada'),
(4, 'Sin Stock'),
(5, 'Vencida');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_paciente`
--

CREATE TABLE `estado_paciente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estado_paciente`
--

INSERT INTO `estado_paciente` (`id`, `nombre`) VALUES
(1, 'Activo'),
(2, 'Inactivo'),
(3, 'Fallecido'),
(4, 'Trasladado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_usuario`
--

CREATE TABLE `estado_usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estado_usuario`
--

INSERT INTO `estado_usuario` (`id`, `nombre`) VALUES
(1, 'Habilitado'),
(2, 'Deshabilitado'),
(3, 'Bloqueado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `forma_farmaceutica`
--

CREATE TABLE `forma_farmaceutica` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `forma_farmaceutica`
--

INSERT INTO `forma_farmaceutica` (`id`, `nombre`) VALUES
(1, 'Comprimido'),
(2, 'Jarabe'),
(3, 'Inyección '),
(4, 'Crema');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicamento`
--

CREATE TABLE `medicamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(70) NOT NULL,
  `forma_farmaceutica` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `concentracion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medicamento`
--

INSERT INTO `medicamento` (`id`, `nombre`, `forma_farmaceutica`, `stock`, `concentracion`) VALUES
(1, 'Paracetamol', 1, 500, '500 mg'),
(2, 'Ibuprofeno', 1, 300, '400 mg'),
(3, 'Amoxicilina', 1, 150, '500 mg'),
(4, 'Losartán', 1, 600, '50 mg'),
(5, 'Metformina', 1, 450, '850 mg'),
(6, 'Diclofenaco Sódico', 3, 50, '75 mg/3ml'),
(7, 'Clorfenamina', 1, 200, '4 mg'),
(8, 'Omeprazol', 1, 350, '20 mg'),
(9, 'Betametasona', 4, 40, '0.05%'),
(10, 'Ketorolaco', 3, 60, '30 mg/ml'),
(11, 'Loratadina', 2, 80, '1 mg/ml'),
(12, 'Ácido Acetilsalicílico', 1, 250, '100 mg'),
(13, 'Enalapril', 1, 400, '10 mg'),
(14, 'Clotrimazol', 4, 75, '1%'),
(15, 'Penicilina Benzatina', 3, 30, '1.200.000 UI');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `id` int(11) NOT NULL,
  `rut` varchar(10) NOT NULL,
  `nombres` varchar(70) NOT NULL,
  `apellidos` varchar(70) NOT NULL,
  `direccion` varchar(90) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `fecha_nacimiento` date NOT NULL,
  `sexo_id` int(11) NOT NULL,
  `estado_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recetas`
--

CREATE TABLE `recetas` (
  `id` int(11) NOT NULL,
  `detalle_cita_id` int(11) NOT NULL,
  `medicamento_id` int(11) NOT NULL,
  `fecha_entrega` datetime NOT NULL,
  `cant_solicitada` int(11) NOT NULL,
  `duracion` varchar(60) NOT NULL,
  `frecuencia` varchar(40) NOT NULL,
  `dosis` varchar(60) NOT NULL,
  `estado_entrega` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `nombre`) VALUES
(1, 'Administrador'),
(2, 'Médico'),
(3, 'SOME'),
(4, 'Farmacéutico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sexo`
--

CREATE TABLE `sexo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `sexo`
--

INSERT INTO `sexo` (`id`, `nombre`) VALUES
(1, 'Masculino'),
(2, 'Femenino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_diagnostico`
--

CREATE TABLE `tipo_diagnostico` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_diagnostico`
--

INSERT INTO `tipo_diagnostico` (`id`, `nombre`) VALUES
(1, 'Sospecha'),
(2, 'Confirmado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `rut` varchar(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `rol_id` int(11) NOT NULL,
  `estado_id` int(11) NOT NULL,
  `intentos_fallidos` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `rut`, `nombre`, `apellido`, `password`, `rol_id`, `estado_id`) VALUES
(1, '1-9', 'Super', 'Administrador', '$2b$12$FaIprdIiPn42kM05ldvCDuXiYYpLq79gv.59m77Ge97tr8bSsYf/.', 1, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `citas_medicas`
--
ALTER TABLE `citas_medicas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_medico` (`id_medico`),
  ADD KEY `id_paciente` (`id_paciente`),
  ADD KEY `estado_cita` (`estado_cita`);

--
-- Indices de la tabla `detalle_cita`
--
ALTER TABLE `detalle_cita`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_cita` (`id_cita`);

--
-- Indices de la tabla `diagnostico`
--
ALTER TABLE `diagnostico`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `diagnosticos_atencion`
--
ALTER TABLE `diagnosticos_atencion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diagnostico_id` (`diagnostico_id`),
  ADD KEY `tipo_diagnostico` (`tipo_diagnostico`);

--
-- Indices de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `especialidad_usuario`
--
ALTER TABLE `especialidad_usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `especialidad_id` (`especialidad_id`);

--
-- Indices de la tabla `estado_cita`
--
ALTER TABLE `estado_cita`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estado_entrega`
--
ALTER TABLE `estado_entrega`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estado_paciente`
--
ALTER TABLE `estado_paciente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estado_usuario`
--
ALTER TABLE `estado_usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `forma_farmaceutica`
--
ALTER TABLE `forma_farmaceutica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `medicamento`
--
ALTER TABLE `medicamento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forma_farmaceutica` (`forma_farmaceutica`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rut` (`rut`),
  ADD KEY `sexo_id` (`sexo_id`),
  ADD KEY `estado_id` (`estado_id`);

--
-- Indices de la tabla `recetas`
--
ALTER TABLE `recetas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `detalle_cita_id` (`detalle_cita_id`),
  ADD KEY `medicamento_id` (`medicamento_id`),
  ADD KEY `estado_entrega` (`estado_entrega`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `sexo`
--
ALTER TABLE `sexo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_diagnostico`
--
ALTER TABLE `tipo_diagnostico`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rut` (`rut`),
  ADD KEY `rol_id` (`rol_id`),
  ADD KEY `estado_id` (`estado_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas_medicas`
--
ALTER TABLE `citas_medicas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_cita`
--
ALTER TABLE `detalle_cita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `diagnostico`
--
ALTER TABLE `diagnostico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `diagnosticos_atencion`
--
ALTER TABLE `diagnosticos_atencion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `especialidad_usuario`
--
ALTER TABLE `especialidad_usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estado_cita`
--
ALTER TABLE `estado_cita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `estado_entrega`
--
ALTER TABLE `estado_entrega`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `estado_paciente`
--
ALTER TABLE `estado_paciente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `estado_usuario`
--
ALTER TABLE `estado_usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `forma_farmaceutica`
--
ALTER TABLE `forma_farmaceutica`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `medicamento`
--
ALTER TABLE `medicamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `recetas`
--
ALTER TABLE `recetas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `sexo`
--
ALTER TABLE `sexo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_diagnostico`
--
ALTER TABLE `tipo_diagnostico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citas_medicas`
--
ALTER TABLE `citas_medicas`
  ADD CONSTRAINT `citas_medicas_ibfk_1` FOREIGN KEY (`id_medico`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `citas_medicas_ibfk_2` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`),
  ADD CONSTRAINT `citas_medicas_ibfk_3` FOREIGN KEY (`id_medico`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `citas_medicas_ibfk_4` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`),
  ADD CONSTRAINT `citas_medicas_ibfk_5` FOREIGN KEY (`estado_cita`) REFERENCES `estado_cita` (`id`);

--
-- Filtros para la tabla `detalle_cita`
--
ALTER TABLE `detalle_cita`
  ADD CONSTRAINT `detalle_cita_ibfk_1` FOREIGN KEY (`id_cita`) REFERENCES `citas_medicas` (`id`);

--
-- Filtros para la tabla `diagnosticos_atencion`
--
ALTER TABLE `diagnosticos_atencion`
  ADD CONSTRAINT `diagnosticos_atencion_ibfk_1` FOREIGN KEY (`diagnostico_id`) REFERENCES `diagnostico` (`id`),
  ADD CONSTRAINT `diagnosticos_atencion_ibfk_2` FOREIGN KEY (`tipo_diagnostico`) REFERENCES `tipo_diagnostico` (`id`);

--
-- Filtros para la tabla `especialidad_usuario`
--
ALTER TABLE `especialidad_usuario`
  ADD CONSTRAINT `especialidad_usuario_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `especialidad_usuario_ibfk_2` FOREIGN KEY (`especialidad_id`) REFERENCES `especialidad` (`id`);

--
-- Filtros para la tabla `medicamento`
--
ALTER TABLE `medicamento`
  ADD CONSTRAINT `medicamento_ibfk_1` FOREIGN KEY (`forma_farmaceutica`) REFERENCES `forma_farmaceutica` (`id`);

--
-- Filtros para la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`sexo_id`) REFERENCES `sexo` (`id`),
  ADD CONSTRAINT `pacientes_ibfk_2` FOREIGN KEY (`estado_id`) REFERENCES `estado_paciente` (`id`);

--
-- Filtros para la tabla `recetas`
--
ALTER TABLE `recetas`
  ADD CONSTRAINT `recetas_ibfk_1` FOREIGN KEY (`detalle_cita_id`) REFERENCES `detalle_cita` (`id`),
  ADD CONSTRAINT `recetas_ibfk_2` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`),
  ADD CONSTRAINT `recetas_ibfk_3` FOREIGN KEY (`estado_entrega`) REFERENCES `estado_entrega` (`id`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`estado_id`) REFERENCES `estado_usuario` (`id`);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_citas_medico`
--

CREATE VIEW vista_citas_medico AS
SELECT 
    c.id,
    c.id_medico,
    CONCAT(u.nombre, ' ', u.apellido) AS nombre_medico,
    CONCAT(
        SUBSTRING_INDEX(p.nombres, ' ', 1), 
        IF(LOCATE(' ', p.nombres) > 0, CONCAT(' ', SUBSTRING(p.nombres, LOCATE(' ', p.nombres) + 1, 1), '.'), ''),
        ' ',
        SUBSTRING_INDEX(p.apellidos, ' ', 1),
        IF(LOCATE(' ', p.apellidos) > 0, CONCAT(' ', SUBSTRING(p.apellidos, LOCATE(' ', p.apellidos) + 1, 1), '.'), '')
    ) AS nombre_paciente,
    c.fecha_hora,
    e.nombre AS nombre_estado
FROM citas_medicas c
INNER JOIN usuarios u ON u.id = c.id_medico
INNER JOIN pacientes p ON p.id = c.id_paciente
INNER JOIN estado_cita e ON e.id = c.estado_cita;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
