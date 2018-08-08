import pandas as pd
import string
"""Lots of dependencies for reading/writing excel files"""

df = pd.read_excel("贷记卡系统 (贷记卡系统)_20180731172617.xlsx")
alpha = string.ascii_letters


def test_chinese(word):
    return word[0] not in alpha


df = df[df["实体"].map(test_chinese)]

df.to_excel('credit_card_system_chinese_test.xlsx')
