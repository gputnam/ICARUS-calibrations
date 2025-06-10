from datetime import datetime

rundate_str_RunA = \
"""8459    6/7/2022 11:35:00
8455    6/6/2022 20:34:00
8446    6/2/2022 13:30:00
8440    6/2/2022 11:40:00
8439    5/31/2022 15:50:00
8437    5/27/2022 10:15:00
8433    5/25/2022 15:58:00
8413    5/23/2022 16:30:00
8370    5/20/2022 13:21:00
8362    5/18/2022 17:21:00
8334    5/16/2022 18:05:00
8324    5/14/2022 2:02:00
8323    5/13/2022 13:08:00
8318    5/12/2022 19:07:00
8264    5/10/2022 16:43:00
8243    5/7/2022 16:30:00
8238    5/6/2022 16:54:00
8230    5/5/2022 21:50:00
8207    5/4/2022 18:15:00
8197    5/2/2022 2:30:00
8196    4/30/2022 23:06:00
8194    4/29/2022 18:55:00
8169    4/28/2022 17:11:00
8148    4/27/2022 15:50:00
8147    4/25/2022 11:45:00
8137    4/25/2022 11:16:00
8136    4/25/2022 3:48:00
8135    4/23/2022 14:05:00
8131    4/22/2022 13:08:00
8129    4/22/2022 2:47:00
8121    4/19/2022 18:20:00
8117    4/18/2022 15:21:00
8112    4/17/2022 9:30:00
8109    4/16/2022 0:48:00
8107    4/15/2022 13:56:00
8087    4/13/2022 2:53:00
8085    4/13/2022 14:45:00
8051    4/9/2022 19:27:00
8031    4/7/2022 18:44:00
8003    4/4/2022 15:00:00
8002    4/2/2022 9:55:00
7977    3/29/2022 19:20:00
7965    3/26/2022 10:40:00
7961    3/25/2022 22:55:00
7950    3/24/2022 18:50:00
7946    3/23/2022 23:10:00
7937    3/22/2022 20:33:00
7937    3/22/2022 20:33:00
7931    3/21/2022 20:35:00
7926    3/18/2022 10:50:00
7918    3/16/2022 22:05:00
7911    3/15/2022 13:23:04
7903    3/14/2022 21:48:09
7897    3/13/2022 9:56:26
7896    3/12/2022 23:45:22
7888    3/11/2022 17:28:52
7874    3/10/2022 17:00:43
7863    3/9/2022 22:17:24
7806    2/27/2022 15:04:19
7803    2/26/2022 21:54:53
7780    2/25/2022 19:13:08
7587    2/5/2022 15:48:04
7586    2/5/2022 2:08:18
7568    1/31/2022 21:48:57
7566    1/31/2022 9:28:22
7564    1/30/2022 3:49:04
7562    1/29/2022 9:07:13
7561    1/28/2022 15:42:53
7518    1/26/2022 15:36:01
7507    1/25/2022 22:35:31
7504    1/24/2022 13:24:00
7503    1/23/2022 13:59:03
7444    1/4/2022 16:18:13
7435    1/3/2022 12:47:52
7428    12/31/2021 14:28:10
7427    12/30/2021 17:16:34
7425    12/30/2021 8:16:23
7424    12/27/2021 9:10:53
7420    12/27/2021 7:05:53
7418    12/26/2021 1:45:12
7416    12/25/2021 1:30:11
7415    12/23/2021 11:39:24
7401    12/21/2021 12:44:00
7397    12/17/2021 19:01:49
7384    12/16/2021 16:48:26
7366    12/15/2021 18:47:34
7356    12/14/2021 18:58:55
7344    12/13/2021 18:41:27
7339    12/11/2021 17:00:57
7334    12/10/2021 20:47:24
7314    12/9/2021 19:20:31
7291    12/8/2021 19:33:31
7262    12/7/2021 17:04:30
7247    12/6/2021 16:53:06
7244    12/4/2021 11:43:09
7243    12/3/2021 19:35:43
7239    12/2/2021 17:34:31
7236    12/1/2021 17:58:02
7230    11/28/2021 8:16:34
7228    11/27/2021 9:58:58
7216    11/25/2021 22:45:58
7213    11/25/2021 6:03:34
7212    11/24/2021 20:55:49
7208    11/23/2021 17:28:49
7190    11/22/2021 15:40:33
7178    11/20/2021 15:20:35
7176    11/19/2021 17:12:05
7152    11/18/2021 17:27:56
7138    11/17/2021 18:25:06
7133    11/16/2021 17:21:17
7125    11/15/2021 19:32:28
7113    11/13/2021 21:24:52
7112    11/13/2021 0:05:39
7108    11/11/2021 18:41:18"""

rundatestr_Run1 = [    
"8460, 06/08/2022 4:20",
"8461, 06/08/2022 14:19",
"8462, 06/09/2022 20:24",
"8468, 06/10/2022 14:30",
"8469, 06/10/2022 16:45",
"8470, 06/12/2022 18:55",
"8471, 06/14/2022 9:40",
"8505, 06/15/2022 17:15",
"8506, 06/19/2022 5:40",
"8507, 06/20/2022 15:39",
"8513, 06/22/2022 17:10",
"8514, 06/23/2022 10:50",
"8515, 06/23/2022 15:47",
"8517, 06/27/2022 14:58",
"8518, 06/28/2022 1:25",
"8521, 06/28/2022 13:20",
"8522, 06/30/2022 1:41",
"8525, 06/30/2022 12:36",
"8527, 07/01/2022 13:13",
"8528, 07/02/2022 0:20",
"8529, 07/02/2022 10:35",
"8530, 07/03/2022 17:20"

]


rundatestr_Run2 = \
"""Run number   Start time  End time    Configuration   Stop notes  Other notes                                                 
9011    10/18/2022 16:10:00 10/18/2022 17:35:00 Physics_General_Thr400_Majority_5_10_00020  stopped to allow trigger modification   first run after BNB restart. Very low beam (1 10^12 pot, 0.3 rep rate)                                                  
9012    10/18/2022 18:16:00 10/19/2022 9:02:00  Physics_General_Thr400_Majority_5_10_00020  network outage   1 10^12 pot, 0.3 rep rate, 0.03 Hz                                                 
9014    10/19/2022 9:30:00  10/19/2022 13:35:00 Physics_General_Thr400_Majority_5_10_00020  restart of MongoDB and Redis     1 10^12 pot, 0.3 rep rate, 0.03 Hz                                                 
9015    10/19/2022 16:50:00 10/20/2022 13:00:00 Physics_General_Thr400_Majority_5_10_00020  CRT cable change     3 10^12 pot, 0.3 rep rate, 0.03 Hz                                                 
9016    10/20/2022 13:36:00 10/21/2022 11:45:00 Physics_General_Thr400_Majority_5_10_00020  stopped to start calibration run for purity  2.1 10^12 pot, 3 rep rate, 0.3 Hz                                                  
9017    10/21/2022 12:30:00 10/21/2022 13:14:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   calibration run for purity  no CRT telescope, 4 Hz                                                  
9018    10/21/2022 13:27:00 10/21/2022 17:04:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   x`  no CRT telescope, 4 Hz                                                  
9019    10/21/2022 17:10:00 10/24/2022 10:15:00 Physics_General_Thr400_Majority_5_10_00020  no beam  2.6 10^12 pot, 5 rep rate, 0.5 Hz                                                  
9020    10/24/2022 10:22:00 10/24/2022 12:47:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   DAQ issues - no more events produced    no CRT telescope, 4 Hz                                                  
9021    10/24/2022 13:06:00 10/25/2022 6:40:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to start DAQ tests  no CRT telescope, 4 Hz                                                  
9022    10/24/2022 15:59:00 10/24/2022 16:25:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   DAQ tests   no CRT telescope, 4 Hz                                                  
changed Work area -> DAQ_26Oct2022GAL                                                                       
9023    10/24/2022 16:40:00 10/24/2022 17:28:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to lower cathode HV no CRT telescope, 4 Hz                                                  
lowered Cathode 500 -> 350 V/cm                                                                     
9024    10/24/2022 18:06:00 10/25/2022 0:11:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   skew issues on EW01T, WW20T no CRT telescope, 4 Hz                                                  
9025    10/25/2022 0:20:00  10/25/2022 5:00:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   skew issues on WW20T    no CRT telescope, 4 Hz                                                  
9026    10/25/2022 5:10:00  10/26/2022 8:01:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to start DAQ testing    no CRT telescope, 4 Hz                                                  
9028    10/26/2022 11:05:00 10/26/2022 16:24:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to take laser data  sbndaq v1_04_00 and nominal trigger fragment definition (ICARUSTriggerV2)                                                   
Runs 9029-9039: Laser calibration of PMTs in WW                                                                         
9040    10/26/2022 19:26:00 10/27/2022 3:40:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   skew issues on WW01T    no CRT telescope, 4 Hz                                                  
9041    10/27/2022 3:47:00  10/27/2022 19:25:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   OM problems no CRT telescope, 4 Hz                                                  
9042    10/27/2022 19:40:00 10/27/2022 21:14:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   lost connection to WE20T - segfault no CRT telescope, 4 Hz                                                  
9043    10/27/2022 22:01:00 10/28/2022 0:32:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   DAQ issues  no CRT telescope, 4 Hz                                                  
9045    10/28/2022 0:45:00  10/28/2022 3:19:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   skew issues on WW20T    no CRT telescope, 4 Hz                                                  
9046    10/28/2022 4:05:00  10/28/2022 11:00:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped for DAQ tests                                                       
9050    10/28/2022 14:20:00 10/29/2022 7:20:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   lost connection to WE01T - segfault no CRT telescope, 4 Hz                                                  
9051    10/29/2022 7:53:00  10/29/2022 20:03:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   skew in WW01B   no CRT telescope, 4 Hz                                                  
9052    10/29/2022 20:15:00 10/30/2022 8:15:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   OM problems - stale shared memory   no CRT telescope, 4 Hz                                                  
9054    10/30/2022 10:00:00 10/30/2022 18:19:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   no triggers transmitted to DAQ                                                      
9055    10/30/2022 19:13:00 10/31/2022 5:00:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   non-documented crash    no CRT telescope, 4 Hz                                                  
9056    10/31/2022 5:15:00  10/31/2022 6:36:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   lowered cathode HV for pump wiring repairs  no CRT telescope, 4 Hz                                                  
9057    10/31/2022 14:49:00 11/1/2022 4:34:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   non-documented crash    no CRT telescope, 4 Hz                                                  
9058    11/1/2022 4:40:00   11/1/2022 14:10:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped for DAQ tests   no CRT telescope, 4 Hz                                                  
"switched to new dev area 28OctGAL. Noise filters in EW17 slots 7,8
WE18 slots 1,2"                                                                     
9065    11/1/2022 17:44:00  11/2/2022 0:11:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   non-documented crash    no CRT telescope, 4 Hz                                                  
9066    11/2/2022 0:24:00   11/2/2022 1:45:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   non-documented crash                                                        
9067    11/02/2022 1:53:00  11/2/2022 4:57:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   incomplete events   no CRT telescope, 4 Hz                                                  
9068    11/2/2022 5:10:00   11/2/2022 9:05:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to allow noise testing  no CRT telescope, 4 Hz                                                  
9069    11/2/2022 9:50:00   11/2/2022 10:47:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   incomplete events - CRT rates end abruptly  All mini-crates except EE18, EW15, WE20M                                                    
9070    11/2/2022 11:30:00  11/2/2022 14:03:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   icaruscrt06esi dead                                                     
9071    11/2/2022 14:17:00  11/2/2022 16:23:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to reinsert missing minicrate   All mini-crates except WE20M.                                                   
9072    11/2/2022 16:30:00  11/3/2022 8:57:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped for noise test                                                      
9075    11/03/2022 16:39:00 11/3/2022 17:59:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to power cycle EE01M (errors)                                                       
9076    11/3/2022 18:31:00  11/3/2022 22:57:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   incomplete events                                                       
9078    11/4/2022 0:12:00   11/4/2022 9:16:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   shared memory issues                                                        
9080    11/4/2022 13:37:00  11/5/2022 8:51:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   dispatcher problems - OM dead   after installing filters on EE01T                                                   
9081    11/5/2022 9:10:00   11/6/2022 10:40:00  "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   Shared memory issues - OM dead                                                      
9083    11/6/2022 12:00:00  11/7/2022 7:35:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to ramp down cathode: restart of West pump                                                      
Cathode back to 500 V/cm                                                                        
Debug build established for TPC DAQ (area 28Oct_GAL)                                                                        
9086    11/07/2022 16:11:00 11/8/2022 7:27:00   "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   incomplete events   no CRT telescope, 4 Hz                                                  
9089    11/8/2022 11:07:00  11/8/2022 15:25:00  Physics_General_Thr400_Majority_5_10_00020  reference run for trigger test                                                      
9090    11/08/2022 15:40:00 11/9/2022 6:03:00   Physics_General_Thr380_Majority_5_10_00001  stopped to start calibration run    all                                                 
9091    11/09/2022 6:35:00  11/09/2022 12:06:00 "Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002
"   stopped to start DAQ tutorial   all                                                 
switched back to previous trigger Labview version (without logger - and NO Trig6 fix)                                                                       
9093    11/9/2022 14:49:00  11/10/2022 6:43:00  Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    dispatcher died (see Slack)                                                     
9094    11/10/2022 7:00:00  11/10/2022 9:09:00  Physics_General_Thr380_Majority_5_10_OverlappingWindow_00001    No beam all components                                                  
9095    11/10/2022 13:53:00 11/11/2022 6:51:00  Physics_General_Thr380_Majority_5_10_OverlappingWindow_00001    No beam all components                                                  
9096    11/10/2022 7:33:00  11/11/2022 14:27:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    Loss of icarustpcwe01b  all components                                                  
9097    11/11/2022 14:55:00 11/11/2022 8:54:00  Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    Stopped to test trigger restart issues  all components                                                  
9099    11/12/2022 9:45:00  11/13/2022 8:53:00  Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002                                                            
9100    11/13/2022 9:05:43  11/13/2022 11:22:03 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    Back pressure warnings, and not getting triggers    all components                                                  
9101    11/13/2022 11:37:06 11/13/2022 18:19:54 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    Lots of imcomplete events and builder warnings  all components                                                  
9102    11/13/2022 18:55:45 11/14/2022 16:01:38 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    Stopped due the OM not running  all components                                                  
9103    11/14/2022 16:17:00 11/14/2022 16:56:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped to run Majority run to check NuMI being seen    all components                                                  
9104    11/14/2022 17:13:07 11/15/2022 9:43:43  Physics_General_Thr380_Majority_5_10_OverlappingWindow_00001    Stopping the run to start TPC debugging all components                                                  
9105~9110 : TPC debugging runs                                                                      
                                                                        
9111    11/15/2022 17:31:04 11/15/2022 22:38:47 Physics_General_thr380_Majority_5_7_OverlappingWindow_00001 Reach 10k events for this test trigger  all components                                                  
9112    11/15/2022 22:54:30 11/16/2022 8:55:48  Physics_General_thr380_Majority_5_6_OverlappingWindow_00001 Stopped for trigger works   all components                                                  
9113-9114 short trigger tests with beam                                                                     
9115    11/16/2022 10:48:41 11/16/2022 12:50:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00001 PMT errors caused run to crash  all components                                                  
9116    11/16/2022 13:17:00 11/16/2022 17:09:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00001 PMT errors caused run to crash  all components                                                  
9117    11/16/2022 17:20:00 11/16/2022 19:45:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00001 reached enough data all components                                                  
9118    11/16/2022 20:00:00 11/17/2022 7:00:00  Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    stopped because of electrical work at FD    all components                                                  
electrical work at FD 7 am -2 pm                                                                        
9126    11/17/2022 16:00:00 11/18/2022 2:50:00  Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped because of back pressure warnings   all components                                                  
9127    11/17/2022 3:08:00  11/18/2022 8:07:53  Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    back pressure warnings  all components                                                  
9128    11/18/2022 8:41:30  11/18/2022 11:45:15 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    crt top warnings    all components                                                  
9129    11/18/2022 12:11:00 11/18/2022 15:29:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped to change TPC debug levels  all components                                                  
no 9130                                                                     
9131    11/18/2022 16:00:00 11/19/2022 3:56:00  Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped bc incomplete events    all components                                                  
9132    11/19/2022 4:10:00  11/19/2022 23:43:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped bc Events rates 0 (backpressure)    all components                                                  
9133    11/20/2022 0:02:00  11/20/2022 15:15:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped bc Events rates 0 (backpressure)    all components                                                  
9134    11/20/2022 15:28:00 11/21/2022 12:07:06 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    OM not updating all components                                                  
9135    11/21/2022 12:30:00 11/21/2022 14:49:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    Run stopped for impedance test and then laser runs                                                      
                                                                        
runs 9136-9144 laser calibrations                                                                       
9145    11/21/2022 18:10:00 11/21/2022 19:57:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped bc back pressure warnings                                                       
9146    11/21/2022 20:10:00 11/22/2022 6:40:00  Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped bc back pressure warnings                                                       
9148    11/22/2022 8:05:00  11/22/2022 10:39:08 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped to work on  trigger (LabView) system                                                        
runs 9149-9150 are  trigger tests runs after labview modification by Donatella and Massimo                                                                      
9150    11/22/2022 12:17:00 11/22/2022 12:44:06 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped to allow new trigger filter test by Jacob                                                       
9151    11/22/2022 12:50:00 11/22/2022 15:05:00 Physics_General_Thr400_Majority_5_10_00021  trigger filter test by Jacob                                                        
runs 9153- 9157  laser runs                                                                     
9158    11/22/2022 18:23:30 11/23/2022 8:07:00  Physics_General_thr380_Majority_5_7_OverlappingWindow_00002 mj 5-7 with beam at 4Hz, 34.5K triggers all components                                                  
runs 9159-9171 are laser runs                                                                       
9172    11/23/2022 12:45:57 11/23/2022 14:26:43 Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 stopped bc beam went away   all components                                                  
9173    11/23/2022 15:25:00 11/23/2022 17:39:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    anded as beam came back                                                     
                                                                        
9174    11/23/2022 17:59:00 11/24/2022 10:12:00 Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 stopped bc beam went away ( 37.9K triggers) all components                                                  
9175    11/24/2022 10:24:00 11/24/2022 16:06:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 stopped bc beam went away (~12K triggers)                                                       
9176    11/24/2022 16:23:00 11/24/2022 16:46:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002        all components                                                  
runs 9177-9180 attempts to restrt data taking dur to PMT errors: resolved by manually powercycling the PMT crates at the building                                                                       
9182    11/24/2022 22:31:00 11/25/2022 11:35:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 completed at ~28K triggers  all components                                                  
9183    11/25/2022 11:40:00 11/26/2022 2:15:00  Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    stopped bc of daq/PMT issues (31.7K triggers)   all components                                                  
9184    11/26/2022 3:54:00  11/28/2022 4:21:00  Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    run stoppec bc WE02 TPC PS failure (~104K triggers) all components                                                  
9185    11/28/2022 5:02:00  11/28/2022 8:05:00  Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    without WE02; stopped to add back WE02                                                      
9186    11/28/2022 8:19:00  11/28/2022 13:36:00 Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    stopped bc PMT empty fragments 2%                                                       
9187    11/28/2022 14:09:00 11/29/2022 8:02:12  Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    stopped bc beam off day                                                     
9188    11/29/2022 8:05:00  11/29/2022 21:00:00 Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    stopped bc beams are back                                                       
9189    11/29/2022 21:12:28 11/29/2022 21:13:20 Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    just started and stopped                                                        
9190    11/29/2022 21:25:25 11/30/2022 8:30:57  Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 stopped bc of losst process in pmteebot01 (~23K)                                                        
9191    11/30/2022 9:05:32  11/30/2022 11:56:57 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 stopped bc rate jumped up to 10Hz and hundreds of incomplete events                                                     
9192    11/30/2022 12:14:33 11/30/2022 14:56:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 stopped bc beam going to lowwrr rate                                                        
9193    11/30/2022 15:09:12 11/30/2022 15:58:43 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 stopped due to PMT empty fragments                                                      
9194    11/30/2022 16:11:31 2022-11-30 18:20:48 Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 Stopped due to empty PMT fragments                                                      
9195    11/30/2022 18:35:00 11/30/2022 20:30:00 Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    trying 5-10 as the others cause PMTs empty fragments: still empty fragments: decided to stop for power cycle PMT crates                                                     
power cycled all PMT VME crates                                                                     
9196    11/30/2022 20:41:00 12/1/2022 12:05:00  Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    NO empty fragments !!!                                                      
9197    12/01/2022 12:22    12/2/2022 4:31:00   Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 PMT error on ewbot02 (~34K)                                                     
9198    12/2/2022 5:31:00   12/2/2022 15:42:00  Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 PMT error on eetop03 (~20K)                                                     
9199    12/02/2022 15:50:00 12/2/2022 21:02:00  Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 stopped bc of incomplete evenrs (7K)                                                        
9201    12/02/2022 21:24:00 12/2/2022 22:05:00  Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 stopped bc of high rate of PMTempty fragments                                                       
9203    12/2/2022 22:30:00  12/3/2022 7:11:00   Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 PMT eetop03 error (~13K triggers)                                                       
9204    12/3/2022 7:33:00   12/3/2022 16:50:00  Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 empty fragments on all 8 PMT boards on server pmt03 (~13K)                                                      
9205    12/03/2022 17:01:00 12/3/2022 21:34:00  Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 PMT error from PMT ewbot01 (                                                        
9206    12/3/2022 21:48:00  12/4/2022 11:28:00  Physics_General_thr380_Majority_5_7_OverlappingWindow_00002 stopped to check RWM signals (~21K triggers)                                                        
9207    12/04/2022 12:10    12/4/2022 12:37:00  Physics_General_thr380_Majority_5_7_OverlappingWindow_00002 test RWM signals PMT onlys                                                      
9208    12/04/2022 12:35:00 2022/12/05 12:52    Physics_General_thr380_Majority_5_7_OverlappingWindow_00002 BNB going 5 Hz with increased intensity. Chaning to 5-5                                                     
BNB at 5Hz rep rate, 4.3e12                                                                     
9209    12/5/2022 13:07:00  12/6/2022 5:30:00   Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 stopped bc TPC ew01t died (30K)                                                     
9210    12/6/2022 6:00:00   12/6/2022 8:10:00   Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 without ew01m; crashed because of pmtwetop02                                                        
9211    12/6/2022 8:15:00   12/6/2022 22:17:00  Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 pmtwetop01 ( 27.4K )    all components                                                  
9212    12/6/2022 22:30:00  12/7/2022 2:23:00   Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 pmtewbot01  all components                                                  
9213    12/07/2022 2:35:00  12/7/2022 3:00:00   Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 pmtwwbot02                                                      
9214    12/07/2022 3:10:00  12/7/2022 6:30:00   Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 lost all pmt processes on pnt01                                                     
9215    12/7/2022 7:00:00   12/7/2022 9:18:00   Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 NO BEAMS ; crashed bc of pmteebot03                                                     
daq tests                                                                       
9221    12/7/2022 14:30:00  12/8/2022 0:10:00   Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 pmtwebot01 (17K)    all components                                                  
9222    12/8/2022 0:42:00   12/-02/2022 01:05:00    Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 crash bc lost all pmt board reders on pmt01 all components                                                  
9223    12/8/2022 1:11:00   12/8/2022 1:50:00   Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 crash bc pmt    all components                                                  
9224    12/8/2022 1:57:00   12/8/2022 2:13:00   Physics_General_thr380_Majority_5_7_OverlappingWindow_00002 crash bc pmt    all components                                                  
remote power cycled ALL PMT VME crates                                                                      
9225    12/8/2022 2:25:00   12/8/2022 10:00:00  Physics_General_thr380_Majority_5_7_OverlappingWindow_00002 stopped for starting PMT tests                                                      
PMT gain calibration runs (9226, 9227,9228,9229,9230)                                                                       
9233    12/8/2022 13:48:00  12/8/2022 18:57:00  Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 pmtwetop02                                                      
9234    12/8/2022 19:42:00  12/8/2022 23:31:00  Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 pmtwwbot03                                                      
9235    12/08/2022 23:51:00 12/10/2022 12:00:00 Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    no issues:stopped to do trigger tests (71K )                                                        
trigger tests with beam , but PMTs only                                                                     
9236-9239   12/10/2022 12:00:00 12/10/2022 13:20:00 Physics_General_thr380_Majority_5_10_OverlappingWindow_00001        PMTs only                                                   
all components again                                                                        
9240    12/10/2022 13:35:00 12/10/2022 17:15:00 Physics_General_thr380_Majority_5_10_OverlappingWindow_00001    stopped to chenge config (5.7K) all components                                                  
9241    12/10/2022 17:23:00 12/11/2022 13:45:00 Physics_General_thr380_Majority_5_7_OverlappingWindow_00001 stopped to try 5-5 (40K)     all components                                                 
9242    12/11/2022 13:56:00 12/11/2022 18:51:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 pmteebot01  all components                                                  
9243    12/11/2022 19:00:00 12/11/2022 22:43:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 pmtewtop02  all components                                                  
9244    12/11/2022 22:58:00 12/13/2022 7:45:00  Physics_General_thr380_Majority_5_6_OverlappingWindow_00002 no issues:64.8K triggers    all components                                                  
9245    12/13/2022 8:10:00  12/13/2022 8:20:00  Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 very short: mistakely started                                                       
9246    12/13/2022 8:20:00  12/13/2022 8:40:00  PMTLAser00031   PMT only for HV tests                                                       
9247    12/13/2022 8:45:00  12/13/2022 12:09:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 stopped to remove TPC crate all components                                                  
9248    12/13/2022 12:21:00     Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 NO EW01M ; ongoing                                                      
9249    12/13/2022 15:30:00 12/13/2022 15:49:00 PMTLAser00031   PMT only for HV tests                                                       
9251    12/13/2022 16:10:00 12/13/2022 21:30:00 Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 incomplete events   all components                                                  
9252    12/13/2022 21:51:00 12/14/2022 4:25:00  Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 incomplete events   all components                                                  
9253    12/14/2022 4:39:00  12/14/2022 6:00:00  Physics_General_thr380_Majority_5_5_OverlappingWindow_00002 beam off for the day    all components                                                  
BEAM OFF                                                                        
9260                PMT ONLT HV run                                                     
9261            Calibration_MINBIAS_BNB_Thr400_Majority_10_FixedWindow_4Hz_00002    no WW20M; stoppeb bc imcomplete events                                                      
DAQ tests : using TCARUSTRiggerV3 boardReader                                                                       
9259-9264           Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003     all components                                                  
                                                                        
9265    12/14/2022 17:29:00 12/15/2022 17:18:00 Physics_General_thr380_Majority_5_6_OverlappingWindow_00004 swapped to swap TPC board in        PMT readout window is 15+35 us (pre+post trigger).                                              
9266    12/14/2022 17:30:00 12/15/2022 4:37:00  Physics_General_thr380_Majority_5_6_OverlappingWindow_00004 pmtwwtop02  all components                                                  
9267    12/15/2022 4:45:00  12/15/2022 6:27:00  Physics_General_thr380_Majority_5_6_OverlappingWindow_00004 incomplete events                                                       
9269    12/15/2022 8:29:00  12/15/2022 10:53:00 Physics_General_thr380_Majority_5_6_OverlappingWindow_00004     without EE20m                                                   
9270            PMTLaser00032       ONLY PMTs + laser on                                                    
9271            PMTLaser00032       ONLY PMTs                                                   
9272    12/15/2022 12:14:00 12/15/2022 14:30:00 Physics_General_thr380_Majority_5_6_OverlappingWindow_00004 incomplete events   all components                                                  
9273    12/15/2022 14:37:00 12/15/2022 15:55:00 Physics_General_thr380_Majority_5_6_OverlappingWindow_00004 stopped to switch to 360 ADC    all components                                                  
changed PMT thresholds to 360 ADC, and baselines                                                                        
9274    12/15/2022 16:01:00     Physics_General_thr360_Majority_5_6_OverlappingWindow_00001     al components                                                   
9275            Physics_General_thr360_Majority_5_6_OverlappingWindow_00001 crashed afyer just few minutes  all components                                                  
9276    12/15/2022 16:53:00 12/15/2022 18:20:00 Physics_General_thr360_Majority_5_10_OverlappingWindow_00001    stopped to change config (2.5K) all components                                                  
9277    12/15/2022 18:27:00 12/15/2022 20::00:00    Physics_General_thr360_Majority_5_7_OverlappingWindow_00001 pmtewbot01  all components                                                  
9278    12/15/2022 20:17:00 12/15/2022 20:23:00 Physics_General_thr360_Majority_5_7_OverlappingWindow_00001 ran a few minutes   al components                                                   
9279    12/15/2022 20:31:00 12/15/2022 21:17:00 Physics_General_thr360_Majority_5_10_nb_OverlappingWindow_00001 pmtwebot01  all components                                                  
9280    12/15/2022 22:04:00 12/16/2022 3:24:00  Physics_General_thr380_Majority_5_10_nb_OverlappingWindow_00001 pmtwetop01  all components                                                  
9281    12/16/2022 3:30:00  12/16/2022 7:31:00  Physics_General_thr380_Majority_5_10_nb_OverlappingWindow_00001 pmtewtop03  all components                                                  
9282    12/16/2022 7:53:00  12/16/2022 10:37:00 Physics_General_thr400_Majority_5_10_nb_OverlappingWindow_00001 stopped for trigger tests   all components                                                  
runs 9283-9284-9285 are trigger tests; no data                                                                      
9286    12/16/2022 11:20:00 12/16/2022 16:15:00 Physics_General_thr400_Majority_5_10_nb_OverlappingWindow_00001 stopped to change config    all components                                                  
9287    12/16/2022 16:41:00 12/16/2022 22:03:00 Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001      all components                                                  
9288    12/16/2022 22:17:00 12/17/2022 10:45:00 Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  pmtwetop01  all components                                                  
9289    12/17/2022 11:00:00 2022-12-18 10:00:00 Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  stopped to do trigger tests (45K)   all components                                                  
trigger tests 9290-9291 and fixed HV of 2 PMTs                                                                      
9292    12/18/2022 10:54:00 12/18/2022 14:20:00 Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  stopped for trigger tests   all components                                                  
changed primitive in enable gate                                                                        
9294    12/18/2022 17:20:00 12/19/2022 14:43:00 Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  stopped to test another config (44K)    all componebts                                                  
9295    12/19/2022 15:00:00 12/19/2022 20:53:00 Physics_General_thr360_Majority_5_7_nb_OverlappingWindow_00001  stopped to un-do change in trigger FPGA     all componebts                                                  
un-do changes in trigger FPGA                                                                       
9296    12/19/2022 21:50:00 12/20/2022 10:07:00 Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  stopped to do trigger work  all components                                                  
9297-9299           Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  after reverting changes made on Sunbday all components   Run stopped due to incomplete events                                               
trigger system restored and OK on 12/20/2022                                                                        
9300    12/20/2022 17:05    12/20/2022 17:15    Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  stopped by RunCo to switch to production    all components                                                  
[Run2]                                                                      
9301    12/20/2022 17:51:00 12/21/2022 6:01 Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  stopped by RunCo because beam off day (24K) all components  Run stopped due to incomplete events                                                
9302    12/21/2022 6:10     Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 stopped for doing laser runs    laser,pmts                                                  
laser runs 9304-9395-9306                                                                       
9307    12/21/2022 12:17:00 12/21/2022 22:40    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 149K    all components   Run stopped due to incomplete events                                               
beam returns                                                                        
9308    12/21/2022 22:47    12/22/2022  Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  pmtwwtop03 (~11.4K) all components  Run was stopped due to PMT digitizers busy                                              
9309    12/22/2022 5:16:00  12/22/2022 9:23 Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  tpcee13 power supply failed all components                                                  
9310    12/22/2022 10:24    12/22/2022 11:20    Physics_General_thr400_Majority_5_7_nb_OverlappingWindow_00001  pmtwwtop03 (~11.4K) all components  Run was stopped due to empty fragments from PMTs                                                
9311    12/22/2022 11:38    12/22/2022 20:48    Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  pmteebot03 (~18K)   all components                                                  
9312    12/22/2022 21:05    12/23/2022 3:30 Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  stopped bc bean was off down for sometime   all components  Run was stopped due to ~13 incomplete events                                                
9313    12/23/2022 3:40 12/23/2022 6:13 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003     all components                                                  
9314    12/23/2022 6:15:00  12/23/2022 6:35 Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  stopped bc beam went away   all components                                                  
9315    12/23/2022 7:42:00  12/23/2022 8:00 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 stopped bc many incomplete events   all components                                                  
9316    12/23/2022 8:13:00  12/23/2022 9:28 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 incomplete events   all components                                                  
9317    12/23/2022 9:53:00  12/23/2022 11:34    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 stopping bs beam is back    all components                                                  
9318    12/23/2022 11:47    12/24/2022 14:50    Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  stopped bc of incomplete events ( ~54K triggers collected)  all components                                                  
9319    12/24/2022 15:08    12/24/2022 15:10    Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  lasted only a few minutse: incomplete events from thr TPC   all components                                                  
9320-9326 attemps to fix TPC issues                                                                     
fixed TPC WW01-02 isues                                                                     
9327    12/24/2022 19:38    12/24/2022 23:19    Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  incomplete events from other TPC crates all components                                                  
9328    12/24/2022 23:30    12/25/2022 4:14 Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  incomplete events from other TPC crates all components                                                  
9329    12/25/2022 4:23 12/25/2022 19:03    Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  PMTs empty fragments (28K triggers) all components                                                  
9330    12/25/2022 19:11    12/28/2022 2:42:00  Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  ew20m blown fuse (101K) all components                                                  
9331    12/28/2022 3:00:00  12/28/2022 4:00 Physics_General_thr380_Majority_5_8_nb_OverlappingWindow_00001  stopped to reinclude ew20m  \without ew20m                                                  
9332    12/28/2022 4:12:00  12/28/2022 17:51    Physics_General_thr380_Majority_5_8_nb_OverlappingWindow_00001  pmtwetop01 (26K)    all components                                                  
9333    12/28/2022 18:32    12/29/2022 3:15:00  Physics_General_thr380_Majority_5_8_nb_OverlappingWindow_00001  pmteebot01  all components                                                  
9335    12/29/2022 4:00 12/29/2022 8:40 Physics_General_thr380_Majority_5_8_nb_OverlappingWindow_00001  pmtewbot02  all components  Run stopped at 48k events. Only one missing sequence id and one incomplete events. According to grafana there are 82 events with empty fragments ( PMT or CRT or both )                                             
9336    12/29/2022 8:57:00  12/29/2022 9:45 Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  pmt and TPC empty fragments all components                                                  
9337    12/29/2022 9:58 12/30/2022 8:27 Physics_General_thr400_Majority_5_8_nb_OverlappingWindow_00001  pmteetop01(~44K)    all components                                                  
9338    12/30/2022 8:43 12/20/2022 14:40    Physics_General_thr380_Majority_5_9_nb_OverlappingWindow_00001  pmtwwbot01(14K) all components                                                  
9339    12/30/2022 15:22:00 12/31/2022 1:36 Physics_General_thr380_Majority_5_9_nb_OverlappingWindow_00001  pmtwetop03 (    all components                                                  
9340    12/31/2022 2:25:00  12/31/2022 4:42 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 Booster down, switching to calibration until it's back  all components                                                  
9341    12/31/2022 5:01 12/31/2022 6:02:00  Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 beam is back    all components                                                  
9342    12/31/2022 6:18 01/03/2023 0:54     stopped by accident (133K)  all components                                                  
9343    01/03/2023 1:44:00  01/03/2023 10:25    Physics_General_thr390_Majority_5_8_OverlappingWindow_00001 pmtewbot02 (~19K)   all components                                                  
9344    01/03/2023 10:54    01/04/2023 6:42:00 AM   Physics_General_thr390_Majority_5_8_OverlappingWindow_00001 pmteebot02 (~   all components                                                  
8345    01/04/2023 7:55:00  01/04/2023 8:45 Physics_General_thr390_Majority_5_8_OverlappingWindow_00001 icaruscrt04eci  all components                                                  
9346    01/03/2023 9:45 01/04/2023 14:25:00 Physics_General_thr390_Majority_5_8_OverlappingWindow_00001 pmtewbot01  all components                                                  
9347    01/04/2023 14:52    01/05/2023 6:00 Physics_General_thr390_Majority_5_8_OverlappingWindow_00001 stopped bc beam off all components                                                  
no beam ; did some trigger tests                                                                        
9353    01/05/2023 8:50 01/05/2023 13:00:00 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 stopped bc beam is coming back (~9K)    all components                                                  
beam back                                                                       
9354    01/05/2023 16:20    01/06/2023 8:48 Physics_General_thr390_Majority_5_8_OverlappingWindow_00001 icarustpcwe01b  all components                                                  
9355    01/06/2023 9:06:00  01/06/2023 9:53:00  Physics_General_thr390_Majority_5_8_OverlappingWindow_00001 ongoing without we01b                                                       
9356    01/06/2023 10:16:00 01/06/2023 10:47:00 Physics_General_thr390_Majority_5_8_OverlappingWindow_00001 pmtwebot03  all components                                                  
9357    01/06/2022 11:00    01/06/2022 14:10    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 icaruspmteetop02    all components                                                  
9358    01/06/2022 14:30    01/06/2023 17:50    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 pmteetop02  all components                                                  
power cycled PMT VME crates                                                                     
9359    01/06/2023 18:34:00 01/07/2023 14:16    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 pmteetop01 (~37.5K) all components                                                  
9360    01/07/2023 14:43    01/07/2023 17:14:00 PM  Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 pmteebot01  all components                                                  
9361    01/07/2023 17:30    01/08/2023 15:00    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 beam off since 2:15 pm (~40K)   all components                                                  
beam issues                                                                     
9362    01/08/2023 15:30    01/08/2023 19:56    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 beam  is back   all components                                                  
beam returns                                                                        
9363    01/08/2023 20:15:00 01/09/2023 6:31:00  Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 pmteebot01 (~20K)   all components                                                  
9364    01/09/2023 7:25 01/09/2023 14:15    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 tpcew03 ps blown fuse   all components                                                  
9365    01/09/2023 15:09    01/10/2023 8:50 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 crt09ssi (~35K) all components                                                  
9366    01/10/2023 9:21:00  01/10/2023 17:11    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 stopped to restrore MsgViewer   all components                                                  
9367    01/10/2023 17:20:00 01/12/2023 15:38    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 pmtwwto03 (~92.6K)  all components                                                  
several runs on partition 7 for bottom crt work                                                                     
9380    01/12/2023 15:57:00 01/14/2023 1:45 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 pmtwwtop02 (~67.6k) all components                                                  
no 9381 and 9382                                                                        
9383    01/14/2023 3:00 01/15/2023 4:14:00  Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 pmtwetop01 (~50.4k) all components                                                  
9384    01/15/2023 4:30:00  01/18/2023 5:47 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 pmtwwtop03 (~147.3k)    all components                                                  
9385    01/18/2023 6:27 01/18/2023 18:57    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 lost process at icarus-evb02-daq, tagged DAQ experts for more details (~24.7k)  all components                                                  
9386    01/18/2023 20:27    01/20/2023 9:19 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 DAQVNC shows very weird behavior, the GUI was not available. Restarted the VNC, but it seems like to stop the run (~73.7k)  all components  beam down at 23/01/19 09:30-10:20                                               
9387    01/20/2023 10:00    01/20/2023 16:00    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 icaruspmtwwbot03 (~12.5k)   all components                                                  
9388    01/20/2023 16:30    01/21/2023 6:56 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 icaruspmtewbot01 (~77.3k)   all components                                                  
9389    01/22/2023 7:17 01/23/2023 2:54 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 icaruspmteebot01 (~39.4k)   all components                                                  
9390    01/23/2023 3:45 01/23/2023 15:00    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 icaruspmtewbot01 (~22.0k)   all components                                                  
Remote power cycle on PMT board                                                                     
9391    01/23/2023 15:23    01/23/2023 17:30    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 icaruspmtwebot02    all components                                                  
Remote power cycle on PMT board                                                                     
9392    01/23/2023 17:45    01/25/2023 6:00 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 BNB off all components                                                  
HV went down to 0V, to take TPC noise data                                                                      
9393    01/25/2023 6:40 01/25/2023 7:24 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 (~11.7k) Stopped to try TPC PS powercycle for EE07 (icarus_tpcps_ee07_m52/curr has value 1.365825, expected at most 1.200000)   all components                                                  
Remotely power cycled TPC PS for EE07 current issue                                                                     
9394    01/25/2023 7:45 01/25/2023 9:45 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 ~28.3k, stopped to start DAQ test   all components                                                  
DAQ test for sbndaq v1_05_00 started                                                                        
PMT baseline test configuration                                                                     
Lots of try/fail of restarting the run; turned out to be an issue in WR                                                                     
9409    01/25/2023 17:46    01/26/2023 14:52    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 ~42.2k; Stopped to utilize this unscheduled beam down time for PMT test confgifs                                                        
9410 ran with pmt test configuration, Test_thr390_CalibOnConfig_false_00001                                                                     
9411 ran with pmt test configuration, Test_thr390_LockTemp_true_00001                                                                       
9412    01/26/2023 15:38    01/27/2023 6:23 Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 ~29.9k; Issue from server, icarus-pmt03-daq                                                     
Remote power cycle on PMT board                                                                     
Remote power cycle on PMT server                                                                        
Re-sync comand applied, waited until pmt03 server has time synchronized                                                                     
9415    01/27/2023 8:00 01/27/2023 12:18    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 Stopped to run LockTemp test config Beam down 01/27/2023 10:30~11:00                                                    
9416    01/27/2023 12:34    01/27/2023 17:04    Test_thr390_LockTemp_true_00001 Issue from server, icarus-pmt01-daq                                                     
Re-sync comand applied, waited until pmt01 server has time synchronized                                                                     
Causality warning again, power-cycling the PMT boards                                                                       
9433    01/27/2023 23:42:00 01/27/2023 10:41    Physics_General_thr390_Majority_5_9_OverlappingWindow_00001 Stopped to test chaning wr off set to 0 (it was 1sec)   Probably a bad data, should not use                                                     
9434    01/28/2023 10:54:46 01/29/2023 16:42    Test_thr390_LockTemp_true_00002 (~61.3k) Stopped to switch back to nominal config                                                       
9435    01/29/2023 17:08    01/30/2023 18:17:00 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    (~49.9k) icaruspmtwebot01                                                       
9436    01/30/2023 19:04:22 01/31/2023 13:47    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    (~37.2k) icaruspmtwwtop03                                                       
9437    01/31/2023 13:58    01/31/2023 16:38    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    icaruscrt08eni, icaruscrt08eno                                                      
9438    01/31/2023 17:06    01/31/2023 20:33    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    icaruspmtwebot02                                                        
remote powercycled PMT boards twice                                                                     
9439    01/31/2023 21:04    02/01/2023 21:30    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    Stopped to swtich to Calibration. This run has very long beam down time Beam down 02/01/2023 08:46~21:30                                                    
9440    02/01/2023 21:45    02/02/2023 9:55 TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00001  Stopped as beam is back                                                     
9441    02/02/2023 10:12    02/03/2023 1:27 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    (~30.7k) icaruspmteebot01                                                       
9442            Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    Causality problem from pmt03 server (grep "Causality" /daq/log/pmt/run9442*)                                                        
9444    02/03/2023 3:11 02/03/2023 3:28 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    icaruspmtwebot03                                                        
9445    02/03/2023 3:42 02/03/2023 11:10    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    lots of tpc incomplete events, with "ALARM: TPC BoardReaders Busy" in Grafana                                                       
Run9446 failed                                                                      
Run9447 failed; TPC06 server shows "System Health: Degraded"                                                                        
Remotely powercycled TPC06 server                                                                       
9448    02/03/2023 12:39    02/05/2023 19:12    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    Stopped to switch to Calibration. Beam will be down until tmmr morning  This run contains many downtimes..                                                  
9449    02/05/2023 19:26    02/06/2023 12:36    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00003 Stopped, we need to also updatd wr time offset to 0 for calibration config.. we forgot this!    This run most likeley to contain wrong PMT/CRT info, due to 1-sec shifted WR time                                                   
9450    02/06/2023 13:01    02/06/2023 14:30    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00009 Stopped to run PMT test runs                                                        
Below are few PMT test runs on "DAQ_31Jan2023_MV_PMTtesting" area to print more messages                                                                        
9451    pmt test run        Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001                                                            
9452    pmt test run    pmt component only  Test_thr390_CalibOnConfig_false_00001                                                           
9453    pmt test run    pmt component only  Test_thr390_LockTemp_true_00002                                                         
Going back to default DAQ area, but we are testing CRT calibration run                                                                      
9454    02/06/2023 17:09    02/06/2023 17:42    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_CRT_00001 Here we use bootfile with _multiple_art_process                                                     
9455    -   -   TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00001  This config was based on old config (~last July), and seems like to be updated. We'll update this this evening                                                      
9456    02/06/2023 19:07    02/06/2023 20:15    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00009 Incomplete events from TPC, and daq vnc is really slow.                                                     
Tried "TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00002" but DAQ was so slow. We killed firefox and restarted                                                                     
9457    02/06/2023 21:22    02/06/2023 21:36    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00009 Tested with nominal calib config to see if we still see slowness or incomplete events. It looks fine, so stopped and switching to trigger test                                                      
Tried again "TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00002" but run did not start.                                                                     
9458    02/06/2023 22:06    02/07/2023 10:27    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00009 Stopped for trigger desktop test                                                        
9459    02/07/2023 10:45    02/07/2023 11:24    TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00003                                                          
9460    02/07/2023 11:54    02/07/2023 14:47    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00009 Stopped for bottom CRT test                                                     
Bottom CRT test runs below, ran on DAQ_12Dec2022_rhowell                                                                        
9462    02/07/2023 17:18    02/07/2023 17:33    BottomCRTTest00003                                                          
Below are few PMT test runs on "DAQ_31Jan2023_MV_PMTtesting" area to print more messages                                                                        
9463    02/07/2023 17:48    02/07/2023 17:58    Test_thr390_pmt_config_all_off_00001    Stopped, but we see lots of "applyRequestsWindowMode_CheckAndFillDataBuffer: A timeout occurred waiting for data to close the request window ({1675814129235026784-1675814129238026784}, buffer={1675814128802617672-1675814129236880696} ). Time waiting: 3009937 us (> 3000000 us)."                                                      
Back to nominal area                                                                        
9464    02/07/2023 18:19    02/07/2023 18:22    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00009 Stopped, we just wanted to check if it runs fine.                                                       
9465    02/07/2023 18:40    02/08/2023 15:58    TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00003  icaruspmtwwtop01                                                        
9466    02/08/2023 16:17    02/09/2023 16:26    TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00003  Stopped as we see many Missing fragment from TPC22/23/24 servers                                                        
9467    02/09/2023 16:49    02/10/2023 15:09    TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00003                                                          
Below are the PMT tests from "DAQ_31Jan2023_MV_PMTtesting" area to print more messages                                                                      
9468    02/10/2023 15:20    02/10/2023 15:36    Test_thr390_pmt_config_all_off_ped_13108_00001  PMTs only (45 triggers)                                                     
9469    02/10/2023 15:50    -   Test_thr390_pmt_config_adcCal_first_00001   PMTs only                                                       
9470    -   -   Test_thr390_pmt_config_all_off_ped_32767_00001  PMTs only just few triggers                                                     
9471    -   -   Test_thr390_pmt_config_all_off_ped_32767_00001  PMTs only 48 triggers                                                       
Back to nominal area                                                                        
9472    02/10/2023 17:23    02/11/2023 8:36 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 stopped bc back pressure errors and OM not responding   Same as Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00009, ,but locktemp to false for PMT                                                 
9473    02/11/2023 8:50 02/11/2023 11:54    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 stopped bc back pressure errors and OM not responding                                                       
9474    02/11/2023 12:11    02/11/2023 16:38    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 stopped bc back pressure errors and OM not responding                                                       
9475    02/11/2023 16:56    02/11/2023 16:58    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 immediately stopped to try 1Hz config                                                       
9476    02/11/2023 17:31    02/13/2023 12:38    TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00003  Stopped to reproduce back-pressure warnings with 4Hz config                                                     
9477    02/13/2023 12:54    02/13/2023 14:59    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 Stopped to reproduce back-pressure warnings with 4Hz config                                                     
9478    02/13/2023 15:13    02/13/2023 15:46    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 Stopped for PMT test runs                                                       
Below are the PMT tests from "DAQ_31Jan2023_MV_PMTtesting" area to print more messages; but DAQ area updated not to register anything                                                                       
9479    02/13/2023 15:58    02/13/2023 16:14    Test_thr390_pmt_config_all_off_00001    see strange errors.. going back to previous area                                                        
9480    02/13/2023 16:21    02/13/2023 16:28    Test_thr390_pmt_config_all_off_00001    no error ,bu                                                        
Back to nominal area                                                                        
9481    02/13/2023 16:41    02/13/2023 20:39    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 evb04 error Seems like evb04 was rebooted for some reason, and that caused the run crash                                                    
9482    02/13/2023 21:46    02/14/2023 8:06 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 Stopped to prepare HV work                                                      
Some PMT test runs                                                                      
Bottom CRT test runs                                                                        
Below for test new PMT standard fcl file; to incorprate with SBND PMT. We want this to last ~2hrs, and then analyze the data if they look fine. Worked in a dev area                                                                        
9492    -   -   Test_thr390_LockTemp_true_new_common_code_00001 Stopped by "missing 4 Fragments" warnings. We have TPC PS issue reported from TPCPS script, that might caused this. We powercylce the PS and try again                                                      
9493    -   -   Test_thr390_LockTemp_true_new_common_code_00001 Stopped by "missing 4 Fragments" warnings. We have TPC PS issue reported from TPCPS script, that might caused this. We powercylce the PS and try again                                                      
9494    -   -   Test_thr390_LockTemp_true_new_common_code_00001 Stopped by "missing 4 Fragments" warnings. We have TPC PS issue reported from TPCPS script, that might caused this. We powercylce the PS and try again                                                      
Going back to nominal area                                                                      
9495    02/14/2023 18:40    02/14/2023 18:53    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 Stopped for CRT calibartion runs    Try nominal area/config if we see the same warnings. We don't                                                   
Below is several CRT calibration runs (still on nominal daq area)                                                                       
9496    02/14/2023 19:53    02/14/2023 20:33    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_CRT225_00001                                                          
9497    02/14/2023 20:40    02/14/2023 21:31    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_CRT235_00001                                                          
9498    02/14/2023 21:40    02/14/2023 22:55    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_CRT245_00001                                                          
CRT calibarion test done                                                                        
9499    02/14/2023 23:09    02/15/2023 0:19 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 Fuse blown: icarus_tpcps_ew01m_p82/volt has value -1.000000, expected at least 8.200000 CRT calibartion finished, switching back to calibration for the rest of the day                                                 
9500    02/15/2023 0:56 02/15/2023 1:02 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 not succesful   Fuse blown: icarus_tpcps_ew01m_p82/volt has value -1.000000, expected at least 8.200000                                                 
9501    02/15/2023 1:18 02/15/2023 1:20 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 not succesful   Fuse blown: icarus_tpcps_ew01m_p82/volt has value -1.000000, expected at least 8.200000                                                 
9502    02/15/2023 1:35 02/15/2023 3:14 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 not succesful   Fuse blown: icarus_tpcps_ew01m_p82/volt has value -1.000000, expected at least 8.200000                                                 
9503    02/15/2023 3:33 02/15/2023 7:58 TriggerTest_MinBias_1Hz_RL75000_noEnable_feb2023_00003  Stopped to swap TPC PS  not succesful                                                   
9504    02/15/2023 8:36 02/15/2023 11:11    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 Stopped for PMT test                                                        
Below is for PMT test runs; working on DAQ_DevAreas/DAQ_14Feb2023GAL                                                                        
9505    -   -   Test_thr390_LockTemp_true_new_common_code_00002                                                         
9506    -   -   Test_thr390_LockTemp_true_new_common_code_00002                                                         
9507    -   -   Test_thr390_LockTemp_true_new_common_code_00002                                                         
9508    -   -   Test_thr390_LockTemp_true_new_common_code_00002                                                         
9509    -   -   Test_thr390_LockTemp_true_new_common_code_00002                                                         
9510    -   -   Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_pmt_new_common_code_00001                                                         
We realized known_boardreaders should be updated; tpc06->tpc28 (server swap!)                                                                       
9511    02/15/2023 13:34    02/15/2023 14:39    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_pmt_new_common_code_00001 Stopped due to back-pressure                                                        
9512    02/15/2023 14:59    02/15/2023 15:24    Test_thr390_LockTemp_true_new_common_code_00002 Stopped, due to applyRequestsWindowMode_CheckAndFillDataBuffer: A timeout occurred waiting for data to close the request window ({1676496111456268280-1676496111459268280}, buffer={1676496111157377392-1676496111458647744} ). Time waiting: 3008230 us (> 3000000 us).                                                        
Going back to production area                                                                       
9513    02/15/2023 15:46    02/15/2023 15:49    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00002   Stopped, due to applyRequestsWindowMode_CheckAndFillDataBuffer: A timeout occurred waiting for data to close the request window ({1676496111456268280-1676496111459268280}, buffer={1676496111157377392-1676496111458647744} ). Time waiting: 3008230 us (> 3000000 us).                                                        
9514    02/15/2023 16:04    02/15/2023 16:05    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    Stopped, due to applyRequestsWindowMode_CheckAndFillDataBuffer: A timeout occurred waiting for data to close the request window ({1676496111456268280-1676496111459268280}, buffer={1676496111157377392-1676496111458647744} ). Time waiting: 3008230 us (> 3000000 us).                                                        
Powercycle PMT boards                                                                       
9515    02/15/2023 16:15    02/15/2023 16:16    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    Stopped, due to applyRequestsWindowMode_CheckAndFillDataBuffer: A timeout occurred waiting for data to close the request window ({1676496111456268280-1676496111459268280}, buffer={1676496111157377392-1676496111458647744} ). Time waiting: 3008230 us (> 3000000 us).                                                        
9516    02/15/2023 16:22    02/15/2023 16:33    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00009 No timeout issue, trying 00010; LockTemp    pmt-only                                                    
9517    02/15/2023 16:39    02/15/2023 16:43    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 No timeout issue, trying with all component pmt-only                                                    
9518    02/15/2023 16:54    02/15/2023 19:02    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00010 Stopped for CRT calibration We want to reproduce the "back-pressure" warnings seen from Run9472                                                 
Below is CRT calibartion runs                                                                       
9519    02/15/2023 19:31    02/15/2023 20:31    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_CRT220_00001                                                          
9520    02/15/2023 20:45    02/15/2023 21:48    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_CRT230_00001                                                          
9521    02/15/2023 21:56    02/15/2023 22:57    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_CRT240_00002                                                          
Below is for couple of DAQ test                                                                     
9522    -   -   Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_PMT_stale10s_00001   We still see timeout. Stopping. This is to understand timeout warnings from physics run                                                 
9523    02/15/2023 23:30    02/16/2023 13:56    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 Stopped for bottom CRT test Same as 00010, but enables multiple art process feature. We want to check if this helps preventing back-pressure warnings                                                   
Below is bottom CRT test (DAQ_DevAreas/DAQ_12Dec2022_rhowell)                                                                       
9524    02/16/2023 14:14    02/16/2023 14:36    BottomCRTTest00004                                                          
9525    02/16/2023 14:55    02/16/2023 15:00    BottomCRTTest00004      Bottom crt only                                                 
9526    02/16/2023 15:16    02/16/2023 23:59    BottomCRTTest00004      all components                                                  
Going back to nominal DAQ area                                                                      
Trigger desktop test                                                                        
9527                Worked!                                                     
9528                Test run with preivous trigger computer                                                     
Below is for PMT test area (DAQ_DevAreas/DAQ_14Feb2023GAL) we want to take data and to be analyzed before we push this to production                                                                        
9529    02/16/2023 16:24    02/16/2023 19:59    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_pmt_new_common_code_00002 Beam will arrive soon. Prepare next test    The config is updated to use multiple art process                                                   
BNB returns, staying at the Dev area, but now try physics config for 20-30 mins.                                                                        
9530    02/16/2023 20:21    02/16/2023 20:30    Test_thr390_LockTemp_true_new_common_code_00003 Stopped, timeout warning    The config is updated to use multiple art process                                                   
Back to production area                                                                     
9531    02/16/2023 20:53    02/16/2023 21:13    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00002   Stopped, empty fragments from all 24 pmt boards. But not every event. Also, this time we don't see applyRequestsWindowMode_CheckAndFillDataBuffer                                                       
9532    02/16/2023 21:31    02/16/2023 21:40    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    It works fine. Trying LockTemp one more time                                                        
9533    02/16/2023 21:52    02/17/2023 9:08 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00002   (~21k) icaruspmtewbot01                                                     
9534    02/17/2023 9:22 02/18/2023 16:38    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00002   (~63.7k) Grafana does not catch the run number, and we are getting lots of timeout warnings                                                     
Grafana showed run number of "N/A". After the restart, both DAQInterface and Grafana show run number "9558"                                                                     
9558    02/18/2023 16:50    02/19/2023 17:56    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00002   (~51.8k) evb01                                                      
9559    -   -       Stopped, pmt timeout warning every minute   timeout warnings every minute since the run start                                                   
Powercycled PMT boards                                                                      
9560    02/19/2023 18:37    02/20/2023 2:24 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00002   (~16.0k) empty fragments from icaruspmtwwtop03                                                      
9561 failed to start                                                                        
9562    02/20/2023 2:57 02/20/2023 12:05    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00002                                                           
Powercycled PMT boards, test without LockTemp                                                                       
9563    02/20/2023 12:25    02/20/2023 12:59    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00001    Saw one set of warnings printed ~12:52  Config without LockTemp. Check if we still see timeout warnings                                                 
Powercycled PMT boards, LockTemp config, but window_close_timeout_us set to 10sec (default was 3sec)                                                                        
9564    02/20/2023 13:14    02/20/2023 13:51    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00003   Empty fragments every minute from PMT   No timeout at all, but empty fragments                                                  
Powercycled PMT boards, Trying without LockTemp, but again window_close_timeout_us set to 10sec (default was 3sec)                                                                      
9565    02/20/2023 14:15    02/20/2023 14:53    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_00002    Two empty fragments. But stopped to test LockTemp again                                                     
Powercycled PMT boards, Trying LockTemp again                                                                       
9566    02/20/2023 15:08    02/20/2023 15:21    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00003                                                           
9567    02/20/2023 15:35    02/20/2023 16:37    Test_thr390_LockTemp_true_00002                                                         
9568    02/20/2023 16:55    02/21/2023 9:48 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00003   Beam is shortly down, good for test another config                                                      
9569    02/21/2023 10:05    02/21/2023 17:06    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00001   OM was not working, and DAQInterface printed ArtdaqSharedMemoryService  I (Jaesung) closed OM terminal, but then everything in Desktop1 disappeared                                                 
9570    02/21/2023 17:45    02/22/2023 7:00 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00001   BNB down for booster study                                                      
Router firmware upgrade                                                                     
9571    02/22/2023 10:40        Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00001       Check if DAQ/Trigger tuns after the router firmware upgrade                                                 
Special PMT peds runs  9572-3-4-5-6                                                                     
Bottom CRT test runs on DAQ_DevAreas/DAQ_12Dec2022_rhowell                                                                      
9579    02/22/2023 14:41    02/22/2023 16:25    BottomCRTTest00005  Stopped for spare CRT test                                                      
Going back to production area (DAQ_ProdAreas/DAQ_24Jan2023REL); We are testing spare top CRT                                                                        
9580    02/22/2023 17:03    02/22/2023 17:41    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00005   Stopped for another test                                                        
BNB is back                                                                     
Moving to DAQ_DevAreas/DAQ_14Feb2023GAL for common PMT code test                                                                        
9581    02/22/2023 17:58    02/22/2023 18:17    Test_thr390_LockTemp_true_new_common_code_00004 Lost process from icarus-evb02-daq                                                      
Going back to production area (DAQ_ProdAreas/DAQ_24Jan2023REL)                                                                      
9582    02/22/2023 19:04    02/22/2023 21:32    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_00005   Stopped to test new pmt ped config                                                      
9583    02/22/2023 21:45    02/23/2023 2:22 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00003   icarustpcee15                                                       
TPCPSEE17 fuse blown                                                                        
9587    02/23/2023 4:23 02/24/2023 9:05 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00003   Stopped to test new pedestals                                                       
9588    02/24/2023 9:28 02/24/2023 15:54    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00004   pmt02 server rebooted and run crashed                                                       
9589    02/24/2023 16:50    02/27/2023 0:48 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00004   (~109k) DAQ interface closed accidentally                                                       
9590    02/27/2023 2:22 02/28/2023 13:09    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00004   (~69.5k) Stopped to change config                                                       
Below are ADC threshold test configs                                                                        
9591    02/28/2023 13:22    02/28/2023 15:19    Physics_General_thr300_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00001   Reached 2hr duration                                                        
9592    02/28/2023 15:40    02/28/2023 17:00    Physics_General_thr500_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00001   NuMI arrived    NuMI turned on                                                  
NuMI back (02/28/2023 16:50)                                                                        
9593    02/28/2023 17:12    03/01/2023 3:42 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00005   (~24k) DAQ interface closed accidentally    Third iteration of PMT ped values                                                   
9594    03/01/2023 4:03 03/03/2023 8:45 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00005   (~129k) Back-pressure warnings                                                      
9595    03/03/2023 9:00 03/04/2023 2:11 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00005   (~41.7k) Server reboot: icarus-tpc20-daq (4 crates)                                                     
9596    -   -   Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   Fuse blown icarus_tpcps_ee18_p82                                                        
TPCPSEE18 fuse blown, and replaced                                                                      
9597    03/03/2023 4:20 03/04/2023 18:12    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   (~32.9k) No beam due to LINAC issue                                                     
9598    03/04/2023 18:25    03/04/2023 21:43    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 (~47.4k) Beam is back                                                       
9599    03/04/2023 21:57    03/07/2023 2:06 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   (~123k) we09 fuse blown                                                     
9600    03/07/2023 2:21 03/07/2023 2:23 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   immediately stopped to exclude we09                                                     
9601    03/07/2023 2:38 03/07/2023 7:39 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   Stopped for TPC PS replacement  tpcew09 was excluded from the components                                                    
TPCPSWE09 fuse blown, and replaced                                                                      
9602    03/07/2023 8:20 03/08/2023 7:58 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   Beam down time scheduled today. But it looks like is was down since 7am                                                     
Below are bottom CRT test runs on DAQ_DevAreas/DAQ_12Dec2022_rhowell                                                                        
9603    03/08/2023 8:26 03/08/2023 9:30 BottomCRTTest00005  Stopped after 1 hr                                                      
Below is a test for common pmt code + new CAEN libraries; DAQ_DevAreas/DAQ_28Feb2023GAL                                                                     
9604    03/08/2023 10:13    03/08/2023 10:16    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00008   Stopped This config does not have increased stale_fragment_timeout and window_close_timeout_us                                                  
9605    03/08/2023 10:30    03/08/2023 10:43    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00009                                                           
9606    03/08/2023 11:08    03/08/2023 11:25    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00009                                                           
9607    03/08/2023 11:42    03/08/2023 12:33    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00010       "The unknown trigger name is: pwrite (from trigger-path specification: pwrite" errprs are printed                                                   
9608    03/08/2023 12:50    03/08/2023 13:01    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00011                                                           
9609    03/08/2023 13:14    03/08/2023 18:43    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00012                                                           
Going back to production area (DAQ_ProdAreas/DAQ_24Jan2023REL)                                                                      
Beam is back (03/08/2023 18:55)                                                                     
9610    03/08/2023 19:05    03/09/2023 0:01 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   Power glitch around 00:00                                                       
Power glitch occured, recovering the detector                                                                       
Rebooted WRS until TAI-UTC = 37 sec                                                                     
9624    3/9/2023 20:07  3/9/2023 20:12  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   Stopped to run calibration  Finally we see triggers!!                                                   
9625    3/9/2023 20:23  3/9/2023 20:39  Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 DAQ VNC issue..                                                         
9626    3/9/2023 21:19  03/10/2023 11:44    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 PMT volatge was fixed 5am today. We need a fresh run start to analyzer the data                                                     
9627    03/10/2023 11:57    03/10/2023 15:07    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 Stopped for laser runs                                                      
Below is PMTLaser runs                                                                      
9628    03/10/2023 15:15    03/10/2023 15:32    PMTlaser00032                                                           
9629    03/10/2023 15:36    03/10/2023 15:53    PMTlaser00032                                                           
9630    03/10/2023 15:59    03/10/2023 16:16    PMTlaser00032                                                           
Back to Calibration                                                                     
9631    03/10/2023 16:31    03/13/2023 12:01    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011                                                         
DAQ test at DAQ_DevAreas/DAQ_28Feb2023GAL                                                                       
9632    03/13/2023 12:10    03/13/2023 12:29    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00011       DAQ test runs                                                   
9633    03/13/2023 12:54    03/13/2023 13:15    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00013       DAQ test runs                                                   
Back to production, DAQ_ProdAreas/DAQ_24Jan2023REL                                                                      
TPC05 swapped to TPC06                                                                      
9634    03/13/2023 15:10    03/13/2023 15:35    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011     Validating TPC05->06 swap                                                   
Below is Trigger LVDS test                                                                      
9635    03/13/2023 16:44    03/13/2023 16:50    Physics_General_thr300_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00002                                                           
9636    03/13/2023 16:54    03/13/2023 17:06    Physics_General_thr350_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00001                                                           
9637    03/13/2023 17:09    03/13/2023 17:20    Physics_General_thr300_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00002                                                           
9638    03/13/2023 17:29    03/13/2023 17:39    Physics_General_thr400_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00001                                                           
9639    03/13/2023 17:43    03/13/2023 17:53    Physics_General_thr450_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00001                                                           
9640    03/13/2023 17:57    03/13/2023 18:08    Physics_General_thr500_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00002                                                           
9641    03/13/2023 18:12    03/13/2023 18:49    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
NuMI returns aroune 18:20 (BNB still not coming)                                                                        
9642    03/13/2023 19:17    03/13/2023 22:34    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   No beam, stopped for daq test                                                       
DAQ test at DAQ_DevAreas/DAQ_28Feb2023GAL                                                                       
9643    03/13/2023 22:55    03/13/2023 23:00    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00013   tpc05 to 06 swap was not applied in known boardreader list, thus missing fragments                                                      
9644    03/13/2023 23:16    03/13/2023 23:37    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00013       tpc04 (ww03-06 are excluded)                                                    
9645    03/13/2023 23:51    03/14/2023 0:06 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00014   Stopped NuMI is back                                                        
Back to production, DAQ_ProdAreas/DAQ_24Jan2023REL                                                                      
9646    03/14/2023 0:19 03/15/2023 13:04    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   NuMI is down, switching Calibration                                                     
9647    03/15/2023 13:25    03/15/2023 13:57    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 NuMI is back (BNB should be back soon as well)                                                      
9648    03/15/2023 14:12    03/15/2023 16:12    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   icaruspmteebot02                                                        
9649    03/15/2023 16:37    03/16/2023 9:33 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   LINAC tank 5 vaccum issue, both beams are down                                                      
Trigger test started below                                                                      
9650    03/16/2023 9:44 03/16/2023 9:56 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
Trigger test on-going, moved to DAQ_DevAreas/DAQ_15Mar2023DT                                                                        
9651    03/16/2023 11:06    03/16/2023 11:07    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9652    03/16/2023 11:31    03/16/2023 11:33    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9653    03/16/2023 11:40    03/16/2023 11:41    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9654    03/16/2023 11:54    03/16/2023 11:55    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9655    03/16/2023 12:01    03/16/2023 12:02    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
Below is Laser runs                                                                     
9656    03/16/2023 12:39    03/16/2023 12:51    PMTlaser00032                                                           
9657    03/16/2023 12:58    03/16/2023 13:07    PMTlaser00032                                                           
Back to production, DAQ_ProdAreas/DAQ_24Jan2023REL                                                                      
9658    03/16/2023 13:43    03/16/2023 15:34    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011                                                         
Trigger test restarted, moved to DAQ_DevAreas/DAQ_15Mar2023DT                                                                       
9659    03/16/2023 16:20    03/16/2023 16:21    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9660    03/16/2023 16:48    03/16/2023 16:49    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9661    03/16/2023 17:09    03/16/2023 17:10    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9662    03/16/2023 17:25    03/16/2023 17:26    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9663    03/16/2023 17:38    03/16/2023 17:39    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9664    03/16/2023 17:50    03/16/2023 17:51    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9665    03/16/2023 18:16    03/16/2023 18:17    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9666    03/16/2023 18:32    03/16/2023 18:33    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9667    03/16/2023 18:49    03/16/2023 18:50    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9668    03/16/2023 19:03    03/16/2023 19:04    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9669    03/16/2023 19:11    03/16/2023 19:16    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9670    03/16/2023 19:27    03/16/2023 19:28    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9671    03/16/2023 19:34    03/16/2023 19:35    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
Back to production, DAQ_ProdAreas/DAQ_24Jan2023REL                                                                      
9672    03/16/2023 19:48    03/17/2023 11:19    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011                                                         
9673    03/17/2023 12:22    03/17/2023 12:23    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9674    03/17/2023 12:41    03/17/2023 12:58    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9675    03/17/2023 13:14    03/17/2023 15:57    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011                                                         
Trigger test restarted, moved to DAQ_DevAreas/DAQ_                                                                      
9676    03/17/2023 16:05    03/17/2023 16:22    PMTlaser00032                                                           
9677    03/17/2023 16:26    03/17/2023 16:35    PMTlaser00032                                                           
9678    03/17/2023 16:39    03/17/2023 16:48    PMTlaser00032                                                           
9679    03/17/2023 17:00    03/17/2023 17:06    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9680    03/17/2023 17:16    03/17/2023 17:17    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9681    03/17/2023 17:27    03/17/2023 17:28    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9682    03/17/2023 17:33    03/17/2023 17:42    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9683    03/17/2023 17:47    03/17/2023 17:49    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9684    03/17/2023 18:02    03/17/2023 18:06    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9685    03/17/2023 18:25    03/17/2023 18:28    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006                                                           
9686    03/17/2023 18:36    03/17/2023 18:37    Physics_General_thr380_Majority_5_10_nb_OverlappingWindow_00001                                                         
Back to production, DAQ_ProdAreas/DAQ_24Jan2023REL                                                                      
9687    03/17/2023 18:49    02/17/2023 19:07    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 bnb is back, switch to physics run                                                      
9688    03/17/2023 19:22    03/18/2023 9:28 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   bnb out                                                     
9689    03/18/2023 9:49 03/18/2023 10:27    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 bnb back                                                        
9690    03/18/2023 10:41    03/20/2023 4:58 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   no EW signals run restarted by shifter                                                      
9691    03/20/2023 5:15 03/20/2023 8:42 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   hardware on daq02 restart                                                       
9692    03/20/2023 9:05 03/20/2023 11:15    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   lost processes in tpc11-daq                                                         
9693    03/20/2023 11:29    03/20/2023 17:53    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   PMT empty fragments                                                     
9694    03/20/2023 18:13    03/21/2023 19:06    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   OM freeze                                                       
9695    03/21/2023 19:20    03/22/2023 7:51 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   PMT error                                                       
9696    03/22/2023 8:11 03/23/2023 5:29 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   beams out, switch to calibration                                                        
9697    03/23/2023 5:47 03/23/2023 8:45 calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 PMT daq test                                                        
9698    03/23/2023 9:51 03/23/2023 21:01    calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011                                                         
9699    03/23/2023 21:21    03/25/2023 16:04    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   PMT server reboot/ PMT error, PMT crates are powercycled                                                        
9700    03/25/2023 17:21    03/27/2023 18:59    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   tpc test                                                        
9701    03/27/2023 19:23    03/27/2023 19:43    tpctest_internalpulse_t2_0x0000-00001                                                           
9702    03/27/2023 19:53    03/27/2023 21:31    tpctest_internalpulse_t2_0x0000-00001                                                           
9703    03/27/2023 20:27    03/27/2023 21:31    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 Beam on                                                     
9704    03/27/2023 21:45    03/29/2023 6:09 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   Beam downtime                                                       
9705    03/29/2023 6:22 03/29/2023 9:01 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 Stopped for network cable arrangement                                                       
                DAQ test                                                        
9710    03/29/2023 14:33    03/29/2023 14:54    tpctest_internalpulse_t2_0x0000-00001   tpc response test                                                       
9711    03/29/2023 15:04    03/29/2023 15:23    tpctest_internalpulse_t2_0x4000-00001   tpc response test                                                       
9712    03/29/2023 15:33    03/29/2023 15:51    tpctest_internalpulse_t2_0x2000-00001   tpc response test                                                       
9713    03/29/2023 16:02    03/29/2023 16:23    tpctest_internalpulse_t2_0x1000-00001   tpc response test                                                       
9714    03/29/2023 16:39    03/29/2023 19:28    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00011 Beam back switch to Physics                                                     
9715    03/29/2023 19:42    03/30/2023 17:44    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   PMT empty fragement events increasing                                                       
9716    03/30/2023 17:57    03/31/2023 3:48 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   increasing PMT% empty fragment                                                      
9717    03/31/2023 4:17 03/31/2023 10:18    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   bnb down, tpc response test                                                     
9718    03/31/2023 10:34    03/31/2023 10:55    tpctest_internalpulse_t2_varied1-00001  tpc response test                                                       
9719    03/31/2023 11:06    03/31/2023 11:27    tpctest_internalpulse_t2_varied2-00001  tpc response test                                                       
9720    03/31/2023 11:49    03/31/2023 11:52    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   PMT fiber connected and NuMI signal checking                                                        
9721    03/31/2023 12:11    03/31/2023 22:22    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   Both beam down switch to Calibration                                                        
9722    03/31/2023 22:37    03/31/2023 22:46    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00012 Beam back switch to Physics                                                     
9723    03/31/2023 23:00    04/01/2023 10:45    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   Beam down swith to Calibration                                                      
9724    04/01/2023 10:59    04/01/2023 13:07    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00012 Beam back switch to Physics                                                     
9725    04/01/2023 13:24    04/03/2023 12:51    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   PMT readout error (ECL #141638)                                                     
9726    04/03/2023 13:13    04/04/2023 1:33 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   this run is started without "wr" component. (ECL #141641), run ended with PMT, PMT03 server reboot (ECL #141738)                                                        
9727    04/04/2023 1:53 04/04/2023 1:55 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   this run was started w.o. "wr" by mistake and immediately stopped.                                                      
9728    04/04/2023 2:07 04/04/2023 12:30    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   stoppoing the run during an intermittent down time for nfs server change (ECL #141837),                                                     
9729    04/04/2023 12:53    04/06/2023 22:13    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   *warning TPC server ew02 temp. (ECL #141909), run ended due to OM crash (ECL #142260, ECL #142261)                                                      
9730    04/06/2023 22:39    04/08/2023 1:54 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   run ended due to pmt02 server reboot (ECL #142471)                                                      
9731    04/08/2023 2:27 04/09/2023 20:20    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   run ended due to DAQ warnings (ECL #142802)                                                     
9732    04/09/2023 20:43    04/10/2023 17:19    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   run restarted due to back pressure warning and OM freeze (ECL #142961)                                                      
9733    04/10/2023 17:33    04/11/2023 8:05 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   switching to calibration run                                                        
9734    04/11/2023 8:20 04/11/2023 8:50 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00012 run stopped for ODH debugging (ECL #143095)                                                     
9735    04/11/2023 10:58    04/12/2023 7:41 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   run stopped due to no triggers (ECL #143258)                                                        
9736-9742               debuggins runs (ECL #143271)                                                        
9743    04/12/2023 10:24    04/12/2023 15:19    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   back pressure warnings, OM stopped (ECL #143307)                                                        
9744    04/12/2023 15:32    04/13/2023 11:15    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   back pressure warnings OM stopped (ECL #143469)                                                     
9745    04/13/2023 11:32    04/14/2023 8:03 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   back pressure warnings, OM stopped (ECL #143602)                                                        
9746    04/14/2023 8:44 04/17/2023 9:38 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   run crashed, back pressure warnings (ECL #144058)                                                       
9747    04/17/2023 10:50    04/18/2023 14:02    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00006   run stopped for TPC filter installation                                                     
Beginning Electronics Filter Installation in Induction 1 (Start with West Cryostat)                                                                     
9748    04/18/2023 14:16    04/18/2023 15:11    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   [WEST cryo only] TPC noise filter installation in east mincrates, run restarted TPC/PMT OM                                                      
9749    04/18/2023 15:21    04/18/2023 17:42    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   [WEST cryo only] TPC noise filter installation in east mincrates                                                        
Running with ALL PARTS after Filter Installation in West Cryostat                                                                       
9750    04/18/2023 17:53    04/19/2023 7:59 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   running with all parts.                                                     
4/19/23 8 AM CDT East Cryostat Electronics Filter Installation in Induction 1                                                                       
9751    04/19/2023 8:11 04/19/2023 12:13    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   [EAST cryo only] TPC noise filter installation in west mincrates                                                        
Running with ALL PARTS after Filter Installation in East Cryostat                                                                       
9752    04/19/2023 12:25    04/20/2023 2:41 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   running with all parts. (this run crashed. lost process in eventbuilder ECL #144521)                                                        
9753    04/20/2023 3:13 04/20/2023 10:42    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
Running without EE01B                                                                       
9754    04/20/2023 10:55    04/20/2023 12:12    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   running without EE01B                                                       
Running with ALL PARTS                                                                      
9755    04/20/2023 12:25    04/20/2023 15:16    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   EE01B back-in, run stopped to exclude WE18                                                      
Running without WE18                                                                        
9756    04/20/2023 15:28    04/20/2023 16:26    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
Running without WE02                                                                        
9757    04/20/2023 16:40    04/20/2023 17:45    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   WE18 in , WE02 out                                                      
Running with ALL PARTS                                                                      
9758    04/20/2023 17:57    04/21/2023 0:47 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   TPC PS out                                                      
9759    04/21/2023 1:37 4/21/2023 5:30  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   This run was missing 576 wires due to PS out                                                        
9760    4/21/2023 5:46  04/21/2023 8:03 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   restart without WE08 which has blown fuse issue until onsite experts can intervene                                                      
Running with WEST only                                                                      
9761    04/21/2023 8:15 04/21/2023 9:37 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   noise filter installation on the east minicrates. WW02 tpc ps replaced after this run                                                       
Running with ALL PARTS                                                                      
9762    04/21/2023 10:12    04/21/2023 23:38    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Run ended due to PMT boardreader crash (A3818 general fault)                                                        
9763    04/22/2023 0:13 04/25/2023 10:36    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Run ended due to PMT boardreader crash (A3818 general fault)                                                        
9764    04/25/2023 11:05    04/25/2023 20:27    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Run ended due to PMT boardreader crash (A3818 general fault)                                                        
9765    04/25/2023 21:36    04/26/2023 5:37 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   TPC PS out                                                      
9766    04/26/2023 6:26 04/26/2023 6:43 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   This run started without tpcps_ee_07                                                        
LINAC/Booster study day (No beam) Trigger test                                                                      
9767    04/26/2023 9:04 04/26/2023 9:19 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Trigger test run                                                        
9768    04/26/2023 9:32 04/26/2023 9:40 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Trigger test run                                                        
9769    04/26/2023 9:58 04/26/2023 10:06    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Trigger test run                                                        
9770    04/26/2023 10:19    04/26/2023 10:28    Test_labview_stop_majority_3_00001  Trigger test run                                                        
9771    04/26/2023 11:34    04/26/2023 11:37    Test_labview_stop_majority_7_9_00001    Trigger test run                                                        
9772    04/26/2023 11:49    04/26/2023 12:06    PMTlaser00032   Laser calibration run                                                       
9773    04/26/2023 12:12    04/26/2023 12:29    PMTlaser00032   laser calibration run                                                       
9774    04/26/2023 13:08    04/26/2023 13:13    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Trigger test run                                                        
9775    04/26/2023 13:35    04/26/2023 13:38    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Trigger test run                                                        
9776    04/26/2023 13:57    04/26/2023 14:18    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00012 Trigger test run                                                        
9777    04/26/2023 14:10    04/26/2023 14:18    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00012 Trigger test run                                                        
9778    04/26/2023 14:31    04/26/2023 14:32    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Trigger test run                                                        
DAQ test                                                                        
9779    04/26/2023 15:08    04/26/2023 15:37    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00001                                                          
9780    04/26/2023 15:51    04/26/2023 17:26    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00001  Beam came back                                                      
9781    04/26/2023 17:42    04/27/2023 10:10    Physics_General_thr390_Majority_5%_9_OverlappingWondow_wr_0_LockTemp_newpeds_win_10s_DAQTest00001   Run 9780 and 9781 are data-taking runs as long as the new DAQ prod area is validated.                                                       
DAQ/trigger test (good for physics)                                                                     
9782    04/27/2023 10:27    04/27/2023 10:34    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9783    04/27/2023 10:48    04/27/2023 11:21    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9784    04/27/2023 11:35    04/27/2023 11:48    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9785    04/27/2023 12:12    04/27/2023 12:16    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9786    04/27/2023 12:31    04/27/2023 12:42    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9787    04/27/2023 12:56    04/27/2023 13:02    Test_labview_stop_majority_7_9_00001                                                            
9788    04/27/2023 13:16    04/27/2023 15:00    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9789    04/27/2023 15:13    04/27/2023 15:18    Test_labview_stop_majority_3_00001                                                          
9790    04/27/2023 15:33    04/27/2023 15:35    Test_labview_stop_majority_12_9_00001                                                           
Back to production                                                                      
9791    04/27/2023 15:52    04/27/2023 19:50    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Incresaing PMT empty fragment                                                       
9792    04/27/2023 20:06    04/29/2023 7:48 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   switching to calibration                                                        
9793    04/29/2023 8:03 04/29/2023 9:05 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00012 switching to physics                                                        
9794    04/29/2023 9:19 04/30/2023 5:18 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   switching to calibration                                                        
9795    04/30/2023 5:32 04/30/2023 10:21    Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00012 switching to physics                                                        
9796    04/30/2023 11:05    05/02/2023 10:40    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Beams are down,                                                     
DAQ/trigger test + PMT synchronization check                                                                        
9798    05/02/2023 11:20    05/02/2023 11:20    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9799    05/02/2023 11:26    05/02/2023 11:27    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9800    05/02/2023 11:31    05/02/2023 11:32    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9801    05/02/2023 11:45    05/02/2023 11:49    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9802    05/02/2023 11:53    05/02/2023 11:56    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9803    05/02/2023 12:01    05/02/2023 12:09    Test_labview_stop_majority_12_9_00001                                                           
9804    05/02/2023 12:43    05/02/2023 12:50    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9805    05/02/2023 13:01    05/02/2023 13:03    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
9806    05/02/2023 13:13    05/02/2023 13:21    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
Back to production                                                                      
9807    05/02/2023 14:00    05/04/2023 23:55    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015                                                           
run 9808-9813 : debugging                                                                       
Production                                                                      
9814    05/05/2023 5:17 05/05/2023 8:29 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   this run used west-cryo only                                                        
run 9815-9833 are debugging                                                                     
Production                                                                      
9834    05/05/2023 15:21    05/05/2023 22:55    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   PMT boardreader crash                                                       
9835    05/05/2023 23:25    05/06/2023 2:58 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   Both beams gone, switch to calibration                                                      
9836    05/06/2023 3:11 05/06/2023 3:27 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_00012 switching back to physics                                                       
9837    05/06/2023 3:55 05/08/2023 19:20    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   DAQ issue                                                       
9838    05/08/2023 19:49    05/10/2023 15:08    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   constant CRT warning                                                        
9839    05/10/2023 16:09    05/10/2023 16:24    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   this run excluded the CRT part with issues (crttop01L01)                                                        
9840    05/10/2023 16:52    05/11/2023 12:10    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   the CRT part is included back in                                                        
9841    05/11/2023 12:25    05/11/2023 13:49    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   [CRT board replacement during this run], crttop01L01, crttop03ET excluded from this run                                                     
Starting from now Top CRTs with mac5 165 and 212 need to be recalibrated since the FEB were replaced.                                                                       
9842    05/11/2023 14:04    05/11/2023 14:14    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_00015   CRT replaced. back in                                                       
DAQ new release test (thses runs should be good for physics)                                                                        
9843    05/11/2023 14:33    05/11/2023 14:41    Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9844    05/11/2023 14:53    5/13/2023 11:53 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    PMT BR crash, under investigation                                                       
9845 and 9846 are PMT debugging efforts on 5/13/23                                                                      
9847    05/13/2023 15:30    5/14/2023 15:00 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    Stopped due to no beams for >30 minutes                                                     
9848    05/14/2023 15:10    5/14/2023 17:57 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00002  Calibration run due to beam downtime                                                        
9849    5/14/2023 18:20 5/15/2023 7:55  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    Restart after return of beams, stopped after beams down for planned outage                                                      
9850    5/15/2023 8:05  5/15/2023 10:53 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00002  Calibration due to planned outage, stopped when beam returned                                                       
9851    5/15/2023 11:05 5/16/2023 14:13 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9852    5/16/2023 14:28 5/16/2023 14:31 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    DAQ quick test to test new DAQInterface version, still issues with log messages                                                         
9853    5/16/2023 14:46 5/16/2023 15:03 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    Had issues reverting to previous area with new DAQInterface version                                                     
9854    5/16/2023 15:19 5/17/2023 9:25  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    Production release version with old DAQInterface version, run with this until issues worked out, stopped due to PMT inc. events                                                     
9855    5/17/2023 9:36  5/17/2023 12:43 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    Stop run due to planned beam outage                                                     
9856 and 9857 are DAQInterface log tests during beam outage                                                                     
9858    5/17/2023 15:11 5/17/2023 15:13 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9859    5/17/2023 15:57 5/17/2023 17:16 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9860    5/17/2023 17:25:00  5/18/2023 2:24  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    Beam returns, stopped due to 1 hour beam outage overnight                                                       
9861    5/18/2023 2:30  5/18/2023 3:56  Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00002  stopped when beam returned 5/18 4:25 AM CDT                                                     
9862    5/18/2023 4:07  5/18/2023 8:35  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    beam returns, stopped again due to beam outage                                                      
9863    5/18/2023 8:57  5/18/2023 10:14 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00002  Initial calibration run during unplanned >= 4 hour beam outage                                                      
9864-9865 are ???                                                                       
9866    5/18/2023 11:10 5/18/2023 11:15 Laser run   laser run                                                       
9867    5/18/2023 11:43 5/18/2023 15:35 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    BNB returns, stopped when notified of more issues with sump pumps at the Booster, beam down again                                                       
9868    5/18/2023 15:50 5/18/2023 15:36 Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00002                                                          
9869    5/18/2023 15:49 5/18/2023 17:40 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9870    5/18/2023 18:53 5/19/2023 5:00  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    beams down again                                                        
9871    5/19/2023 5:16  5/19/2023 5:54  Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00002                                                          
Run 9872-9891 likely have bad NuMI data due to change in $AD timing relative to RWM causing no opening of large gate for out-of-spill scint. activity                                                                       
9872    5/19/2023 6:10  5/21 16:56  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    beam returns, stopped when DAQInterface accidentally closed by shifter                                                      
9873    5/21/2023 17:35 5/23/2023 1:12  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    incomplete events, pointing to blown TPC power supply fuse on ee05                                                      
9874    5/23/2023 1:23  5/23/2023 2:09  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    likely not good EE data, had a blown PS fuse on ee05                                                        
9875    5/23/2023 2:23  5/23/2023 7:15  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    removed ee05 from the run due to blown fuse                                                     
9876    5/23/2023 7:40  5/23/2023 11:32 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    replaced ee05 PS, running with all components                                                       
9877-9885 are PMT debugging efforts after server self-reboot and subsequent causality warning clearing                                                                      
9886    5/23/2023 17:38 5/24/2023 11:31 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9887    5/24/2023 11:45 5/24/2023 11:58 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    test? not good for physics analysis                                                     
9888    5/24/2023 12:07 5/24/2023 12:09 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    test?                                                       
9889    5/24/2023 12:21 5/24/2023 16:43 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9890    5/24/2023 16:56 5/24/2023 18:43 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9891    5/24/2023 18:57 5/24/2023 19:32 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9892    5/24/2023 19:45 5/25/2023 2:04  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9893    5/25/2023 2:18  5/25/2023 2:26  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9894    5/25/2023 2:41  5/26/2023 8:37  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002                                                            
9895    5/26/2023 8:57  5/26/2023 9:28  Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    test                                                        
9896    5/26/2023 9:59  5/26/2023 16:00 Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    Stopped when both beams went down due to labwide work stoppage                                                      
runs 9897-9910 are trigger test runs                                                                        
9911    5/28/2023       Calibration_MINBIAS_BNB_Thr400_Majority10_FixedWindow_4Hz_DAQTest00002  Calibration running with beams down                                                     
9912                                                                        
BNB returns! 10:45 AM on 6/1/2023                                                                       
9913    6/1/2023        Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    no log file start message...                                                        
9914    6/1/2023 12:48      Physics_General_thr390_Majority_5_9_OverlappingWindow_wr_0_LockTemp_newpeds_win_10s_DAQTest00002    restored start message in log file                                                      """

rundatedat_RunA = [s.split("    ")[:2] for s in rundate_str_RunA.split("\n")]

rundate_RunA = []
for r, d in rundatedat_RunA:
    try:
        d = datetime.strptime(d.split(" ")[0], "%m/%d/%Y")
        r = int(r)
    except:
        continue
    rundate_RunA.append((r, d))

rundate_Run1 = []

for run, date in map(lambda s: s.split(","), rundatestr_Run1):
    run = int(run)
    date = datetime.strptime(date.split(" ")[1], "%m/%d/%Y")
    rundate_Run1.append((run, date))

rundatedat_Run2 = [s.split("    ")[:2] for s in rundatestr_Run2.split("\n") if s[0] == "9"]

rundate_Run2 = []
for r, d in rundatedat_Run2:
    try:
        d = datetime.strptime(d.split(" ")[0], "%m/%d/%Y")
        r = int(r)
    except:
        continue
    rundate_Run2.append((r, d))

run2date = dict(rundate_RunA + rundate_Run1 + rundate_Run2)
