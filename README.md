# ApiCumulus

API para Cumulus en Python

## Instalacion

1. Instalar Python 2.7+
2. Intalar pip + virtualenv
3. Crear un nuevo virtualenv
```sh
$ virtualenv ENV
```
4. Activar el virtualenv
```sh
$ source ENV/bin/activate
```
5. Instalar dependencias de python
```sh
$ pip install -r requirements.txt
```
6. Correr las migraciones de django
```sh
$ ./manage.py migrate
```
7. Levantar el servidor
```sh
$ ./manage.py runserver
```

## Ejemplos de Api
### Pacientes
#### Paciente Id por CURP
URL: `/pacientes/{curp}/`
* GET
```javascript
{
    "id": 1
}
```

#### Paciente pertenece a hospital
URL: `/pacientes/{curp}/hospital/{hospital_id}/`
* GET
```javascript
{
    "id": 1
}
```

#### Informacion del Paciente
URL: `/pacientes/{paciente_id}/`
* GET
```javascript
{
    "id": 1,
    "nombre": "Ana",
    "segundoNombre": "Maria",
    "apellido": "Gonzalez",
    "apellido2": "Trevino",
    "curp": "GOTA750512MGDRA01",
    "sexo": "M",
    "fechaNacimiento": "1975-05-12"
    "hospitales": [
        {
            "id": 2
            "nombre": "Clinica de la mujer",
        },
        // ...
    ],
    "historia": [
        {
            "id": 1
            "paciente": 1,
            "personal": "personal",
            "familiar": "familiar",
            "clinica": "historia",
        },
        // ...
    ],
}
```

#### Agregar/Remover permisos para un hospital
URL: `/pacientes/{paciente_id}/hospital/{hospital_id}/`
* POST
```javascript
{
    "mensaje": "Se dio permiso al hospital"
}
```
* DELETE
```javascript
{
    "mensaje": "Se removio el permiso al hospital"
}
```

### Eventos
#### Ver lista de eventos de un paciente
URL: `/pacientes/{paciente_id}/eventos`
* GET
```javascript
[
    {
        "id": 1,
        "paciente": 1,
        "medico": "Dr Ismael Tamez Lopez",
        "cedula": "465146113165",
        "especialidad": "NA",
        "tipo": "A",
        "fecha": "2015-03-09T09:00:00Z",
        "motivo": "Estudio de laboratorio",
        "tomas": [
            {
                "id": 1,
                "evento": 1,
                "paciente": 1,
                "fecha": "2015-10-10T00:00:00Z",
                "signos": [
                    {
                        "id": 1,
                        "toma": 1,
                        "nombre": "peso",
                        "valor": 60,
                        "unidad": "kg",
                    },
                    // ...
                ]
            },
            // ...
        ],
        "intervenciones": [
            {
                "id": 1,
                "evento": 1,
                "paciente": 1,
                "nombre": "Colecistectomia laparoscopica",
                "fecha": "2014-08-17T14:30:00Z",
                "codigo": "51.23",
            },
            // ...
        ],
        "recetas": [
            {
                "id": 1,
                "evento": 1,
                "paciente": 1,
                "notas": "evitar bebidas frías, y alimentos irritantes",
                "fecha": "2013-11-21T20:00:00Z",
                "medicamentos": [
                    {
                        "id": 1,
                        "receta": 1,
                        "paciente": 1,
                        "via": "oral",
                        "codigo": "as4",
                        "indicacion": "cada 6 hrs x 5 días",
                        "dosis": "1 tableta",
                        "nombre": "ibuprofeno 400mg",
                    },
                    // ...
                ]
            },
            // ...
        ],
        "diagnosticos": [
            {
                "id": 1,
                "evento": 1,
                "paciente": 1,
                "codigo": "R07",
                "nombre": "Dolor de garganta y en el pecho",
                "fecha": "2013-11-21T20:00:00Z",
            },
            // ...
        ]
    },
    // ...
]
```

### Alergias
#### Ver lista de alergias de un paciente
URL: `/pacientes/{paciente_id}/alergias`
* GET
```javascript
[
    {
        "id": 1,
        "paciente": 1,
        "reaccion": "urticaria",
        "severidad": "M",
        "tipo": "C",
        "nombre": "Frutos secos (almendra, nuez, pistache, etc)",
    },
    // ...
]
```
* POST
```javascript
{
    "id": 1,
    "mensaje": "Alergia creada",
}
```

### Diagnosticos
#### Ver lista de diagnosticos de un paciente
URL: `/pacientes/{paciente_id}/diagnosticos`
* GET
```javascript
[
    {
        "id": 1,
        "evento": 1,
        "paciente": 1,
        "nombre": "Urticaria alergica",
        "fecha": "1985-01-23T06:40:06Z",
        "codigo": "L50.0",
    },
    // ...
]
```

### Intervenciones
#### Ver lista de intervenciones de un paciente
URL: `/pacientes/{paciente_id}/intervenciones`
* GET
```javascript
[
    {
        "evento": 3,
        "paciente": 1,
        "nombre": "Colecistectomia laparoscopica",
        "fecha": "2014-08-17T14:30:00Z",
        "codigo": "51.23",
        "id": 1,
    },
    // ...
]
```

### Medicamentos
#### Ver lista de medicamentos de un paciente
URL: `/pacientes/{paciente_id}/medicamentos`
* GET
```javascript
[
    {
        "id": 1,
        "receta": 1,
        "paciente": 1,
        "via": "oral",
        "indicacion": "cada 6 hrs x 5 días",
        "dosis": "1 tableta",
        "nombre": "ibuprofeno 400mg",
        "codigo": "as4",
    },
    // ...
]
```
* POST
```javascript
{
    "id": 1,
    "mensaje": "Medicamento creado", 
}
```


### Recetas
#### Ver lista de recetas de un paciente
URL: `/pacientes/{paciente_id}/recetas`
* GET
```javascript
[
    {
        "id": 1,
        "evento": 1,
        "paciente": 1,
        "notas": "evitar bebidas frías, y alimentos irritantes",
        "fecha": "2013-11-21T20:00:00Z",
        "medicamentos": [
            {
                "id": 1,
                "receta": 1,
                "paciente": 1,
                "via": "oral",
                "indicacion": "cada 6 hrs x 5 días",
                "dosis": "1 tableta",
                "nombre": "ibuprofeno 400mg",
                "codigo": "as4",
            },
            // ...
        ],
    },
    // ...
]
```

### Tomas de Signos Vitales
#### Ver lista de toams de signos vitales de un paciente
URL: `/pacientes/{paciente_id}/tomas_signos`
* GET
```javascript
[
    {
        "id": 1,
        "evento": 1,
        "paciente": 1,
        "fecha": "2015-10-10T00:00:00Z",
        "signos": [
            {
                "nombre": "peso",
                "valor": 60,
                "toma": 1,
                "id": 1,
                "unidad": "kg"
            },
            // ...
        ],
    },
    // ...
]
```
