import pytest
import warnings

def pytest_addoption(parser):
    print("in pytest_addoption...")
    parser.addoption("--mode", action="store", default=None)


warning = False
def pytest_generate_tests(metafunc):
    print('in pytest_generate_test...')
    global warning
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.mode
    if option_value is None:
        if warning:
            warnings.warn("Please provide '--mode=rt|sim|emu' to pytest")
            warning=False
        pytest.skip()
    if 'mode' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("mode", [option_value])

# def pytest_addoption(parser):
#     parser.addoption(
#         "--stringinput",
#         action = "append",
#         default = [],
#         help = "list of stringinputs to pass to test functions",
#     )

# def pytest_generate_t_ests(metafunc):
#     if "stringinput" in metafunc.fixturenames:
#         metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))