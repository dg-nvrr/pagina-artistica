-- TABLAS (DDL)
CREATE TABLE IF NOT EXISTS Categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_tecnica VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Obras (
    id_obra INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(100) NOT NULL,
    precio INTEGER NOT NULL,
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);

-- DATOS INICIALES (DML)
INSERT INTO Categorias (nombre_tecnica) VALUES ('Pintura'), ('Orfebreria'), ('Mixta');

INSERT INTO Obras (titulo, precio, id_categoria) VALUES 
('Atardeceres', 150000, 1),
('Colgante Lunar', 45000, 2),
('Abstracción III', 80000, 3);

-- CONSULTA DE PRUEBA (JOIN)
SELECT Obras.titulo, Categorias.nombre_tecnica, Obras.precio 
FROM Obras 
INNER JOIN Categorias ON Obras.id_categoria = Categorias.id_categoria;