API Cumulus
===

# Informacion de Paciente
## Tabla de datos

<table>
<tr><th> Parametro </th><th> Tipo </th><th> Descripcion </th></tr>
<tr><td> nombre </td><td> String </td><td> Nombre(s) del Paciente </td></tr>
<tr><td> apellido </td><td> String </td><td> Primer Apellido del Paciente </td></tr>
<tr><td> apellidoSegundo </td><td> String </td><td> Demas Apellidos del Paciente </td></tr>
<tr><td> telefono </td><td> String </td><td> Telefono de contacto </td></tr>
<tr><td> telefonoAlt </td><td> String </td><td> Telefono alterno </td></tr>
<tr><td> correo </td><td> String </td><td> Correo electronico </td></tr>
<tr><td> fechaNacimiento </td><td> String, formato “yyyy-mm-dd” </td><td> Fecha de Nacimiento del Paciente </td></tr>
<tr><td> sexo </td><td> String, “H”, “M” o "NA" </td><td> Sexo del Paciente: <b>H</b>ombre, <b>M</b>ujer o <b>N</b>o <b>A</b>plica </td></tr>
<tr><td> curp </td><td> String, 18 caracteres </td><td> CURP del Paciente </td></tr>
<tr><td> calle </td><td> String </td><td> Calle y numero de la direccion del Paciente </td></tr>
<tr><td> codigoPostal </td><td> String </td><td> Codigo Postal </td></tr>
<tr><td> ciudad </td><td> String </td><td> Ciudad o Municipio </td></tr>
<tr><td> estado </td><td> String </td><td> Estado </td></tr>
<tr><td> pais </td><td> String </td><td> Pais </td></tr>
<tr><td> alergias </td><td> N cantidad con la siguiente informacion </td><td> Alergias del paciente </td></tr>
<tr><td> • nombre </td><td> String </td><td> Nombre o Descripcion breve de la alergia </td></tr>
<tr><td> • tipo </td><td> String, “M”, “A” o "C” </td><td> Tipo de la alergia: <b>M</b>edicamento, <b>A</b>mbiente o <b>C</b>omida </td></tr>
<tr><td> • severidad </td><td> String, “A”, °M” o “B” </td><td> Severidad de la alergia: <b>A</b>lta, <b>M</b>edia o <b>B</b>aja </td></tr>
<tr><td> • reaccion </td><td> String </td><td> Reaccion alergica del Paciente </td></tr>
</table>

## JSON Ejemplo
```javascript
{
  "nombre": "Ana Maria",
  "apellido": "Gonzalez",
  "apellidoSegundo": "Trevino",
  "fechaNacimiento": "1975-05-12",
  "curp":"GOTA750512MGDRA01",
  "sexo":"M",
  "telefono": "80808080",
  "telfonoAlt": "8111111111",
  "correo": "ana.maria@prueba.com",
  // Demograficos
  "calle": "Calle #123"
  "cp": "67890",
  "ciudad": "Monterrey",
  "estado": "Nuevo Leon",
  "pais": "Mexico",
  // Alergias
  "alergias": [
    {
      "nombre": "Almendras",
      "reaccion": "Irritacion en la Piel",
      "tipo": "C",
      "severidad": "B"
    },
    // ...
  ]
}
```

# Evento
## Tabla de datos
<table>
<tr><th> Parametro </th><th> Tipo </th><th> Descripcion </th></tr>
<tr><td> medico </td><td> String </td><td> Nombre completo del Medico </td></tr>
<tr><td> cedula </td><td> String </td><td> Cedula profesional del Medico </td></tr>
<tr><td> especialidad </td><td> String </td><td> Especialidad del Medico </td></tr>
<tr><td> tipo </td><td> String, “C”, “A”, “H” o "U" </td><td> Tipo de evento: <b>C</b>onsulta, <b>A</b>mbulatorio, <b>H</b>ospitalizacion o <b>U</b>rgencia </td></tr>
<tr><td> fechaInicio </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se comenzo el evento </td></tr>
<tr><td> fechaFin </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se finalizo el evento </td></tr>
<tr><td> motivo </td><td> String </td><td> Una descripcion breve del motivo del evento </td></tr>
<tr><td> tomas </td><td> N cantidad con la siguiente informacion </td><td> Tomas de signos vitales que se realizaron a lo largo del evento </td></tr>
<tr><td> • fecha </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se realizo la toma de signos vitales </td></tr>
<tr><td> • signos </td><td> N cantidad con la siguiente informacion </td><td> Lista de los signos vitales tomados durante esta fecha </td></tr>
<tr><td> &nbsp; ° valor </td><td> Float </td><td> Valor obtenido en la toma de signo vital </td></tr>
<tr><td> &nbsp; ° unidad </td><td> String </td><td> Unidad de la toma de signo vital, ej. "KG" </td></tr>
<tr><td> &nbsp; ° nombre </td><td> String </td><td> Nombre del signo vital, ej "Peso" </td></tr>
<tr><td> intervenciones </td><td> N cantidad con la siguiente informacion </td><td> Lista de intervenciones medicas, ej. Cirujias </td></tr>
<tr><td> • nombre </td><td> String </td><td> Nombre de la intervencion </td></tr>
<tr><td> • codigo </td><td> String </td><td> Codigo CIE9V3 (ICD9V3) de la intervencion </td></tr>
<tr><td> recetas </td><td> N cantidad con la siguiente informacion </td><td> Recetas medicas  </td></tr>
<tr><td> • fecha </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se recetaron los medicamentos </td></tr>
<tr><td> • nota </td><td> String </td><td> Indicaciones extra sobre la receta medica </td></tr>
<tr><td> • medicamentos </td><td> N cantidad con la siguiente informacion </td><td> Lista de medicamentos de la Receta </td></tr>
<tr><td> &nbsp; ° nombre </td><td> String </td><td> Nombre de medicamento </td></tr>
<tr><td> &nbsp; ° codigo </td><td> String </td><td> Codigo de indentificacion del medicamento </td></tr>
<tr><td> &nbsp; ° clasificacion </td><td> String </td><td> Clasificacion del codigo, ej. "GPI" o "NDC" </td></tr>
<tr><td> &nbsp; ° indicacion </td><td> String </td><td> Indiicaciones sobre frequencia </td></tr>
<tr><td> &nbsp; ° via </td><td> String </td><td> Via de adminstracion </td></tr>
<tr><td> &nbsp; ° dosis </td><td> String </td><td> Dosis del medicamento </td></tr>
<tr><td> diagnosticos </td><td> N cantidad con la siguiente informacion </td><td> Diagnosticos del Paciente </td></tr>
<tr><td> • fecha </td><td> String, formato “yyyy-mm-ddTHH:MM:SSZ” </td><td> Fecha en que se realizo el diagnostico </td></tr>
<tr><td> • nombre </td><td> String </td><td> Nombre del diagnostico </td></tr>
<tr><td> • codigo </td><td> String </td><td> Codigo de CIE10 (ICD10CM6) del padecimiento </td></tr>
<tr><td> cuestionarios </td><td> N cantidad con la siguiente informacion </td><td> Cuestionarios del paciente </td></tr>
<tr><td> • titulo </td><td> String </td><td> Titulo del cuestionario, las preguntas se agrupan mediante esto </td></tr>
<tr><td> • pregunta </td><td> String </td><td> Pregunta </td></tr>
<tr><td> • respuesta </td><td> String </td><td> Respuesta </td></tr>
<tr><td> • descripcion </td><td> String </td><td> Detalles extra de la respuesta a la pregunta </td></tr>
</table>

## JSON Ejemplo
```javascript
{
  "medico": "Dr Ismael Tamez Lopez",
  "cedula": "465146113165",
  "especialidad": "NA",
  "tipo": "C",
  "fechaInicio": "2015-12-01T08:00:00Z",
  "fechaFin": "2015-12-01T09:00:00Z",
  "motivo": "Fiebre",
  "tomas": [
    {
      "fecha": "2015-12-01T08:15:00Z"
      "signos": [
        {
          "nombre": "Peso",
          "valor": 60.0,
          "unidad": "kg"
        },
        // ...
      ]
    },
    // ...
  ],
  "intervenciones": [
    {
      "fecha": "2015-12-01T09:00:00Z"
      "nombre": "Colecistectomia laparoscopica",
      "codigo": "51.23",
    },
    // ...
  ],
  "recetas": [
    {
      "notas": "evitar bebidas frías, y alimentos irritantes",
      "fecha": "2015-12-01T08:30:00Z",
      "medicamentos": [
        {
          "via": "oral",
          "nombre": "Ibuprofeno 400mg",
          "codigo": "66-10-00-20-00-03-20",
          "clasificacion": "GPI",
          "via": "oral",
          "indicacion": "cada 6 hrs x 5 días",
          "dosis": "1 tableta"
        },
        // ...
      ]
    }
    // ...
  ],
  "diagnosticos": [
    {
      "fecha": "2015-12-01T09:00:00Z"
      "nombre": "Dolor de garganta y en el pecho",
      "codigo": "R07",
    },
    // ...
  ],
  "cuestionarios": [
    {
      "titulo": "Patologicos",
      "pregunta": "Diabetes?",
      "respuesta": "true",
      "descripcion": "Tipo 1"
    },
    // ...
  ]
}
```
