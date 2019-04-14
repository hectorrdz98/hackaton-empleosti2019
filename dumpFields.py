import pickle

cosa = [
    {
        "id": 1,
        "name": "Aplicaciones Empresariales"
    },
    {
        "id": 2,
        "name": "Gestión de Información"
    },
    {
        "id": 3,
        "name": "Gestión de Infraestructura"
    },
    {
        "id": 4,
        "name": "Gestión de Proyectos y Procesos"
    },
    {
        "id": 5,
        "name": "Ingeniería de Software"
    },
    {
        "id": 6,
        "name": "Marketing Digital"
    },
    {
        "id": 7,
        "name": "Programación"
    },
    {
        "id": 8,
        "name": "Recursos Humanos"
    },
    {
        "id": 9,
        "name": "Redes y Telecomunicaciones"
    },
    {
        "id": 10,
        "name": "Seguridad"
    },
    {
        "id": 11,
        "name": "Ventas"
    },
    {
        "id": 12,
        "name": "Diseño"
    }
]

file = open('fields.data', 'wb')
pickle.dump(cosa, file)
file.close()