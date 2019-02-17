blue_percent = 0.05
silver_percent = 0.07
golden_percent = 0.1
blue_purchase_max = 15_000
silver_purchase_max = 150_000
coefficient = 1000 #бонусы начисляются на каждую 1000 рублей,
                   #соответственно вводится коэффициент для коррекции


def s_m_bonus(full_purchase, last_purchase):
    if full_purchase < blue_purchase_max:
        bonus = (int(last_purchase/coefficient) * blue_percent) * coefficient
    if blue_purchase_max < full_purchase < silver_purchase_max:
        bonus = (int(last_purchase/coefficient) * silver_percent) * coefficient
    if full_purchase > silver_purchase_max:
        bonus = (int(last_purchase/coefficient) * golden_percent) * coefficient
    return bonus

"""
s_m_bonus(10_000, 4_700)
200.0
s_m_bonus(80_000, 1_200)
70.0
s_m_bonus(160_000, 4_600)
400.0
"""