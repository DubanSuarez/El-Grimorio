-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-10-2026 a las 19:38:50
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
-- Base de datos: `sitio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autores`
--

CREATE TABLE `autores` (
  `Id` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `nacionalidad` varchar(255) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `fecha_fallecimiento` date DEFAULT NULL,
  `biografia` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `autores`
--

INSERT INTO `autores` (`Id`, `Nombre`, `nacionalidad`, `fecha_nacimiento`, `fecha_fallecimiento`, `biografia`) VALUES
(1, 'Jane Austen', 'Británica', '1775-12-16', '1817-07-18', 'Novelista inglesa reconocida por retratar la sociedad de su época con ironía y elegancia. Sus obras más famosas incluyen Orgullo y prejuicio, Emma y Sentido y sensibilidad.'),
(2, 'Gabriel García Márquez', 'Colombiana', '0000-00-00', '0000-00-00', 'Novelista, cuentista y periodista colombiano, ganador del Premio Nobel de Literatura en 1982.'),
(3, 'J. K. Rowling', 'Británica', '0000-00-00', NULL, 'Escritora británica, reconocida mundialmente por la saga de Harry Potter.'),
(4, 'Julio Verne', 'Francesa', '0000-00-00', '0000-00-00', 'Escritor francés considerado uno de los padres de la ciencia ficción.'),
(5, 'Stephen King', 'Estadounidense', '0000-00-00', NULL, 'Escritor estadounidense famoso por sus novelas de terror, suspenso y fantasía.'),
(6, 'Isabel Allende', 'Chilena', '0000-00-00', NULL, 'Escritora chilena reconocida por sus novelas de realismo mágico e historia.'),
(9, 'J. R. R. Tolkien', 'Británico', '1892-01-03', '1973-09-02', 'Escritor, filólogo y profesor universitario británico, considerado uno de los mayores autores de literatura fantástica. Es conocido por crear el legendario mundo de la Tierra Media y por obras como El Hobbit y El Señor de los Anillos.'),
(10, 'George R. R. Martin', 'Estadounidense', '1948-09-20', '0000-00-00', 'Escritor y guionista estadounidense, reconocido mundialmente por la saga Canción de hielo y fuego, que inspiró la exitosa serie Game of Thrones. Sus historias destacan por sus personajes complejos y giros inesperados.'),
(11, 'Brandon Sanderson', 'Estadounidense', '1975-12-19', '0000-00-00', 'Escritor estadounidense de fantasía y ciencia ficción. Es el creador del universo Cosmere, que reúne varias de sus novelas más exitosas, como Nacidos de la Bruma y El Archivo de las Tormentas.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `Id` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `Estado` tinyint(1) NOT NULL,
  `FechaRegistro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`Id`, `Nombre`, `Descripcion`, `Estado`, `FechaRegistro`) VALUES
(1, 'Fantasía', 'Obras ambientadas en mundos imaginarios donde la magia, criaturas míticas y aventuras extraordinarias forman parte de la historia.', 1, '2026-07-22 19:16:34'),
(2, 'Terror', 'Libros diseñados para provocar miedo, tensión o suspenso mediante elementos sobrenaturales, psicológicos o de horror.', 0, '2026-07-22 19:16:41'),
(3, 'Romance', 'Novelas centradas en las relaciones sentimentales, el amor y el desarrollo emocional de sus protagonistas.', 1, '2026-07-22 19:16:49'),
(4, 'Historia', 'Obras que narran acontecimientos históricos, biografías y sucesos relevantes de diferentes épocas y culturas.', 0, '2026-07-22 19:16:57'),
(5, 'Programación', 'Libros dedicados al aprendizaje de lenguajes de programación, desarrollo de software, algoritmos y tecnologías informáticas.', 0, '2026-07-22 19:17:03'),
(6, 'Ciencia', 'Obras relacionadas con las ciencias naturales, físicas, biológicas y tecnológicas, orientadas a la divulgación y el aprendizaje.', 1, '2026-07-22 19:17:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `editoriales`
--

CREATE TABLE `editoriales` (
  `Id` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Pais` varchar(255) NOT NULL,
  `Ciudad` varchar(255) NOT NULL,
  `SitioWeb` varchar(255) NOT NULL,
  `Estado` tinyint(1) NOT NULL,
  `FechaRegistro` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `editoriales`
--

INSERT INTO `editoriales` (`Id`, `Nombre`, `Pais`, `Ciudad`, `SitioWeb`, `Estado`, `FechaRegistro`) VALUES
(1, 'Planeta', 'España', 'Barcelona', 'http://planeta.es', 1, '0000-00-00'),
(2, 'Norma', 'Colombia', 'Bogotá', 'http://edicionesnorma.com', 1, '0000-00-00'),
(3, 'Penguin Random House', 'España', 'Barcelona', 'http://penguinrandomhousegrupoeditorial.com', 1, '0000-00-00'),
(4, 'Minotauro', 'España', 'Barcelona', 'http://planetadelibros.com', 1, '0000-00-00'),
(6, 'Anagrama', 'España', 'Barcelona', 'https://www.anagrama-ed.es', 1, '2026-07-22'),
(7, 'HarperCollins', 'Estados Unidos', 'Nueva York', 'https://www.harpercollins.com', 1, '2026-07-22'),
(8, 'Oxford University Press', 'Reino Unido', 'Oxford', 'https://global.oup.com', 1, '2026-07-22'),
(9, 'McGraw Hill', 'Estados Unidos', 'Columbus', 'https://www.mheducation.com', 1, '2026-07-22'),
(10, 'Pearson', 'Reino Unido', 'Londres', 'https://www.pearson.com', 1, '2026-07-22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idiomas`
--

CREATE TABLE `idiomas` (
  `Id` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `CodigoISO` varchar(255) NOT NULL,
  `Estado` tinyint(1) NOT NULL,
  `FechaRegistro` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `idiomas`
--

INSERT INTO `idiomas` (`Id`, `Nombre`, `CodigoISO`, `Estado`, `FechaRegistro`) VALUES
(1, 'Español', 'es', 1, '0000-00-00'),
(2, 'Inglés', 'en', 1, '0000-00-00'),
(3, 'Francés', 'fr', 1, '0000-00-00'),
(5, 'Alemán', 'de', 1, '2026-07-22'),
(6, 'Italiano', 'it', 1, '2026-07-22'),
(7, 'Portugués', 'pt', 1, '2026-07-22'),
(8, 'Japonés', 'ja', 1, '2026-07-22'),
(9, 'Chino (Mandarín)', 'zh', 1, '2026-07-22'),
(10, 'Coreano', 'cr', 0, '2026-08-19');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lectores`
--

CREATE TABLE `lectores` (
  `Id` int(11) NOT NULL,
  `TipoDocumento` varchar(20) NOT NULL,
  `NumeroDocumento` varchar(30) NOT NULL,
  `NombreCompleto` varchar(150) NOT NULL,
  `Telefono` varchar(20) DEFAULT NULL,
  `Correo` varchar(120) DEFAULT NULL,
  `Direccion` varchar(200) DEFAULT NULL,
  `TipoLector` enum('Estudiante','Docente','Administrativo','Externo') DEFAULT 'Externo',
  `Estado` enum('Activo','Inactivo') DEFAULT 'Activo',
  `FechaRegistro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `lectores`
--

INSERT INTO `lectores` (`Id`, `TipoDocumento`, `NumeroDocumento`, `NombreCompleto`, `Telefono`, `Correo`, `Direccion`, `TipoLector`, `Estado`, `FechaRegistro`) VALUES
(1, 'CC', '1020304050', 'Juan Pérez Gómez', '3104567890', 'juanperez@gmail.com', 'Cra 10 #15-20, Tunja', 'Estudiante', 'Activo', '2026-07-07 20:43:51'),
(2, 'CC', '1193577504', 'María Fernanda López', '3116547890', 'maria.lopez@gmail.com', 'Calle 45 #12-15, Tunja', 'Docente', 'Activo', '2026-07-07 20:43:51'),
(3, 'TI', '1002547896', 'Carlos Andrés Rodríguez', '3209874561', 'carlos@gmail.com', 'Vereda Pirgua, Tunja', 'Estudiante', 'Activo', '2026-07-07 20:43:51'),
(4, 'CE', 'E45879632', 'Ana Sofía Martínez', '3157894562', 'anamartinez@gmail.com', 'Av. Norte #20-18, Duitama', 'Externo', 'Activo', '2026-07-07 20:43:51'),
(5, 'CC', '987654321', 'Luis Eduardo Torres', '3124567898', 'luis@gmail.com', 'Barrio Santa Inés, Sogamoso', 'Estudiante', 'Activo', '2026-07-07 20:43:51'),
(7, 'CC', 'Diego Sierra', 'Diego Felipe Sierra Paez', '3141342659', 'DagoooSierra@gmail.com', 'Florida, Tunja', 'Docente', 'Activo', '2026-08-19 00:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `Id` int(11) NOT NULL,
  `IdAutor` int(11) NOT NULL,
  `IdCategoria` int(11) NOT NULL,
  `IdEditorial` int(11) NOT NULL,
  `IdIdioma` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `AñoPublicacion` varchar(255) NOT NULL,
  `Paginas` varchar(255) NOT NULL,
  `Descripcion` text NOT NULL,
  `FechaRegistro` varchar(255) NOT NULL,
  `Imagen` varchar(255) NOT NULL,
  `Url` varchar(25) NOT NULL,
  `Cantidad` int(11) NOT NULL DEFAULT 1,
  `Disponibles` int(11) NOT NULL DEFAULT 1,
  `Estado` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`Id`, `IdAutor`, `IdCategoria`, `IdEditorial`, `IdIdioma`, `Nombre`, `AñoPublicacion`, `Paginas`, `Descripcion`, `FechaRegistro`, `Imagen`, `Url`, `Cantidad`, `Disponibles`, `Estado`) VALUES
(11, 1, 1, 4, 2, 'El Hobbit', '1937', '310', 'Bilbo Bolsón emprende una inesperada aventura junto a un grupo de enanos para recuperar un antiguo reino custodiado por el dragón Smaug.', '2026-07-22', 'LIBRO__El_Hobbit.jpg', 'https://example.com/libro', 5, 4, '1'),
(12, 2, 4, 1, 1, 'Cien años de soledad', '1967', '471', 'La historia de la familia Buendía en el mítico pueblo de Macondo, considerada una de las obras más importantes de la literatura hispanoamericana.', '2026-07-22', 'portada_cien_anos_de_soledad.jpg', 'https://example.com/libro', 4, 4, '1'),
(13, 3, 3, 3, 2, 'Orgullo y prejuicio', '1813', '432', 'Una novela clásica que explora el amor, los prejuicios y las diferencias sociales en la Inglaterra del siglo XIX.', '2026-07-22', 'Orgullo_y_prejuicio_de_Jane_Austen.jpg', 'https://example.com/libro', 6, 5, '1'),
(23, 4, 1, 6, 2, 'Juego de Tronos', '1996', '694', 'Primera entrega de la saga Canción de hielo y fuego, donde diversas casas nobles luchan por el control del Trono de Hierro.', '2026-07-22', 'Img1.jpg', 'https://example.com/libro', 8, 7, '1'),
(24, 11, 1, 3, 2, 'El Imperio Final', '2006', '541', 'Primera novela de la saga Nacidos de la Bruma, donde un grupo de rebeldes intenta derrocar a un gobernante inmortal utilizando poderes basados en los metales.', '2026-07-22', 'El_imperio_final_Nacidos_de_la_bruma_1_-_Brandon_Sanderson_nueva_edicion.jpg', 'https://example.com/libro', 7, 6, '1'),
(25, 5, 5, 8, 1, 'Python para Principiantes', '2024', '420', 'Guía práctica para aprender programación en Python desde cero mediante ejemplos, ejercicios y proyectos sencillos.', '2026-07-22', 'Gemini_Generated_Image_ppc6vappc6vappc6.jpg', 'https://example.com/libro', 10, 10, '1'),
(31, 1, 1, 1, 1, 'El Reino de los Cristales Eternos', '2023', '428', 'Una joven descubre un reino oculto donde los cristales contienen la memoria de antiguas civilizaciones y deberá evitar que caigan en manos equivocadas.', '2026-07-22', 'Gemini_Generated_Image_ibpboyibpboyibpb.jpg', 'https://example.com/crist', 8, 8, '1'),
(32, 5, 2, 2, 1, 'Código Omega', '2025', '365', 'Un grupo de ingenieros desarrolla una inteligencia artificial capaz de alterar cualquier sistema digital, desencadenando una carrera contra el tiempo.', '2026-07-22', 'Gemini_Generated_Image_prsh9hprsh9hprsh.jpg', 'https://example.com/omega', 6, 6, '1'),
(33, 3, 3, 3, 2, 'La Biblioteca de las Sombras', '2022', '512', 'Una inmensa biblioteca esconde libros prohibidos capaces de modificar la realidad cada vez que alguien los lee.', '2026-07-22', 'Gemini_Generated_Image_5fcev85fcev85fce.jpg', 'https://example.com/sombr', 10, 10, '1'),
(34, 4, 4, 4, 1, 'El Último Guardián del Tiempo', '2024', '398', 'El último guardián debe restaurar la línea temporal antes de que la historia desaparezca para siempre.', '2026-07-22', 'El_guardian_del_tiempo_oceano_mitch_albom.jpg', 'https://example.com/guard', 5, 5, '1'),
(35, 4, 4, 4, 1, 'Lotus Splendor', '2026', '286', 'Una historia inspirada en la innovación y la tecnología, donde un joven programador transforma un pequeño centro estético mediante un revolucionario sistema de gestión.', '2026-07-22', 'Gemini_Generated_Image_v02igzv02igzv02i.jpg', 'https://example.com/lotus', 7, 6, '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `Id` int(11) NOT NULL,
  `IdLibro` int(11) NOT NULL,
  `IdLector` int(11) NOT NULL,
  `IdUsuario` int(11) NOT NULL,
  `FechaPrestamo` datetime NOT NULL,
  `FechaDevolucionProgramada` date NOT NULL,
  `FechaDevolucionReal` date DEFAULT NULL,
  `Estado` enum('Prestado','Devuelto','Vencido','Anulado') DEFAULT 'Prestado',
  `Observaciones` text DEFAULT NULL,
  `FechaRegistro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`Id`, `IdLibro`, `IdLector`, `IdUsuario`, `FechaPrestamo`, `FechaDevolucionProgramada`, `FechaDevolucionReal`, `Estado`, `Observaciones`, `FechaRegistro`) VALUES
(1, 12, 3, 1, '2026-07-07 21:06:17', '2026-07-24', '2026-07-07', 'Devuelto', '566', '2026-07-07 21:06:18'),
(2, 12, 1, 1, '0000-00-00 00:00:00', '2026-07-30', '2026-08-20', 'Devuelto', '454545', '2026-07-07 21:15:30'),
(4, 25, 2, 1, '2026-08-20 11:36:00', '2026-08-31', '2026-08-20', 'Anulado', 'aaaaaaaaaaaaaaaaaaaaaa', '2026-08-20 11:36:42'),
(5, 32, 5, 1, '2026-08-20 11:43:19', '2026-08-29', NULL, 'Anulado', 'fgdfgdfgdfgfd', '2026-08-20 11:43:19'),
(6, 31, 5, 1, '2026-08-20 13:33:35', '2026-08-28', '2026-08-20', 'Devuelto', '123', '2026-08-20 13:33:35'),
(7, 35, 3, 1, '2026-08-20 13:33:49', '2026-08-31', NULL, 'Prestado', 'asd', '2026-08-20 13:33:49');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `Id` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`Id`, `Nombre`) VALUES
(1, 'Administrador'),
(2, 'Bibliotecario'),
(3, 'Invitado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `Id` int(11) NOT NULL,
  `IdRol` int(11) NOT NULL,
  `Usuario` varchar(255) NOT NULL,
  `Contrasena` varchar(255) NOT NULL,
  `NombreCompleto` varchar(255) NOT NULL,
  `Correo` varchar(255) NOT NULL,
  `Estado` tinyint(1) NOT NULL,
  `FechaRegistro` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`Id`, `IdRol`, `Usuario`, `Contrasena`, `NombreCompleto`, `Correo`, `Estado`, `FechaRegistro`) VALUES
(1, 1, 'Dubancho', 'scrypt:32768:8:1$PXu8AUYisdVnPElo$e7079ee9b434fa11d35b24030564bf7e59541663b59efe098d0ab221ab62ee7d9000a80039e0f5c649e397e85dbdc9ac3f393122cebb47bb757e1e639dc71967', 'Duban Suarez', 'desuarez@gmail.com', 1, '2026-07-07'),
(3, 3, '123', 'scrypt:32768:8:1$eqVcFBLQzHjQQsAT$0705c1faf54fe018d50636fd9d0241f0aa2b5cecaac3abefacec60e209c00ee18e3099c14a34c12607ba24beac24456911061de591afb4915a696768c5be0687', '123', '123@sfd', 0, '2026-08-19'),
(4, 2, 'asddsa', 'scrypt:32768:8:1$gJDU39BbVGjXORkK$7b23f92c22f38c9e9193182f78c3c9cb61f199dd149febe8978ad894f656ccc9657fd9433710408831929841e42c6f96a62378bcffb22a7e2bf50a5c45b35b70', 'asdasd', 'asdsa@asd', 0, '2026-08-19');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `editoriales`
--
ALTER TABLE `editoriales`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `idiomas`
--
ALTER TABLE `idiomas`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `lectores`
--
ALTER TABLE `lectores`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `NumeroDocumento` (`NumeroDocumento`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `IdAutor` (`IdAutor`),
  ADD KEY `IdCategoria` (`IdCategoria`),
  ADD KEY `IdEditorial` (`IdEditorial`),
  ADD KEY `IdIdioma` (`IdIdioma`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `fk_prestamo_libro` (`IdLibro`),
  ADD KEY `fk_prestamo_lector` (`IdLector`),
  ADD KEY `fk_prestamo_usuario` (`IdUsuario`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `IdRol` (`IdRol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autores`
--
ALTER TABLE `autores`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `editoriales`
--
ALTER TABLE `editoriales`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `idiomas`
--
ALTER TABLE `idiomas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `lectores`
--
ALTER TABLE `lectores`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `libros`
--
ALTER TABLE `libros`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `libros`
--
ALTER TABLE `libros`
  ADD CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`IdAutor`) REFERENCES `autores` (`Id`),
  ADD CONSTRAINT `libros_ibfk_2` FOREIGN KEY (`IdCategoria`) REFERENCES `categorias` (`Id`),
  ADD CONSTRAINT `libros_ibfk_3` FOREIGN KEY (`IdEditorial`) REFERENCES `editoriales` (`Id`),
  ADD CONSTRAINT `libros_ibfk_4` FOREIGN KEY (`IdIdioma`) REFERENCES `idiomas` (`Id`);

--
-- Filtros para la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `fk_prestamo_lector` FOREIGN KEY (`IdLector`) REFERENCES `lectores` (`Id`),
  ADD CONSTRAINT `fk_prestamo_libro` FOREIGN KEY (`IdLibro`) REFERENCES `libros` (`Id`),
  ADD CONSTRAINT `fk_prestamo_usuario` FOREIGN KEY (`IdUsuario`) REFERENCES `usuario` (`Id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`IdRol`) REFERENCES `rol` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
