RAW_SQL = \
"""
SELECT
    'D' as tipo,
    id,
    ts_headline('spanish',
    codigo || ' ' || nombre,
    to_tsquery('spanish',
    %s)) as highlight,
    fecha
FROM
    pacientes_diagnostico
WHERE
    paciente_id = 1
    and to_tsvector('spanish', codigo || ' ' || nombre) @@ plainto_tsquery('spanish', %s)
UNION
SELECT
    'M' as tipo,
    id,
    ts_headline('spanish',
    codigo || ' ' || nombre,
    to_tsquery('spanish',
    %s)) as highlight,
    null
FROM
    pacientes_medicamento
WHERE
    paciente_id = 1
    and to_tsvector('spanish', codigo || ' ' || nombre) @@ plainto_tsquery('spanish', %s)
UNION
SELECT
    'A' as tipo,
    id,
    ts_headline('spanish',
    nombre,
    to_tsquery('spanish',
    %s)) as highlight,
    null
FROM
    pacientes_alergia
WHERE
    paciente_id = 1
    and to_tsvector('spanish', nombre) @@ plainto_tsquery('spanish', %s)
UNION
SELECT
    'I' as tipo,
    id,
    ts_headline('spanish',
    codigo || ' ' || nombre,
    to_tsquery('spanish',
    %s)) as highlight,
    fecha
FROM
    pacientes_intervencion
WHERE
    paciente_id = 1
    and to_tsvector('spanish', codigo || ' ' || nombre) @@ plainto_tsquery('spanish', %s)
UNION
SELECT
    'E' as tipo,
    id,
    ts_headline('spanish',
    motivo,
    to_tsquery('spanish',
    %s)) as highlight,
    fecha
FROM
    pacientes_evento
WHERE
    paciente_id = 1
    and to_tsvector('spanish', motivo) @@ plainto_tsquery('spanish', %s)
"""
