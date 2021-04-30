KPP_CODE = {
    u'01' : u'Постановка на учет в налоговом органе российской организации в качестве налогоплательщика по месту ее нахождения',
    u'02' : u'Постановка на учет налогоплательщика - российской организации по месту нахождения ее обособленного подразделения в зависимости от вида подразделения',
    u'03' : u'Постановка на учет налогоплательщика – российской организации по месту нахождения ее филиала, не исполняющего обязанности организации по уплате налогов и сборов',
    u'04' : u'Постановка на учет налогоплательщика - российской организации по месту нахождения ее обособленного подразделения в зависимости от вида подразделения',
    u'05' : u'Постановка на учет налогоплательщика - российской организации по месту нахождения ее обособленного подразделения в зависимости от вида подразделения',
    u'06' : u'Постановка на учет налогоплательщика - российской организации по месту нахождения принадлежащего ей недвижимого имущества (за исключением транспортных средств) - в зависимости от вида имущества',
    u'07' : u'Постановка на учет налогоплательщика - российской организации по месту нахождения принадлежащего ей недвижимого имущества (за исключением транспортных средств) - в зависимости от вида имущества',
    u'08' : u'Постановка на учет налогоплательщика - российской организации по месту нахождения принадлежащего ей недвижимого имущества (за исключением транспортных средств) - в зависимости от вида имущества',
    u'30' : u'Российская организация - налоговый агент, не учтенная в качестве налогоплательщика',
    u'31' : u'Постановка на учет налогоплательщика - российской организации по месту нахождения обособленного подразделения, в отношении которого не проведена процедура оформления в соответствии с пунктом 3 статьи 55 Гражданского кодекса Российской Федерации, исполняющего обязанности организации по уплате налогов и сборов',
    u'32' : u'Постановка на учет налогоплательщика - российской организации по месту нахождения обособленного подразделения, в отношении которого не проведена процедура оформления в соответствии с пунктом 3 статьи 55 Гражданского кодекса Российской Федерации, не исполняющего обязанности организации по уплате налогов и сборов',
    u'51' : u'Постановка на учет отделений иностранных организаций',
    u'52' : u'Постановка на учет отделений иностранных организаций в Российской Федерации, созданных филиалом этой иностранной организации в иностранном государстве',
    u'53' : u'резервный код',
    u'54' : u'резервный код',
    u'55' : u'резервный код',
    u'56' : u'резервный код',
    u'57' : u'резервный код',
    u'58' : u'резервный код',
    u'59' : u'резервный код',
    u'60' : u'Постановка на учет посольств иностранных государств',
    u'61' : u'Постановка на учет консульств иностранных государств',
    u'62' : u'Постановка на учет представительств, приравненных к дипломатическим',
    u'63' : u'Постановка на учет международных организаций',
    u'64' : u'резервный код',
    u'65' : u'резервный код',
    u'66' : u'резервный код',
    u'67' : u'резервный код',
    u'68' : u'резервный код',
    u'69' : u'резервный код',
    u'70' : u'Постановка на учет иностранных и международных организаций, имеющих недвижимое имущество в Российской Федерации, за исключением транспортных средств, относящихся к недвижимому имуществу',
    u'71' : u'Постановка на учет иностранных и международных организаций, имеющих транспортные средства в Российской Федерации, не относящиеся к недвижимому имуществу',
    u'72' : u'Постановка на учет иностранных и международных организаций, имеющих морские транспортные средства в Российской Федерации',
    u'73' : u'Постановка на учет иностранных и международных организаций, имеющих речные транспортные средства в Российской Федерации',
    u'74' : u'Постановка на учет иностранных и международных организаций, имеющих воздушные транспортные средства в Российской Федерации',
    u'75' : u'Постановка на учет иностранных и международных организаций, имеющих космические объекты в Российской Федерации',
    u'76' : u'резервный код',
    u'77' : u'резервный код',
    u'78' : u'резервный код',
    u'79' : u'резервный код',
    u'80' : u'Учет иностранных и международных организаций в связи с открытием в банках рублевых счетов типа "Т" (текущие)',
    u'81' : u'Учет иностранных и международных организаций в связи с открытием счетов в банках типа "И" (инвестиционные)',
    u'82' : u'учет иностранных и международных организаций в связи с открытием счетов в банках типа "С" (специальные)',
    u'83' : u'Учет иностранных и международных организаций в связи с открытием в банках счетов типа "Т" (текущие) в иностранной валюте',
    u'84' : u'Учет иностранных и международных организаций в связи с открытием корреспондентских счетов в банка',
    }


OGRN_CODES  = {
    u'1' : u'юридическое лицо',
    u'5' : u'юридическое лицо',
    u'3' : u'индивидуальный предприниматель',
    }


SOUN_SCHEMA = {'1' : {'name' : 'kod', 'type' : 'string'},
               '2' : {'name' : 'vid', 'type' : 'string'},
               '3' : {'name' : 'kodp', 'type' : 'string'},
               '4' : {'name' : 'kodv', 'type' : 'string'},
               '5' : {'name' : 'naimk', 'type' : 'string'},
               '6' : {'name' : 'naim', 'type' : 'string'},
               '7' : {'name' : 'psono', 'type' : 'int'},
               '8' : {'name' : 'puch', 'type' : 'int'},
               '9' : {'name' : 'potchdok', 'type' : 'int'},
               '10' : {'name' : 'potch', 'type' : 'int'},
               '11' : {'name' : 'spro_u', 'type' : 'string'},
               '12' : {'name' : 'spro_f', 'type' : 'string'},
               '13' : {'name' : 'inn', 'type' : 'string'},
               '14' : {'name' : 'kpp', 'type' : 'string'},
               '15' : {'name' : 'adres', 'type' : 'string'},
               '16' : {'name' : 'tel', 'type' : 'string'},
               '17' : {'name' : 'email', 'type' : 'string'},
               '18' : {'name' : 'cite', 'type' : 'string'},
               '19' : {'name' : 'dokum', 'type' : 'string'},
               '20' : {'name' : 'nomdok', 'type' : 'string'},
               '21' : {'name' : 'datadok', 'type' : 'date'},
               '22' : {'name' : 'datan', 'type' : 'date'},
               '23' : {'name' : 'datak', 'type' : 'date'},
               '24' : {'name' : 'coment', 'type' : 'string'},
               }

SSRF_SCHEMA = {'1' : {'name' : 'code', 'type' : 'string'},
               '2' : {'name' : 'name', 'type' : 'string'},
               }

OKV_SCHEMA = {'1' : {'name' : 'id', 'type' : 'int'},
              '2' : {'name' : 'ncode', 'type' : 'string'},
              '3' : {'name' : 'ccode', 'type' : 'string'},
              '4' : {'name' : 'name', 'type' : 'string'},
              '5' : {'name' : 'countries', 'type' : 'string'},
              }

PLANSCHET_SCHEMA = {'1' : {'name' : 'id', 'type' : 'int'},
                    '2' : {'name' : 'code', 'type' : 'string'},
                    '3' : {'name' : 'name', 'type' : 'string'},
                    '4' : {'name' : 'stype', 'type' : 'int'},
                    '5' : {'name' : 'parent_id', 'type' : 'int'},
                    '6' : {'name' : 'level', 'type' : 'int'},
                    }


RUS_INN_FACTOR = (2, 4, 10, 3, 5, 9, 4, 6, 8)

RUS_ACCOUNT_MASK = [7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1]

def calc_personal_check_digits(number):
    """Calculate the check digits for the 12-digit personal ИНН."""
    weights = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
    d1 = str(sum(w * int(n) for w, n in zip(weights, number)) % 11 % 10)
    weights = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
    d2 = str(sum(w * int(n) for w, n in zip(weights, number[:10] + d1)) % 11 % 10)
    return d1 + d2


def _check_inn(code):
    """Validates INN code"""
    if code is not None and code.isdigit():
        if len(code) == 10:
            asum = 0
            for i in range(0, 9):
                asum += int(code[i]) * RUS_INN_FACTOR[i]
            asum = (asum % 11) % 10
            return (int(code[9]) == asum)
        elif len(code) == 12:
            weights = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
            d1 = str(sum(w * int(n) for w, n in zip(weights, code)) % 11 % 10)
            weights = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
            d2 = str(sum(w * int(n) for w, n in zip(weights, code[:10] + d1)) % 11 % 10)
            chsum = d1 + d2
            return chsum == code[-2:]
    return False


def _check_ogrn(code):
    """Validates OGRN code"""
    if code is not None and code.isdigit() and len(code) == 13:
        v = code[0:12]
        v1 = int(v) % 11
        if v1 > 9:
            v1 = v1 - ((v1 / 10) * 10)      
        return v1 == int(code[12])
    elif code is not None and code.isdigit() and len(code) == 15:
        v = code[0:14]
        v1 = int(v) % 11
        if v1 > 9:
            v1 = v1 - ((v1 / 10) * 10)
        print(v1, int(code[14]))
        return v1 == int(code[14])
    return False
