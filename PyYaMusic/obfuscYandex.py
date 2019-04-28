__all__ = ['obfuscYandex']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['f', 'r', 't', 'n', 'p', 's', 'a', 'u', 'l', 'c', '_', 'm', 'h', 'd', 'v', 'A', 'e', 'o', 'i'])
    @Js
    def PyJsHoisted_i_(t, n, this, arguments, var=var):
        var = Scope({'t':t, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n'])
        return ((var.get('t')<<var.get('n'))|PyJsBshift(var.get('t'),(Js(32.0)-var.get('n'))))
    PyJsHoisted_i_.func_name = 'i'
    var.put('i', PyJsHoisted_i_)
    @Js
    def PyJsHoisted_e_(t, n, this, arguments, var=var):
        var = Scope({'t':t, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 't', 'n', 'u', 'e', 'o', 'i'])
        pass
        def PyJs_LONG_1_(var=var):
            return ((((Js(2147483648.0)^var.get('u'))^var.get('r'))^var.get('o')) if (var.put('i', (Js(1073741824.0)&var.get('t')))&var.put('e', (Js(1073741824.0)&var.get('n')))) else (((((Js(3221225472.0)^var.get('u'))^var.get('r'))^var.get('o')) if (Js(1073741824.0)&var.get('u')) else (((Js(1073741824.0)^var.get('u'))^var.get('r'))^var.get('o'))) if (var.get('i')|var.get('e')) else ((var.get('u')^var.get('r'))^var.get('o'))))
        return PyJsComma(PyJsComma(PyJsComma(var.put('r', (Js(2147483648.0)&var.get('t'))),var.put('o', (Js(2147483648.0)&var.get('n')))),var.put('u', ((Js(1073741823.0)&var.get('t'))+(Js(1073741823.0)&var.get('n'))))),PyJs_LONG_1_())
    PyJsHoisted_e_.func_name = 'e'
    var.put('e', PyJsHoisted_e_)
    @Js
    def PyJsHoisted_r_(t, n, r, o, u, s, a, this, arguments, var=var):
        var = Scope({'t':t, 'n':n, 'r':r, 'o':o, 'u':u, 's':s, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 't', 'n', 's', 'a', 'u', 'c', 'o'])
        pass
        return var.get('e')(var.get('i')(var.put('t', var.get('e')(var.get('t'), var.get('e')(var.get('e')(((var.put('c', var.get('n'))&var.get('r'))|((~var.get('c'))&var.get('o'))), var.get('u')), var.get('a')))), var.get('s')), var.get('n'))
    PyJsHoisted_r_.func_name = 'r'
    var.put('r', PyJsHoisted_r_)
    @Js
    def PyJsHoisted_o_(t, n, r, o, u, s, a, this, arguments, var=var):
        var = Scope({'t':t, 'n':n, 'r':r, 'o':o, 'u':u, 's':s, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 't', 'n', 's', 'a', 'u', 'c', 'o'])
        pass
        return var.get('e')(var.get('i')(var.put('t', var.get('e')(var.get('t'), var.get('e')(var.get('e')(((var.get('n')&var.put('c', var.get('o')))|(var.get('r')&(~var.get('c')))), var.get('u')), var.get('a')))), var.get('s')), var.get('n'))
    PyJsHoisted_o_.func_name = 'o'
    var.put('o', PyJsHoisted_o_)
    @Js
    def PyJsHoisted_u_(t, n, r, o, u, s, a, this, arguments, var=var):
        var = Scope({'t':t, 'n':n, 'r':r, 'o':o, 'u':u, 's':s, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 't', 'n', 's', 'a', 'u', 'o'])
        return var.get('e')(var.get('i')(var.put('t', var.get('e')(var.get('t'), var.get('e')(var.get('e')(((var.get('n')^var.get('r'))^var.get('o')), var.get('u')), var.get('a')))), var.get('s')), var.get('n'))
    PyJsHoisted_u_.func_name = 'u'
    var.put('u', PyJsHoisted_u_)
    @Js
    def PyJsHoisted_s_(t, n, r, o, u, s, a, this, arguments, var=var):
        var = Scope({'t':t, 'n':n, 'r':r, 'o':o, 'u':u, 's':s, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 't', 'n', 's', 'a', 'u', 'o'])
        return var.get('e')(var.get('i')(var.put('t', var.get('e')(var.get('t'), var.get('e')(var.get('e')((var.get('r')^(var.get('n')|(~var.get('o')))), var.get('u')), var.get('a')))), var.get('s')), var.get('n'))
    PyJsHoisted_s_.func_name = 's'
    var.put('s', PyJsHoisted_s_)
    @Js
    def PyJsHoisted_a_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'n', 'i', 't'])
        var.put('i', Js(''))
        var.put('e', Js(''))
        #for JS loop
        var.put('n', Js(0.0))
        while (var.get('n')<=Js(3.0)):
            try:
                var.put('i', var.put('e', (Js('0')+(PyJsBshift(var.get('t'),(Js(8.0)*var.get('n')))&Js(255.0)).callprop('toString', Js(16.0)))).callprop('substr', (var.get('e').get('length')-Js(2.0)), Js(2.0)), '+')
            finally:
                    (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
        return var.get('i')
    PyJsHoisted_a_.func_name = 'a'
    var.put('a', PyJsHoisted_a_)
    var.put('n', var.get('String').get('fromCharCode'))
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    var.put('m', var.get('Array')())
    #for JS loop
    @Js
    def PyJs_anonymous_2_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 't', 'i'])
        def PyJs_LONG_4_(var=var):
            def PyJs_LONG_3_(var=var):
                return (((((((((var.get('n')(Js(88.0))+var.get('n')((Js(39523855.0)/Js(556674.0))))+var.get('n')((Js(47450778.0)/Js(578668.0))))+var.get('n')((Js(82156899.0)/Js(760712.0))))+var.get('n')((Js(5026300.0)/Js(76156.0))))+var.get('n')((Js(26011178.0)/Js(298979.0))))+var.get('n')((Js(28319886.0)/Js(496840.0))))+var.get('n')((Js(23477867.0)/Js(335398.0))))+var.get('n')((Js(21650560.0)/Js(246029.0))))+var.get('n')((Js(22521465.0)/Js(208532.0))))
            return (((((((((PyJs_LONG_3_()+var.get('n')((Js(16067393.0)/Js(159083.0))))+var.get('n')((Js(94458862.0)/Js(882793.0))))+var.get('n')((Js(67654429.0)/Js(656839.0))))+var.get('n')(Js(98.000015474072)))+var.get('n')((Js(11508494.0)/Js(143856.0))))+var.get('n')((Js(30221073.0)/Js(265097.0))))+var.get('n')((Js(18712908.0)/Js(228206.0))))+var.get('n')((Js(21423113.0)/Js(297543.0))))+var.get('n')((Js(65168784.0)/Js(556998.0))))
        var.put('t', ((((PyJs_LONG_4_()+var.get('n')((Js(48924535.0)/Js(589452.0))))+var.get('n')((Js(61018985.0)/Js(581133.0))))+var.get('n')((Js(10644616.0)/Js(163763.0))))+var.get('t').callprop('replace', JsRegExp('/\\r\\n/g'), Js('\n'))))
        #for JS loop
        var.put('i', Js(''))
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('t').get('length')):
            try:
                var.put('r', var.get('t').callprop('charCodeAt', var.get('e')))
                def PyJs_LONG_5_(var=var):
                    return (PyJsComma(var.put('i', var.get('n')(((var.get('r')>>Js(6.0))|Js(192.0))), '+'),var.put('i', var.get('n')(((Js(63.0)&var.get('r'))|Js(128.0))), '+')) if ((var.get('r')>Js(127.0)) and (var.get('r')<Js(2048.0))) else PyJsComma(PyJsComma(var.put('i', var.get('n')(((var.get('r')>>Js(12.0))|Js(224.0))), '+'),var.put('i', var.get('n')((((var.get('r')>>Js(6.0))&Js(63.0))|Js(128.0))), '+')),var.put('i', var.get('n')(((Js(63.0)&var.get('r'))|Js(128.0))), '+')))
                (var.put('i', var.get('n')(var.get('r')), '+') if (var.get('r')<Js(128.0)) else PyJs_LONG_5_())
            finally:
                    (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
        return var.get('i')
    PyJs_anonymous_2_._set_name('anonymous')
    @Js
    def PyJs_anonymous_6_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 't', 'n', 's', 'u', 'e', 'o', 'i'])
        #for JS loop
        var.put('i', var.get('t').get('length'))
        var.put('e', (var.get('i')+Js(8.0)))
        var.put('r', (Js(16.0)*(((var.get('e')-(var.get('e')%Js(64.0)))/Js(64.0))+Js(1.0))))
        var.put('o', var.get('Array')((var.get('r')-Js(1.0))))
        var.put('u', Js(0.0))
        var.put('s', Js(0.0))
        while (var.get('s')<var.get('i')):
            PyJsComma(PyJsComma(var.put('u', ((var.get('s')%Js(4.0))*Js(8.0))),var.get('o').put(var.put('n', ((var.get('s')-(var.get('s')%Js(4.0)))/Js(4.0))), (var.get('o').get(var.get('n'))|(var.get('t').callprop('charCodeAt', var.get('s'))<<var.get('u'))))),(var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1)))
        
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('u', ((var.get('s')%Js(4.0))*Js(8.0))),var.get('o').put(var.put('n', ((var.get('s')-(var.get('s')%Js(4.0)))/Js(4.0))), (var.get('o').get(var.get('n'))|(Js(128.0)<<var.get('u'))))),var.get('o').put((var.get('r')-Js(2.0)), (var.get('i')<<Js(3.0)))),var.get('o').put((var.get('r')-Js(1.0)), PyJsBshift(var.get('i'),Js(29.0)))),var.get('o'))
    PyJs_anonymous_6_._set_name('anonymous')
    PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('m', PyJs_anonymous_6_(var.put('t', PyJs_anonymous_2_(var.get('t'))))),var.put('v', Js(1732584193.0))),var.put('_', Js(4023233417.0))),var.put('p', Js(2562383102.0))),var.put('A', Js(271733878.0))),var.put('c', Js(0.0)))
    while (var.get('c')<var.get('m').get('length')):
        try:
            def PyJs_LONG_28_(var=var):
                def PyJs_LONG_26_(var=var):
                    def PyJs_LONG_22_(var=var):
                        def PyJs_LONG_18_(var=var):
                            def PyJs_LONG_14_(var=var):
                                def PyJs_LONG_10_(var=var):
                                    def PyJs_LONG_7_(var=var):
                                        return var.get('r')(var.get('p'), var.put('A', var.get('r')(var.get('A'), var.put('v', var.get('r')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(0.0))), Js(7.0), Js(3614090360.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(1.0))), Js(12.0), Js(3905402710.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(2.0))), Js(17.0), Js(606105819.0))
                                    def PyJs_LONG_8_(var=var):
                                        return var.get('r')(var.get('p'), var.put('A', var.get('r')(var.get('A'), var.put('v', var.get('r')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(4.0))), Js(7.0), Js(4118548399.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(5.0))), Js(12.0), Js(1200080426.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(6.0))), Js(17.0), Js(2821735955.0))
                                    def PyJs_LONG_9_(var=var):
                                        return var.get('r')(var.get('p'), var.put('A', var.get('r')(var.get('A'), var.put('v', var.get('r')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(8.0))), Js(7.0), Js(1770035416.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(9.0))), Js(12.0), Js(2336552879.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(10.0))), Js(17.0), Js(4294925233.0))
                                    return var.get('r')(var.put('_', var.get('r')(var.put('_', var.get('r')(var.get('_'), var.put('p', PyJs_LONG_7_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(3.0))), Js(22.0), Js(3250441966.0))), var.put('p', PyJs_LONG_8_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(7.0))), Js(22.0), Js(4249261313.0))), var.put('p', PyJs_LONG_9_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(11.0))), Js(22.0), Js(2304563134.0))
                                def PyJs_LONG_11_(var=var):
                                    return var.get('r')(var.get('p'), var.put('A', var.get('r')(var.get('A'), var.put('v', var.get('r')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(12.0))), Js(7.0), Js(1804603682.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(13.0))), Js(12.0), Js(4254626195.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(14.0))), Js(17.0), Js(2792965006.0))
                                def PyJs_LONG_12_(var=var):
                                    return var.get('o')(var.get('p'), var.put('A', var.get('o')(var.get('A'), var.put('v', var.get('o')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(1.0))), Js(5.0), Js(4129170786.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(6.0))), Js(9.0), Js(3225465664.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(11.0))), Js(14.0), Js(643717713.0))
                                def PyJs_LONG_13_(var=var):
                                    return var.get('o')(var.get('p'), var.put('A', var.get('o')(var.get('A'), var.put('v', var.get('o')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(5.0))), Js(5.0), Js(3593408605.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(10.0))), Js(9.0), Js(38016083.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(15.0))), Js(14.0), Js(3634488961.0))
                                return var.get('o')(var.put('_', var.get('o')(var.put('_', var.get('r')(var.put('_', PyJs_LONG_10_()), var.put('p', PyJs_LONG_11_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(15.0))), Js(22.0), Js(1236535329.0))), var.put('p', PyJs_LONG_12_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(0.0))), Js(20.0), Js(3921069994.0))), var.put('p', PyJs_LONG_13_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(4.0))), Js(20.0), Js(3889429448.0))
                            def PyJs_LONG_15_(var=var):
                                return var.get('o')(var.get('p'), var.put('A', var.get('o')(var.get('A'), var.put('v', var.get('o')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(9.0))), Js(5.0), Js(568446438.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(14.0))), Js(9.0), Js(3275163606.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(3.0))), Js(14.0), Js(4107603335.0))
                            def PyJs_LONG_16_(var=var):
                                return var.get('o')(var.get('p'), var.put('A', var.get('o')(var.get('A'), var.put('v', var.get('o')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(13.0))), Js(5.0), Js(2850285829.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(2.0))), Js(9.0), Js(4243563512.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(7.0))), Js(14.0), Js(1735328473.0))
                            def PyJs_LONG_17_(var=var):
                                return var.get('u')(var.get('p'), var.put('A', var.get('u')(var.get('A'), var.put('v', var.get('u')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(5.0))), Js(4.0), Js(4294588738.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(8.0))), Js(11.0), Js(2272392833.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(11.0))), Js(16.0), Js(1839030562.0))
                            return var.get('u')(var.put('_', var.get('o')(var.put('_', var.get('o')(var.put('_', PyJs_LONG_14_()), var.put('p', PyJs_LONG_15_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(8.0))), Js(20.0), Js(1163531501.0))), var.put('p', PyJs_LONG_16_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(12.0))), Js(20.0), Js(2368359562.0))), var.put('p', PyJs_LONG_17_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(14.0))), Js(23.0), Js(4259657740.0))
                        def PyJs_LONG_19_(var=var):
                            return var.get('u')(var.get('p'), var.put('A', var.get('u')(var.get('A'), var.put('v', var.get('u')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(1.0))), Js(4.0), Js(2763975236.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(4.0))), Js(11.0), Js(1272893353.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(7.0))), Js(16.0), Js(4139469664.0))
                        def PyJs_LONG_20_(var=var):
                            return var.get('u')(var.get('p'), var.put('A', var.get('u')(var.get('A'), var.put('v', var.get('u')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(13.0))), Js(4.0), Js(681279174.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(0.0))), Js(11.0), Js(3936430074.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(3.0))), Js(16.0), Js(3572445317.0))
                        def PyJs_LONG_21_(var=var):
                            return var.get('u')(var.get('p'), var.put('A', var.get('u')(var.get('A'), var.put('v', var.get('u')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(9.0))), Js(4.0), Js(3654602809.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(12.0))), Js(11.0), Js(3873151461.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(15.0))), Js(16.0), Js(530742520.0))
                        return var.get('u')(var.put('_', var.get('u')(var.put('_', var.get('u')(var.put('_', PyJs_LONG_18_()), var.put('p', PyJs_LONG_19_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(10.0))), Js(23.0), Js(3200236656.0))), var.put('p', PyJs_LONG_20_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(6.0))), Js(23.0), Js(76029189.0))), var.put('p', PyJs_LONG_21_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(2.0))), Js(23.0), Js(3299628645.0))
                    def PyJs_LONG_23_(var=var):
                        return var.get('s')(var.get('p'), var.put('A', var.get('s')(var.get('A'), var.put('v', var.get('s')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(0.0))), Js(6.0), Js(4096336452.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(7.0))), Js(10.0), Js(1126891415.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(14.0))), Js(15.0), Js(2878612391.0))
                    def PyJs_LONG_24_(var=var):
                        return var.get('s')(var.get('p'), var.put('A', var.get('s')(var.get('A'), var.put('v', var.get('s')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(12.0))), Js(6.0), Js(1700485571.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(3.0))), Js(10.0), Js(2399980690.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(10.0))), Js(15.0), Js(4293915773.0))
                    def PyJs_LONG_25_(var=var):
                        return var.get('s')(var.get('p'), var.put('A', var.get('s')(var.get('A'), var.put('v', var.get('s')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(8.0))), Js(6.0), Js(1873313359.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(15.0))), Js(10.0), Js(4264355552.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(6.0))), Js(15.0), Js(2734768916.0))
                    return var.get('s')(var.put('_', var.get('s')(var.put('_', var.get('s')(var.put('_', PyJs_LONG_22_()), var.put('p', PyJs_LONG_23_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(5.0))), Js(21.0), Js(4237533241.0))), var.put('p', PyJs_LONG_24_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(1.0))), Js(21.0), Js(2240044497.0))), var.put('p', PyJs_LONG_25_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(13.0))), Js(21.0), Js(1309151649.0))
                def PyJs_LONG_27_(var=var):
                    return var.get('s')(var.get('p'), var.put('A', var.get('s')(var.get('A'), var.put('v', var.get('s')(var.get('v'), var.get('_'), var.get('p'), var.get('A'), var.get('m').get((var.get('c')+Js(4.0))), Js(6.0), Js(4149444226.0))), var.get('_'), var.get('p'), var.get('m').get((var.get('c')+Js(11.0))), Js(10.0), Js(3174756917.0))), var.get('v'), var.get('_'), var.get('m').get((var.get('c')+Js(2.0))), Js(15.0), Js(718787259.0))
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('f', var.get('v')),var.put('h', var.get('_'))),var.put('l', var.get('p'))),var.put('d', var.get('A'))),var.put('_', var.get('s')(var.put('_', PyJs_LONG_26_()), var.put('p', PyJs_LONG_27_()), var.get('A'), var.get('v'), var.get('m').get((var.get('c')+Js(9.0))), Js(21.0), Js(3951481745.0)))),var.put('v', var.get('e')(var.get('v'), var.get('f')))),var.put('_', var.get('e')(var.get('_'), var.get('h')))),var.put('p', var.get('e')(var.get('p'), var.get('l')))),var.put('A', var.get('e')(var.get('A'), var.get('d'))))
            PyJs_LONG_28_()
        finally:
                var.put('c', Js(16.0), '+')
    return (((var.get('a')(var.get('v'))+var.get('a')(var.get('_')))+var.get('a')(var.get('p')))+var.get('a')(var.get('A'))).callprop('toLowerCase')
PyJs_anonymous_0_._set_name('anonymous')
var.put('o', PyJs_anonymous_0_)
# print(var.get('o')(Js("music/11/8/data-0.2:9378423167:4448756"+"11efb9c71bf319ab9fe03587d57f20cc2c90e5103f8c54e75c3868e7d761afb1")))

def obfuscateYandex(inp):
    return str(var.get('o')(Js(inp)))[1:-1]

# Add lib to the module scope
output = var.to_python()