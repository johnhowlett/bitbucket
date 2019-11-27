import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

# test bitbucket installation


def test_properties_file(host):
    properties = host.file("/data/git/shared/bitbucket.properties")
    assert properties.exists
    assert properties.contains("jdbc.user=stashuser")


def test_javaopts_file(host):
    javaopts = host.file("/app/git/latest/bin/_start-webapp.sh")
    assert javaopts.exists
    assert javaopts.contains("dirproxy.mobi.ch")
