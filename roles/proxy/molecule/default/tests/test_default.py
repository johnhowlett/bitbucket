import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# test to check the proxy setup
def test_proxy_setup_file(host):
    assert host.file("/tmp/proxy_setup.sh").exists
