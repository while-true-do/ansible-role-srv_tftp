# Some examples are given below.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tftp_package(host):
    pkg = host.package('tftp-server')

    assert pkg.is_installed


def test_tftp_boot_package(host):
    pkg = host.package('syslinux-tftpboot')

    assert pkg.is_installed


def test_tftp_socket(host):
    srv = host.service('tftp.socket')

    assert srv.is_running
    assert srv.is_enabled


def test_tftboot_dir(host):
    dir = host.file('/var/lib/tftpboot')

    assert dir.is_directory


def test_syslinux_files(host):
    file = host.file('/var/lib/tftpboot/pxelinux.0')

    assert file.exists


def test_syslinux_pxe_file(host):
    file = host.file('/var/lib/tftpboot/pxelinux.cfg/default')

    assert file.exists
