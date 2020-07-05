# arr = [2]
# for i in range(2, 1000000):
#     isPrime = True
#     for j in arr:
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime:
#         arr.append(i)
n = int(input())
arr = [2, 3, 4, 5, 7,
       11, 13, 17, 19, 22,
       23, 27, 29, 31, 37,
       41, 43, 47, 53, 58,
       59, 61, 67, 71, 73,
       79, 83, 85, 89, 94,
       97, 101, 103, 107, 109,
       113, 121, 127, 131, 137,
       139, 149, 151, 157, 163,
       166, 167, 173, 179, 181,
       191, 193, 197, 199, 202,
       211, 223, 227, 229, 233,
       239, 241, 251, 257, 263,
       265, 269, 271, 274, 277,
       281, 283, 293, 307, 311,
       313, 317, 319, 331, 337,
       346, 347, 349, 353, 355,
       359, 367, 373, 378, 379,
       382, 383, 389, 391, 397,
       401, 409, 419, 421, 431,
       433, 438, 439, 443, 449,
       454, 457, 461, 463, 467,
       479, 483, 487, 491, 499,
       503, 509, 517, 521, 523,
       526, 535, 541, 547, 557,
       562, 563, 569, 571, 576,
       577, 587, 588, 593, 599,
       601, 607, 613, 617, 619,
       627, 631, 634, 636, 641,
       643, 645, 647, 648, 653,
       654, 659, 661, 663, 666,
       673, 677, 683, 690, 691,
       701, 706, 709, 719, 727,
       728, 729, 733, 739, 743,
       751, 757, 761, 762, 769,
       773, 778, 787, 797, 809,
       811, 821, 823, 825, 827,
       829, 839, 852, 853, 857,
       859, 861, 863, 877, 881,
       883, 887, 895, 907, 911,
       913, 915, 919, 922, 929,
       937, 941, 947, 953, 958,
       967, 971, 977, 983, 985,
       991, 997, 1009, 1013, 1019,
       1021, 1031, 1033, 1039, 1049,
       1051, 1061, 1063, 1069, 1086,
       1087, 1091, 1093, 1097, 1103,
       1109, 1111, 1117, 1123, 1129,
       1151, 1153, 1163, 1165, 1171,
       1181, 1187, 1193, 1201, 1213,
       1217, 1219, 1223, 1229, 1231,
       1237, 1249, 1255, 1259, 1277,
       1279, 1282, 1283, 1284, 1289,
       1291, 1297, 1301, 1303, 1307,
       1319, 1321, 1327, 1361, 1367,
       1373, 1376, 1381, 1399, 1409,
       1423, 1427, 1429, 1433, 1439,
       1447, 1449, 1451, 1453, 1459,
       1471, 1481, 1483, 1487, 1489,
       1493, 1499, 1507, 1511, 1523,
       1531, 1543, 1549, 1553, 1559,
       1567, 1571, 1579, 1581, 1583,
       1597, 1601, 1607, 1609, 1613,
       1619, 1621, 1626, 1627, 1633,
       1637, 1642, 1657, 1663, 1667,
       1669, 1678, 1693, 1697, 1699,
       1709, 1721, 1723, 1733, 1736,
       1741, 1747, 1753, 1755, 1759,
       1776, 1777, 1783, 1787, 1789,
       1795, 1801, 1811, 1822, 1823,
       1831, 1842, 1847, 1858, 1861,
       1867, 1871, 1872, 1873, 1877,
       1879, 1881, 1889, 1894, 1901,
       1903, 1907, 1908, 1913, 1921,
       1931, 1933, 1935, 1949, 1951,
       1952, 1962, 1966, 1973, 1979,
       1987, 1993, 1997, 1999, 2003,
       2011, 2017, 2027, 2029, 2038,
       2039, 2053, 2063, 2067, 2069,
       2079, 2081, 2083, 2087, 2089,
       2099, 2111, 2113, 2129, 2131,
       2137, 2141, 2143, 2153, 2155,
       2161, 2173, 2179, 2182, 2203,
       2207, 2213, 2218, 2221, 2227,
       2237, 2239, 2243, 2251, 2265,
       2267, 2269, 2273, 2281, 2286,
       2287, 2293, 2297, 2309, 2311,
       2326, 2333, 2339, 2341, 2347,
       2351, 2357, 2362, 2366, 2371,
       2373, 2377, 2381, 2383, 2389,
       2393, 2399, 2409, 2411, 2417,
       2423, 2434, 2437, 2441, 2447,
       2459, 2461, 2467, 2473, 2475,
       2477, 2484, 2503, 2515, 2521,
       2531, 2539, 2543, 2549, 2551,
       2556, 2557, 2576, 2578, 2579,
       2583, 2591, 2593, 2605, 2609,
       2614, 2617, 2621, 2633, 2647,
       2657, 2659, 2663, 2671, 2677,
       2679, 2683, 2687, 2688, 2689,
       2693, 2699, 2707, 2711, 2713,
       2719, 2722, 2729, 2731, 2741,
       2745, 2749, 2751, 2753, 2767,
       2777, 2785, 2789, 2791, 2797,
       2801, 2803, 2819, 2833, 2837,
       2839, 2843, 2851, 2857, 2861,
       2879, 2887, 2888, 2897, 2902,
       2903, 2909, 2911, 2917, 2927,
       2934, 2939, 2944, 2953, 2957,
       2958, 2963, 2964, 2965, 2969,
       2970, 2971, 2974, 2999, 3001,
       3011, 3019, 3023, 3037, 3041,
       3046, 3049, 3061, 3067, 3079,
       3083, 3089, 3091, 3109, 3119,
       3121, 3137, 3138, 3163, 3167,
       3168, 3169, 3174, 3181, 3187,
       3191, 3203, 3209, 3217, 3221,
       3226, 3229, 3246, 3251, 3253,
       3257, 3258, 3259, 3271, 3294,
       3299, 3301, 3307, 3313, 3319,
       3323, 3329, 3331, 3343, 3345,
       3347, 3359, 3361, 3366, 3371,
       3373, 3389, 3390, 3391, 3407,
       3413, 3433, 3442, 3449, 3457,
       3461, 3463, 3467, 3469, 3491,
       3499, 3505, 3511, 3517, 3527,
       3529, 3533, 3539, 3541, 3547,
       3557, 3559, 3564, 3571, 3581,
       3583, 3593, 3595, 3607, 3613,
       3615, 3617, 3622, 3623, 3631,
       3637, 3643, 3649, 3659, 3663,
       3671, 3673, 3677, 3690, 3691,
       3694, 3697, 3701, 3709, 3719,
       3727, 3733, 3739, 3761, 3767,
       3769, 3779, 3793, 3797, 3802,
       3803, 3821, 3823, 3833, 3847,
       3851, 3852, 3853, 3863, 3864,
       3865, 3877, 3881, 3889, 3907,
       3911, 3917, 3919, 3923, 3929,
       3930, 3931, 3943, 3946, 3947,
       3967, 3973, 3989, 4001, 4003,
       4007, 4013, 4019, 4021, 4027,
       4049, 4051, 4054, 4057, 4073,
       4079, 4091, 4093, 4099, 4111,
       4126, 4127, 4129, 4133, 4139,
       4153, 4157, 4159, 4162, 4173,
       4177, 4185, 4189, 4191, 4198,
       4201, 4209, 4211, 4217, 4219,
       4229, 4231, 4241, 4243, 4253,
       4259, 4261, 4271, 4273, 4279,
       4283, 4289, 4297, 4306, 4327,
       4337, 4339, 4349, 4357, 4363,
       4369, 4373, 4391, 4397, 4409,
       4414, 4421, 4423, 4428, 4441,
       4447, 4451, 4457, 4463, 4464,
       4472, 4481, 4483, 4493, 4507,
       4513, 4517, 4519, 4523, 4547,
       4549, 4557, 4561, 4567, 4583,
       4591, 4592, 4594, 4597, 4603,
       4621, 4637, 4639, 4643, 4649,
       4651, 4657, 4663, 4673, 4679,
       4691, 4702, 4703, 4721, 4723,
       4729, 4733, 4743, 4751, 4759,
       4765, 4783, 4787, 4788, 4789,
       4793, 4794, 4799, 4801, 4813,
       4817, 4831, 4832, 4855, 4861,
       4871, 4877, 4880, 4889, 4903,
       4909, 4918, 4919, 4931, 4933,
       4937, 4943, 4951, 4954, 4957,
       4959, 4960, 4967, 4969, 4973,
       4974, 4981, 4987, 4993, 4999,
       5003, 5009, 5011, 5021, 5023,
       5039, 5051, 5059, 5062, 5071,
       5077, 5081, 5087, 5088, 5098,
       5099, 5101, 5107, 5113, 5119,
       5147, 5153, 5167, 5171, 5172,
       5179, 5189, 5197, 5209, 5227,
       5231, 5233, 5237, 5242, 5248,
       5253, 5261, 5269, 5273, 5279,
       5281, 5297, 5298, 5303, 5305,
       5309, 5323, 5333, 5347, 5351,
       5381, 5386, 5387, 5388, 5393,
       5397, 5399, 5407, 5413, 5417,
       5419, 5422, 5431, 5437, 5441,
       5443, 5449, 5458, 5471, 5477,
       5479, 5483, 5485, 5501, 5503,
       5507, 5519, 5521, 5526, 5527,
       5531, 5539, 5557, 5563, 5569,
       5573, 5581, 5591, 5602, 5623,
       5638, 5639, 5641, 5642, 5647,
       5651, 5653, 5657, 5659, 5669,
       5674, 5683, 5689, 5693, 5701,
       5711, 5717, 5737, 5741, 5743,
       5749, 5772, 5779, 5783, 5791,
       5801, 5807, 5813, 5818, 5821,
       5827, 5839, 5843, 5849, 5851,
       5854, 5857, 5861, 5867, 5869,
       5874, 5879, 5881, 5897, 5903,
       5915, 5923, 5926, 5927, 5935,
       5936, 5939, 5946, 5953, 5981,
       5987, 5998, 6007, 6011, 6029,
       6036, 6037, 6043, 6047, 6053,
       6054, 6067, 6073, 6079, 6084,
       6089, 6091, 6096, 6101, 6113,
       6115, 6121, 6131, 6133, 6143,
       6151, 6163, 6171, 6173, 6178,
       6187, 6188, 6197, 6199, 6203,
       6211, 6217, 6221, 6229, 6247,
       6252, 6257, 6259, 6263, 6269,
       6271, 6277, 6287, 6295, 6299,
       6301, 6311, 6315, 6317, 6323,
       6329, 6337, 6343, 6344, 6353,
       6359, 6361, 6367, 6373, 6379,
       6385, 6389, 6397, 6421, 6427,
       6439, 6449, 6451, 6457, 6469,
       6473, 6481, 6491, 6502, 6521,
       6529, 6531, 6547, 6551, 6553,
       6563, 6567, 6569, 6571, 6577,
       6581, 6583, 6585, 6599, 6603,
       6607, 6619, 6637, 6653, 6659,
       6661, 6673, 6679, 6684, 6689,
       6691, 6693, 6701, 6702, 6703,
       6709, 6718, 6719, 6733, 6737,
       6760, 6761, 6763, 6779, 6781,
       6791, 6793, 6803, 6816, 6823,
       6827, 6829, 6833, 6835, 6841,
       6855, 6857, 6863, 6869, 6871,
       6880, 6883, 6899, 6907, 6911,
       6917, 6934, 6947, 6949, 6959,
       6961, 6967, 6971, 6977, 6981,
       6983, 6991, 6997, 7001, 7013,
       7019, 7026, 7027, 7039, 7043,
       7051, 7057, 7062, 7068, 7069,
       7078, 7079, 7089, 7103, 7109,
       7119, 7121, 7127, 7129, 7136,
       7151, 7159, 7177, 7186, 7187,
       7193, 7195, 7207, 7211, 7213,
       7219, 7227, 7229, 7237, 7243,
       7247, 7249, 7253, 7283, 7287,
       7297, 7307, 7309, 7321, 7331,
       7333, 7339, 7349, 7351, 7369,
       7393, 7402, 7411, 7417, 7433,
       7438, 7447, 7451, 7457, 7459,
       7465, 7477, 7481, 7487, 7489,
       7499, 7503, 7507, 7517, 7523,
       7529, 7537, 7541, 7547, 7549,
       7559, 7561, 7573, 7577, 7583,
       7589, 7591, 7603, 7607, 7621,
       7627, 7639, 7643, 7649, 7669,
       7673, 7674, 7681, 7683, 7687,
       7691, 7695, 7699, 7703, 7712,
       7717, 7723, 7726, 7727, 7741,
       7753, 7757, 7759, 7762, 7764,
       7782, 7784, 7789, 7793, 7809,
       7817, 7823, 7824, 7829, 7834,
       7841, 7853, 7867, 7873, 7877,
       7879, 7883, 7901, 7907, 7915,
       7919, 7927, 7933, 7937, 7949,
       7951, 7952, 7963, 7978, 7993,
       8005, 8009, 8011, 8014, 8017,
       8023, 8039, 8053, 8059, 8069,
       8073, 8077, 8081, 8087, 8089,
       8093, 8095, 8101, 8111, 8117,
       8123, 8147, 8149, 8154, 8158,
       8161, 8167, 8171, 8179, 8185,
       8191, 8196, 8209, 8219, 8221,
       8231, 8233, 8237, 8243, 8253,
       8257, 8263, 8269, 8273, 8277,
       8287, 8291, 8293, 8297, 8307,
       8311, 8317, 8329, 8347, 8353,
       8363, 8369, 8372, 8377, 8387,
       8389, 8412, 8419, 8421, 8423,
       8429, 8431, 8443, 8447, 8461,
       8466, 8467, 8501, 8513, 8518,
       8521, 8527, 8537, 8539, 8543,
       8545, 8563, 8568, 8573, 8581,
       8597, 8599, 8609, 8623, 8627,
       8628, 8629, 8641, 8647, 8653,
       8663, 8669, 8677, 8680, 8681,
       8689, 8693, 8699, 8707, 8713,
       8719, 8731, 8736, 8737, 8741,
       8747, 8753, 8754, 8761, 8766,
       8779, 8783, 8790, 8792, 8803,
       8807, 8819, 8821, 8831, 8837,
       8839, 8849, 8851, 8861, 8863,
       8864, 8867, 8874, 8883, 8887,
       8893, 8901, 8914, 8923, 8929,
       8933, 8941, 8951, 8963, 8969,
       8971, 8999, 9001, 9007, 9011,
       9013, 9015, 9029, 9031, 9036,
       9041, 9043, 9049, 9059, 9067,
       9091, 9094, 9103, 9109, 9127,
       9133, 9137, 9151, 9157, 9161,
       9166, 9173, 9181, 9184, 9187,
       9193, 9199, 9203, 9209, 9221,
       9227, 9229, 9239, 9241, 9257,
       9274, 9276, 9277, 9281, 9283,
       9285, 9293, 9294, 9296, 9301,
       9311, 9319, 9323, 9330, 9337,
       9341, 9343, 9346, 9349, 9355,
       9371, 9377, 9382, 9386, 9387,
       9391, 9396, 9397, 9403, 9413,
       9414, 9419, 9421, 9427, 9431,
       9433, 9437, 9439, 9461, 9463,
       9467, 9473, 9479, 9483, 9491,
       9497, 9511, 9521, 9522, 9533,
       9535, 9539, 9547, 9551, 9571,
       9587, 9598, 9601, 9613, 9619,
       9623, 9629, 9631, 9633, 9634,
       9639, 9643, 9648, 9649, 9657,
       9661, 9677, 9679, 9684, 9689,
       9697, 9708, 9717, 9719, 9721,
       9733, 9735, 9739, 9742, 9743,
       9749, 9760, 9767, 9769, 9778,
       9781, 9787, 9791, 9803, 9811,
       9817, 9829, 9833, 9839, 9840,
       9843, 9849, 9851, 9857, 9859,
       9861, 9871, 9880, 9883, 9887,
       9895, 9901, 9907, 9923, 9924,
       9929, 9931, 9941, 9942, 9949,
       9967, 9968, 9973, 9975, 9985,
       ]
for i in range(n):
    tmp = int(input())
    num = tmp
    res = []
    if tmp in arr:
        print(1)
    else:
        print(0)
    # while tmp != 1:
    #     for j in arr:
    #         if tmp % j == 0:
    #             res.append(j)
    #             tmp = tmp // j
    #             break
    # sum1 = 0
    # for j in str(num):
    #     sum1 += int(j)
    # sum2 = 0
    # for j in res:
    #     for k in str(j):
    #         sum2 += int(k)
    # if sum1 == sum2:
    #     print(1)
    # else:
    #     print(0)