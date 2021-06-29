# Bitbucket Playbook

## Roles

Which roles are used.

- proxy _seems not to work_
- ansible-bitbucket

## Directory structure

```bash
$ tree
.
├── README.md
├── ansible.yml
├── bitbucket-playbook.yml
├── hosts
│   ├── production
│   │   ├── group_vars
│   │   │   └── all.yml
│   │   └── inventory
│   ├── shared_vars.yml
│   └── staging
│       ├── group_vars
│       │   └── all.yml
│       └── inventory
├── roles
│   ├── ansible-bitbucket
│   │   ├── README.md
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── host_vars
│   │   ├── molecule
│   │   │   └── default
│   │   │       ├── Dockerfile.j2
│   │   │       ├── INSTALL.rst
│   │   │       ├── molecule.yml
│   │   │       ├── playbook.yml
│   │   │       └── tests
│   │   │           ├── test_bitbucket.py
│   │   │           └── test_default.py
│   │   ├── tasks
│   │   │   ├── configure.yml
│   │   │   ├── install.yml
│   │   │   ├── main.yml
│   │   │   ├── service.yml
│   │   │   ├── snapshot.yml
│   │   │   └── switch.yml
│   │   ├── templates
│   │   │   ├── bin
│   │   │   │   ├── _start-webapp.sh.j2
│   │   │   │   ├── set-bitbucket-home.sh.j2
│   │   │   │   └── set-jre-home.sh.j2
│   │   │   ├── bitbucket.properties.j2
│   │   │   ├── bitbucket.service.j2
│   │   │   └── jmx
│   │   │       ├── jmx.access.j2
│   │   │       └── set-jmx-opts.sh.j2
│   │   └── vars
│   │       └── main.yml
│   └── proxy
│       ├── files
│       │   └── proxy_setup.sh
│       ├── molecule
│       │   └── default
│       │       ├── Dockerfile.j2
│       │       ├── INSTALL.rst
│       │       ├── molecule.yml
│       │       ├── playbook.yml
│       │       └── tests
│       │           └── test_default.py
│       └── tasks
│           └── main.yml
└── tasks
    └── load_vars.yml

27 directories, 42 files
```

## Remote Hook
test test test

