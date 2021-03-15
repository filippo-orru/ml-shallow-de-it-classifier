from numpy import array


def get_parameters():
    return {
        0: {
            'W1':
            array([[
                -2.99551029e-01, 9.11458725e-01, 1.48344397e-01,
                8.11045466e-01, -1.44307842e+00, -3.59899313e+00,
                8.18251142e+00, -6.33475984e+00, 4.98147640e+00,
                -5.94391153e+00, -2.32398553e+00, -7.75457699e-01,
                -3.78332008e-01, -4.41247651e-01, -3.07362044e-01,
                -2.40401548e-01, -1.74946750e-01, -2.95532528e-02,
                -2.02663615e-01, -2.48374725e-01, -2.89540574e-02,
                8.70991432e-02, 5.76550503e-02, 4.42067254e-02, 3.37718777e-02,
                3.10134323e-02, 3.28479970e-02, 2.28754496e-02, 2.36360750e-02
            ],
                   [
                       7.01912315e-01, -1.84714402e-01, 2.24703978e-01,
                       -4.41478603e-02, 4.21132295e-01, -4.97015933e-01,
                       -8.47967472e-01, 2.21863328e-01, -1.54798208e+00,
                       7.73519160e-01, -6.00301702e-01, 5.58653625e-02,
                       1.87099547e-01, -1.41985779e-01, 2.97357669e-01,
                       -1.41524362e-01, 1.36610614e-01, 5.34063144e-02,
                       -1.97353448e-02, -1.49179835e-01, 2.70477700e-02,
                       1.19702718e-01, 6.73982030e-02, 7.00537815e-02,
                       2.28212323e-02, 2.55006686e-02, 3.76589511e-02,
                       1.56917249e-02, 2.90863087e-02
                   ],
                   [
                       7.95037404e-01, -9.26386997e-01, 2.13937943e-03,
                       -1.19826938e+00, 1.07135345e+00, -1.55825546e+00,
                       4.05341490e+00, 1.83655923e+00, -1.64757967e+00,
                       -1.47580483e+00, -1.40507192e+00, 1.59910430e-01,
                       6.69621652e-02, -4.92993595e-01, 7.22414601e-01,
                       -6.38177074e-01, 4.60455948e-01, 1.03163835e-01,
                       -2.49252287e-01, -6.36790379e-01, 3.56559259e-02,
                       3.37093128e-01, 2.35346707e-01, 2.44464882e-01,
                       9.09832632e-02, 8.67915238e-02, 8.32937679e-02,
                       6.35285129e-02, 9.79407399e-02
                   ],
                   [
                       -8.95696035e-01, 4.88921305e-02, -3.21582301e-01,
                       -2.23698325e-01, -3.70817106e-01, 9.11623595e-01,
                       2.06073512e+00, -8.22052909e-01, 2.13218727e+00,
                       -1.12856318e+00, 8.70899709e-01, 9.00920482e-02,
                       -1.77435571e-01, 2.45509214e-01, -1.98251980e-01,
                       1.86778522e-01, -1.45405755e-01, -2.98678481e-02,
                       4.93102156e-02, 1.42235312e-01, -8.52075877e-03,
                       -9.56118777e-02, -6.77416944e-02, -6.72882557e-02,
                       -2.69167109e-02, -2.81659189e-02, -2.84082201e-02,
                       -2.26946741e-02, -2.68779153e-02
                   ],
                   [
                       3.49706308e-01, -7.47518775e-01, -3.22294170e-01,
                       2.34101174e+00, -8.18104369e+00, 8.08746014e+00,
                       -4.67632210e+00, -8.73749678e-01, 3.66771361e+00,
                       -4.19791245e+00, 4.74168832e+00, -2.95519420e+00,
                       1.25723294e+00, -3.97173428e-01, 9.17546077e-01,
                       -1.05968155e+00, 4.53510139e-01, 1.45379917e+00,
                       1.21860950e+00, -6.60676447e-01, 3.67997464e-01,
                       1.14721454e+00, 9.51529932e-01, 9.46992147e-01,
                       5.21893274e-01, 4.78962757e-01, 5.50396933e-01,
                       4.80508845e-01, 5.78806267e-01
                   ],
                   [
                       -4.19808055e-01, 6.72699907e-01, -8.00445328e-01,
                       -1.16052450e+00, 7.44680254e-02, 5.90582465e+00,
                       -4.09963074e+00, 8.24241504e+00, -7.93840848e+00,
                       4.76373042e+00, 1.24515520e+00, -3.01795501e+00,
                       1.76604278e+00, -5.25115993e-01, -8.59161901e-01,
                       7.27889687e-01, -6.11789814e-02, 1.31791214e-01,
                       -3.11539078e-01, 2.43910650e-01, -4.75315705e-01,
                       -9.00522211e-01, -7.38221580e-01, -7.39616551e-01,
                       -1.72546440e-01, -1.47029545e-01, -2.10658198e-01,
                       -1.65391340e-01, -1.76364193e-01
                   ],
                   [
                       2.03217843e-02, 1.01445893e+00, 5.49808546e-01,
                       -4.43983166e+00, 3.71081813e+00, -5.96542865e+00,
                       7.00295651e+00, 3.68402640e+00, -7.35640659e-02,
                       -7.32137713e-01, -2.08979332e-01, 7.62768964e-01,
                       3.81374886e-01, -4.26659691e-01, 1.99579643e-01,
                       -5.19812341e-01, -7.20201532e-01, -4.81232051e-01,
                       -1.10587017e+00, -1.68513299e+00, -3.36501574e-01,
                       2.26885954e-01, 1.31585548e-01, 1.38125899e-01,
                       6.54171235e-02, 4.61861126e-02, 4.66371830e-02,
                       4.72511653e-02, 5.46254875e-02
                   ],
                   [
                       -8.39381164e-01, 1.12674900e-01, -3.01499203e-01,
                       -1.49827443e-01, -3.92808032e-01, 7.16951944e-01,
                       1.60362960e+00, -5.41201863e-01, 1.96153061e+00,
                       -1.00330792e+00, 7.87393232e-01, 3.51337235e-02,
                       -1.60003595e-01, 1.91831275e-01, -2.31460756e-01,
                       1.94531430e-01, -1.58701663e-01, -4.01304380e-02,
                       4.19088441e-02, 1.30537717e-01, -2.67165175e-02,
                       -9.66216355e-02, -7.97775913e-02, -5.73769253e-02,
                       -1.89778420e-02, -9.51273570e-03, -1.49191459e-02,
                       -1.73078682e-02, -1.33458128e-02
                   ]]),
            'W2':
            array([[
                2.66343496, -0.15518902, -0.92974708, 0.5282119, -2.60162345,
                2.67259062, -1.71360673, 0.33266272
            ]]),
            'b1':
            array([[1.47731312], [0.09466858], [-0.75553994], [-0.24901944],
                   [-1.53796658], [-0.79245765], [-0.93634914], [-0.2035799]]),
            'b2':
            array([[-1.96273007]])
        },
        1: {
            'W1':
            array([[
                -3.41415751e-01, 2.21761893e-01, -3.93197365e-01,
                4.37367960e-01, -2.64174617e-01, 7.56852845e-01,
                -1.29426882e+00, -6.97614602e-02, 8.12357846e-02,
                -5.96720786e-01, 2.79051910e-02, -4.00773603e-01,
                -3.78927576e-01, -1.48158215e-01, -3.46021782e-01,
                2.04618940e-02, -2.29237440e-01, -1.78730944e-02,
                1.92492874e-01, 1.97810734e-01, 1.36194373e-01, 8.88729628e-02,
                -2.19449190e-01, -1.17958494e-01, -3.99682246e-02,
                -3.45950160e-02, -5.44754946e-02, -2.84020867e-02,
                -3.61557220e-02
            ],
                   [
                       7.26839963e-01, 5.36179675e-01, 6.24553239e-01,
                       -4.40785797e-01, -1.40751960e+00, 7.69766639e+00,
                       -1.10675081e+01, -5.49320640e+00, 1.12685548e+00,
                       9.92636381e-01, 4.88368144e-01, -3.16588245e+00,
                       4.32712911e-01, 8.58557415e-01, -2.95105031e-01,
                       1.31578768e-01, -1.77153324e-01, 1.71394437e-02,
                       2.61522257e-01, 2.83047711e-01, 1.60189678e-01,
                       1.12837060e-01, -2.06283956e-01, -1.22851312e-01,
                       -2.89232174e-02, -4.96866395e-02, -5.66414718e-02,
                       -3.21746628e-02, -1.52500535e-02
                   ],
                   [
                       1.05250487e+00, -1.20335134e+00, -2.55907168e-01,
                       2.16076431e+00, -6.98882202e+00, 6.74225117e+00,
                       -2.30186413e+00, -1.01321046e+01, 1.31908276e+01,
                       -1.16142362e+01, 1.16355686e+01, -4.38754049e+00,
                       -1.18276883e+00, 1.99084656e+00, 1.75780261e+00,
                       -2.99240760e+00, 2.85295829e+00, 6.82384419e-01,
                       -8.08288864e-01, -7.97851372e-01, -5.94772431e-01,
                       -4.04062501e-01, 7.83291704e-01, 4.68932670e-01,
                       2.02332767e-01, 1.82102511e-01, 2.14172086e-01,
                       2.00515116e-01, 2.10521891e-01
                   ],
                   [
                       2.83207172e-01, 1.08268624e+00, 1.06725425e+00,
                       -1.16573909e+00, 4.92295335e-01, -9.50260604e-01,
                       -8.04755826e+00, 5.32283831e+00, -3.89431760e+00,
                       5.03842768e-01, -8.78688293e-01, 2.93079480e-01,
                       -8.52708093e-02, -1.11042534e+00, 3.72435424e-01,
                       -4.12399473e-01, 2.65076886e-01, -1.16565385e-01,
                       -4.95984082e-01, -4.76270148e-01, -2.34490864e-01,
                       -1.62341636e-01, 3.26739659e-01, 2.00725490e-01,
                       5.40398821e-02, 6.51297249e-02, 7.11113697e-02,
                       6.49973062e-02, 7.77481685e-02
                   ],
                   [
                       1.85655618e-01, -2.18241027e-01, 8.57072535e-02,
                       -2.12243101e-01, -2.27789334e-01, -2.44946352e-01,
                       1.75749680e+00, -1.29089361e-01, 5.65370065e-01,
                       7.48794205e-01, -6.77271954e-02, 3.35401964e-01,
                       3.47316363e-01, 2.83894303e-01, 2.54728765e-01,
                       6.68856020e-02, 1.71292190e-01, 3.05720496e-02,
                       -8.88394286e-02, -1.03370682e-01, -6.48303877e-02,
                       -2.70846312e-02, 1.46747630e-01, 5.98068175e-02,
                       3.10533412e-02, 4.00240376e-02, 3.88102233e-02,
                       4.38310964e-02, 2.74541184e-02
                   ],
                   [
                       -4.09609216e-01, 2.04814979e-01, -4.31991801e-01,
                       5.18346245e-01, -3.64490616e-01, 8.46706482e-01,
                       -1.10184239e+00, -1.55394360e-01, 3.04838099e-01,
                       -4.74681425e-01, 6.18888002e-02, -3.95653788e-01,
                       -3.56036596e-01, -1.09341796e-01, -3.59802297e-01,
                       5.03716299e-02, -2.52609719e-01, 9.74468789e-05,
                       2.19063763e-01, 2.19110108e-01, 1.39127951e-01,
                       8.99463550e-02, -2.17941994e-01, -1.24423507e-01,
                       -5.48042178e-02, -1.95662665e-02, -4.87374623e-02,
                       -3.87257236e-02, -5.33308310e-02
                   ],
                   [
                       3.20332251e+00, -8.43225410e-01, 1.48430649e+00,
                       -9.34965382e-01, 2.89884748e-01, 4.35165248e+00,
                       -9.76102792e+00, -3.21559651e+00, -5.95358306e+00,
                       5.96629831e+00, -4.46379350e+00, 2.90255990e+00,
                       4.46514795e+00, 1.49518579e+00, 1.23198256e+00,
                       -2.31121484e-02, 4.09798020e-01, -1.73874375e-01,
                       -9.52869171e-01, -9.24865749e-01, -8.87845737e-01,
                       -7.79101864e-01, 7.09907612e-01, 5.14928265e-01,
                       8.93306645e-02, 7.96336304e-02, 6.69268521e-02,
                       6.13321357e-02, 8.42694260e-02
                   ],
                   [
                       -6.07291468e-01, 3.73163857e-01, -4.95587966e-01,
                       8.31038654e-01, -7.02036849e-01, 7.17529690e-01,
                       -1.09458750e+00, -3.04832577e-01, 6.99896809e-01,
                       8.41221933e-02, 3.03284966e-01, -2.70570720e-01,
                       -3.61719329e-02, 6.50629645e-01, -3.66897769e-01,
                       2.02815420e-01, -2.08098858e-01, 5.26174921e-02,
                       3.45273353e-01, 3.18365149e-01, 1.63220466e-01,
                       1.28573222e-01, -2.64673916e-01, -1.58178981e-01,
                       -4.98395115e-02, -5.15273703e-02, -4.34630264e-02,
                       -6.45747748e-02, -5.46176790e-02
                   ],
                   [
                       -9.58112967e-01, -2.82853167e-01, -1.20973833e+00,
                       3.74006023e+00, -3.52718825e+00, 6.95226974e+00,
                       -5.84495992e+00, 1.91737829e+00, 6.74231093e+00,
                       -1.03999545e+01, 5.92908487e+00, -6.24612735e+00,
                       4.69293610e+00, 7.17190653e-01, -2.82365794e+00,
                       -7.60633268e-01, -1.09032375e+00, 6.75444834e-01,
                       1.68240261e+00, 1.71559188e+00, -2.89519977e-02,
                       -1.23766597e-01, -1.04459202e+00, -3.15626921e-01,
                       -9.15100928e-02, -1.01048659e-01, -1.13052086e-01,
                       -9.88815644e-02, -1.13329937e-01
                   ]]),
            'W2':
            array([[
                0.05030393, 4.36387942, -2.39745726, -3.24684335, -0.08878033,
                0.02782287, -1.73634453, 0.18258072, 2.13473984
            ]]),
            'b1':
            array([[0.46373631], [1.55554204], [-1.27848578], [1.40889477],
                   [-0.50511337], [0.39851207], [4.13725098], [0.37113929],
                   [2.08734345]]),
            'b2':
            array([[-1.91091268]])
        },
        2: {'W1': array([[-1.25626949e+00, -2.34418490e+00,  4.37364924e+00,
         2.76285848e+00,  1.76784784e+00,  7.81759353e-01,
         8.11153294e-01,  5.44246695e-01, -6.59642871e-02,
         3.46151684e-01,  5.08531280e-01,  4.00793195e-01,
         1.31256039e-02,  2.63702655e-02,  2.79179011e-01,
        -6.98321801e-02,  6.95048210e-02,  1.11027705e-01,
         8.80448331e-02,  5.26689411e-02,  7.66661783e-02,
         1.06997601e-01,  8.58057432e-02,  6.13598706e-02,
         2.77904139e-02,  2.38476191e-02,  2.27156701e-02,
         1.33558603e-02,  2.75064403e-02],
       [-7.68220854e-02, -8.85451986e-01,  3.08924156e-01,
         4.14417246e+00, -4.62800462e+00,  2.47125239e+00,
         6.29226659e+00, -8.65917574e+00, -6.18089878e+00,
        -1.55324095e+00, -5.50076443e-01, -5.99970268e-01,
        -1.55169364e-01, -8.02655148e-02, -2.16803807e-01,
         5.38662574e-02, -8.40458719e-02, -8.83770859e-02,
        -7.33062167e-02, -2.89497247e-02, -8.17706293e-02,
        -9.35544910e-02, -7.08863493e-02, -4.75358343e-02,
        -3.09553725e-02, -8.55673835e-03, -7.70044273e-03,
        -1.61912772e-02, -3.39957391e-02],
       [-9.00146691e-01,  1.35942658e+00, -4.18839119e-04,
        -3.35809777e+00,  8.24812850e+00, -8.08176479e+00,
         1.56571461e+01, -1.44324148e+01,  9.49848124e+00,
        -6.76293553e+00,  1.94521508e+00, -1.17359565e+00,
        -5.62577356e-01,  1.80911472e+00, -2.89483186e+00,
         1.20053825e+00, -1.22607758e+00, -7.64733169e-01,
         2.91561919e-02, -6.07563898e-02, -9.26947811e-01,
        -1.25223661e+00, -9.96077950e-01, -6.31372589e-01,
        -9.51074601e-02, -7.59539442e-02, -7.68055382e-02,
        -6.78818246e-02, -9.68588861e-02],
       [-1.76806147e+00, -3.53687637e-02,  1.42500507e+00,
         2.57617537e+00, -5.93787243e-01, -1.06958756e+01,
        -2.25256818e-03,  6.68942032e+00,  1.90901833e+00,
         1.10117147e+01, -1.01735245e+01,  2.36179829e+00,
         1.26430603e+00,  2.07782120e-01,  1.02354086e+00,
         8.83059338e-01, -6.14822144e-01, -4.31955181e-01,
        -5.64600387e-01, -2.86813494e-01, -3.31034362e-01,
        -3.83055331e-01, -4.69111780e-01, -5.54083073e-01,
         1.58812379e-02, -7.43652881e-04,  2.84384427e-03,
         1.26689407e-03, -6.44972300e-03],
       [ 8.42252832e-01,  1.65771675e+00,  1.46349335e-01,
        -7.75029257e-01, -2.41982419e-01,  9.52588246e+00,
        -6.79751471e+00,  1.35893241e+01, -1.47388939e+01,
        -5.41718995e+00,  3.20552051e+00,  1.05091290e+00,
        -5.47302154e-01,  2.46605974e+00, -2.53894036e+00,
        -1.73787450e+00, -1.47956987e+00, -2.24854835e-01,
        -1.28472508e-01, -4.97315002e-02, -1.88866549e-01,
        -3.31889802e-01, -3.41519194e-01, -2.25328480e-01,
        -1.62699603e-01, -1.27953758e-01, -1.48728839e-01,
        -1.48547011e-01, -1.62546256e-01],
       [ 3.45658520e+00, -4.17486408e-01,  1.10073670e+00,
        -1.65327496e+00,  7.39743614e-01, -3.40911784e+00,
        -7.86829354e-01, -6.85203806e-01, -9.25015177e+00,
         8.31634328e+00, -5.12799242e+00,  5.13507139e+00,
         4.56695658e-01,  1.78803560e+00, -9.84483774e-01,
        -9.36546005e-01, -1.29346739e+00,  1.23049697e-01,
        -4.96272661e-01, -5.62696176e-01,  1.00276960e+00,
         1.21722245e+00,  1.04896506e-01,  8.20039226e-02,
         3.12639800e-02, -3.42243278e-03,  2.69832242e-02,
         1.80675391e-02,  5.95897159e-03]]), 'W2': array([[-2.61498756,  2.18827074,  2.28691503,  2.40030213,  2.42959356,
        -2.25734757]]), 'b1': array([[-0.47150053],
       [ 1.34639912],
       [ 2.48160701],
       [-0.32563116],
       [-3.74029629],
       [ 2.45083649]]), 'b2': array([[2.89910664]])}
    }