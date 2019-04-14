import pickle

cosa = [
    {
        "id": 1,
        "name": "MS Dynamics",
        "field_id": 1,
        "field_name": "Aplicaciones Empresariales"
    },
    {
        "id": 2,
        "name": "PeopleSoft",
        "field_id": 1,
        "field_name": "Aplicaciones Empresariales"
    },
    {
        "id": 3,
        "name": "JD Edwards",
        "field_id": 1,
        "field_name": "Aplicaciones Empresariales"
    },
    {
        "id": 4,
        "name": "Oracle EBS",
        "field_id": 1,
        "field_name": "Aplicaciones Empresariales"
    },
    {
        "id": 5,
        "name": "SAP",
        "field_id": 1,
        "field_name": "Aplicaciones Empresariales"
    },
    {
        "id": 6,
        "name": "Bases de Datos Embebidas",
        "field_id": 2,
        "field_name": "Gestión de Información"
    },
    {
        "id": 7,
        "name": "Bases de Datos Relacionales",
        "field_id": 2,
        "field_name": "Gestión de Información"
    },
    {
        "id": 8,
        "name": "Big Data",
        "field_id": 2,
        "field_name": "Gestión de Información"
    },
    {
        "id": 9,
        "name": "Business Intelligence",
        "field_id": 2,
        "field_name": "Gestión de Información"
    },
    {
        "id": 10,
        "name": "Data Warehouse",
        "field_id": 2,
        "field_name": "Gestión de Información"
    },
    {
        "id": 11,
        "name": "Enterprise Content Management",
        "field_id": 2,
        "field_name": "Gestión de Información"
    },
    {
        "id": 12,
        "name": "Integración de Datos y ETL",
        "field_id": 2,
        "field_name": "Gestión de Información"
    },
    {
        "id": 13,
        "name": "NoSQL",
        "field_id": 2,
        "field_name": "Gestión de Información"
    },
    {
        "id": 14,
        "name": "AS400",
        "field_id": 3,
        "field_name": "Gestión de Infraestructura"
    },
    {
        "id": 15,
        "name": "Virtualización de Servidores",
        "field_id": 3,
        "field_name": "Gestión de Infraestructura"
    },
    {
        "id": 16,
        "name": "Servidores de Aplicaciones (Application Servers)",
        "field_id": 3,
        "field_name": "Gestión de Infraestructura"
    },
    {
        "id": 17,
        "name": "Integración de Aplicaciones EAI y SOA",
        "field_id": 3,
        "field_name": "Gestión de Infraestructura"
    },
    {
        "id": 18,
        "name": "Administración de Sistemas Mainframe",
        "field_id": 3,
        "field_name": "Gestión de Infraestructura"
    },
    {
        "id": 19,
        "name": "Administración de Servidores Windows",
        "field_id": 3,
        "field_name": "Gestión de Infraestructura"
    },
    {
        "id": 20,
        "name": "Administración de Servidores Unix",
        "field_id": 3,
        "field_name": "Gestión de Infraestructura"
    },
    {
        "id": 21,
        "name": "Administración de Proyectos",
        "field_id": 4,
        "field_name": "Gestión de Proyectos y Procesos"
    },
    {
        "id": 22,
        "name": "Gestión de Servicios (IT Service Management)",
        "field_id": 4,
        "field_name": "Gestión de Proyectos y Procesos"
    },
    {
        "id": 23,
        "name": "Governance, Risk management, and Compliance",
        "field_id": 4,
        "field_name": "Gestión de Proyectos y Procesos"
    },
    {
        "id": 24,
        "name": "Gestión de Procesos de Negocio (BPM)",
        "field_id": 4,
        "field_name": "Gestión de Proyectos y Procesos"
    },
    {
        "id": 25,
        "name": "Analista de Sistemas",
        "field_id": 5,
        "field_name": "Ingeniería de Software"
    },
    {
        "id": 26,
        "name": "Análisis de Requerimientos",
        "field_id": 5,
        "field_name": "Ingeniería de Software"
    },
    {
        "id": 27,
        "name": "Diseño de Software",
        "field_id": 5,
        "field_name": "Ingeniería de Software"
    },
    {
        "id": 28,
        "name": "Gestión de Configuración (CM)",
        "field_id": 5,
        "field_name": "Ingeniería de Software"
    },
    {
        "id": 29,
        "name": "Testing/QA",
        "field_id": 5,
        "field_name": "Ingeniería de Software"
    },
    {
        "id": 30,
        "name": "Community Manager",
        "field_id": 6,
        "field_name": "Marketing Digital"
    },
    {
        "id": 31,
        "name": "Content Curator",
        "field_id": 6,
        "field_name": "Marketing Digital"
    },
    {
        "id": 32,
        "name": "SEO - SEM",
        "field_id": 6,
        "field_name": "Marketing Digital"
    },
    {
        "id": 33,
        "name": "Actionscript3",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 34,
        "name": "Assembler",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 35,
        "name": "C",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 36,
        "name": "C#/Net",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 37,
        "name": "C++",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 38,
        "name": "COBOL",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 39,
        "name": "Clojure",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 40,
        "name": "ABAP",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 41,
        "name": "PL-SQL",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 42,
        "name": "Delphi",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 43,
        "name": "RPG",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 44,
        "name": "Power Builder",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 45,
        "name": "Go",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 46,
        "name": "Lotus Notes",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 47,
        "name": "Java",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 48,
        "name": "Javascript",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 49,
        "name": "Lua",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 51,
        "name": "Perl",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 52,
        "name": "PHP",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 53,
        "name": "Python",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 54,
        "name": "Ruby",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 55,
        "name": "Scala",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 56,
        "name": "Scheme",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 57,
        "name": "Shell",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 58,
        "name": "Visual Basic",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 59,
        "name": "Air - Flash",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 60,
        "name": "Android",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 62,
        "name": "iOS",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 63,
        "name": "Windows",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 64,
        "name": "HTML",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 65,
        "name": "CSS",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 66,
        "name": "HTML5",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 67,
        "name": "JQuery",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 68,
        "name": "AngularJS",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 69,
        "name": "EmberJS",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 70,
        "name": "KnockoutJS",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 71,
        "name": "BackboneJS",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 72,
        "name": "Adminstración de Personal",
        "field_id": 8,
        "field_name": "Recursos Humanos"
    },
    {
        "id": 73,
        "name": "Capacitación y Desarrollo",
        "field_id": 8,
        "field_name": "Recursos Humanos"
    },
    {
        "id": 74,
        "name": "Reclutamiento",
        "field_id": 8,
        "field_name": "Recursos Humanos"
    },
    {
        "id": 75,
        "name": "Redes Inalámbricas",
        "field_id": 9,
        "field_name": "Redes y Telecomunicaciones"
    },
    {
        "id": 76,
        "name": "Redes de Voz",
        "field_id": 9,
        "field_name": "Redes y Telecomunicaciones"
    },
    {
        "id": 77,
        "name": "Redes P2P",
        "field_id": 9,
        "field_name": "Redes y Telecomunicaciones"
    },
    {
        "id": 78,
        "name": "Firewalls",
        "field_id": 9,
        "field_name": "Redes y Telecomunicaciones"
    },
    {
        "id": 79,
        "name": "Auditoría de Seguridad",
        "field_id": 10,
        "field_name": "Seguridad"
    },
    {
        "id": 80,
        "name": "Criptografía",
        "field_id": 10,
        "field_name": "Seguridad"
    },
    {
        "id": 81,
        "name": "Penetration Tester",
        "field_id": 10,
        "field_name": "Seguridad"
    },
    {
        "id": 82,
        "name": "Ventas TI",
        "field_id": 11,
        "field_name": "Ventas"
    },
    {
        "id": 85,
        "name": "UX",
        "field_id": 12,
        "field_name": "Diseño"
    },
    {
        "id": 86,
        "name": "UI",
        "field_id": 12,
        "field_name": "Diseño"
    },
    {
        "id": 87,
        "name": "Diseño Web",
        "field_id": 12,
        "field_name": "Diseño"
    },
    {
        "id": 88,
        "name": "PhoneGap",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 89,
        "name": "Software Embebido",
        "field_id": 7,
        "field_name": "Programación"
    },
    {
        "id": 90,
        "name": "Xamarin",
        "field_id": 7,
        "field_name": "Programación"
    }
]

file = open('skills.data', 'wb')
pickle.dump(cosa, file)
file.close()
