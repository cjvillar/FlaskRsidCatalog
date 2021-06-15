from scripts.litvar_api import litvar_url


def test_litvar_url():
    rs = 'rs121913527'
    test = litvar_url(rs)
    assert test[2].status_code == 200
    assert test[0] == 'rs121913527##'
    assert test[3]['name'] == 'KRAS'

