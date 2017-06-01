# Return the specified data column wise

Consider you have dictionary such that keys are string and values are list like given:

        {‘X’:[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

Convert this dictionary to pandas dataframe so that keys should be column and values should be rows.

Sample Output:


|ROW Index| X | Y | Z |
|---------|----|----|----|
|0  |78  |84  |86
|1  |85  |94  |97
|2  |96  |89  |96
|3  |80  |83  |72
|4  |86  |86  |83
