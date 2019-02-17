from lib import s_m_bonus


def test_main_sm():
    result = s_m_bonus(10_000, 4_700)

    assert 200.0 == result