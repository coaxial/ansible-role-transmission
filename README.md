# transmission role

[![CI](https://github.com/coaxial/ansible-role-transmission/actions/workflows/ci.yml/badge.svg)](https://github.com/coaxial/ansible-role-transmission/actions/workflows/ci.yml)

Galaxy: https://galaxy.ansible.com/coaxial/transmission

## Variables and their defaults

| variable name             | default value | description                                                                             |
| ------------------------- | ------------- | --------------------------------------------------------------------------------------- |
| transmission\_\_group     | `media`       | Transmission user's group                                                               |
| transmission\_\_group_id  | `1100`        | Transmission user's group GID                                                           |
| transmission\_\_use_nginx | `yes`         | Whether to install and configure nginx (`no` if you're installing/managing it yourself) |
