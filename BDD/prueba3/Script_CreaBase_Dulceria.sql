DROP TABLE boleta;
DROP TABLE cliente;

CREATE TABLE cliente (
    id_cliente      NUMBER NOT NULL,
    nombre_cliente  VARCHAR2(35) NOT NULL,
    direccion       VARCHAR2(50) NOT NULL,
    telefono        VARCHAR2(15) NOT NULL,
    id_comuna       DATE NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT pk_cliente PRIMARY KEY ( id_cliente );

CREATE TABLE boleta (
    id_boleta     NUMBER NOT NULL,
    id_cliente    NUMBER NOT NULL,
    id_empleado   NUMBER NOT NULL,
    fecha_boleta  DATE NOT NULL
);

ALTER TABLE boleta ADD CONSTRAINT pk_boleta PRIMARY KEY ( id_boleta );

ALTER TABLE boleta
    ADD CONSTRAINT fk_boleta_cliente FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE empleado 
  ADD CONSTRAINT fk_equipo_empleado FOREIGN KEY (id_equipo) 
   REFERENCES equipo (id_equipo);


INSERT INTO cliente VALUES (1,'ALCARAZ NOVOA MONTSERRAT','RUBEN BARRALES 1630','564522114', 102);
