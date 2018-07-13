from selfdrive.car import dbc_dict

class CAR:
  ELANTRA = "HYUNDAI ELANTRA 2017"
  GENESIS = "HYUNDAI GENESIS 2018"
  SORENTO = "Kia Sorento 2018 GT Line"
  STINGER = "Kia Stinger 2018 GT2"


class ECU:
  CAM = 0 # camera

#addr: (ecu, cars, bus, 1/freq*100, vl)
STATIC_MSGS = [(0x141, ECU.CAM, (CAR.ELANTRA), 0,   2, '\x00\x00\x00\x46'),
              ]


def check_ecu_msgs(fingerprint, candidate, ecu):
  # return True if fingerprint contains messages normally sent by a given ecu
  ecu_msgs = [x[0] for x in STATIC_MSGS if (x[1] == ecu and
                                            candidate in x[2] and
                                            x[3] == 0)]

  return any(msg for msg in fingerprint if msg in ecu_msgs)


FINGERPRINTS = {
  #REAL CAR.ELANTRA: [{
  #   66: 4, 67: 8, 68: 5, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 512: 3, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 897: 8, 899: 8, 902: 8, 903: 7, 905: 3, 909: 8, 916: 8, 1040: 5, 1056: 7, 1057: 8, 1170: 8, 1265: 4, 1280: 1, 1290: 1, 1292: 8, 1314: 5, 1322: 5, 1345: 8, 1349: 4, 1351: 8, 1353: 8, 1363: 7, 1366: 6, 1367: 6, 1369: 8, 1407: 1, 1415: 8, 1419: 3, 1425: 1, 1427: 6, 1440: 5, 1456: 3, 1486: 8, 1487: 7, 1491: 1, 1530: 6
  # }],
  CAR.ELANTRA: [{
    66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 8, 399: 8, 512: 8, 544: 8, 593: 8, 608: 8, 688: 8, 790: 8, 809: 8, 832: 8, 897: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 8, 1170: 8, 1265: 8, 1280: 8, 1282: 8, 1287: 8, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1314: 8, 1322: 8, 1345: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1415: 8, 1419: 8, 1425: 8, 1427: 8, 1440: 8, 1456: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8,
  }],
  CAR.GENESIS: [{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1024: 2, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1456: 4, 2016: 8, 2017: 8, 2024: 8, 2025: 8,
  }],
  CAR.SORENTO: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1384: 8, 1407: 8, 1411: 8, 1419: 8, 1425: 2, 1427: 6, 1444: 8, 1456: 4, 1470: 8, 1489: 1
  }],
  CAR.STINGER: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1378: 4, 1379: 8, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8
  }],
}


DBC = {
  CAR.ELANTRA: dbc_dict('hyundai_2015_ccan', None), ## TODO: find radar dbc
  CAR.GENESIS: dbc_dict('hyundai_2015_ccan', None),
  CAR.SORENTO: dbc_dict('kia_sorento_2018', 'kia_sorento_2018'), # Radar Messages are in same dbc
  CAR.STINGER: dbc_dict('kia_stinger_2018', None),
}
