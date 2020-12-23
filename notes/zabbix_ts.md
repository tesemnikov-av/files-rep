## TS ZABBIX



--------------------------------------------------------------------------------

### Общие правила:

* Ночью адм. ОС и АС письма не читают. Требуется Добавлять деж. Смену АС, СХД, SAN, звонить по графику или Хабаровск.
* В консоли должны отображаться все открытые проблемы без ограничения по времени.
* По всем сообщениям должна быть реакция. Если есть сообщения по которым не понятно что делать - сообщайте адм. ОС
* Сообщения требуется закрывать, но перед этим требуется оповестить ответственных

Расшифровка номера ошибки:

#### TSA000BC

* TS: Идентификатор кодов ошибок TS
* A: Идентификатор логической группы 
* 000: Уникальный номер сообщения
* B: Группа рассылки
* C: Наличие инцидента

|   | 0    | 1            | 2            | 3               | 4  | 5    |
|---|------|--------------|--------------|-----------------|----|------|
| A | C: CPU  | M: Memory       | N: Network      | S: Storage and SAN | O:OS | V:VRTS |
| B | ОС   | ОС, СУБД, АС | ОС, СХД, SAN |                 |    |      |
| C | True | False        |              |                 |    |      |

Полный перечень ошибок:

#### TSC00110 Высокая утилизация CPU
  
Самые тяжелые процессы

AIX:
```shell 
ps -eo users,pid,pcpu,args | sort +2n
```

SUN:
 
```shell 
ps -eo users,pid,pcpu,args | sort +2n
``` 
   
##### 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Сообщения типа:
Call or Write Storage and SAN team for analyze problem
 
Означают что ошибки регистрируются на диски с внешнего массива:
Направляем коллегам из СХД и SAN следующую информацию , с просьбой проверить ошибки в SAN и на массиве (AIX ставим в копию):
 
∙             Имя сервера
∙             Серийный номер массива (vxdmpadm listenclosure)
∙             WWN хоста (wwnshow)
 
root@vishera20 /# vxdmpadm listenclosure
ENCLR_NAME        ENCLR_TYPE     ENCLR_SNO      STATUS       ARRAY_TYPE     LUN_COUNT    FIRMWARE
===================================================================================================
san_vc0           SAN_VC         020320015130         CONNECTED    IBMSVC-ALUA   4         0000
 
Если массивов несколько, смотрим на котором регистрируются ошибки через команду vxdmpadm getsubpaths (см. ниже)
 
root@vishera20 /# wwnshow
fcs0:  10:00:00:10:9B:21:F7:49
fcs1:  10:00:00:10:9B:21:F7:4A
fcs2:  10:00:00:10:9B:21:F8:9C
fcs3:  10:00:00:10:9B:21:F8:9D
fcs4:  10:00:00:10:9B:21:A9:2E
fcs5:  10:00:00:10:9B:21:A9:2F
fcs6:  10:00:00:10:9B:21:A9:19
fcs7:  10:00:00:10:9B:21:A9:1A
 
Смотрим ошибки на сервере:
# errpt
DCB47997   0213051320 T H hdisk547       DISK OPERATION ERROR
DCB47997   0213050520 T H hdisk1209      DISK OPERATION ERROR
DCB47997   0212012720 T H hdisk842       DISK OPERATION ERROR
C62E1EB7   0210231620 P H hdisk731       DISK OPERATION ERROR
 
# смотрим через какие контролеры выданы диски, на которых регистрируются ошибки
root@vishera16 /# vxdmpadm getsubpaths | grep hdisk547
hdisk547     ENABLED(A)   -          3pardata0_53088 3pardata0    fscsi0            -
root@vishera16 /# vxdmpadm getsubpaths | grep hdisk1209
hdisk1209    ENABLED(A)   -          3pardata0_52910 3pardata0    fscsi6            -
root@vishera16 /# vxdmpadm getsubpaths | grep hdisk842
hdisk842     ENABLED(A)   -          3pardata1_39872 3pardata1    fscsi2            -
 
3pardata0 в данном случае имя массива.
 
На сервере мы проверяем уровень сигнала контроллера/ов:
 
Для POWER7:
# lsattr -El proc0 -a type -F value                                                                             # Смотрим поколение сервера
PowerPC_POWER7
# /oper/efc_power /dev/fscsi0                                                                                # Смотрим уровень сигнала
TX: 16a5 -> 0.5797 mW, -2.37 dBm
RX: 131c -> 0.4892 mW, -3.11 dBm
 
Для POWER8:
# lsattr -El proc0 -a type -F value                                                                             # Смотрим поколение сервера
PowerPC_POWER8
# /oper/emfc_power /dev/fscsi0 | egrep "TX power|RX power"               # Смотрим уровень сигнала
                TX power:       153c (0.5436mW / -2.65 dB)
                RX power:       1314 (0.4884mW / -3.11 dB)
                TX power:       1564 (0.5476mW / -2.62 dB)
                RX power:       10ac (0.4268mW / -3.70 dB)
 
Потенциально проблемным считаем порты  с уровнем сигнала от -5.
Если ошибок много и они регистрируются на одно порту и/или на порту низкий уровень сигнала то выключаем данный путь:
# vxdmpadm disable ctlr=fscsi0
 
Сообщения типа:
LINK ERROR
ADAPTER ERROR
Говорят что проблемы на определенном порту, либо локально на сервере, либо где-то в SAN.
То же самое: направляем письмо в SAN/СХД со всей информацией и проверяем уровень сигнала, открываем заявку в IBM.
При необходимости адаптер отключаем.
 
Сообщения типа:
Call AIX team and check SAS disk in active VGs
Означают что ошибки регистрируются на внутреннем диски сервера в активной группе томов и требуется перезеркалирование с дежурным на телефоне.
Если ошибок не много и система не является MC++, а так же  если узел является резервным, то можно дождаться утра для оповещения администраторов.
 
Алгоритм перезеркалирования следующий:
unmirrorvg rootvg hdiskX
reducevg [-d] rootvg hdiskX
 
Возможно, потребуется обнулить устройство аварийного сброса (по сигналу от администратора)
sysdumpdev -Pp /dev/sysdumpnull
 
extendvg [-f] rootvg hdiskY
chvg -Qn rootvg
mirrorvg -s rootvg
syncvg -v rootvg
bosboot -a
bootlist -m normal hdiskZ hdiskY
 
Возможно, потребуется создать и назначить устройство аварийного сброса (по сигналу от администратора)
mklv -t sysdump -y lg_dumplv rootvg NUMBER_OF_LP
sysdumpdev -Pp /dev/lg_dumplv
 
hdiskX – сбойный диск
hdiskY – подменный диск
hdiskZ – оставшийся рабочий диск rootvg
 
diskopererr.sh still running. Call AIX support to check
 
Разовые срабатывания не критичны.
Но если метрика срабатывает достаточно долго (более 30 мин)  – требуется подключить администраторов AIX.
Возможно подвисла команда errpt или демон vxconfigd.
 
Write AIX team to check SAS disk
Ошибки на диск, который в данный момент не используется. Не критично, просто пишем письмо.
 
Тесемников А. В.: 46-992
