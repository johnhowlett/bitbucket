import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# test to check the user gitadmin
def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("gitadmin")


def test_group_file(host):
    group = host.file("/etc/group")
    assert group.contains("git")

# test for dependencies git and perl


def test_git_installed(host):
    bitbucket_package_name = _get_git_package_name(
        host.system_info.distribution)
    bitbucket_package = host.package(bitbucket_package_name)
    assert bitbucket_package.is_installed


def test_perl_installed(host):
    perl_package_name = "perl"
    perl_package = host.package(perl_package_name)
    assert perl_package.is_installed


def test_bitbucket_service_enabled(host):
    bitbucket_service_name = _get_git_package_name(
        host.system_info.distribution)
    bitbucket_service = host.service(bitbucket_service_name)
    assert bitbucket_service.is_enabled
    #assert bitbucket_service.is_running


def test_nginx_is_installed(host):
    nginx = host.package("git")
    assert nginx.is_installed
    assert nginx.version.startswith("2.1")


def _get_git_package_name(host_distro):
    return {
        "ubuntu": "git",
        "debian": "git",
        "centos": "git"
    }.get(host_distro, "git")
