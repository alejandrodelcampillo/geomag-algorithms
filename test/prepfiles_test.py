from geomagio.pcdcp.PCDCPParser import PCDCPParser
from geomagio.edge import EdgeFactory
from numpy.testing import assert_almost_equal


def test_prepfiles_raw():
    # gather raw example file from magproc
    pcdcp = PCDCPParser()
    pcdcp.parse(open("etc/prepfiles/CMO2020061.raw").read())
    h_data = pcdcp.data["H"]
    e_data = pcdcp.data["E"]
    z_data = pcdcp.data["Z"]
    f_data = pcdcp.data["F"]

    pcdcp.parse(open("etc/prepfiles/CMO202061_prep.raw").read())
    result_h_data = pcdcp.data["H"]
    result_e_data = pcdcp.data["E"]
    result_z_data = pcdcp.data["Z"]
    result_f_data = pcdcp.data["F"]

    assert_almost_equal(result_h_data[0:-1], h_data, decimal=2)
    assert_almost_equal(result_e_data[0:-1], e_data, decimal=2)
    assert_almost_equal(result_z_data[0:-1], z_data, decimal=2)
    assert_almost_equal(result_f_data[0:-1], f_data, decimal=2)


def test_prepfiles_min():
    # gather min example file from magproc
    pcdcp = PCDCPParser()
    pcdcp.parse(open("etc/prepfiles/CMO2020061.min").read())
    h_data = pcdcp.data["H"]
    e_data = pcdcp.data["E"]
    z_data = pcdcp.data["Z"]
    f_data = pcdcp.data["F"]

    pcdcp.parse(open("etc/prepfiles/CMO202061_prep.min").read())
    result_h_data = pcdcp.data["H"]
    result_e_data = pcdcp.data["E"]
    result_z_data = pcdcp.data["Z"]
    result_f_data = pcdcp.data["F"]

    assert_almost_equal(result_h_data[0:-1], h_data, decimal=2)
    assert_almost_equal(result_e_data[0:-1], e_data, decimal=2)
    assert_almost_equal(result_z_data[0:-1], z_data, decimal=2)
    assert_almost_equal(result_f_data[0:-1], f_data, decimal=2)