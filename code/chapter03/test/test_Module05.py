from nose.tools import with_setup


def setUpModule():
    'called once, before anything else in this module'
    print "In setUpModule()..."


def tearDownModule():
    'called once, after everything else in this module'
    print "In tearDownModule()..."


def setup_function():
    'setup_function(): attached @with_setup decorator'
    print "\nsetup_function()..."


def teardown_function():
    'teardown_function(): attached @with_setup decorator'
    print "teardown_function()..."


def test_case01():
    print "In test_case01()..."


def test_case02():
    print "In test_case02()..."


@with_setup(setup_function, teardown_function)
def test_case03():
    print "In test_case03()..."

