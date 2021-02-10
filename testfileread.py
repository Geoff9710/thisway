#file input test
#include python libraries
import csv
import sys

#import scipy, scipy.stats.chisquare
import math
#import scipy
#initialize variables
col_1 = "CompanyName"
col_2 = "RegisteredNumber"
col_3 ="Date Incorporated"
col_5 ="Years In Business"
col_9 = "100" #Credit Limit 1
col_10 = "100" #Credit Limit 2
col_14 = 999
col_15 = "N/A"
col_16 = 1
col_17 = 1
col_18 = 1
col_31 = 1
col_32 = 1
col_36 = 1
col_41 = 1
col_44 = 1
col_47 = 1
col_50 = 1
col_53 = 1
col_56 = 1
col_59 = 1
col_62 = 1
col_65 = 1
col_68 = 1
col_71 = 1
col_74 = 1
col_75 = 1
col_78 = 1
col_80 = 1
col_81 = 1
col_82 = 1
col_83 = 1
col_84 = 1
col_85 = 1
col_86 = 1
col_87 = 1
col_88 = 1
col_89 = 1
col_90 = 1 # somewhere in the Delphi score set
col_91 = 1
col_92 = 1
col_93 = 1
col_94 = 1
col_95 = 1
col_96 = 1
col_97 = 1
col_98 = 1
col_99 = 1
col_100 = 1
col_101 = 1
col_102 = 1
col_103 = 1
col_104 = 1
col_105 = 1
col_106 = 1
col_107 = 1
col_108 = 1
col_109 = 1
col_110 = 1
col_111 = 1
col_112 = 1
col_113 = 1
col_115 = 1
col_116 = 1
col_117 = 1
col_118 = 1
col_119 = 1
col_120 = 1
col_121 = 1
col_122 = 1
col_123 = 1
col_124 = 1
col_125 = 1
col_126 = 1
col_127 = 1
col_128 = 1
col_129 = 1
col_130 = 1
col_131 = 1
col_132 = 1
col_133 = 1
col_134 = 1
col_135 = 1
col_136 = 1
col_137 = 1
col_138 = 1
col_139 = 1
col_140 = 1
col_141 = 1
col_142 = 1
col_143 = 1
col_144 = 1
col_588 = 1
col_589 = 1
col_593 = 1
col_594 = 1
col_595 = 1
col_596 = 1
col_597 = 1
col_598 = 1
col_599 = 1
col_600 = 1
col_601 = 1
col_602 = 1
col_603 = 1
col_604 = 1
col_605 = 1
col_606 = 1
col_607 = 1
col_608 = 1
col_609 = 1
col_610 = 1
col_611 = 1
col_612 = 1
col_613 = 1
col_614 = 1
col_615 = 1
col_616 = 1
col_617 = 1
col_618 = 1
col_619 = 1
col_620 = 1
col_621 = 1
col_622 = 1
col_623 = 1
col_624 = 1
col_625 = 1
col_626 = 1
col_627 = 1
col_628 = 1
col_629 = 1
col_630 = 1



mean1=  1.1
mean2 = 1.1
chi1 = 1.1
chi2 = 1.1
chi_mean = 1.1
counter1 = 0
smooth_sd_factor = 1
smooth_total = 0
smooth_mean = 1
trend_total = 0
comparison_trend = 1
trend_difference = 0
trending_count = 0
pearson_chi_square_mean = 1
test_list_flat =[]
test_list_down = []
test_list_up =[]
dbt_trend_score = 0
delphi_trend_score = 1
credit_limit_trend_score = 1
ecl = " "
other_co_delphi_trend_score = 1
all_co_delphi_trend_score = 1
same_industry_delphi_trend_score = 1
same_asset_delphi_trend_score = 1
same_age_delphi_trend_score = 1
industry_dbt_trend_score = 1

list_test = ["HOMEFUELS DIRECT LTD",6464646,"4-Jan-08","70-74 BRUNSWICK STREET, STOCKTON ON TEES,","01642 700725","10 years 2 months "  ,"www.homefuelsdirect.com","WHOLESALE FUELS AND RELATED PRODUCTS","A below average risk company; little reason to doubt credit transactions to the limit assigned.","£ 3,400","£ 1,700","Below Average Risk","41:1","21 February 2018 at 08:56:48",78,"L",0,"L",0,0,"This company pays within its terms",17,"No Legal Notices Recorded","GBP","31/03/2017",110168,-36.09,"D",22979,-70.31,"D", 25781, -17.74, "D", 1, 1, "This Company is not part of a Group", "A below average risk company; little reason to doubt credit transactions to the limit assigned.", "Out of 100", "Below Average Risk 41:1", 93, "£9,600",3200, 95, "£9,800",3300, 84,"£7,200","£2,900",95,"£9,800","£3,300",95,"£9,800","£3,300",95,"£9,800","£3,300",92,"£9,500","£3,200",92,"£9,500","£3,200",88,"£7,600","£3,000",88,"£7,600","£3,000",78,"£3,400","£1,700",78,"£3,400","£1,700",78,"£3,400","£1,700",95,44,52,64,57,84,44,52,64,56,95,45,51,64,57,95,44,51,64,56,95,44,50,64,56,92,44,50,64,56,92,44,49,64,56,0,44,49,63,56,88,44,49,63,55,88,44,49,63,55,78,44,49,64,56,78,44,49,64,57,78,45,49,64,57,"Wholesale Trade and Commission Trade, Except of Motor Vehicles and Motorcycles","£90,000 to £150,000","Incorporated between March 2004 and March 2008","Accounts are due to be filed within the next 10 Calendar Months.  The Accounts were prepared by a Director,",42825,43101,"UK GAAP",52,"GBP",2802,0,0,0,2802,0,0,0,0,0,0,2802,0,0,0,0,50616,50175,0,0,441,53998,2752,107366,84387,65183,0,0,19090,0,0,0,0,0,0,0,114,0,22979,25781,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25781,2,0,0,0,0,0,25779,0,25781,25781,"UK GAAP",52,"GBP",0, 0, 0, 0, 0, 0,0 , 0, 0,0 ,11781,11781,0,0 ,0,0,0,0,0,0,0,0,160611,160611,83223,0,0,0,0,0,0,0,0,0,0,0,0,83223,77388,89169,57829,0,0,0,0,0,0,57829,0,0,0,0,0,0,31340,0,0,0,0,0,0,0,31340,31340,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5588,5588,0,0,0,0,0,0,0,0,0,0,126813,126813,36285,0,0,0,0,0,0,0,0,0,0,0,0,36285,90528,96116,72555,0,0,0,0,0,0,72555,0,1117,0,0,1117,0,22444,0,0,0,0,0,0,0,22444,22444,0,"UK GAAP",52,"GBP",8786,0,0,0,0,0,0,0,0,0,0,8786,0,0,0,0,52023,0,0,0,0,92572,0,144595,134958,0,0,0,0,0,0,0,0,0,0,0,0,134958,9637,18423,0,0,0,0,0,0,0,0,0,1757,0,0,1757,0,16666,2,2,0,0,0,0,16664,0,16666,16666,"We have not received any Cash Flow statements for this company",1.27,1.27,0,0,0,74.05,23.4,0,0,0,0,80,0,0,0,0,0,0.93,1.93,0,0,0,0,18.18,0,0,0,0,0,0,0,0,0,0,3.49,3.49,0,0,0,0,0,16.95,0,0,0,0,0,0,0,0,0,0,1.07,1.07,0,0,0,0,0,10.87,0,0,0,0,3196,0,0,0,0,0,0,0,0,1.27,74.05,23.4,0,0,0,0,0,0,0,0,1.93,0,18.18,0,0,0,0,0,0,0,0,-34.07,0,28.71,0,0,0,0,0,15.6,2.9,59,1.3,0,41.6,0,"N/A",39748,549985,17795,"Industry Median based on 2,955 similar companies in 1980 SIC Code 6120 - INDUSTRIAL MATERIALS WHOLESALING",0,0,0,1.27,74.05,23.4,0,0,0,0,0,0,2.8,0.4,30,1,0,7,0,"N/A",30951,279239,1034,15.6,2.9,59,1.3,0,41.6,0,"N/A",39748,549985,17795,32.6,7.3,80,2.4,173,78.9,0,"N/A",54544,1144039,49899,2,5,8,"This company pays faster than the industry average. There is a consistent payment pattern. This company has 0 accounts placed for collection. This company has 0 outstanding unpaid accounts. This company pays within its terms.",0,0,1,2,0,17,0,17,15,17,10,17,10,16,0,16,0,16,0,16,0,16,0,17,0,17,0,17,0,17,0,17,0,17,0,17,0,17,0,17,3,17,0,15,0,24,0,16,0,6,0,2,0,0,0,0,0,"This company pays its accounts on average 0 days beyond terms. The payment information we have for this company over the last 6 months available shows a consistent payment pattern.","A search of our databases has shown that there are no County Court Judgments recorded against this company","A search of our databases has shown that there are no Legal Notices recorded against this company","A search of our databases has shown that there are no Mortgages or Charges registered against this company","There are no Consumer Credit Licences registered to this company","The Company was incorporated 10 years 2 months ago.  There have been no changes in registered office in the last 12 months.","HOMEFUELS DIRECT LTD",6464646,"Private Limited",39451,"10 years 2 months","GBP 8","70-74 BRUNSWICK STREET, STOCKTON ON TEES, CLEVELAND TS18 1DW","70-74 Brunswick Street, STOCKTON-ON-TEES, Cleveland TS18 1DW","01642 700725","www.homefuelsdirect.com",6120,"INDUSTRIAL MATERIALS WHOLESALING",5151,"WHOLESALE FUELS AND RELATED PRODUCTS","FUEL TO HOMES AND BUSINESS.","STOKESLEY BUSINESS CENTRE, 51 HIGH STREET, STOKESLEY, NORTH YORKSHIRE","Total Exemption Full","31 March",42825,43131,"NICHOLE ROBERTS","This Company has no parent Company","ORD",1,8,8,"yes",100,100,"GBP","Christopher Bicknell","ORD","1.00",8,8,"GBP",100,100,"Christophe David Bicknell","Duport Director Ltd","Thomas Elles Bicknell","Duport Secretary Ltd",39457,"There are no alert notices for this company."]
#
col_594 = list_test[594]
col_596 = list_test[596]
col_598 = list_test[598]
col_600 = list_test[600]
col_602 = list_test[602]
col_604 = list_test[604]
col_606 = list_test[606]
col_608 = list_test[608]
col_610 = list_test[610]
col_612 = list_test[612]
col_614 = list_test[614]
col_616 = list_test[616]

#
print(col_594)
print(col_596)
print(col_598)
print(col_600)
print(col_602)
print(col_604)
print(col_606)
print(col_608)
print(col_610)
print(col_612)
print(col_614)
print(col_616)

# #
# # # calculate the chi-square smoothed average for the series ( removes outliers more than 1 degree of freedom)
# # #The Basic Arithmetic mean
mean1 = ((col_594 + col_596 + col_598 + col_600 + col_602 + col_604 + col_606 + col_608 + col_610 + col_612 + col_614 + col_616)/12)
print("The arithmetic mean is:")
print(mean1)
# in this case we are just looking at the DBT trend score for the same insdustry.
#
# # #The Chi smoothing 1 band
# # #χ2=n∑i=1(Oi−Ei)2Eiχ2=∑i=1n(Oi−Ei)2Ei
# # #We already know n = 13, so do not need to evaluate or use special library really.
# # # already done the sum (and divided it by 12) for the test values.
# # #
# # #we need the distribution chi square value/variance from the distribution curve from the mean
print("So Chi square sum of variances is: ")
# chi2 = ((col_594 - mean1) +(col_596 - mean1)+(col_598 - mean1)+(col_600 - mean1) +(col_602 - mean1)+(col_604 - mean1)+(col_606 - mean1)+(col_608 - mean1) +(col_610 - mean1)+(col_612 - mean1)+ (col_614 - mean1) + (col_616 - mean1)
print(chi2)
chi1 = math.sqrt(abs(chi2))
print("Here is a standard deviation")
print(chi1)
smooth_sd_factor = chi1
print("And the smooth sd factor is: ")
print(smooth_sd_factor)
#The Company values smoothed (outliers above n chi variance
# establish how many Sd's the mean of the company scores are from the chi standard deviation to use in the test.
# If the trend is up, it is bad so add to the score, if the trend is down it is good so decrease the score factor.
print(abs(col_594 - mean1))
# #
if abs(col_594 - mean1) <= (smooth_sd_factor):
    smooth_total = smooth_total + col_594
    counter1 = counter1 + 1
    print("test 594 passed")
if col_594 < col_596:
    trend_total = trend_total + 120
elif col_594 > col_596:
    trend_total = trend_total - 120
# #
if abs(col_596 - mean1) <= (smooth_sd_factor):
    smooth_total = smooth_total + col_596
    counter1 = counter1 + 1
    print(counter1)
    print("test 596 passed")

if ((col_594 + col_596)/2) <= col_598:
    trend_total = trend_total + 110
else:
    trend_total = trend_total - 110
# #
if abs(col_598 - mean1) <= (smooth_sd_factor):
     smooth_total = smooth_total + col_598
     counter1 = counter1 + 1
     print(counter1)
     print("test 598 passed")
if ((col_594 + col_596 + col_598)/3) < col_600:
    trend_total = trend_total + 100
elif ((col_594 + col_596 + col_598)/3) > col_600:
    trend_total = trend_total - 100
# #
if abs(col_600 - mean1) <= (smooth_sd_factor):
    smooth_total = smooth_total + col_600
    counter1 = counter1 + 1
    print(counter1)
    print("test 600 passed")
if ((col_594 + col_596 + col_598 + col_600)/4) < col_602:
    trend_total = trend_total + 90
elif ((col_594 + col_596 + col_598 + col_600)/4) > col_602:
    trend_total = trend_total - 90
# #
if abs(col_602 - mean1) <= (smooth_sd_factor):
    smooth_total = smooth_total + col_602
    counter1 = counter1 + 1
    print(counter1)
    print("test 602 passed")
if ((col_594 + col_596 + col_598 + col_600 + col_602)/5) < col_604:
    trend_total = trend_total + 80
else:
    trend_total = trend_total - 80
#
if abs(col_604 - mean1)<= (smooth_sd_factor):
    smooth_total = smooth_total + col_604
    counter1 = counter1 + 1
    print(counter1)
    print("test =604 passed")
if ((col_594 + col_596 + col_598 + col_600 + col_602 + col_604) / 6) < col_606:
    trend_total = trend_total + 70
elif ((col_594 + col_596 + col_598 + col_600 + col_602 + col_604) / 6) > col_606:
    trend_total = trend_total - 70

if abs(col_606 - mean1) <= (smooth_sd_factor):
    smooth_total = smooth_total + col_606
    counter1 = counter1 + 1
    print(counter1)
    print("test 606 passed")
#
if abs(col_608 - mean1) <= (smooth_sd_factor):
    smooth_total = smooth_total + col_608
    counter1 = counter1 + 1
    print(counter1)
    print("test 608 passed")
#
if abs(col_610 - mean1) <= (smooth_sd_factor):
    smooth_total = smooth_total + col_610
    counter1 = counter1 + 1
    print(counter1)
    print("test 610 passed")
#
if abs(col_612 - mean1) <= (smooth_sd_factor):
    smooth_total = smooth_total + col_612
    counter1 = counter1 + 1
    print(counter1)
    print("test 612 passed")
#
if abs(col_614 - mean1)<= (smooth_sd_factor):
    smooth_total = smooth_total + col_614
    counter1 = counter1 + 1
    print(counter1)
    print("test 614 passed")

if abs(col_616 - mean1) <= (smooth_sd_factor):
        smooth_total = smooth_total + col_616
        counter1 = counter1 + 1
        print(counter1)
        print("test 616 passed")


print(" The Smooth Total is :")
print(smooth_total)
print(" The trend Total is :")
print(trend_total)
print(counter1)

# # # # # # test_list_flat = [17,17,17,16,16,16,16,16,17,17,17,17]
# # # # # # test_list_down = [10,10,11,13,13,14,16,16,17,17,17,17]
# # # # # # test_list_up = [20,18,18,17,16,17,16,16,15,14,13,11]
# # # # # # # if max and median is greater than 1 SD above, then trend is up, else
# # # # # # #if min and median is greater than 1 SD below, then trend is down.
# # # # # # #in a 12 month pattern, it is not possible to identify seasonality completely.
# # # # # # # Evaluate  banding score based on range sets:
# # # # # # #Because of the rolling average trend factor, there are 30 possible ranges of scores, to be assigned to the percentiles -30, -20, -10, 10, 20
# # # # # # #range is over 20% up,  over 10% up, between 10% up and 10% down, between 10% down and 20% down, between 20 % down and 30% down.
# # # # # #
if smooth_mean !=0:
    if (trend_total - smooth_total) <= -230:
        industry_dbt_trend_score = 20
    elif (trend_total- smooth_total)  < -30:
        industry_dbt_trend_score =  10
    elif (trend_total- smooth_total)  < 190:
        industry_dbt_trend_score = -10
    elif (trend_total- smooth_total)  < 280:
        industry_dbt_trend_score = -20
    elif trend_total  > 280:
        industry_dbt_trend_score = -30
print(industry_dbt_trend_score)
#



#------------------------------   Old working



# col_31 = list_test[31]Working Capital
# col_32 = list_test[32]Shareholder funds
# col_40 = list_test[40]
# col_43 = list_test[43]
# col_46 = list_test[46]
# col_49 = list_test[49]
# col_52 = list_test[52]
# col_55 = list_test[55]
# col_58 = list_test[58]
# col_61 = list_test[61]
# col_64 = list_test[64]
# col_67 = list_test[67]
# col_70 = list_test[70]
# col_73 = list_test[73]
# # col_81 = list_test[81] # somewhere in the Delphi score comparisons set
# # col_88 = list_test[88]
# # #print(col_14)
# #print(col_18)
# print(col_40)
# print(col_43)
# print(col_46)
# print(col_49)
# print(col_52)
# print(col_55)
# print(col_58)
# print(col_61)
# print(col_64)
# print(col_67)
# print(col_70)
# print(col_73)
#
#
#
#
# # calculate the chi-square smoothed average for the series ( removes outliers more than 1 degree of freedom)
# #The Basic Arithmetic mean
# mean1 = ((col_40+col_43+col_46+col_49+col_52+col_55+col_58+col_61+col_64+col_67+col_70+col_73)/12)
# print("The arithmetic mean is:")
# print(mean1)
# # in this case we are just looking at the delphi score trend for the subject company.
#
# # #The Chi smoothing 1 band
# # #χ2=n∑i=1(Oi−Ei)2Eiχ2=∑i=1n(Oi−Ei)2Ei
# # #We already know n = 12, so do not need to evaluate or use special library really.
# # # already done the sum (and divided it by 12) for the test values.
# #
# # #we need the distribution chi square value/variance from the distribution curve from the mean
# print("So Chi square sum of variances is: ")
# chi2 = ((col_40 - mean1) +(col_43 - mean1)+(col_46 - mean1)+(col_49 - mean1) +(col_52 - mean1)+(col_55 - mean1)+(col_58 - mean1)+(col_61 - mean1) +(col_64 - mean1)+(col_67 - mean1)+ (col_70 - mean1) + (col_73 - mean1))
# print(chi2)
# chi1 = math.sqrt(abs(chi2))
# print("Here is a standard deviation")
# print(chi1)
# smooth_sd_factor =((mean1 * chi1)*100000)
# print("And the smooth sd factor is: ")
# print(smooth_sd_factor)
# # #The Company values smoothed (outliers above n chi variance
# # # establish how many Sd's the mean of the company scores are from the chi standard deviation to use in the test.
# # # print("The factor that the mean of the series varies from the chi square sd is:")
# # # print(smooth_sd_factor)
# # print("So the series will not include values that are +/- ")
# # print(smooth_sd_factor)
# # # Check if Company DBT values are more than the chi1 variance, and get a new smoothed average, add 1 to the counter if it does not pass the test, update the aggregator
# # #also, evaluate from the latest to the oldest whether there is an upward or a downward trend on the smoothed values.  Each subsequent older period not an outlier has a lesser impact.
# # # and use rolling averages
# print(abs(col_40 - mean1))
#
# if abs(col_73 - mean1) <=(smooth_sd_factor):
#     smooth_total = col_73
#     print("test 73 passed")
# else:
#     smooth_total = 0
# if col_73 > col_70:
#     trend_total = 120
# else:
#     trend_total = -120
#
# if abs(col_70 - mean1) <= (smooth_sd_factor):
#      smooth_total = smooth_total + col_70
#      counter1 = counter1 + 1
#      print("test 70 passed")
#
# if ((col_70 + col_73)/2) > col_67:
#     trend_total = trend_total + 110
# else:
#     trend_total = trend_total - 110
# if abs(col_67 - mean1) <= (smooth_sd_factor):
#      smooth_total = smooth_total + col_67
#      counter1 = counter1 + 1
#      print("test 67 passed")
#
# if ((col_73 + col_70 +col_67)/3) > col_64:
#     trend_total = trend_total + 100
# else:
#     trend_total = trend_total - 100
# if (col_64 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_64
#     counter1 = counter1 + 1
#     print("test 64 passed")
# if ((col_73 + col_70 + col_67 + col_64)/4) > col_61:
#     trend_total = trend_total + 90
# else:
#     trend_total = trend_total - 90
# if abs(col_61- mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_61
#     counter1 = counter1 + 1
#     print("test 61 passed")
# if ((col_73 + col_70 + col_67 + col_64 + col_61)/5) > col_58:
#     trend_total = trend_total + 80
# else:
#     trend_total = trend_total - 80
# if abs(col_58-mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_58
#     counter1 = counter1 + 1
#     print("test 58 passed")
# if ((col_73 + col_70 + col_67 + col_64 + col_61 + col_58) / 6) > col_55:
#     trend_total = trend_total + 70
# else:
#     trend_total = trend_total - 70
# if abs(col_55-mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_55
#     counter1 = counter1 + 1
#     print("test 55 passed")
# if abs(col_52 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_52
#     counter1 = counter1 + 1
#     print("test 52 passed")
# if abs(col_49- mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_49
#     counter1 = counter1 + 1
#     print("test 49 passed")
# if abs(col_46- mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_46
#     counter1 = counter1 + 1
#     print("test 46 passed")
# if abs(col_43 - mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_43
#     counter1 = counter1 + 1
#     print("test 43 passed")
# if abs(col_40 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_40
#     counter1 = counter1 + 1
#     print("test 40 passed")
# print(smooth_total)
# print(counter1)
# # compare chi-square smoothed mean to latest Delphi Score
# smooth_mean = smooth_total/counter1
# if smooth_mean > 0:
#     trend_difference = ((col_40/smooth_mean))
# # #This would eatablish a trend difference - either increases or decreses the trend based on the current period avarage score and smoothed average score difference.
# #
# print(smooth_mean)
# print(trend_difference)
# # #if there is a negative or positive trend, there will be a factor to apply to correctly position in the range buckets.
# trending_count = trend_difference * smooth_mean
# print(trending_count)
# #
# # #it is possible to score in the trend_total moving average for the last six months a value between -570 and 570.  The sample scored -570 and the scores earso that should not have an impact.
# # # a positive value of the trend_total is a bad thing in the case of DBT, as the days beyond terms are trending up for this company.  A negative value is good.
# # #If the smoothed average and the latest DBT are close, there will be a trend_difference of 0.
# # # If the Smooth Mean is lower than col_18  . trend difference may be negative, indicating that the trend was up - need to factor in the rolling average trend to this value
# # # if the smooth mean is higher than col_8, trend is positive, indicating that the DBT actually decreased as trend difference
# print(trend_total)
# # #trend_difference samples
# print(trending_count)
# # test_list_flat = [17,17,17,16,16,16,16,16,17,17,17,17]
# # test_list_down = [10,10,11,13,13,14,16,16,17,17,17,17]
# # test_list_up = [20,18,18,17,16,17,16,16,15,14,13,11]
# # # if max and median is greater than 1 SD above, then trend is up, else
# # #if min and median is greater than 1 SD below, then trend is down.
# # #in a 12 month pattern, it is not possible to identify seasonality completely.
# # # Evaluate  banding score based on range sets:
# # #Because of the rolling average trend factor, there are 30 possible ranges of scores, to be assigned to the percentiles -30, -20, -10, 10, 20
# # #range is over 20% up,  over 10% up, between 10% up and 10% down, between 10% down and 20% down, between 20 % down and 30% down.
# #
# if smooth_mean !=0:
#    if trending_count <= -230:
#         delphi_trend_score = 20
#    elif trending_count < -30:
#        delphi_trend_score =  10
#    elif trending_count < 190:
#         delphi_trend_score = -10
#    elif trending_count <280:
#         delphi_trend_score = -20
#    elif trending_count > 280:
#        delphi_trend_score = -30
# print(delphi_trend_score)
#
#
# # get the range of
# # values for the chi-square smoothed mean over last 12 months
# #col_101 = list_test[101]
# #col_588 = list_test[588]
# col_18 = list_test[18]
# col_593 = list_test[593]
# col_594 = list_test[594]
# col_595 = list_test[595]
# col_596 = list_test[596]
# col_597 = list_test[597]
# col_598 = list_test[598]
# col_599 = list_test[599]
# col_600 = list_test[600]
# col_601 = list_test[601]
# col_602 = list_test[602]
# col_603 = list_test[603]
# col_604 = list_test[604]
# col_605 = list_test[605]
# col_606 = list_test[606]
# col_607 = list_test[607]
# col_608 = list_test[608]
# col_609 = list_test[609]
# col_610 = list_test[610]
# col_611 = list_test[611]
# col_612 = list_test[612]
# col_613 = list_test[613]
# col_614 = list_test[614]
# col_615 = list_test[615]
# col_616 = list_test[616]
# #print(col_101)
# #print(col_588)
# print(col_593)
# #print(col_594) #Ind
# print(col_595)
# # #print(col_596)
# # print(col_597)
# # #print(col_598)
# # print(col_599)
# # #print(col_600)
# print(col_601)
# # #print(col_602)
# # print(col_603)
# # #print(col_604)
# # print(col_605)
# # #print(col_606)
# # print(col_607)
# # #print(col_608)
# # print(col_609)
# # #print(col_610)
# # print(col_611)
# # #print(col_612)
# # print(col_613)
# # #print(col_614)
# # print(col_615)
# # #print(col_616)
# # #print(col_18)
# # calculate the chi-square smoothed average for the series ( removes outliers more than 1 degree of freedom)
# #The Basic Arithmetic mean
# mean1 = ((col_593+col_595+col_597+col_599+col_601+col_603+col_605+col_607+col_609+col_611+col_613+col_615)/12)
# print("The arithmetic mean is:")
# print(mean1)
# #The industry trend
# mean2 = ((col_594+col_596+col_598+col_600+col_602+col_604+col_606+col_608+col_610+col_612+ col_614+col_616)/12)
# print("The industry mean is :")
# print(mean2)
# #The Chi smoothing 1 band
# #χ2=n∑i=1(Oi−Ei)2Eiχ2=∑i=1n(Oi−Ei)2Ei
# #We already know n = 12, so do not need to evaluate or use special library really.
# # already done the sum (and divided it by 12) for the test values.
#
# #we need the distribution chi square value/variance from the distribution curve from the comparison variable
# #print("So Chi square sum of variances is: ")
# chi2 = ((col_594- mean2) +(col_596- mean2)+(col_598-mean2)+(col_600-mean2) +(col_602-mean2)+(col_604-mean2)+(col_606-mean2)+(col_608-mean2) +(col_610-mean2)+(col_612-mean2)+(col_614-mean2)+(col_616-mean2))
# #print(chi2)
# chi1 = math.sqrt(chi2)
# print("Here is a standard deviation on industry average")
# print(chi1)
# smooth_sd_factor = (abs(mean2-mean1)- (mean2/2))
# print("And the smooth sd factor is: ")
# print(smooth_sd_factor)
# #The Company values smoothed (outliers above n chi variance
# # establish how many Sd's the mean of the company scores are from the chi standard deviation to use in the test.
# # print("The factor that the mean of the series varies from the chi square sd is:")
# # print(smooth_sd_factor)
# print("So the series will not include values that are +/- ")
# print(smooth_sd_factor)
# # Check if Company DBT values are more than the chi1 variance, and get a new smoothed average, add 1 to the counter if it does not pass the test, update the aggregator
# #also, evaluate from the latest to the oldest whether there is an upward or a downward trend on the smoothed values.  Each subsequent older period not an outlier has a lesser impact.
# # and use rolling averages
# print(abs(col_593 - mean1))
# print(smooth_sd_factor * mean2)
# if abs(col_593 - mean1) <=(smooth_sd_factor):
#     smooth_total = col_593
#     print("test 593 passed")
# else:
#     smooth_total = 0
# if col_593 > col_595:
#     trend_total = 120
# else:
#     trend_total = -120
# if abs(col_595 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_595
#     counter1 = counter1 + 1
#     print("test 595 passed")
# if ((col_593 + col_595)/2) > col_597:
#     trend_total = trend_total + 110
# else:
#     trend_total = trend_total - 110
# if abs(col_597 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_597
#     counter1 = counter1 + 1
#     print("test 597 passed")
# if ((col_593 + col_595+col_597)/3) > col_599:
#     trend_total = trend_total + 100
# else:
#     trend_total = trend_total - 100
# if (col_599-mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_599
#     counter1 = counter1 + 1
#     print("test 599 passed")
# if ((col_593 + col_595 + col_597 + col_599)/4) > col_601:
#     trend_total = trend_total + 90
# else:
#     trend_total = trend_total - 90
# if abs(col_601- mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_601
#     counter1 = counter1 + 1
#     print("test 601 passed")
# if ((col_593 + col_595 + col_597 + col_599+col_601)/5) > col_603:
#     trend_total = trend_total + 80
# else:
#     trend_total = trend_total - 80
# if abs(col_603-mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_603
#     counter1 = counter1 + 1
#     print("test 603 passed")
# if ((col_593 + col_595 + col_597 + col_599 + col_601 + col_601) / 6) > col_605:
#     trend_total = trend_total + 70
# else:
#     trend_total = trend_total - 70
# if abs(col_605-mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_605
#     counter1 = counter1 + 1
#     print("test 605 passed")
# if abs(col_607 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_607
#     counter1 = counter1 + 1
#     print("test 607 passed")
# if abs(col_609- mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_609
#     counter1 = counter1 + 1
#     print("test 609 passed")
# if abs(col_611- mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_611
#     counter1 = counter1 + 1
#     print("test 611 passed")
# if abs(col_613 - mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_613
#     counter1 = counter1 + 1
#     print("test 613 passed")
# if abs(col_615 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_615
#     counter1 = counter1 + 1
#     print("test 615 passed")
# print(smooth_total)
# print(counter1)
# # compare chi-square smoothed mean to latest DBT
# smooth_mean = smooth_total/counter1
# if smooth_mean > 0:
#     trend_difference = 100 -((col_18/smooth_mean)*100)
# #This would eatablish a trend difference - either increases or decreses the trend based on the current period avarage score and smoothed average score difference.
#
# print(smooth_mean)
# print(trend_difference)
# #if there is a negative or positive trend, there will be a factor to apply to correctly position in the range buckets.
# trending_count = trend_difference * smooth_mean
# print(trending_count)
#
# #it is possible to score in the trend_total moving average for the last six months a value between -570 and 570.  The sample scored -90 so that should not have an impact.
# # a positive value of the trend_total is a bad thing in the case of DBT, as the days beyond terms are trending up for this company.  A negative value is good.
# #If the smoothed average and the latest DBT are close, there will be a trend_difference of 0.
# # If the Smooth Mean is lower than col_18  . trend difference may be negative, indicating that the trend was up - need to factor in the rolling average trend to this value
# # if the smooth mean is higher than col_8, trend is positive, indicating that the DBT actually decreased as trend difference
# print(trend_total)
# #trend_difference samples
# #print(trending_count)
# test_list_flat = [17,17,17,16,16,16,16,16,17,17,17,17]
# test_list_down = [10,10,11,13,13,14,16,16,17,17,17,17]
# test_list_up = [20,18,18,17,16,17,16,16,15,14,13,11]
# # if max and median is greater than 1 SD above, then trend is up, else
# #if min and median is greater than 1 SD below, then trend is down.
# #in a 12 month pattern, it is not possible to identify seasonality completely.
# # Evaluate  banding score based on range sets:
# #Because of the rolling average trend factor, there are 30 possible ranges of scores, to be assigned to the percentiles -30, -20, -10, 10, 20
# #range is over 20% up,  over 10% up, between 10% up and 10% down, between 10% down and 20% down, between 20 % down and 30% down.
#
# if smooth_mean !=0:
#    if trending_count <= -230:
#         dbt_trend_score = 20
#    elif trending_count < -30:
#        dbt_trend_score =  10
#    elif trending_count < 190:
#         dbt_trend_score = -10
#    elif trending_count <280:
#         dbt_trend_score = -20
#    elif trending_count > 280:
#        dbt_trend_score = -30
# print(dbt_trend_score)


#sum(cost[c] * cases[c] for c in range(len(cost))) / sum(cases)
# See what `zip()` does to your `cost` and `cases`
#print(list(zip(____, ____)))

# Calculate the weighted average
#print(sum([x * y for x, y in zip(cost, cases)]) / sum(cases))

# if col_593 > col_595:
#     trending = 120
# else:
#     trending = -120
# print(trending_count)
# if ((col_593 + col595/col_593)/2) > col_595:
#       trending_count = trending_count + 110
# else:
#       trending_count = trending_count - 110

# data_line =[]
# first_limit = 1
# second_limit = 1
# ecl = "$2,000"
# rcl = "$2,000"
# lmt_range_factor = 0.0000000001
# denominator = 1  # bottom of the fraction
# numerator = 1  # top of the fraction
# shareholders_funds = 1
#ccj_value_open = 1
# col_31 = list_test[31]
# col_18 = list_test[18]
# print(col_31)
#print(col_18)
#need to extract the numbers from the value as a string with currency symbol and punctuation.
#ecl = Experian credit limit minimum of the two values, usually the first
# ecl = col_9.replace("£","")
# ecl = ecl.replace(",","")
# rcl = col_10.replace("£","")
# rcl = rcl.replace(",","")
# first_limit = int(ecl)
# second_limit = int(rcl)
# print(first_limit)
# print(second_limit)
# denominator = first_limit
# #if global(Requested_CreditLimti) != 1:
# #    denominator = global.Requested_CreditLimit
# #    numerator = first_limit
#
# lmt_range_factor = (numerator / denominator)
# print(lmt_range_factor)
# lmt_range_factor = lmt_range_factor * 100
# print(lmt_range_factor)

#lower_limit = int(col_9)
#print(lower_limit)
#exit ="False"

#years_in_business = float(1.101)
#years= float(1.0)
#months = float(0.5)
#age_string_len = len(col_5)
#print(age_string_len)
#years = float(col_5[0:2])
#print(years)
#months = float(col_5[9:11])/12
#print(months)
#years_in_business = years + months
#print(years_in_business)
#with open("Homefuels.csv", "r") as csv_file:
#    data_line = list(csv_file)[1]
#   print(list_test)
#   print(data_line)
# #Used to debug/test
#found out that the list from the csv is in an invalid format to treat as a list, there needs to be quotes on anything that is not a number.
#Evaluate if any values have been detected.
# Return in return code order (future) and call logging(future) to record.
#Used in debug/test
#    lengthlist = len(data_line)
#lengthlist = len(list_test)
#print(lengthlist)
#if lengthlist != 0:
#    data_read = 1
#    print(data_read)
#    col_1 = list_test[14]
#    print(col_1)
#    if col_1 != 999:
#        exit = "True"
#print(exit)


#Calculate years in business from text version of years in business up to report creation

#   print(list_test[1])
#    print(data_line[0])
#    print(data_line[1])
#    print(list_test[2])
#   print(data_line[2])
#    print(list_test[3])
#    print(data_line[3])
#    print(col_1)
# when the content is addressed and typed, then the list feature reads by field, and not as a character string
# so need to loop over the data_line to quote anything but integers, or collect character by  character up to the field delimeter.

  #  print(data_line)
#parse out the fields - first few are here
# Company Name,Registered Number,Date incorporated,Registered Office,Telephone Number,Age of Company,Website,Industry Type,Comment,Credit Limit,

#   for data_line ins
#
# get the range of values for over last 12 months strip out currency code and punctuation and convert to integer.
# ecl = list_test[41].replace("£","")
# #print(ecl)
# ecl = ecl.replace(",","")
# #print(ecl)
# col_41 = int(ecl)
#
# ecl = list_test[44].replace("£","")
# ecl = ecl.replace(",","")
# col_44 = int(ecl)
#
# ecl = list_test[47].replace("£","")
# ecl = ecl.replace(",","")
# col_47 = int(ecl)
#
# ecl = list_test[50].replace("£","")
# ecl = ecl.replace(",","")
# col_50 = int(ecl)
#
# ecl = list_test[53].replace("£","")
# ecl = ecl.replace(",","")
# col_53 = int(ecl)
#
# cl = list_test[56].replace("£","")
# ecl = ecl.replace(",","")
# col_56 = int(ecl)
#
# ecl = list_test[59].replace("£","")
# ecl = ecl.replace(",","")
# col_59 = int(ecl)
#
# ecl = list_test[62].replace("£","")
# ecl = ecl.replace(",","")
# col_62 = int(ecl)
#
# ecl = list_test[65].replace("£","")
# ecl = ecl.replace(",","")
# col_65 = int(ecl)
#
# ecl = list_test[68].replace("£","")
# ecl = ecl.replace(",","")
# col_68 = int(ecl)
#
# ecl = list_test[71].replace("£","")
# ecl = ecl.replace(",","")
# col_71 = int(ecl)
#
# ecl = list_test[74].replace("£","")
# ecl = ecl.replace(",","")
# col_74 = int(ecl)
#

# col_73 = list_test[73]
# col_81 = list_test[81] # somewhere in the Delphi score comparisons set
# col_88 = list_test[88]

# col_81 = 1
# col_82 = 1
# col_83 = 1
# col_84 = 1
# col_85 = 1
# col_86 = 1
# col_87 = 1
# col_88 = 1
# col_89 = 1
# col_90 = 1 # somewhere in the Delphi score set
# col_91 = 1
# col_92 = 1
# col_93 = 1
# col_94 = 1
# col_95 = 1
# col_96 = 1
# col_97 = 1
# col_98 = 1
# col_99 = 1
# col_100 = 1
# col_101 = 1
# col_102 = 1
# col_103 = 1
# col_104 = 1
# col_105 = 1
# col_106 = 1
# col_107 = 1
# col_108 = 1
# col_109 = 1
# col_110 = 1
# col_111 = 1
# col_112 = 1
# col_113 = 1
# col_115 = 1
# col_116 = 1
# col_117 = 1
# col_118 = 1
# col_119 = 1
# col_120 = 1
# col_121 = 1
# col_122 = 1
# col_123 = 1
# col_124 = 1
# col_125 = 1
# col_126 = 1
# col_127 = 1
# col_128 = 1
# col_129 = 1
# col_130 = 1
# col_131 = 1
# col_132 = 1
# col_133 = 1
# col_134 = 1
# col_135 = 1
# col_136 = 1
# col_137 = 1
# col_138 = 1
# col_139 = 1
# col_140 = 1
# col_141 = 1
# col_142 = 1
# col_143 = 1
# col_144 = 1
# col_588 = 1
# col_589 = 1
# col_593 = 1
# col_594 = 1
# col_595 = 1
# col_596 = 1
# col_597 = 1
# col_598 = 1
# col_599 = 1
# col_600 = 1
# col_601 = 1
# col_602 = 1
# col_603 = 1
# col_604 = 1
# col_605 = 1
# col_606 = 1
# col_607 = 1
# col_608 = 1
# col_609 = 1
# col_610 = 1
# col_611 = 1
# col_612 = 1
# col_613 = 1
# col_614 = 1
# col_615 = 1
# col_616 = 1
# mean1=  1.1
# mean2 = 1.1
# chi1 = 1.1
# chi2 = 1.1
# chi_mean = 1.1
# counter1 = 0
# smooth_sd_factor = 1
# smooth_total = 1
# smooth_mean = 1
# trend_total = 0
# comparison_trend = 1
# trend_difference = 0
# trending_count = 0
# pearson_chi_square_mean = 1
# test_list_flat =[]
# test_list_down = []
# test_list_up =[]
# dbt_trend_score = 0
# delphi_trend_score = 1
# credit_limit_trend_score = 1
# ecl = " "
# other_co_delphi_trend_score = 1
# all_co_delphi_trend_score = 1
#
# list_test = ["HOMEFUELS DIRECT LTD",6464646,"4-Jan-08","70-74 BRUNSWICK STREET, STOCKTON ON TEES,","01642 700725","10 years 2 months "  ,"www.homefuelsdirect.com","WHOLESALE FUELS AND RELATED PRODUCTS","A below average risk company; little reason to doubt credit transactions to the limit assigned.","£ 3,400","£ 1,700","Below Average Risk","41:1","21 February 2018 at 08:56:48",78,"L",0,"L",0,0,"This company pays within its terms",17,"No Legal Notices Recorded","GBP","31/03/2017",110168,-36.09,"D",22979,-70.31,"D", 25781, -17.74, "D", 1, 1, "This Company is not part of a Group", "A below average risk company; little reason to doubt credit transactions to the limit assigned.", "Out of 100", "Below Average Risk 41:1", 93, "£9,600",3200, 95, "£9,800",3300, 84,"£7,200","£2,900",95,"£9,800","£3,300",95,"£9,800","£3,300",95,"£9,800","£3,300",92,"£9,500","£3,200",92,"£9,500","£3,200",88,"£7,600","£3,000",88,"£7,600","£3,000",78,"£3,400","£1,700",78,"£3,400","£1,700",78,"£3,400","£1,700",95,44,52,64,57,84,44,52,64,56,95,45,51,64,57,95,44,51,64,56,95,44,50,64,56,92,44,50,64,56,92,44,49,64,56,0,44,49,63,56,88,44,49,63,55,88,44,49,63,55,78,44,49,64,56,78,44,49,64,57,78,45,49,64,57,"Wholesale Trade and Commission Trade, Except of Motor Vehicles and Motorcycles","£90,000 to £150,000","Incorporated between March 2004 and March 2008","Accounts are due to be filed within the next 10 Calendar Months.  The Accounts were prepared by a Director,",42825,43101,"UK GAAP",52,"GBP",2802,0,0,0,2802,0,0,0,0,0,0,2802,0,0,0,0,50616,50175,0,0,441,53998,2752,107366,84387,65183,0,0,19090,0,0,0,0,0,0,0,114,0,22979,25781,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25781,2,0,0,0,0,0,25779,0,25781,25781,"UK GAAP",52,"GBP",0, 0, 0, 0, 0, 0,0 , 0, 0,0 ,11781,11781,0,0 ,0,0,0,0,0,0,0,0,160611,160611,83223,0,0,0,0,0,0,0,0,0,0,0,0,83223,77388,89169,57829,0,0,0,0,0,0,57829,0,0,0,0,0,0,31340,0,0,0,0,0,0,0,31340,31340,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5588,5588,0,0,0,0,0,0,0,0,0,0,126813,126813,36285,0,0,0,0,0,0,0,0,0,0,0,0,36285,90528,96116,72555,0,0,0,0,0,0,72555,0,1117,0,0,1117,0,22444,0,0,0,0,0,0,0,22444,22444,0,"UK GAAP",52,"GBP",8786,0,0,0,0,0,0,0,0,0,0,8786,0,0,0,0,52023,0,0,0,0,92572,0,144595,134958,0,0,0,0,0,0,0,0,0,0,0,0,134958,9637,18423,0,0,0,0,0,0,0,0,0,1757,0,0,1757,0,16666,2,2,0,0,0,0,16664,0,16666,16666,"We have not received any Cash Flow statements for this company",1.27,1.27,0,0,0,74.05,23.4,0,0,0,0,80,0,0,0,0,0,0.93,1.93,0,0,0,0,18.18,0,0,0,0,0,0,0,0,0,0,3.49,3.49,0,0,0,0,0,16.95,0,0,0,0,0,0,0,0,0,0,1.07,1.07,0,0,0,0,0,10.87,0,0,0,0,3196,0,0,0,0,0,0,0,0,1.27,74.05,23.4,0,0,0,0,0,0,0,0,1.93,0,18.18,0,0,0,0,0,0,0,0,-34.07,0,28.71,0,0,0,0,0,15.6,2.9,59,1.3,0,41.6,0,"N/A",39748,549985,17795,"Industry Median based on 2,955 similar companies in 1980 SIC Code 6120 - INDUSTRIAL MATERIALS WHOLESALING",0,0,0,1.27,74.05,23.4,0,0,0,0,0,0,2.8,0.4,30,1,0,7,0,"N/A",30951,279239,1034,15.6,2.9,59,1.3,0,41.6,0,"N/A",39748,549985,17795,32.6,7.3,80,2.4,173,78.9,0,"N/A",54544,1144039,49899,2,5,8,"This company pays faster than the industry average. There is a consistent payment pattern. This company has 0 accounts placed for collection. This company has 0 outstanding unpaid accounts. This company pays within its terms.",0,0,1,2,0,17,0,17,15,17,10,17,10,16,0,16,0,16,0,16,0,16,0,17,0,17,0,17,0,17,0,17,0,17,0,17,0,17,0,17,3,17,0,15,0,24,0,16,0,6,0,2,0,0,0,0,0,"This company pays its accounts on average 0 days beyond terms. The payment information we have for this company over the last 6 months available shows a consistent payment pattern.","A search of our databases has shown that there are no County Court Judgments recorded against this company","A search of our databases has shown that there are no Legal Notices recorded against this company","A search of our databases has shown that there are no Mortgages or Charges registered against this company","There are no Consumer Credit Licences registered to this company","The Company was incorporated 10 years 2 months ago.  There have been no changes in registered office in the last 12 months.","HOMEFUELS DIRECT LTD",6464646,"Private Limited",39451,"10 years 2 months","GBP 8","70-74 BRUNSWICK STREET, STOCKTON ON TEES, CLEVELAND TS18 1DW","70-74 Brunswick Street, STOCKTON-ON-TEES, Cleveland TS18 1DW","01642 700725","www.homefuelsdirect.com",6120,"INDUSTRIAL MATERIALS WHOLESALING",5151,"WHOLESALE FUELS AND RELATED PRODUCTS","FUEL TO HOMES AND BUSINESS.","STOKESLEY BUSINESS CENTRE, 51 HIGH STREET, STOKESLEY, NORTH YORKSHIRE","Total Exemption Full","31 March",42825,43131,"NICHOLE ROBERTS","This Company has no parent Company","ORD",1,8,8,"yes",100,100,"GBP","Christopher Bicknell","ORD","1.00",8,8,"GBP",100,100,"Christophe David Bicknell","Duport Director Ltd","Thomas Elles Bicknell","Duport Secretary Ltd",39457,"There are no alert notices for this company."]
#
# col_81 = list_test[81] #Mar All
# col_86 = list_test[86]
# col_91 = list_test[91]
# col_96 = list_test[96]
# col_101 = list_test[101]
# col_106 = list_test[106]
# col_111 = list_test[111]
# col_116 = list_test[116]
# col_121 = list_test[121]
# col_126 = list_test[126]
# col_131 = list_test[131]
# col_136 = list_test[136]
# col_141 = list_test[141]
#
#
# # #print(col_14)
# #print(col_18)
# print(col_81) #Same Indus
# # print(col_82)same asset
# # print(col_83) same age
# print(col_86)
# # print(col_87)
# print(col_91) # may same indus
# print(col_96)
# print(col_101)
# print(col_106) # June same indus
# print(col_111) #july all cos
# print(col_116)
# print(col_121)
# print(col_126)
# print(col_131)
# print(col_136)
# print(col_141)
#
# # calculate the chi-square smoothed average for the series ( removes outliers more than 1 degree of freedom)
# #The Basic Arithmetic mean
# mean1 = ((col_81 + col_86 + col_91 + col_96 + col_101 + col_106 + col_111 + col_116 + col_121 + col_126 + col_131 + col_136 + col_141)/13)
# print("The arithmetic mean is:")
# print(mean1)
# # # # in this case we are just looking at the delphi score trend for the subject company.
# # #
# # # # #The Chi smoothing 1 band
# # # # #χ2=n∑i=1(Oi−Ei)2Eiχ2=∑i=1n(Oi−Ei)2Ei
# # # # #We already know n = 12, so do not need to evaluate or use special library really.
# # # # # already done the sum (and divided it by 12) for the test values.
# # # #
# # # # #we need the distribution chi square value/variance from the distribution curve from the mean
# print("So Chi square sum of variances is: ")
# chi2 = ((col_81 - mean1) +(col_86 - mean1)+(col_91 - mean1)+(col_96 - mean1) +(col_101 - mean1)+(col_106 - mean1)+(col_111 - mean1)+(col_116 - mean1) +(col_121 - mean1)+(col_126 - mean1)+ (col_131 - mean1) + (col_136 - mean1) + col_141 - mean1)
# print(chi2)
# chi1 = math.sqrt(abs(chi2))
# print("Here is a standard deviation")
# print(chi1)
# smooth_sd_factor =((mean1 * chi1)*100000)+ (abs((col_81-mean1)))
# print("And the smooth sd factor is: ")
# print(smooth_sd_factor)
# # # # #The Company values smoothed (outliers above n chi variance
# # # # # establish how many Sd's the mean of the company scores are from the chi standard deviation to use in the test.
# # print("The factor that the mean of the series varies from the chi square sd is:")
# # print(smooth_sd_factor)
# # print("So the series will not include values that are +/- ")
# # print(smooth_sd_factor)
# # # Check if Company ecl values are more than the chi1 variance, and get a new smoothed average, add 1 to the counter if it does not pass the test, update the aggregator
# # #also, evaluate from the latest to the oldest whether there is an upward or a downward trend on the smoothed values.  Each subsequent older period not an outlier has a lesser impact.
# # # # # # and use rolling averages
# # print(abs(col_81 - mean1))
# #
# if abs(col_81 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_81
#     counter1 = counter1 + 1
#
#     print("test 81 passed")
# if col_81 > col_86:
#     trend_total = trend_total + 120
# else:
#     trend_total = trend_total - 120
#
# if col_81 > col_86:
#     trend_total = 120
# elif col_81 < col_86:
#     trend_total = -120
#
# if abs(col_86 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_86
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 86 passed")
# if ((col_81 + col_86)/2) > col_91:
#     trend_total = trend_total + 110
# else:
#     trend_total = trend_total - 110
#
# if abs(col_91 - mean1) <= (smooth_sd_factor):
#      smooth_total = smooth_total + col_91
#      counter1 = counter1 + 1
#      print(counter1)
#      print("test 91 passed")
# if ((col_81 + col_86 + col_91)/3) > col_95:
#     trend_total = trend_total + 100
# else:
#     trend_total = trend_total - 100
#
# if abs(col_96 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_96
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 95 passed")
# if ((col_81 + col_86 + col_91 + col_96)/4) > col_101:
#     trend_total = trend_total + 90
# else:
#     trend_total = trend_total - 90
#
# if abs(col_101 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_101
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 101 passed")
# if ((col_81 + col_86 + col_91 + col_96 + col_101)/5) > col_106:
#     trend_total = trend_total + 80
# else:
#     trend_total = trend_total - 80
#
# if abs(col_106 - mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_106
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 106 passed")
# if ((col_81 + col_86 + col_91 + col_96 + col_101 + col_106) / 6) > col_111:
#     trend_total = trend_total + 70
# else:
#     trend_total = trend_total - 70
#
# if abs(col_111 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_111
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 111 passed")
# if abs(col_116 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_116
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 116 passed")
# if abs(col_121 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_121
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 121 passed")
# if abs(col_126 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_126
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 126 passed")
# if abs(col_131 - mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_131
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 131 passed")
# #Reduce trend if last 2 periods are not moving significantly
# if abs(col_131 - col_136) <=(smooth_sd_factor):
#     trend_total = trend_total - smooth_total
#
# if abs(col_136 - mean1) <= (smooth_sd_factor):
#         smooth_total = smooth_total + col_136
#         counter1 = counter1 + 1
#         print(counter1)
#         print("test 136 passed")
#
# if abs(col_141 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_141
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 141 passed")
# if abs(col_136 - col_141) <= (smooth_sd_factor):
#     trend_total = trend_total + 300
# else:
#     trend_total = trend_total - 300
# print(" The Smooth Total is :")
# print(smooth_total)
# print(" The trend Total is :")
# print(trend_total)
# print(counter1)
# # compare chi-square smoothed mean to latest Delphi Score
# smooth_mean = smooth_total/counter1
# if smooth_mean > 0:
#     trend_difference = ((col_81/smooth_mean))
# # # # #This would eatablish a trend difference - either increases or decreses the trend based on the current period avarage score and smoothed average score difference.
# # # #
# #
# # # # #if there is a negative or positive trend, there will be a factor to apply to correctly position in the range buckets.
# trending_count = trend_difference * smooth_mean
# print(trending_count)
# # # #
# # # # #it is possible to score in the trend_total moving average for the last six months a value between -570 and 570.  The sample scored -570 and the scores so that should not have an impact.
# # # # # a positive value of the trend_total is a good thing in the case of Delphi score, as the delphi score that is higher is a lower risk.  A negative value is bad.
# # # # #If the smoothed average and the latest Delphi are close, there will be a trend_difference of 0.
# # # # # If the Smooth Mean is lower than col_18  . trend difference may be negative, indicating that the trend was up - need to factor in the rolling average trend to this value
# # # # # if the smooth mean is higher than col_8, trend is positive, indicating that the DBT actually decreased as trend difference
# # print(trend_total)
# # # # #trend_difference samples
# # # #print(" The trending count")
# # # #print(trending_count)
# # # # test_list_flat = [17,17,17,16,16,16,16,16,17,17,17,17]
# # # # test_list_down = [10,10,11,13,13,14,16,16,17,17,17,17]
# # # # test_list_up = [20,18,18,17,16,17,16,16,15,14,13,11]
# # # # # if max and median is greater than 1 SD above, then trend is up, else
# # # # #if min and median is greater than 1 SD below, then trend is down.
# # # # #in a 12 month pattern, it is not possible to identify seasonality completely.
# # # # # Evaluate  banding score based on range sets:
# # # # #Because of the rolling average trend factor, there are 30 possible ranges of scores, to be assigned to the percentiles -30, -20, -10, 10, 20
# # # # #range is over 20% up,  over 10% up, between 10% up and 10% down, between 10% down and 20% down, between 20 % down and 30% down.
# # # #
# if smooth_mean !=0:
#     if (trend_total - smooth_total) <= -230:
#         all_co_delphi_trend_score = 20
#     elif (trend_total- smooth_total)  < -30:
#         all_co_delphi_trend_score =  10
#     elif (trend_total- smooth_total)  < 190:
#         all_co_delphi_trend_score = -10
#     elif (trend_total- smooth_total)  < 280:
#         all_co_delphi_trend_score = -20
#     elif trend_total  > 280:
#         all_co_delphi_trend_score = -30
# print(all_co_delphi_trend_score)


# col_82 = list_test[82] #Mar All
# col_87 = list_test[87]
# col_92 = list_test[92]
# col_97 = list_test[97]
# col_102 = list_test[102]
# col_107 = list_test[107]
# col_112 = list_test[112]
# col_117 = list_test[117]
# col_122 = list_test[122]
# col_127 = list_test[127]
# col_132 = list_test[132]
# col_137 = list_test[137]
# col_142 = list_test[142]
#
#
# # #print(col_14)
# #print(col_18)
# print(col_82)# same asset
# # print(col_83) same age
# print(col_87)
# # print(col_87)
# print(col_92) # may same indus
# print(col_97)
# print(col_102)
# print(col_107) # June same indus
# print(col_112) #july all cos
# print(col_117)
# print(col_122)
# print(col_127)
# print(col_132)
# print(col_137)
# print(col_142)
#
# # calculate the chi-square smoothed average for the series ( removes outliers more than 1 degree of freedom)
# #The Basic Arithmetic mean
# mean1 = ((col_82 + col_87 + col_92 + col_97 + col_102 + col_107 + col_112 + col_117 + col_122 + col_127 + col_132 + col_137 + col_142)/13)
# print("The arithmetic mean is:")
# print(mean1)
# # in this case we are just looking at the delphi score trend for the subject company.
#
# #The Chi smoothing 1 band
# #χ2=n∑i=1(Oi−Ei)2Eiχ2=∑i=1n(Oi−Ei)2Ei
# #We already know n = 13, so do not need to evaluate or use special library really.
# # already done the sum (and divided it by 12) for the test values.
# #
# #we need the distribution chi square value/variance from the distribution curve from the mean
# print("So Chi square sum of variances is: ")
# chi2 = ((col_82 - mean1) +(col_87 - mean1)+(col_92 - mean1)+(col_97 - mean1) +(col_102 - mean1)+(col_107 - mean1)+(col_112 - mean1)+(col_117 - mean1) +(col_122 - mean1)+(col_127 - mean1)+ (col_132 - mean1) + (col_137 - mean1) + col_142 - mean1)
# print(chi2)
# chi1 = math.sqrt(abs(chi2))
# print("Here is a standard deviation")
# print(chi1)
# smooth_sd_factor =((mean1 * chi1)*100000)+ (abs((col_81-mean1)))
# print("And the smooth sd factor is: ")
# print(smooth_sd_factor)
# # # # # #The Company values smoothed (outliers above n chi variance
# # # # # # establish how many Sd's the mean of the company scores are from the chi standard deviation to use in the test.
# # # print("The factor that the mean of the series varies from the chi square sd is:")
# # # print(smooth_sd_factor)
# # # print("So the series will not include values that are +/- ")
# # # print(smooth_sd_factor)
# # # # Check if Company ecl values are more than the chi1 variance, and get a new smoothed average, add 1 to the counter if it does not pass the test, update the aggregator
# # # #also, evaluate from the latest to the oldest whether there is an upward or a downward trend on the smoothed values.  Each subsequent older period not an outlier has a lesser impact.
# # # # # # # and use rolling averages
# print(abs(col_82 - mean1))
#
# if abs(col_82 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_82
#     counter1 = counter1 + 1
#     print("test 82 passed")
# if col_82 > col_87:
#     trend_total = trend_total + 120
# elif col_82 < col_87:
#     trend_total = trend_total - 120
# #
# if abs(col_87 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_87
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 86 passed")
#
# if ((col_82 + col_87)/2) >= col_92:
#     trend_total = trend_total + 110
# else:
#     trend_total = trend_total - 110
# #
# if abs(col_92 - mean1) <= (smooth_sd_factor):
#      smooth_total = smooth_total + col_92
#      counter1 = counter1 + 1
#      print(counter1)
#      print("test 92 passed")
# if ((col_82 + col_87 + col_92)/3) > col_97:
#     trend_total = trend_total + 100
# elif ((col_82 + col_87 + col_92)/3) < col_97:
#     trend_total = trend_total - 100
#
# if abs(col_97 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_97
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 97 passed")
# if ((col_82 + col_87 + col_92 + col_97)/4) > col_102:
#     trend_total = trend_total + 90
# elif ((col_82 + col_87 + col_92 + col_97)/4) < col_102:
#     trend_total = trend_total - 90
#
# if abs(col_102 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_102
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 102 passed")
# if ((col_82 + col_87 + col_92 + col_97 + col_102)/5) > col_107:
#     trend_total = trend_total + 80
# else:
#     trend_total = trend_total - 80
# #
# if abs(col_107 - mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_107
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 107 passed")
# if ((col_82 + col_87 + col_93 + col_97+ col_102 + col_107) / 6) > col_112:
#     trend_total = trend_total + 70
# elif ((col_82 + col_87 + col_93 + col_97+ col_102 + col_107) / 6) < col_112:
#     trend_total = trend_total - 70
# #
# if abs(col_112 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_112
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 112 passed")
# if abs(col_117 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_117
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 117 passed")
# if abs(col_122 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_122
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 122 passed")
# if abs(col_127 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_127
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 127 passed")
# if abs(col_132 - mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_132
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 132 passed")
# # #Reduce trend if last 2 periods are not moving significantly
# if abs(col_132 - col_137) <=(smooth_sd_factor):
#     trend_total = trend_total - smooth_total
# #
# if abs(col_137 - mean1) <= (smooth_sd_factor):
#         smooth_total = smooth_total + col_137
#         counter1 = counter1 + 1
#         print(counter1)
#         print("test 137 passed")
# #
# if abs(col_142 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_142
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 142 passed")
# if abs(col_137 - col_142) <= (smooth_sd_factor):
#     trend_total = trend_total + 300
# else:
#     trend_total = trend_total - 300
#
# print(" The Smooth Total is :")
# print(smooth_total)
# print(" The trend Total is :")
# print(trend_total)
# print(counter1)
# # # compare chi-square smoothed mean to latest Delphi Score
# smooth_mean = smooth_total/counter1
# # if smooth_mean > 0:
# #     trend_difference = ((col_81/smooth_mean))
# # # # # #This would eatablish a trend difference - either increases or decreses the trend based on the current period avarage score and smoothed average score difference.
# # # # #
# # #
# # # # # #if there is a negative or positive trend, there will be a factor to apply to correctly position in the range buckets.
# trending_count = trend_difference * smooth_mean
# print(trending_count)
# # # # #
# # # # # #it is possible to score in the trend_total moving average for the last six months a value between -570 and 570.  The sample scored -570 and the scores so that should not have an impact.
# # # # # # a positive value of the trend_total is a good thing in the case of Delphi score, as the delphi score that is higher is a lower risk.  A negative value is bad.
# # # # # #If the smoothed average and the latest Delphi are close, there will be a trend_difference of 0.
# # # # # # If the Smooth Mean is lower than col_18  . trend difference may be negative, indicating that the trend was up - need to factor in the rolling average trend to this value
# # # # # # if the smooth mean is higher than col_8, trend is positive, indicating that the DBT actually decreased as trend difference
# # # print(trend_total)
# # # # # #trend_difference samples
# # # # #print(" The trending count")
# # # # #print(trending_count)
# # # # # test_list_flat = [17,17,17,16,16,16,16,16,17,17,17,17]
# # # # # test_list_down = [10,10,11,13,13,14,16,16,17,17,17,17]
# # # # # test_list_up = [20,18,18,17,16,17,16,16,15,14,13,11]
# # # # # # if max and median is greater than 1 SD above, then trend is up, else
# # # # # #if min and median is greater than 1 SD below, then trend is down.
# # # # # #in a 12 month pattern, it is not possible to identify seasonality completely.
# # # # # # Evaluate  banding score based on range sets:
# # # # # #Because of the rolling average trend factor, there are 30 possible ranges of scores, to be assigned to the percentiles -30, -20, -10, 10, 20
# # # # # #range is over 20% up,  over 10% up, between 10% up and 10% down, between 10% down and 20% down, between 20 % down and 30% down.
# # # # #
# if smooth_mean !=0:
#     if (trend_total - smooth_total) <= -230:
#         same_asset_delphi_trend_score = 20
#     elif (trend_total- smooth_total)  < -30:
#         same_asset_delphi_trend_score =  10
#     elif (trend_total- smooth_total)  < 190:
#         same_asset_delphi_trend_score = -10
#     elif (trend_total- smooth_total)  < 280:
#         same_asset_delphi_trend_score = -20
#     elif trend_total  > 280:
#         same_asset_delphi_trend_score = -30
# print(same_asset_delphi_trend_score)
# #
# #
# col_1 = "CompanyName"
# col_2 = "RegisteredNumber"
# col_3 ="Date Incorporated"
# col_5 ="Years In Business"
# col_9 = "100" #Credit Limit 1
# col_10 = "100" #Credit Limit 2
# col_14 = 999
# col_15 = "N/A"
# col_16 = 1
# col_17 = 1
# col_18 = 1
# col_31 = 1
# col_32 = 1
# col_36 = 1
# col_41 = 1
# col_44 = 1
# col_47 = 1
# col_50 = 1
# col_53 = 1
# col_56 = 1
# col_59 = 1
# col_62 = 1
# col_65 = 1
# col_68 = 1
# col_71 = 1
# col_74 = 1
# col_75 = 1
# col_78 = 1
# col_80 = 1
# col_81 = 1
# col_82 = 1
# col_83 = 1
# col_84 = 1
# col_85 = 1
# col_86 = 1
# col_87 = 1
# col_88 = 1
# col_89 = 1
# col_90 = 1 # somewhere in the Delphi score set
# col_91 = 1
# col_92 = 1
# col_93 = 1
# col_94 = 1
# col_95 = 1
# col_96 = 1
# col_97 = 1
# col_98 = 1
# col_99 = 1
# col_100 = 1
# col_101 = 1
# col_102 = 1
# col_103 = 1
# col_104 = 1
# col_105 = 1
# col_106 = 1
# col_107 = 1
# col_108 = 1
# col_109 = 1
# col_110 = 1
# col_111 = 1
# col_112 = 1
# col_113 = 1
# col_115 = 1
# col_116 = 1
# col_117 = 1
# col_118 = 1
# col_119 = 1
# col_120 = 1
# col_121 = 1
# col_122 = 1
# col_123 = 1
# col_124 = 1
# col_125 = 1
# col_126 = 1
# col_127 = 1
# col_128 = 1
# col_129 = 1
# col_130 = 1
# col_131 = 1
# col_132 = 1
# col_133 = 1
# col_134 = 1
# col_135 = 1
# col_136 = 1
# col_137 = 1
# col_138 = 1
# col_139 = 1
# col_140 = 1
# col_141 = 1
# col_142 = 1
# col_143 = 1
# col_144 = 1
# col_588 = 1
# col_589 = 1
# col_593 = 1
# col_594 = 1
# col_595 = 1
# col_596 = 1
# col_597 = 1
# col_598 = 1
# col_599 = 1
# col_600 = 1
# col_601 = 1
# col_602 = 1
# col_603 = 1
# col_604 = 1
# col_605 = 1
# col_606 = 1
# col_607 = 1
# col_608 = 1
# col_609 = 1
# col_610 = 1
# col_611 = 1
# col_612 = 1
# col_613 = 1
# col_614 = 1
# col_615 = 1
# col_616 = 1
# mean1=  1.1
# mean2 = 1.1
# chi1 = 1.1
# chi2 = 1.1
# chi_mean = 1.1
# counter1 = 0
# smooth_sd_factor = 1
# smooth_total = 0
# smooth_mean = 1
# trend_total = 0
# comparison_trend = 1
# trend_difference = 0
# trending_count = 0
# pearson_chi_square_mean = 1
# test_list_flat =[]
# test_list_down = []
# test_list_up =[]
# dbt_trend_score = 0
# delphi_trend_score = 1
# credit_limit_trend_score = 1
# ecl = " "
# other_co_delphi_trend_score = 1
# all_co_delphi_trend_score = 1
# same_industry_delphi_trend_score = 1
# same_asset_delphi_trend_score = 1
# same_age_delphi_trend_score = 1
#
# list_test = ["HOMEFUELS DIRECT LTD",6464646,"4-Jan-08","70-74 BRUNSWICK STREET, STOCKTON ON TEES,","01642 700725","10 years 2 months "  ,"www.homefuelsdirect.com","WHOLESALE FUELS AND RELATED PRODUCTS","A below average risk company; little reason to doubt credit transactions to the limit assigned.","£ 3,400","£ 1,700","Below Average Risk","41:1","21 February 2018 at 08:56:48",78,"L",0,"L",0,0,"This company pays within its terms",17,"No Legal Notices Recorded","GBP","31/03/2017",110168,-36.09,"D",22979,-70.31,"D", 25781, -17.74, "D", 1, 1, "This Company is not part of a Group", "A below average risk company; little reason to doubt credit transactions to the limit assigned.", "Out of 100", "Below Average Risk 41:1", 93, "£9,600",3200, 95, "£9,800",3300, 84,"£7,200","£2,900",95,"£9,800","£3,300",95,"£9,800","£3,300",95,"£9,800","£3,300",92,"£9,500","£3,200",92,"£9,500","£3,200",88,"£7,600","£3,000",88,"£7,600","£3,000",78,"£3,400","£1,700",78,"£3,400","£1,700",78,"£3,400","£1,700",95,44,52,64,57,84,44,52,64,56,95,45,51,64,57,95,44,51,64,56,95,44,50,64,56,92,44,50,64,56,92,44,49,64,56,0,44,49,63,56,88,44,49,63,55,88,44,49,63,55,78,44,49,64,56,78,44,49,64,57,78,45,49,64,57,"Wholesale Trade and Commission Trade, Except of Motor Vehicles and Motorcycles","£90,000 to £150,000","Incorporated between March 2004 and March 2008","Accounts are due to be filed within the next 10 Calendar Months.  The Accounts were prepared by a Director,",42825,43101,"UK GAAP",52,"GBP",2802,0,0,0,2802,0,0,0,0,0,0,2802,0,0,0,0,50616,50175,0,0,441,53998,2752,107366,84387,65183,0,0,19090,0,0,0,0,0,0,0,114,0,22979,25781,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25781,2,0,0,0,0,0,25779,0,25781,25781,"UK GAAP",52,"GBP",0, 0, 0, 0, 0, 0,0 , 0, 0,0 ,11781,11781,0,0 ,0,0,0,0,0,0,0,0,160611,160611,83223,0,0,0,0,0,0,0,0,0,0,0,0,83223,77388,89169,57829,0,0,0,0,0,0,57829,0,0,0,0,0,0,31340,0,0,0,0,0,0,0,31340,31340,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5588,5588,0,0,0,0,0,0,0,0,0,0,126813,126813,36285,0,0,0,0,0,0,0,0,0,0,0,0,36285,90528,96116,72555,0,0,0,0,0,0,72555,0,1117,0,0,1117,0,22444,0,0,0,0,0,0,0,22444,22444,0,"UK GAAP",52,"GBP",8786,0,0,0,0,0,0,0,0,0,0,8786,0,0,0,0,52023,0,0,0,0,92572,0,144595,134958,0,0,0,0,0,0,0,0,0,0,0,0,134958,9637,18423,0,0,0,0,0,0,0,0,0,1757,0,0,1757,0,16666,2,2,0,0,0,0,16664,0,16666,16666,"We have not received any Cash Flow statements for this company",1.27,1.27,0,0,0,74.05,23.4,0,0,0,0,80,0,0,0,0,0,0.93,1.93,0,0,0,0,18.18,0,0,0,0,0,0,0,0,0,0,3.49,3.49,0,0,0,0,0,16.95,0,0,0,0,0,0,0,0,0,0,1.07,1.07,0,0,0,0,0,10.87,0,0,0,0,3196,0,0,0,0,0,0,0,0,1.27,74.05,23.4,0,0,0,0,0,0,0,0,1.93,0,18.18,0,0,0,0,0,0,0,0,-34.07,0,28.71,0,0,0,0,0,15.6,2.9,59,1.3,0,41.6,0,"N/A",39748,549985,17795,"Industry Median based on 2,955 similar companies in 1980 SIC Code 6120 - INDUSTRIAL MATERIALS WHOLESALING",0,0,0,1.27,74.05,23.4,0,0,0,0,0,0,2.8,0.4,30,1,0,7,0,"N/A",30951,279239,1034,15.6,2.9,59,1.3,0,41.6,0,"N/A",39748,549985,17795,32.6,7.3,80,2.4,173,78.9,0,"N/A",54544,1144039,49899,2,5,8,"This company pays faster than the industry average. There is a consistent payment pattern. This company has 0 accounts placed for collection. This company has 0 outstanding unpaid accounts. This company pays within its terms.",0,0,1,2,0,17,0,17,15,17,10,17,10,16,0,16,0,16,0,16,0,16,0,17,0,17,0,17,0,17,0,17,0,17,0,17,0,17,0,17,3,17,0,15,0,24,0,16,0,6,0,2,0,0,0,0,0,"This company pays its accounts on average 0 days beyond terms. The payment information we have for this company over the last 6 months available shows a consistent payment pattern.","A search of our databases has shown that there are no County Court Judgments recorded against this company","A search of our databases has shown that there are no Legal Notices recorded against this company","A search of our databases has shown that there are no Mortgages or Charges registered against this company","There are no Consumer Credit Licences registered to this company","The Company was incorporated 10 years 2 months ago.  There have been no changes in registered office in the last 12 months.","HOMEFUELS DIRECT LTD",6464646,"Private Limited",39451,"10 years 2 months","GBP 8","70-74 BRUNSWICK STREET, STOCKTON ON TEES, CLEVELAND TS18 1DW","70-74 Brunswick Street, STOCKTON-ON-TEES, Cleveland TS18 1DW","01642 700725","www.homefuelsdirect.com",6120,"INDUSTRIAL MATERIALS WHOLESALING",5151,"WHOLESALE FUELS AND RELATED PRODUCTS","FUEL TO HOMES AND BUSINESS.","STOKESLEY BUSINESS CENTRE, 51 HIGH STREET, STOKESLEY, NORTH YORKSHIRE","Total Exemption Full","31 March",42825,43131,"NICHOLE ROBERTS","This Company has no parent Company","ORD",1,8,8,"yes",100,100,"GBP","Christopher Bicknell","ORD","1.00",8,8,"GBP",100,100,"Christophe David Bicknell","Duport Director Ltd","Thomas Elles Bicknell","Duport Secretary Ltd",39457,"There are no alert notices for this company."]
# #
# col_83 = list_test[83]
# col_88 = list_test[88]
# col_93 = list_test[93]
# col_98 = list_test[98]
# col_103 = list_test[103]
# col_108 = list_test[108]
# col_113 = list_test[113]
# col_118 = list_test[118]
# col_123 = list_test[123]
# col_128 = list_test[128]
# col_133 = list_test[133]
# col_138 = list_test[138]
# col_143 = list_test[143]
# #
# print(col_83) #same age
# print(col_88)
# print(col_93)
# print(col_98)
# print(col_103)
# print(col_108) # June same indus
# print(col_113) #july all cos
# print(col_118)
# print(col_123)
# print(col_128)
# print(col_133)
# print(col_138)
# print(col_143)
# #
# # # calculate the chi-square smoothed average for the series ( removes outliers more than 1 degree of freedom)
# # #The Basic Arithmetic mean
# mean1 = ((col_83 + col_88 + col_93 + col_98 + col_103 + col_108 + col_113 + col_118 + col_123 + col_128 + col_133 + col_138 + col_143)/13)
# print("The arithmetic mean is:")
# print(mean1)
# # # in this case we are just looking at the delphi score trend for the subject company.
# #
# # #The Chi smoothing 1 band
# # #χ2=n∑i=1(Oi−Ei)2Eiχ2=∑i=1n(Oi−Ei)2Ei
# # #We already know n = 13, so do not need to evaluate or use special library really.
# # # already done the sum (and divided it by 12) for the test values.
# # #
# # #we need the distribution chi square value/variance from the distribution curve from the mean
# print("So Chi square sum of variances is: ")
# chi2 = ((col_83 - mean1) +(col_88 - mean1)+(col_93 - mean1)+(col_98 - mean1) +(col_103 - mean1)+(col_108 - mean1)+(col_113 - mean1)+(col_118 - mean1) +(col_123 - mean1)+(col_128 - mean1)+ (col_133 - mean1) + (col_138 - mean1) + col_143 - mean1)
# print(chi2)
# chi1 = math.sqrt(abs(chi2))
# print("Here is a standard deviation")
# print(chi1)
# smooth_sd_factor =((mean1 * chi1)*100000)+ (abs((col_83-mean1)))
# print("And the smooth sd factor is: ")
# print(smooth_sd_factor)
# #The Company values smoothed (outliers above n chi variance
# # establish how many Sd's the mean of the company scores are from the chi standard deviation to use in the test.
#
# # Check if Company ecl values are more than the chi1 variance, and get a new smoothed average, add 1 to the counter if it does not pass the test, update the aggregator
# #also, evaluate from the latest to the oldest whether there is an upward or a downward trend on the smoothed values.  Each subsequent older period not an outlier has a lesser impact.
# # and use rolling averages
# print(abs(col_83 - mean1))
# #
# if abs(col_83 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_83
#     counter1 = counter1 + 1
#     print("test 83 passed")
# if col_83 > col_88:
#     trend_total = trend_total + 120
# elif col_83 < col_88:
#     trend_total = trend_total - 120
# #
# if abs(col_88 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_88
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 88 passed")
#
# if ((col_83 + col_88)/2) >= col_93:
#     trend_total = trend_total + 110
# else:
#     trend_total = trend_total - 110
# #
# if abs(col_93 - mean1) <= (smooth_sd_factor):
#      smooth_total = smooth_total + col_93
#      counter1 = counter1 + 1
#      print(counter1)
#      print("test 93 passed")
# if ((col_83 + col_88 + col_93)/3) > col_98:
#     trend_total = trend_total + 100
# elif ((col_83 + col_88 + col_93)/3) < col_98:
#     trend_total = trend_total - 100
# #
# if abs(col_98 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_98
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 98 passed")
# if ((col_83 + col_88 + col_93 + col_98)/4) > col_103:
#     trend_total = trend_total + 90
# elif ((col_83 + col_88 + col_93 + col_98)/4) < col_103:
#     trend_total = trend_total - 90
# #
# if abs(col_103 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_103
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 103 passed")
# if ((col_83 + col_88 + col_93 + col_98 + col_103)/5) > col_108:
#     trend_total = trend_total + 80
# else:
#     trend_total = trend_total - 80
#
# if abs(col_108 - mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_108
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 108 passed")
# if ((col_83 + col_88 + col_93 + col_98 + col_103 + col_108) / 6) > col_113:
#     trend_total = trend_total + 70
# elif ((col_83 + col_88 + col_93 + col_98+ col_103 + col_108) / 6) < col_113:
#     trend_total = trend_total - 70
#
# if abs(col_113 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_113
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 113 passed")
#
# if abs(col_118 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_118
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 118 passed")
#
# if abs(col_123 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_123
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 123 passed")
#
# if abs(col_128 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_128
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 128 passed")
#
# if abs(col_133 - mean1)<= (smooth_sd_factor):
#     smooth_total = smooth_total + col_133
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 133 passed")
#
# if abs(col_138 - mean1) <= (smooth_sd_factor):
#         smooth_total = smooth_total + col_138
#         counter1 = counter1 + 1
#         print(counter1)
#         print("test 138 passed")
#
# if abs(col_143 - mean1) <= (smooth_sd_factor):
#     smooth_total = smooth_total + col_143
#     counter1 = counter1 + 1
#     print(counter1)
#     print("test 143 passed")
#
# #
# print(" The Smooth Total is :")
# print(smooth_total)
# print(" The trend Total is :")
# print(trend_total)
# print(counter1)
# # # # compare chi-square smoothed mean to latest Delphi Score
# smooth_mean = smooth_total/counter1
# if smooth_mean > 0:
#     trend_difference = ((col_83/smooth_mean))
# # # # # # #This would eatablish a trend difference - either increases or decreses the trend based on the current period avarage score and smoothed average score difference.
# # # # # #
# # # #
# # # # # # #if there is a negative or positive trend, there will be a factor to apply to correctly position in the range buckets.
# trending_count = trend_difference * smooth_mean
# #
# #it is possible to score in the trend_total moving average for the last six months a value between -570 and 570.  The sample scored -570 and the scores so that should not have an impact.
# # a positive value of the trend_total is a good thing in the case of Delphi score, as the delphi score that is higher is a lower risk.  A negative value is bad.
# #If the smoothed average and the latest Delphi are close, there will be a trend_difference of 0.
# # If the Smooth Mean is lower than col_18  . trend difference may be negative, indicating that the trend was up - need to factor in the rolling average trend to this value
# # if the smooth mean is higher than col_8, trend is positive, indicating that the DBT actually decreased as trend difference
# #trend_difference samples
# print(" The trending count")
# print(trending_count)
# # # # # # test_list_flat = [17,17,17,16,16,16,16,16,17,17,17,17]
# # # # # # test_list_down = [10,10,11,13,13,14,16,16,17,17,17,17]
# # # # # # test_list_up = [20,18,18,17,16,17,16,16,15,14,13,11]
# # # # # # # if max and median is greater than 1 SD above, then trend is up, else
# # # # # # #if min and median is greater than 1 SD below, then trend is down.
# # # # # # #in a 12 month pattern, it is not possible to identify seasonality completely.
# # # # # # # Evaluate  banding score based on range sets:
# # # # # # #Because of the rolling average trend factor, there are 30 possible ranges of scores, to be assigned to the percentiles -30, -20, -10, 10, 20
# # # # # # #range is over 20% up,  over 10% up, between 10% up and 10% down, between 10% down and 20% down, between 20 % down and 30% down.
# # # # # #
# if smooth_mean !=0:
#     if (trend_total - smooth_total) <= -230:
#         same_asset_delphi_trend_score = 20
#     elif (trend_total- smooth_total)  < -30:
#         same_asset_delphi_trend_score =  10
#     elif (trend_total- smooth_total)  < 190:
#         same_asset_delphi_trend_score = -10
#     elif (trend_total- smooth_total)  < 280:
#         same_asset_delphi_trend_score = -20
#     elif trend_total  > 280:
#         same_asset_delphi_trend_score = -30
# print(same_asset_delphi_trend_score)
