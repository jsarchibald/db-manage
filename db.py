commands = {
    "Windows": {
        "MongoDB": {
            "start": ["sc stop MongoDB", "sc start MongoDB"],
            "stop": ["sc stop MongoDB"]
        },
        "MySQL": {
            "start": ["sc stop mysql80", "sc start mysql80"],
            "stop": ["sc stop mysql80"]
        },
        "PostgreSQL": {
            "start": ["sc stop postgresql-x64-12", "sc start postgresql-x64-12"],
            "stop": ["sc stop postgresql-x64-12"]
        }
    }
}