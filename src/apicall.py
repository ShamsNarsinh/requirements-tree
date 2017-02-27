import requests
api_url = "http://pypi.python.org/pypi/"


def get_data_for_a_package(pkg_name):
    data = requests.get(api_url+pkg_name+"/json").json()
    return data["info"]
