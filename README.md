<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_tftp.svg)](https://github.com/while-true-do/ansible-role-srv_tftp/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_tftp.svg)](https://github.com/while-true-do/ansible-role-srv_tftp/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_tftp.svg)](https://github.com/while-true-do/ansible-role-srv_tftp/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_tftp.svg)](https://github.com/while-true-do/ansible-role-srv_tftp/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_tftp.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_tftp)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_tftp%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_tftp)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_tftp%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_tftp)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_tftp%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_tftp)

# Ansible Role: srv_tftp

An Ansible Role to install and configure a tftp server.

## Motivation

A very common scenario in IT Operations is, that a server needs to be deployed
via PXE boot. This involves tftp and syslinux.

## Description

This Ansible Role installs and configures tftp and syslinux.

- install tftp-server
- enable tftp-server
- install syslinux packages
- configure PXE Boot Configuration (pxelinux.cfg/default)

## Requirements

Used Modules:

-   [Ansible package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/package_facts_module.html)
-   [Ansible firewalld Module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)
-   [Ansible template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible file Module](https://docs.ansible.com/ansible/latest/modules/file_module.html)
-   [Ansible command Module](https://docs.ansible.com/ansible/latest/modules/command_module.html)
-   [Ansible stat Module](https://docs.ansible.com/ansible/latest/modules/stat_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_tftp)
```
ansible-galaxy install while_true_do.srv_tftp
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_tftp)
```
git clone https://github.com/while-true-do/ansible-role-srv_tftp.git while_true_do.srv_tftp
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_tftp

## Package Management
wtd_srv_tftp_package: "tftp-server"
# State can be present|latest|absent
wtd_srv_tftp_package_state: "present"

## Management for tftpboot
# tftp is most likely used for pxe, bootp
# enabled can be true|false
wtd_srv_tftp_boot_enabled: true

# Packages for tftpboot
wtd_srv_tftp_boot_package: "syslinux-tftpboot"
# State can be present|latest|absent
wtd_srv_tftp_boot_package_state: "present"

# Configuration for tftpboot
wtd_srv_tftp_boot_conf:
  timeout: "300"
  title: "PXE Boot"
  label_reboot: true
  label_poweroff: true
  labels: []
  #   - label: ""
  #     default: false
  #     kernel: ""
  #     append: ""

## Service Management
wtd_srv_tftp_service: "tftp.socket"
# State can be started|stopped
wtd_srv_tftp_service_state: "started"
wtd_srv_tftp_service_enabled: true

## Firewalld Management
wtd_srv_tftp_fw_mgmt: true
wtd_srv_tftp_fw_service: "tftp"
# State can be enabled|disabled
wtd_srv_tftp_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_tftp_fw_zone: "public"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_tftp
```

#### Advanced

Configuring multiple labels. Be aware, that you have to download and prepare
the needed OS files on your own.

```
- hosts: all
  roles:
  - role: while_true_do.srv_tftp
    wtd_srv_tftp_boot_conf:
      timeout: "100"
      title: "While True Do Boot"
      labels:
      - label: "CentOS 7.6"
        default: true
        kernel: "centos76/vmlinuz"
        append: "initrd=centos76/initrd.img"
      - label: "Fedora 30"
        kernel: "fedora30/vmlinuz"
        append: "initrd=fedora30/initrd.img"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_tftp/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_tftp/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
