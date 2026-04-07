"""
Iran CO₂ Emissions Dashboard
BS in Analytics and Sustainability Studies (2024-28)
TISS Mumbai — Novid Salhot (M2024BSASS019) — Country: Iran
Data Source: Our World in Data (OWID)
"""

# ──────────────────────────────────────────────────────────────────────────────
# DEPENDENCIES  →  pip install dash dash-bootstrap-components plotly pandas kaleido
# ──────────────────────────────────────────────────────────────────────────────

import json, io, base64
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html, Input, Output, State, callback_context
import dash_bootstrap_components as dbc

# ══════════════════════════════════════════════════════════════════════════════
# EMBEDDED DATA  (All 285 rows, no external file needed)
# ══════════════════════════════════════════════════════════════════════════════
RAW_JSON = r"""
[{"Country":"Algeria","ISO Code":"DZA","Year":2006,"Population":33623505,"GDP (Constant US$)":346000000000.0,"GDP per Capita (Constant US$)":10290.42035,"Total CO2 Emissions (Mt)":103.79776,"Per Capita CO2 (Mt)":3.087059498,"Share of Global CO2 (%)":0.339273214,"Coal CO2 (Mt)":2.700367928,"Oil CO2 (Mt)":35.2330246,"Gas CO2 (Mt)":49.30644608,"Cement CO2 (Mt)":4.441604137,"Flaring CO2 (Mt)":12.11631298,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2007,"Population":34189420,"GDP (Constant US$)":372000000000.0,"GDP per Capita (Constant US$)":10880.55896,"Total CO2 Emissions (Mt)":107.5486984,"Per Capita CO2 (Mt)":3.145671844,"Share of Global CO2 (%)":0.341432482,"Coal CO2 (Mt)":3.011807919,"Oil CO2 (Mt)":38.32177734,"Gas CO2 (Mt)":51.07616043,"Cement CO2 (Mt)":4.659999847,"Flaring CO2 (Mt)":10.4789505,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2008,"Population":34816963,"GDP (Constant US$)":396000000000.0,"GDP per Capita (Constant US$)":11373.76629,"Total CO2 Emissions (Mt)":108.5960846,"Per Capita CO2 (Mt)":3.11905694,"Share of Global CO2 (%)":0.338836938,"Coal CO2 (Mt)":3.008245945,"Oil CO2 (Mt)":37.36307144,"Gas CO2 (Mt)":51.55056,"Cement CO2 (Mt)":5.092050076,"Flaring CO2 (Mt)":11.58215332,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2009,"Population":35490442,"GDP (Constant US$)":418000000000.0,"GDP per Capita (Constant US$)":11777.81894,"Total CO2 Emissions (Mt)":116.3279724,"Per Capita CO2 (Mt)":3.277726889,"Share of Global CO2 (%)":0.369142652,"Coal CO2 (Mt)":1.593840003,"Oil CO2 (Mt)":44.8913269,"Gas CO2 (Mt)":54.89404678,"Cement CO2 (Mt)":5.691974163,"Flaring CO2 (Mt)":9.256780624,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2010,"Population":36188237,"GDP (Constant US$)":451000000000.0,"GDP per Capita (Constant US$)":12462.6132,"Total CO2 Emissions (Mt)":117.8473587,"Per Capita CO2 (Mt)":3.256510019,"Share of Global CO2 (%)":0.353708267,"Coal CO2 (Mt)":1.216485977,"Oil CO2 (Mt)":45.36540604,"Gas CO2 (Mt)":53.36783218,"Cement CO2 (Mt)":7.746408939,"Flaring CO2 (Mt)":10.15122414,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2011,"Population":36903374,"GDP (Constant US$)":482000000000.0,"GDP per Capita (Constant US$)":13061.13636,"Total CO2 Emissions (Mt)":124.7152405,"Per Capita CO2 (Mt)":3.37950778,"Share of Global CO2 (%)":0.361703247,"Coal CO2 (Mt)":1.121148944,"Oil CO2 (Mt)":46.91973877,"Gas CO2 (Mt)":56.72063446,"Cement CO2 (Mt)":7.734612942,"Flaring CO2 (Mt)":12.21910286,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2012,"Population":37646165,"GDP (Constant US$)":498000000000.0,"GDP per Capita (Constant US$)":13228.43907,"Total CO2 Emissions (Mt)":135.5934601,"Per Capita CO2 (Mt)":3.601786613,"Share of Global CO2 (%)":0.387911528,"Coal CO2 (Mt)":1.106528044,"Oil CO2 (Mt)":48.5406723,"Gas CO2 (Mt)":64.11633301,"Cement CO2 (Mt)":7.542937756,"Flaring CO2 (Mt)":14.28698158,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2013,"Population":38414176,"GDP (Constant US$)":512000000000.0,"GDP per Capita (Constant US$)":13328.41293,"Total CO2 Emissions (Mt)":141.5342712,"Per Capita CO2 (Mt)":3.684428215,"Share of Global CO2 (%)":0.401221752,"Coal CO2 (Mt)":0.776767969,"Oil CO2 (Mt)":52.01780701,"Gas CO2 (Mt)":65.4500351,"Cement CO2 (Mt)":7.896093845,"Flaring CO2 (Mt)":15.39357567,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2014,"Population":39205035,"GDP (Constant US$)":532000000000.0,"GDP per Capita (Constant US$)":13569.68563,"Total CO2 Emissions (Mt)":152.4346619,"Per Capita CO2 (Mt)":3.888139725,"Share of Global CO2 (%)":0.429808736,"Coal CO2 (Mt)":0.57891202,"Oil CO2 (Mt)":53.58233643,"Gas CO2 (Mt)":73.83326721,"Cement CO2 (Mt)":8.087319374,"Flaring CO2 (Mt)":16.35283089,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2015,"Population":40019528,"GDP (Constant US$)":552000000000.0,"GDP per Capita (Constant US$)":13793.26613,"Total CO2 Emissions (Mt)":160.3216095,"Per Capita CO2 (Mt)":4.006084442,"Share of Global CO2 (%)":0.452840805,"Coal CO2 (Mt)":0.534943998,"Oil CO2 (Mt)":55.59020615,"Gas CO2 (Mt)":78.76866913,"Cement CO2 (Mt)":8.26320076,"Flaring CO2 (Mt)":17.16458702,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2016,"Population":40850719,"GDP (Constant US$)":569000000000.0,"GDP per Capita (Constant US$)":13928.76341,"Total CO2 Emissions (Mt)":158.3083191,"Per Capita CO2 (Mt)":3.875288486,"Share of Global CO2 (%)":0.447289228,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":54.62792969,"Gas CO2 (Mt)":78.67901611,"Cement CO2 (Mt)":8.928498268,"Flaring CO2 (Mt)":16.07287407,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2017,"Population":41689302,"GDP (Constant US$)":577000000000.0,"GDP per Capita (Constant US$)":13840.48119,"Total CO2 Emissions (Mt)":165.2516327,"Per Capita CO2 (Mt)":3.963885784,"Share of Global CO2 (%)":0.459356278,"Coal CO2 (Mt)":0.923349977,"Oil CO2 (Mt)":55.32405472,"Gas CO2 (Mt)":82.35402679,"Cement CO2 (Mt)":10.10031796,"Flaring CO2 (Mt)":16.54989052,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2018,"Population":42505033,"GDP (Constant US$)":584000000000.0,"GDP per Capita (Constant US$)":13739.54938,"Total CO2 Emissions (Mt)":174.4611816,"Per Capita CO2 (Mt)":4.104483128,"Share of Global CO2 (%)":0.474931002,"Coal CO2 (Mt)":1.546208024,"Oil CO2 (Mt)":56.23140717,"Gas CO2 (Mt)":88.88864136,"Cement CO2 (Mt)":11.40373898,"Flaring CO2 (Mt)":16.39118195,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2019,"Population":43294551,"GDP (Constant US$)":590000000000.0,"GDP per Capita (Constant US$)":13627.58099,"Total CO2 Emissions (Mt)":182.4249878,"Per Capita CO2 (Mt)":4.213578701,"Share of Global CO2 (%)":0.491889626,"Coal CO2 (Mt)":1.275099993,"Oil CO2 (Mt)":59.63656235,"Gas CO2 (Mt)":91.99771881,"Cement CO2 (Mt)":12.54189014,"Flaring CO2 (Mt)":16.97371864,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2020,"Population":44042094,"GDP (Constant US$)":560000000000.0,"GDP per Capita (Constant US$)":12715.10841,"Total CO2 Emissions (Mt)":171.1385345,"Per Capita CO2 (Mt)":3.88579464,"Share of Global CO2 (%)":0.486766636,"Coal CO2 (Mt)":0.575260997,"Oil CO2 (Mt)":54.12953568,"Gas CO2 (Mt)":87.0256958,"Cement CO2 (Mt)":11.87852001,"Flaring CO2 (Mt)":17.52951622,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2021,"Population":44761099,"GDP (Constant US$)":579000000000.0,"GDP per Capita (Constant US$)":12935.33923,"Total CO2 Emissions (Mt)":182.0358124,"Per Capita CO2 (Mt)":4.066830635,"Share of Global CO2 (%)":0.493765384,"Coal CO2 (Mt)":1.176169038,"Oil CO2 (Mt)":57.34283066,"Gas CO2 (Mt)":96.25901031,"Cement CO2 (Mt)":11.92486668,"Flaring CO2 (Mt)":15.33294106,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2022,"Population":45477391,"GDP (Constant US$)":596000000000.0,"GDP per Capita (Constant US$)":13105.41319,"Total CO2 Emissions (Mt)":192.7785645,"Per Capita CO2 (Mt)":4.238997936,"Share of Global CO2 (%)":0.513695717,"Coal CO2 (Mt)":0.758448005,"Oil CO2 (Mt)":61.61016083,"Gas CO2 (Mt)":101.3791046,"Cement CO2 (Mt)":12.83649826,"Flaring CO2 (Mt)":16.1943512,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2023,"Population":46164222,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":202.8466492,"Per Capita CO2 (Mt)":4.394022942,"Share of Global CO2 (%)":0.532489181,"Coal CO2 (Mt)":0.734112978,"Oil CO2 (Mt)":64.67647552,"Gas CO2 (Mt)":109.2219315,"Cement CO2 (Mt)":12.83649826,"Flaring CO2 (Mt)":15.37762642,"Other Industry CO2 (Mt)":null},{"Country":"Algeria","ISO Code":"DZA","Year":2024,"Population":46814302,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":198.203186,"Per Capita CO2 (Mt)":4.233817101,"Share of Global CO2 (%)":0.513498664,"Coal CO2 (Mt)":0.605760992,"Oil CO2 (Mt)":68.143013,"Gas CO2 (Mt)":101.7996979,"Cement CO2 (Mt)":12.83649826,"Flaring CO2 (Mt)":14.81821632,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2006,"Population":1172878888,"GDP (Constant US$)":4070000000000.0,"GDP per Capita (Constant US$)":3470.094007,"Total CO2 Emissions (Mt)":1293.321411,"Per Capita CO2 (Mt)":1.102689743,"Share of Global CO2 (%)":4.227348804,"Coal CO2 (Mt)":773.5512695,"Oil CO2 (Mt)":370.5438843,"Gas CO2 (Mt)":82.57962036,"Cement CO2 (Mt)":64.90540314,"Flaring CO2 (Mt)":1.741353989,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2007,"Population":1190676028,"GDP (Constant US$)":4400000000000.0,"GDP per Capita (Constant US$)":3695.379681,"Total CO2 Emissions (Mt)":1393.485229,"Per Capita CO2 (Mt)":1.17033112,"Share of Global CO2 (%)":4.423867226,"Coal CO2 (Mt)":842.5357666,"Oil CO2 (Mt)":392.817749,"Gas CO2 (Mt)":87.95613098,"Cement CO2 (Mt)":68.33326721,"Flaring CO2 (Mt)":1.842344999,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2008,"Population":1207930960,"GDP (Constant US$)":4650000000000.0,"GDP per Capita (Constant US$)":3849.557759,"Total CO2 Emissions (Mt)":1490.366455,"Per Capita CO2 (Mt)":1.233817577,"Share of Global CO2 (%)":4.650178909,"Coal CO2 (Mt)":910.753418,"Oil CO2 (Mt)":414.2041321,"Gas CO2 (Mt)":90.27657318,"Cement CO2 (Mt)":73.24472809,"Flaring CO2 (Mt)":1.88765204,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2009,"Population":1225524764,"GDP (Constant US$)":4990000000000.0,"GDP per Capita (Constant US$)":4071.725147,"Total CO2 Emissions (Mt)":1613.327637,"Per Capita CO2 (Mt)":1.316438198,"Share of Global CO2 (%)":5.119559765,"Coal CO2 (Mt)":983.9468994,"Oil CO2 (Mt)":433.7709045,"Gas CO2 (Mt)":112.4631042,"Cement CO2 (Mt)":81.26795959,"Flaring CO2 (Mt)":1.878800988,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2010,"Population":1243481565,"GDP (Constant US$)":5360000000000.0,"GDP per Capita (Constant US$)":4310.478057,"Total CO2 Emissions (Mt)":1678.529541,"Per Capita CO2 (Mt)":1.349862814,"Share of Global CO2 (%)":5.037955761,"Coal CO2 (Mt)":1015.983032,"Oil CO2 (Mt)":440.6919861,"Gas CO2 (Mt)":134.1211548,"Cement CO2 (Mt)":86.02924347,"Flaring CO2 (Mt)":1.70412302,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2011,"Population":1261224956,"GDP (Constant US$)":5720000000000.0,"GDP per Capita (Constant US$)":4535.273404,"Total CO2 Emissions (Mt)":1765.694824,"Per Capita CO2 (Mt)":1.399984121,"Share of Global CO2 (%)":5.12092638,"Coal CO2 (Mt)":1074.38501,"Oil CO2 (Mt)":461.3699951,"Gas CO2 (Mt)":135.9772034,"Cement CO2 (Mt)":91.3144989,"Flaring CO2 (Mt)":2.648179054,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2012,"Population":1278674501,"GDP (Constant US$)":6050000000000.0,"GDP per Capita (Constant US$)":4731.462147,"Total CO2 Emissions (Mt)":1926.986328,"Per Capita CO2 (Mt)":1.507018685,"Share of Global CO2 (%)":5.512804508,"Coal CO2 (Mt)":1206.451782,"Oil CO2 (Mt)":491.147522,"Gas CO2 (Mt)":125.5576935,"Cement CO2 (Mt)":100.2371597,"Flaring CO2 (Mt)":3.592236042,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2013,"Population":1295829507,"GDP (Constant US$)":6420000000000.0,"GDP per Capita (Constant US$)":4954.355465,"Total CO2 Emissions (Mt)":1995.337158,"Per Capita CO2 (Mt)":1.539814591,"Share of Global CO2 (%)":5.656387806,"Coal CO2 (Mt)":1276.383301,"Oil CO2 (Mt)":498.3144531,"Gas CO2 (Mt)":109.5539932,"Cement CO2 (Mt)":107.8198395,"Flaring CO2 (Mt)":3.265639067,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2014,"Population":1312277184,"GDP (Constant US$)":6880000000000.0,"GDP per Capita (Constant US$)":5242.794803,"Total CO2 Emissions (Mt)":2148.052002,"Per Capita CO2 (Mt)":1.636888862,"Share of Global CO2 (%)":6.056703568,"Coal CO2 (Mt)":1407.057007,"Oil CO2 (Mt)":513.8397217,"Gas CO2 (Mt)":107.8009949,"Cement CO2 (Mt)":115.8248978,"Flaring CO2 (Mt)":3.529486895,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2015,"Population":1328024494,"GDP (Constant US$)":7390000000000.0,"GDP per Capita (Constant US$)":5564.6564,"Total CO2 Emissions (Mt)":2231.817383,"Per Capita CO2 (Mt)":1.68055439,"Share of Global CO2 (%)":6.30394125,"Coal CO2 (Mt)":1449.586548,"Oil CO2 (Mt)":557.5231323,"Gas CO2 (Mt)":103.0624237,"Cement CO2 (Mt)":117.5079117,"Flaring CO2 (Mt)":4.137465954,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2016,"Population":1343944296,"GDP (Constant US$)":8060000000000.0,"GDP per Capita (Constant US$)":5997.272375,"Total CO2 Emissions (Mt)":2352.540039,"Per Capita CO2 (Mt)":1.750474453,"Share of Global CO2 (%)":6.646939754,"Coal CO2 (Mt)":1499.401123,"Oil CO2 (Mt)":616.1124268,"Gas CO2 (Mt)":109.9890976,"Cement CO2 (Mt)":123.281311,"Flaring CO2 (Mt)":3.756229877,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2017,"Population":1359657398,"GDP (Constant US$)":8550000000000.0,"GDP per Capita (Constant US$)":6288.348824,"Total CO2 Emissions (Mt)":2425.721924,"Per Capita CO2 (Mt)":1.784068465,"Share of Global CO2 (%)":6.742871761,"Coal CO2 (Mt)":1551.256104,"Oil CO2 (Mt)":634.1159668,"Gas CO2 (Mt)":116.4794922,"Cement CO2 (Mt)":121.0472412,"Flaring CO2 (Mt)":2.823090076,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2018,"Population":1374659067,"GDP (Constant US$)":9170000000000.0,"GDP per Capita (Constant US$)":6670.744929,"Total CO2 Emissions (Mt)":2595.227051,"Per Capita CO2 (Mt)":1.887906075,"Share of Global CO2 (%)":7.064917088,"Coal CO2 (Mt)":1668.317871,"Oil CO2 (Mt)":658.7147217,"Gas CO2 (Mt)":126.7396545,"Cement CO2 (Mt)":138.9648895,"Flaring CO2 (Mt)":2.489685059,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2019,"Population":1389030307,"GDP (Constant US$)":9600000000000.0,"GDP per Capita (Constant US$)":6911.296285,"Total CO2 Emissions (Mt)":2611.174561,"Per Capita CO2 (Mt)":1.879854321,"Share of Global CO2 (%)":7.040755272,"Coal CO2 (Mt)":1661.940063,"Oil CO2 (Mt)":677.883667,"Gas CO2 (Mt)":125.2325058,"Cement CO2 (Mt)":143.6641388,"Flaring CO2 (Mt)":2.454173088,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2020,"Population":1402617694,"GDP (Constant US$)":8950000000000.0,"GDP per Capita (Constant US$)":6380.926206,"Total CO2 Emissions (Mt)":2422.731934,"Per Capita CO2 (Mt)":1.727293253,"Share of Global CO2 (%)":6.890938759,"Coal CO2 (Mt)":1561.79895,"Oil CO2 (Mt)":607.5351563,"Gas CO2 (Mt)":127.6837006,"Cement CO2 (Mt)":122.9082031,"Flaring CO2 (Mt)":2.805991888,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2021,"Population":1414203896,"GDP (Constant US$)":9800000000000.0,"GDP per Capita (Constant US$)":6929.693821,"Total CO2 Emissions (Mt)":2675.778076,"Per Capita CO2 (Mt)":1.89207375,"Share of Global CO2 (%)":7.257948875,"Coal CO2 (Mt)":1767.296509,"Oil CO2 (Mt)":623.4846191,"Gas CO2 (Mt)":133.191864,"Cement CO2 (Mt)":149.0334625,"Flaring CO2 (Mt)":2.77154994,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2022,"Population":1425423209,"GDP (Constant US$)":10500000000000.0,"GDP per Capita (Constant US$)":7366.233364,"Total CO2 Emissions (Mt)":2831.131592,"Per Capita CO2 (Mt)":1.986169219,"Share of Global CO2 (%)":7.544096947,"Coal CO2 (Mt)":1855.854126,"Oil CO2 (Mt)":684.0137329,"Gas CO2 (Mt)":124.0087051,"Cement CO2 (Mt)":164.3314972,"Flaring CO2 (Mt)":2.923605919,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2023,"Population":1438069597,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":3062.756348,"Per Capita CO2 (Mt)":2.129769325,"Share of Global CO2 (%)":8.039988518,"Coal CO2 (Mt)":2032.047607,"Oil CO2 (Mt)":718.1830444,"Gas CO2 (Mt)":132.4195862,"Cement CO2 (Mt)":177.2386627,"Flaring CO2 (Mt)":2.867526054,"Other Industry CO2 (Mt)":null},{"Country":"India","ISO Code":"IND","Year":2024,"Population":1450935785,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":3193.478027,"Per Capita CO2 (Mt)":2.200978279,"Share of Global CO2 (%)":8.273564339,"Coal CO2 (Mt)":2108.032715,"Oil CO2 (Mt)":747.3328247,"Gas CO2 (Mt)":149.3521576,"Cement CO2 (Mt)":185.9696655,"Flaring CO2 (Mt)":2.79053998,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2006,"Population":73392747,"GDP (Constant US$)":995000000000.0,"GDP per Capita (Constant US$)":13557.19796,"Total CO2 Emissions (Mt)":501.0149841,"Per Capita CO2 (Mt)":6.826491833,"Share of Global CO2 (%)":1.637616754,"Coal CO2 (Mt)":5.983269215,"Oil CO2 (Mt)":233.3621368,"Gas CO2 (Mt)":221.5384827,"Cement CO2 (Mt)":17.25258446,"Flaring CO2 (Mt)":22.87850952,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2007,"Population":74602648,"GDP (Constant US$)":1100000000000.0,"GDP per Capita (Constant US$)":14744.78493,"Total CO2 Emissions (Mt)":507.7710571,"Per Capita CO2 (Mt)":6.806341171,"Share of Global CO2 (%)":1.612009764,"Coal CO2 (Mt)":6.576927185,"Oil CO2 (Mt)":225.1763763,"Gas CO2 (Mt)":236.5202179,"Cement CO2 (Mt)":19.40012741,"Flaring CO2 (Mt)":20.09744072,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2008,"Population":75514201,"GDP (Constant US$)":1130000000000.0,"GDP per Capita (Constant US$)":14964.07278,"Total CO2 Emissions (Mt)":528.5281982,"Per Capita CO2 (Mt)":6.999056816,"Share of Global CO2 (%)":1.649091363,"Coal CO2 (Mt)":5.858695984,"Oil CO2 (Mt)":233.9374695,"Gas CO2 (Mt)":246.8749695,"Cement CO2 (Mt)":21.60574532,"Flaring CO2 (Mt)":20.25128937,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2009,"Population":76457831,"GDP (Constant US$)":1210000000000.0,"GDP per Capita (Constant US$)":15825.71705,"Total CO2 Emissions (Mt)":543.4059448,"Per Capita CO2 (Mt)":7.107263565,"Share of Global CO2 (%)":1.724385858,"Coal CO2 (Mt)":4.396800041,"Oil CO2 (Mt)":232.9094849,"Gas CO2 (Mt)":261.0636597,"Cement CO2 (Mt)":24.56090736,"Flaring CO2 (Mt)":20.47507477,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2010,"Population":77420851,"GDP (Constant US$)":1310000000000.0,"GDP per Capita (Constant US$)":16920.50634,"Total CO2 Emissions (Mt)":561.4960327,"Per Capita CO2 (Mt)":7.252517223,"Share of Global CO2 (%)":1.685280085,"Coal CO2 (Mt)":5.45199585,"Oil CO2 (Mt)":227.5292511,"Gas CO2 (Mt)":277.2200928,"Cement CO2 (Mt)":30.10358429,"Flaring CO2 (Mt)":21.19119072,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2011,"Population":78383602,"GDP (Constant US$)":1350000000000.0,"GDP per Capita (Constant US$)":17222.99008,"Total CO2 Emissions (Mt)":576.3657227,"Per Capita CO2 (Mt)":7.353141308,"Share of Global CO2 (%)":1.671594739,"Coal CO2 (Mt)":5.529010773,"Oil CO2 (Mt)":223.6959534,"Gas CO2 (Mt)":293.2647705,"Cement CO2 (Mt)":32.91478348,"Flaring CO2 (Mt)":20.96120834,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2012,"Population":79370583,"GDP (Constant US$)":1320000000000.0,"GDP per Capita (Constant US$)":16630.84672,"Total CO2 Emissions (Mt)":599.2783203,"Per Capita CO2 (Mt)":7.550383568,"Share of Global CO2 (%)":1.714441061,"Coal CO2 (Mt)":4.283216,"Oil CO2 (Mt)":247.1661072,"Gas CO2 (Mt)":292.2736206,"Cement CO2 (Mt)":34.82416153,"Flaring CO2 (Mt)":20.73122406,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2013,"Population":80414689,"GDP (Constant US$)":1290000000000.0,"GDP per Capita (Constant US$)":16041.84529,"Total CO2 Emissions (Mt)":609.996521,"Per Capita CO2 (Mt)":7.585635662,"Share of Global CO2 (%)":1.729220033,"Coal CO2 (Mt)":4.268559933,"Oil CO2 (Mt)":253.3362885,"Gas CO2 (Mt)":294.9336853,"Cement CO2 (Mt)":36.71770477,"Flaring CO2 (Mt)":20.74028587,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2014,"Population":81502045,"GDP (Constant US$)":1350000000000.0,"GDP per Capita (Constant US$)":16564.00155,"Total CO2 Emissions (Mt)":644.2276001,"Per Capita CO2 (Mt)":7.904434681,"Share of Global CO2 (%)":1.816480875,"Coal CO2 (Mt)":3.664000034,"Oil CO2 (Mt)":247.8036499,"Gas CO2 (Mt)":335.0068359,"Cement CO2 (Mt)":34.96812057,"Flaring CO2 (Mt)":22.78499985,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2015,"Population":82619365,"GDP (Constant US$)":1330000000000.0,"GDP per Capita (Constant US$)":16097.92087,"Total CO2 Emissions (Mt)":641.9587402,"Per Capita CO2 (Mt)":7.770075798,"Share of Global CO2 (%)":1.813262105,"Coal CO2 (Mt)":4.349143028,"Oil CO2 (Mt)":227.0531158,"Gas CO2 (Mt)":356.7689514,"Cement CO2 (Mt)":31.23033524,"Flaring CO2 (Mt)":22.55718231,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2016,"Population":83812230,"GDP (Constant US$)":1410000000000.0,"GDP per Capita (Constant US$)":16823.32042,"Total CO2 Emissions (Mt)":644.680481,"Per Capita CO2 (Mt)":7.691962242,"Share of Global CO2 (%)":1.821500182,"Coal CO2 (Mt)":3.45511198,"Oil CO2 (Mt)":200.1217041,"Gas CO2 (Mt)":380.6998901,"Cement CO2 (Mt)":30.61806679,"Flaring CO2 (Mt)":29.7857666,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2017,"Population":85026761,"GDP (Constant US$)":1490000000000.0,"GDP per Capita (Constant US$)":17523.89462,"Total CO2 Emissions (Mt)":696.4074707,"Per Capita CO2 (Mt)":8.190450668,"Share of Global CO2 (%)":1.935830474,"Coal CO2 (Mt)":4.715542793,"Oil CO2 (Mt)":229.0610809,"Gas CO2 (Mt)":399.5021362,"Cement CO2 (Mt)":29.90846443,"Flaring CO2 (Mt)":33.22028732,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2018,"Population":86117999,"GDP (Constant US$)":1480000000000.0,"GDP per Capita (Constant US$)":17185.72212,"Total CO2 Emissions (Mt)":664.5232544,"Per Capita CO2 (Mt)":7.716427326,"Share of Global CO2 (%)":1.809013844,"Coal CO2 (Mt)":4.462751865,"Oil CO2 (Mt)":206.5066986,"Gas CO2 (Mt)":390.8425293,"Cement CO2 (Mt)":30.27233887,"Flaring CO2 (Mt)":32.43891144,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2019,"Population":87051649,"GDP (Constant US$)":1440000000000.0,"GDP per Capita (Constant US$)":16541.90376,"Total CO2 Emissions (Mt)":727.2685547,"Per Capita CO2 (Mt)":8.354448318,"Share of Global CO2 (%)":1.961002588,"Coal CO2 (Mt)":5.785427094,"Oil CO2 (Mt)":230.9040985,"Gas CO2 (Mt)":429.3123474,"Cement CO2 (Mt)":35.30322266,"Flaring CO2 (Mt)":25.96344185,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2020,"Population":87723448,"GDP (Constant US$)":1450000000000.0,"GDP per Capita (Constant US$)":16529.21805,"Total CO2 Emissions (Mt)":745.5957642,"Per Capita CO2 (Mt)":8.499389648,"Share of Global CO2 (%)":2.120686293,"Coal CO2 (Mt)":6.503632069,"Oil CO2 (Mt)":210.0251923,"Gas CO2 (Mt)":465.3339844,"Cement CO2 (Mt)":38.80783844,"Flaring CO2 (Mt)":24.92513847,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2021,"Population":88455490,"GDP (Constant US$)":1530000000000.0,"GDP per Capita (Constant US$)":17296.83483,"Total CO2 Emissions (Mt)":779.5252686,"Per Capita CO2 (Mt)":8.812626839,"Share of Global CO2 (%)":2.114433289,"Coal CO2 (Mt)":7.280367851,"Oil CO2 (Mt)":229.4836426,"Gas CO2 (Mt)":472.8465271,"Cement CO2 (Mt)":37.41871262,"Flaring CO2 (Mt)":32.49603271,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2022,"Population":89524247,"GDP (Constant US$)":1570000000000.0,"GDP per Capita (Constant US$)":17537.14834,"Total CO2 Emissions (Mt)":767.1784668,"Per Capita CO2 (Mt)":8.569504738,"Share of Global CO2 (%)":2.044295311,"Coal CO2 (Mt)":7.459904194,"Oil CO2 (Mt)":208.0785522,"Gas CO2 (Mt)":480.6272583,"Cement CO2 (Mt)":38.63775253,"Flaring CO2 (Mt)":32.37505722,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2023,"Population":90608708,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":789.6758423,"Per Capita CO2 (Mt)":8.715230942,"Share of Global CO2 (%)":2.072964191,"Coal CO2 (Mt)":6.26320982,"Oil CO2 (Mt)":211.0248566,"Gas CO2 (Mt)":495.0460815,"Cement CO2 (Mt)":38.9499321,"Flaring CO2 (Mt)":38.39173126,"Other Industry CO2 (Mt)":null},{"Country":"Iran","ISO Code":"IRN","Year":2024,"Population":91567737,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":792.6311646,"Per Capita CO2 (Mt)":8.656227112,"Share of Global CO2 (%)":2.053524256,"Coal CO2 (Mt)":6.39766407,"Oil CO2 (Mt)":213.7289429,"Gas CO2 (Mt)":492.6575623,"Cement CO2 (Mt)":36.95560837,"Flaring CO2 (Mt)":42.89137268,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2006,"Population":28616518,"GDP (Constant US$)":190000000000.0,"GDP per Capita (Constant US$)":6639.521971,"Total CO2 Emissions (Mt)":98.83811951,"Per Capita CO2 (Mt)":3.45388341,"Share of Global CO2 (%)":0.323062122,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":71.60189056,"Gas CO2 (Mt)":11.95929623,"Cement CO2 (Mt)":1.509443998,"Flaring CO2 (Mt)":13.76749039,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2007,"Population":28391606,"GDP (Constant US$)":201000000000.0,"GDP per Capita (Constant US$)":7079.557247,"Total CO2 Emissions (Mt)":61.36141968,"Per Capita CO2 (Mt)":2.16125226,"Share of Global CO2 (%)":0.194802761,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":34.6614418,"Gas CO2 (Mt)":12.02891159,"Cement CO2 (Mt)":1.904649019,"Flaring CO2 (Mt)":12.76641655,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2008,"Population":28971042,"GDP (Constant US$)":232000000000.0,"GDP per Capita (Constant US$)":8007.996399,"Total CO2 Emissions (Mt)":94.33540344,"Per Capita CO2 (Mt)":3.25619626,"Share of Global CO2 (%)":0.294341326,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":62.78630447,"Gas CO2 (Mt)":15.24956799,"Cement CO2 (Mt)":2.707410097,"Flaring CO2 (Mt)":13.59212399,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2009,"Population":30058207,"GDP (Constant US$)":260000000000.0,"GDP per Capita (Constant US$)":8649.883874,"Total CO2 Emissions (Mt)":105.2114563,"Per Capita CO2 (Mt)":3.500257254,"Share of Global CO2 (%)":0.333866686,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":70.19857788,"Gas CO2 (Mt)":16.70051193,"Cement CO2 (Mt)":2.912777901,"Flaring CO2 (Mt)":15.39958858,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2010,"Population":31045367,"GDP (Constant US$)":298000000000.0,"GDP per Capita (Constant US$)":9598.855765,"Total CO2 Emissions (Mt)":113.983429,"Per Capita CO2 (Mt)":3.671511889,"Share of Global CO2 (%)":0.342111051,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":78.47188568,"Gas CO2 (Mt)":14.81721592,"Cement CO2 (Mt)":3.315342903,"Flaring CO2 (Mt)":17.37898064,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2011,"Population":32161425,"GDP (Constant US$)":344000000000.0,"GDP per Capita (Constant US$)":10696.04347,"Total CO2 Emissions (Mt)":123.5256042,"Per Capita CO2 (Mt)":3.840800285,"Share of Global CO2 (%)":0.358253062,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":84.86190033,"Gas CO2 (Mt)":13.90854359,"Cement CO2 (Mt)":4.126976967,"Flaring CO2 (Mt)":20.62818146,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2012,"Population":33654843,"GDP (Constant US$)":392000000000.0,"GDP per Capita (Constant US$)":11647.65499,"Total CO2 Emissions (Mt)":134.0395508,"Per Capita CO2 (Mt)":3.982771635,"Share of Global CO2 (%)":0.383466065,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":92.91281128,"Gas CO2 (Mt)":13.15339661,"Cement CO2 (Mt)":4.095958233,"Flaring CO2 (Mt)":23.87738228,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2013,"Population":35281987,"GDP (Constant US$)":422000000000.0,"GDP per Capita (Constant US$)":11960.77761,"Total CO2 Emissions (Mt)":141.7043762,"Per Capita CO2 (Mt)":4.016337872,"Share of Global CO2 (%)":0.401704013,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":98.72647858,"Gas CO2 (Mt)":13.05849552,"Cement CO2 (Mt)":4.831110001,"Flaring CO2 (Mt)":25.0883007,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2014,"Population":36550058,"GDP (Constant US$)":425000000000.0,"GDP per Capita (Constant US$)":11627.88852,"Total CO2 Emissions (Mt)":137.5127106,"Per Capita CO2 (Mt)":3.762311459,"Share of Global CO2 (%)":0.387734413,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":94.73271942,"Gas CO2 (Mt)":12.63347244,"Cement CO2 (Mt)":3.635004997,"Flaring CO2 (Mt)":26.51150703,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2015,"Population":37560535,"GDP (Constant US$)":436000000000.0,"GDP per Capita (Constant US$)":11607.92837,"Total CO2 Emissions (Mt)":142.5299988,"Per Capita CO2 (Mt)":3.794674397,"Share of Global CO2 (%)":0.402586997,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":94.84145355,"Gas CO2 (Mt)":12.9855547,"Cement CO2 (Mt)":4.038894176,"Flaring CO2 (Mt)":30.66409683,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2016,"Population":38469628,"GDP (Constant US$)":502000000000.0,"GDP per Capita (Constant US$)":13049.25538,"Total CO2 Emissions (Mt)":153.1321411,"Per Capita CO2 (Mt)":3.98059845,"Share of Global CO2 (%)":0.432664305,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":97.27187347,"Gas CO2 (Mt)":17.61284828,"Cement CO2 (Mt)":5.250563145,"Flaring CO2 (Mt)":32.99685287,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2017,"Population":39337358,"GDP (Constant US$)":485000000000.0,"GDP per Capita (Constant US$)":12329.24692,"Total CO2 Emissions (Mt)":167.4723511,"Per Capita CO2 (Mt)":4.25733614,"Share of Global CO2 (%)":0.465529293,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":105.6551056,"Gas CO2 (Mt)":22.61787224,"Cement CO2 (Mt)":5.654451847,"Flaring CO2 (Mt)":33.54492188,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2018,"Population":40265629,"GDP (Constant US$)":508000000000.0,"GDP per Capita (Constant US$)":12616.21916,"Total CO2 Emissions (Mt)":186.1564484,"Per Capita CO2 (Mt)":4.623209953,"Share of Global CO2 (%)":0.506768703,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":114.291153,"Gas CO2 (Mt)":28.76972771,"Cement CO2 (Mt)":9.693346977,"Flaring CO2 (Mt)":33.40221786,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2019,"Population":41192172,"GDP (Constant US$)":538000000000.0,"GDP per Capita (Constant US$)":13060.73397,"Total CO2 Emissions (Mt)":191.7776184,"Per Capita CO2 (Mt)":4.655681133,"Share of Global CO2 (%)":0.517107964,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":114.1995544,"Gas CO2 (Mt)":32.99431992,"Cement CO2 (Mt)":10.90501499,"Flaring CO2 (Mt)":33.67873001,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2020,"Population":42116602,"GDP (Constant US$)":453000000000.0,"GDP per Capita (Constant US$)":10755.85348,"Total CO2 Emissions (Mt)":172.0980377,"Per Capita CO2 (Mt)":4.086227894,"Share of Global CO2 (%)":0.489495724,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":93.02162933,"Gas CO2 (Mt)":35.1047821,"Cement CO2 (Mt)":11.30890465,"Flaring CO2 (Mt)":32.66271591,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2021,"Population":43071208,"GDP (Constant US$)":488000000000.0,"GDP per Capita (Constant US$)":11330.07461,"Total CO2 Emissions (Mt)":193.1151581,"Per Capita CO2 (Mt)":4.483624935,"Share of Global CO2 (%)":0.523817718,"Coal CO2 (Mt)":0.0,"Oil CO2 (Mt)":111.6310883,"Gas CO2 (Mt)":36.1343689,"Cement CO2 (Mt)":11.7127943,"Flaring CO2 (Mt)":33.63690948,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2022,"Population":44070556,"GDP (Constant US$)":528000000000.0,"GDP per Capita (Constant US$)":11980.78826,"Total CO2 Emissions (Mt)":217.6439056,"Per Capita CO2 (Mt)":4.938533306,"Share of Global CO2 (%)":0.579954207,"Coal CO2 (Mt)":0.00639,"Oil CO2 (Mt)":134.8347321,"Gas CO2 (Mt)":36.05935287,"Cement CO2 (Mt)":13.08601761,"Flaring CO2 (Mt)":33.65741348,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2023,"Population":45074055,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":227.9096985,"Per Capita CO2 (Mt)":5.056338787,"Share of Global CO2 (%)":0.598281741,"Coal CO2 (Mt)":0.00639,"Oil CO2 (Mt)":143.7993011,"Gas CO2 (Mt)":37.76173401,"Cement CO2 (Mt)":13.08601761,"Flaring CO2 (Mt)":33.25625229,"Other Industry CO2 (Mt)":null},{"Country":"Iraq","ISO Code":"IRQ","Year":2024,"Population":46042015,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":233.635498,"Per Capita CO2 (Mt)":5.074398041,"Share of Global CO2 (%)":0.605295658,"Coal CO2 (Mt)":0.00639,"Oil CO2 (Mt)":147.5327606,"Gas CO2 (Mt)":38.82801056,"Cement CO2 (Mt)":13.08601761,"Flaring CO2 (Mt)":34.18232727,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2006,"Population":2364741,"GDP (Constant US$)":160000000000.0,"GDP per Capita (Constant US$)":67660.68673,"Total CO2 Emissions (Mt)":76.22190094,"Per Capita CO2 (Mt)":32.23266602,"Share of Global CO2 (%)":0.249138802,"Coal CO2 (Mt)":0.002455,"Oil CO2 (Mt)":45.8806076,"Gas CO2 (Mt)":26.23423958,"Cement CO2 (Mt)":0.948794007,"Flaring CO2 (Mt)":3.155805111,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2007,"Population":2507890,"GDP (Constant US$)":175000000000.0,"GDP per Capita (Constant US$)":69779.77503,"Total CO2 Emissions (Mt)":77.29495239,"Per Capita CO2 (Mt)":30.82071114,"Share of Global CO2 (%)":0.245386586,"Coal CO2 (Mt)":0.002043,"Oil CO2 (Mt)":48.05937576,"Gas CO2 (Mt)":25.53932953,"Cement CO2 (Mt)":0.931162,"Flaring CO2 (Mt)":2.763041973,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2008,"Population":2651433,"GDP (Constant US$)":184000000000.0,"GDP per Capita (Constant US$)":69396.43581,"Total CO2 Emissions (Mt)":84.44237518,"Per Capita CO2 (Mt)":31.847826,"Share of Global CO2 (%)":0.263473541,"Coal CO2 (Mt)":0.001267,"Oil CO2 (Mt)":54.36276627,"Gas CO2 (Mt)":26.61895943,"Cement CO2 (Mt)":1.090852022,"Flaring CO2 (Mt)":2.368529081,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2009,"Population":2795489,"GDP (Constant US$)":175000000000.0,"GDP per Capita (Constant US$)":62600.85445,"Total CO2 Emissions (Mt)":88.83209229,"Per Capita CO2 (Mt)":31.77694321,"Share of Global CO2 (%)":0.281890184,"Coal CO2 (Mt)":0.002317,"Oil CO2 (Mt)":61.74939346,"Gas CO2 (Mt)":24.10179138,"Cement CO2 (Mt)":0.832221985,"Flaring CO2 (Mt)":2.146368027,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2010,"Population":2943374,"GDP (Constant US$)":176000000000.0,"GDP per Capita (Constant US$)":59795.32333,"Total CO2 Emissions (Mt)":89.72100067,"Per Capita CO2 (Mt)":30.48236465,"Share of Global CO2 (%)":0.269289523,"Coal CO2 (Mt)":0.003378,"Oil CO2 (Mt)":58.74124908,"Gas CO2 (Mt)":28.13219261,"Cement CO2 (Mt)":0.828836024,"Flaring CO2 (Mt)":2.015347004,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2011,"Population":3132815,"GDP (Constant US$)":201000000000.0,"GDP per Capita (Constant US$)":64159.5498,"Total CO2 Emissions (Mt)":87.15087128,"Per Capita CO2 (Mt)":27.81871033,"Share of Global CO2 (%)":0.252757818,"Coal CO2 (Mt)":0.050818,"Oil CO2 (Mt)":51.24103928,"Gas CO2 (Mt)":32.8587532,"Cement CO2 (Mt)":0.928569973,"Flaring CO2 (Mt)":2.071687937,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2012,"Population":3337025,"GDP (Constant US$)":215000000000.0,"GDP per Capita (Constant US$)":64428.64528,"Total CO2 Emissions (Mt)":101.2005768,"Per Capita CO2 (Mt)":30.32658577,"Share of Global CO2 (%)":0.289518923,"Coal CO2 (Mt)":0.531852007,"Oil CO2 (Mt)":62.82660675,"Gas CO2 (Mt)":34.73105621,"Cement CO2 (Mt)":0.983030021,"Flaring CO2 (Mt)":2.128029108,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2013,"Population":3507755,"GDP (Constant US$)":217000000000.0,"GDP per Capita (Constant US$)":61862.92942,"Total CO2 Emissions (Mt)":83.04668427,"Per Capita CO2 (Mt)":23.67516708,"Share of Global CO2 (%)":0.235420987,"Coal CO2 (Mt)":0.58940202,"Oil CO2 (Mt)":44.24646378,"Gas CO2 (Mt)":34.56617737,"Cement CO2 (Mt)":1.207777977,"Flaring CO2 (Mt)":2.436861992,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2014,"Population":3665769,"GDP (Constant US$)":218000000000.0,"GDP per Capita (Constant US$)":59469.10457,"Total CO2 Emissions (Mt)":74.99373627,"Per Capita CO2 (Mt)":20.45784569,"Share of Global CO2 (%)":0.211454287,"Coal CO2 (Mt)":0.811269999,"Oil CO2 (Mt)":36.12516022,"Gas CO2 (Mt)":34.28207779,"Cement CO2 (Mt)":1.130890012,"Flaring CO2 (Mt)":2.644335985,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2015,"Population":3834465,"GDP (Constant US$)":219000000000.0,"GDP per Capita (Constant US$)":57113.57386,"Total CO2 Emissions (Mt)":93.31747437,"Per Capita CO2 (Mt)":24.33650398,"Share of Global CO2 (%)":0.263582408,"Coal CO2 (Mt)":0.846946001,"Oil CO2 (Mt)":50.47726059,"Gas CO2 (Mt)":39.06711197,"Cement CO2 (Mt)":1.252056956,"Flaring CO2 (Mt)":1.674098015,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2016,"Population":4003976,"GDP (Constant US$)":226000000000.0,"GDP per Capita (Constant US$)":56443.89477,"Total CO2 Emissions (Mt)":104.0188293,"Per Capita CO2 (Mt)":25.97888565,"Share of Global CO2 (%)":0.293898016,"Coal CO2 (Mt)":0.778208017,"Oil CO2 (Mt)":58.28691101,"Gas CO2 (Mt)":41.25664139,"Cement CO2 (Mt)":1.615558028,"Flaring CO2 (Mt)":2.081512928,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2017,"Population":4154686,"GDP (Constant US$)":215000000000.0,"GDP per Capita (Constant US$)":51748.79642,"Total CO2 Emissions (Mt)":100.0103607,"Per Capita CO2 (Mt)":24.07170105,"Share of Global CO2 (%)":0.27800262,"Coal CO2 (Mt)":0.534137011,"Oil CO2 (Mt)":54.6868515,"Gas CO2 (Mt)":41.92927551,"Cement CO2 (Mt)":1.37322402,"Flaring CO2 (Mt)":1.486868978,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2018,"Population":4323389,"GDP (Constant US$)":220000000000.0,"GDP per Capita (Constant US$)":50886.00633,"Total CO2 Emissions (Mt)":102.4530106,"Per Capita CO2 (Mt)":23.69738388,"Share of Global CO2 (%)":0.278905094,"Coal CO2 (Mt)":0.746029973,"Oil CO2 (Mt)":55.92729568,"Gas CO2 (Mt)":42.76987076,"Cement CO2 (Mt)":1.37322402,"Flaring CO2 (Mt)":1.636587024,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2019,"Population":4442201,"GDP (Constant US$)":219000000000.0,"GDP per Capita (Constant US$)":49299.88535,"Total CO2 Emissions (Mt)":104.654213,"Per Capita CO2 (Mt)":23.55909157,"Share of Global CO2 (%)":0.282188982,"Coal CO2 (Mt)":0.578492999,"Oil CO2 (Mt)":54.85933685,"Gas CO2 (Mt)":46.26695251,"Cement CO2 (Mt)":1.575168967,"Flaring CO2 (Mt)":1.374261975,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2020,"Population":4400146,"GDP (Constant US$)":200000000000.0,"GDP per Capita (Constant US$)":45453.03724,"Total CO2 Emissions (Mt)":90.10260773,"Per Capita CO2 (Mt)":20.4771862,"Share of Global CO2 (%)":0.256277442,"Coal CO2 (Mt)":0.162671,"Oil CO2 (Mt)":35.48950577,"Gas CO2 (Mt)":51.68804932,"Cement CO2 (Mt)":1.37322402,"Flaring CO2 (Mt)":1.389161944,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2021,"Population":4360748,"GDP (Constant US$)":202000000000.0,"GDP per Capita (Constant US$)":46322.32819,"Total CO2 Emissions (Mt)":87.86885071,"Per Capita CO2 (Mt)":20.14994812,"Share of Global CO2 (%)":0.238340989,"Coal CO2 (Mt)":0.277678013,"Oil CO2 (Mt)":30.80691147,"Gas CO2 (Mt)":54.09896088,"Cement CO2 (Mt)":1.413612962,"Flaring CO2 (Mt)":1.271690965,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2022,"Population":4589514,"GDP (Constant US$)":219000000000.0,"GDP per Capita (Constant US$)":47717.47074,"Total CO2 Emissions (Mt)":115.8488846,"Per Capita CO2 (Mt)":25.2420826,"Share of Global CO2 (%)":0.308701724,"Coal CO2 (Mt)":0.336952001,"Oil CO2 (Mt)":65.63865662,"Gas CO2 (Mt)":47.31271362,"Cement CO2 (Mt)":1.466119051,"Flaring CO2 (Mt)":1.09444499,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2023,"Population":4838781,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":123.1687164,"Per Capita CO2 (Mt)":25.45449448,"Share of Global CO2 (%)":0.323328048,"Coal CO2 (Mt)":0.621074975,"Oil CO2 (Mt)":68.08499146,"Gas CO2 (Mt)":51.75854492,"Cement CO2 (Mt)":1.466119051,"Flaring CO2 (Mt)":1.237982988,"Other Industry CO2 (Mt)":null},{"Country":"Kuwait","ISO Code":"KWT","Year":2024,"Population":4934508,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":129.5186462,"Per Capita CO2 (Mt)":26.24752998,"Share of Global CO2 (%)":0.335552901,"Coal CO2 (Mt)":0.622776985,"Oil CO2 (Mt)":72.45774841,"Gas CO2 (Mt)":53.83282089,"Cement CO2 (Mt)":1.466119051,"Flaring CO2 (Mt)":1.139186025,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2006,"Population":21459141,"GDP (Constant US$)":834000000000.0,"GDP per Capita (Constant US$)":38864.5566,"Total CO2 Emissions (Mt)":444.9772644,"Per Capita CO2 (Mt)":20.73602486,"Share of Global CO2 (%)":1.454452038,"Coal CO2 (Mt)":0.038036,"Oil CO2 (Mt)":283.7658081,"Gas CO2 (Mt)":141.0127106,"Cement CO2 (Mt)":12.20019436,"Flaring CO2 (Mt)":7.960536003,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2007,"Population":22368313,"GDP (Constant US$)":896000000000.0,"GDP per Capita (Constant US$)":40056.66409,"Total CO2 Emissions (Mt)":423.3140869,"Per Capita CO2 (Mt)":18.92472076,"Share of Global CO2 (%)":1.343885899,"Coal CO2 (Mt)":0.054790001,"Oil CO2 (Mt)":258.4658813,"Gas CO2 (Mt)":142.8520355,"Cement CO2 (Mt)":13.96100998,"Flaring CO2 (Mt)":7.980377197,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2008,"Population":23287884,"GDP (Constant US$)":1010000000000.0,"GDP per Capita (Constant US$)":43370.19198,"Total CO2 Emissions (Mt)":469.4303894,"Per Capita CO2 (Mt)":20.15770912,"Share of Global CO2 (%)":1.464697003,"Coal CO2 (Mt)":0.108299002,"Oil CO2 (Mt)":288.8171387,"Gas CO2 (Mt)":154.4095306,"Cement CO2 (Mt)":18.0881958,"Flaring CO2 (Mt)":8.007230759,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2009,"Population":24217656,"GDP (Constant US$)":1040000000000.0,"GDP per Capita (Constant US$)":42943.87533,"Total CO2 Emissions (Mt)":503.9696655,"Per Capita CO2 (Mt)":20.81001091,"Share of Global CO2 (%)":1.599242926,"Coal CO2 (Mt)":0.067369998,"Oil CO2 (Mt)":326.0666809,"Gas CO2 (Mt)":150.5903931,"Cement CO2 (Mt)":19.87462616,"Flaring CO2 (Mt)":7.370578766,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2010,"Population":25157134,"GDP (Constant US$)":1160000000000.0,"GDP per Capita (Constant US$)":46110.18091,"Total CO2 Emissions (Mt)":555.6397705,"Per Capita CO2 (Mt)":22.0867672,"Share of Global CO2 (%)":1.667702794,"Coal CO2 (Mt)":0.169965997,"Oil CO2 (Mt)":359.6448364,"Gas CO2 (Mt)":168.2680664,"Cement CO2 (Mt)":20.6687088,"Flaring CO2 (Mt)":6.888176918,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2011,"Population":26105636,"GDP (Constant US$)":1350000000000.0,"GDP per Capita (Constant US$)":51712.9711,"Total CO2 Emissions (Mt)":540.2358398,"Per Capita CO2 (Mt)":20.6942234,"Share of Global CO2 (%)":1.566809893,"Coal CO2 (Mt)":0.170003995,"Oil CO2 (Mt)":335.7103271,"Gas CO2 (Mt)":177.0994415,"Cement CO2 (Mt)":21.98893738,"Flaring CO2 (Mt)":5.26709795,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2012,"Population":27062447,"GDP (Constant US$)":1420000000000.0,"GDP per Capita (Constant US$)":52471.2344,"Total CO2 Emissions (Mt)":605.7122803,"Per Capita CO2 (Mt)":22.38202095,"Share of Global CO2 (%)":1.732847452,"Coal CO2 (Mt)":0.192636997,"Oil CO2 (Mt)":386.2185669,"Gas CO2 (Mt)":190.6708984,"Cement CO2 (Mt)":24.9841671,"Flaring CO2 (Mt)":3.646018982,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2013,"Population":28026825,"GDP (Constant US$)":1460000000000.0,"GDP per Capita (Constant US$)":52092.95024,"Total CO2 Emissions (Mt)":583.1779175,"Per Capita CO2 (Mt)":20.80784798,"Share of Global CO2 (%)":1.653194427,"Coal CO2 (Mt)":0.238622993,"Oil CO2 (Mt)":359.3811646,"Gas CO2 (Mt)":192.0106964,"Cement CO2 (Mt)":27.78912735,"Flaring CO2 (Mt)":3.758332014,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2014,"Population":28998127,"GDP (Constant US$)":1520000000000.0,"GDP per Capita (Constant US$)":52417.17853,"Total CO2 Emissions (Mt)":585.1091309,"Per Capita CO2 (Mt)":20.17747879,"Share of Global CO2 (%)":1.649788976,"Coal CO2 (Mt)":0.256942004,"Oil CO2 (Mt)":355.2797546,"Gas CO2 (Mt)":196.5223083,"Cement CO2 (Mt)":29.39550972,"Flaring CO2 (Mt)":3.654615879,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2015,"Population":29974944,"GDP (Constant US$)":1590000000000.0,"GDP per Capita (Constant US$)":53044.3026,"Total CO2 Emissions (Mt)":624.5469971,"Per Capita CO2 (Mt)":20.83563614,"Share of Global CO2 (%)":1.764081359,"Coal CO2 (Mt)":0.259882987,"Oil CO2 (Mt)":390.526062,"Gas CO2 (Mt)":200.4989166,"Cement CO2 (Mt)":29.2140274,"Flaring CO2 (Mt)":4.048099995,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2016,"Population":30717804,"GDP (Constant US$)":1630000000000.0,"GDP per Capita (Constant US$)":53063.68906,"Total CO2 Emissions (Mt)":641.1741943,"Per Capita CO2 (Mt)":20.87304878,"Share of Global CO2 (%)":1.811593413,"Coal CO2 (Mt)":0.329757988,"Oil CO2 (Mt)":395.7243958,"Gas CO2 (Mt)":212.8002167,"Cement CO2 (Mt)":28.43586922,"Flaring CO2 (Mt)":3.883928061,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2017,"Population":30782400,"GDP (Constant US$)":1630000000000.0,"GDP per Capita (Constant US$)":52952.3364,"Total CO2 Emissions (Mt)":644.4865112,"Per Capita CO2 (Mt)":20.9368515,"Share of Global CO2 (%)":1.791503787,"Coal CO2 (Mt)":0.520287991,"Oil CO2 (Mt)":393.1252136,"Gas CO2 (Mt)":222.8591309,"Cement CO2 (Mt)":23.62956429,"Flaring CO2 (Mt)":4.352303028,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2018,"Population":30365119,"GDP (Constant US$)":1670000000000.0,"GDP per Capita (Constant US$)":54997.31452,"Total CO2 Emissions (Mt)":652.2041626,"Per Capita CO2 (Mt)":21.47872925,"Share of Global CO2 (%)":1.775477886,"Coal CO2 (Mt)":0.461663991,"Oil CO2 (Mt)":391.611969,"Gas CO2 (Mt)":231.0445099,"Cement CO2 (Mt)":24.74881172,"Flaring CO2 (Mt)":4.337221146,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2019,"Population":30472809,"GDP (Constant US$)":1690000000000.0,"GDP per Capita (Constant US$)":55459.27847,"Total CO2 Emissions (Mt)":708.3347168,"Per Capita CO2 (Mt)":23.24481201,"Share of Global CO2 (%)":1.909949422,"Coal CO2 (Mt)":0.483648002,"Oil CO2 (Mt)":446.9933472,"Gas CO2 (Mt)":233.2245941,"Cement CO2 (Mt)":23.68429947,"Flaring CO2 (Mt)":3.948855877,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2020,"Population":30991206,"GDP (Constant US$)":1610000000000.0,"GDP per Capita (Constant US$)":51950.22098,"Total CO2 Emissions (Mt)":653.5646973,"Per Capita CO2 (Mt)":21.0887146,"Share of Global CO2 (%)":1.858923793,"Coal CO2 (Mt)":0.425022006,"Oil CO2 (Mt)":388.2792358,"Gas CO2 (Mt)":234.9526825,"Cement CO2 (Mt)":25.65122032,"Flaring CO2 (Mt)":4.256532192,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2021,"Population":31328374,"GDP (Constant US$)":1680000000000.0,"GDP per Capita (Constant US$)":53625.50894,"Total CO2 Emissions (Mt)":695.3944702,"Per Capita CO2 (Mt)":22.19695473,"Share of Global CO2 (%)":1.88623178,"Coal CO2 (Mt)":0.516623974,"Oil CO2 (Mt)":420.6491699,"Gas CO2 (Mt)":241.8643036,"Cement CO2 (Mt)":28.37277985,"Flaring CO2 (Mt)":3.991555929,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2022,"Population":32175351,"GDP (Constant US$)":1820000000000.0,"GDP per Capita (Constant US$)":56565.03949,"Total CO2 Emissions (Mt)":666.9935303,"Per Capita CO2 (Mt)":20.72995377,"Share of Global CO2 (%)":1.77733314,"Coal CO2 (Mt)":0.509296,"Oil CO2 (Mt)":435.5067139,"Gas CO2 (Mt)":197.9454803,"Cement CO2 (Mt)":29.53600883,"Flaring CO2 (Mt)":3.496023893,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2023,"Population":33264289,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":677.4418945,"Per Capita CO2 (Mt)":20.36544037,"Share of Global CO2 (%)":1.778340936,"Coal CO2 (Mt)":0.630457997,"Oil CO2 (Mt)":443.7353516,"Gas CO2 (Mt)":198.9709015,"Cement CO2 (Mt)":29.42770576,"Flaring CO2 (Mt)":4.677474022,"Other Industry CO2 (Mt)":null},{"Country":"Saudi Arabia","ISO Code":"SAU","Year":2024,"Population":33962751,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":692.1334839,"Per Capita CO2 (Mt)":20.37919426,"Share of Global CO2 (%)":1.793157935,"Coal CO2 (Mt)":0.70064497,"Oil CO2 (Mt)":451.4613037,"Gas CO2 (Mt)":205.9694061,"Cement CO2 (Mt)":29.3800602,"Flaring CO2 (Mt)":4.622074127,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2006,"Population":5009106,"GDP (Constant US$)":307000000000.0,"GDP per Capita (Constant US$)":61288.3816,"Total CO2 Emissions (Mt)":122.7231827,"Per Capita CO2 (Mt)":24.50001717,"Share of Global CO2 (%)":0.401132822,"Coal CO2 (Mt)":1.066223979,"Oil CO2 (Mt)":31.6935997,"Gas CO2 (Mt)":82.56091309,"Cement CO2 (Mt)":5.606507778,"Flaring CO2 (Mt)":1.795936942,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2007,"Population":5624640,"GDP (Constant US$)":368000000000.0,"GDP per Capita (Constant US$)":65426.40951,"Total CO2 Emissions (Mt)":134.1031494,"Per Capita CO2 (Mt)":23.84208679,"Share of Global CO2 (%)":0.425734341,"Coal CO2 (Mt)":0.512960017,"Oil CO2 (Mt)":33.79673767,"Gas CO2 (Mt)":91.29589081,"Cement CO2 (Mt)":6.772087097,"Flaring CO2 (Mt)":1.725476027,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2008,"Population":6302669,"GDP (Constant US$)":465000000000.0,"GDP per Capita (Constant US$)":73778.26759,"Total CO2 Emissions (Mt)":155.0303802,"Per Capita CO2 (Mt)":24.59757614,"Share of Global CO2 (%)":0.483719289,"Coal CO2 (Mt)":1.374065042,"Oil CO2 (Mt)":35.06980896,"Gas CO2 (Mt)":107.8073196,"Cement CO2 (Mt)":9.182032585,"Flaring CO2 (Mt)":1.597156048,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2009,"Population":6707063,"GDP (Constant US$)":481000000000.0,"GDP per Capita (Constant US$)":71715.44385,"Total CO2 Emissions (Mt)":169.0881042,"Per Capita CO2 (Mt)":25.21045494,"Share of Global CO2 (%)":0.536565959,"Coal CO2 (Mt)":1.040575981,"Oil CO2 (Mt)":45.08185577,"Gas CO2 (Mt)":113.4704132,"Cement CO2 (Mt)":7.904863834,"Flaring CO2 (Mt)":1.590404034,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2010,"Population":6938372,"GDP (Constant US$)":490000000000.0,"GDP per Capita (Constant US$)":70621.75392,"Total CO2 Emissions (Mt)":185.8484039,"Per Capita CO2 (Mt)":26.78559113,"Share of Global CO2 (%)":0.557807326,"Coal CO2 (Mt)":2.476912975,"Oil CO2 (Mt)":57.38670349,"Gas CO2 (Mt)":116.8692551,"Cement CO2 (Mt)":7.459520817,"Flaring CO2 (Mt)":1.656015038,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2011,"Population":7199436,"GDP (Constant US$)":551000000000.0,"GDP per Capita (Constant US$)":76533.77292,"Total CO2 Emissions (Mt)":198.5181885,"Per Capita CO2 (Mt)":27.57413101,"Share of Global CO2 (%)":0.57574898,"Coal CO2 (Mt)":1.678081036,"Oil CO2 (Mt)":58.34812164,"Gas CO2 (Mt)":130.1685181,"Cement CO2 (Mt)":6.603162766,"Flaring CO2 (Mt)":1.720309973,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2012,"Population":7497122,"GDP (Constant US$)":577000000000.0,"GDP per Capita (Constant US$)":76962.86655,"Total CO2 Emissions (Mt)":208.3235626,"Per Capita CO2 (Mt)":27.78713799,"Share of Global CO2 (%)":0.595980942,"Coal CO2 (Mt)":5.250605106,"Oil CO2 (Mt)":62.53459167,"Gas CO2 (Mt)":132.6098328,"Cement CO2 (Mt)":6.143937111,"Flaring CO2 (Mt)":1.784605026,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2013,"Population":7831851,"GDP (Constant US$)":607000000000.0,"GDP per Capita (Constant US$)":77504.0281,"Total CO2 Emissions (Mt)":214.1880646,"Per Capita CO2 (Mt)":27.34833145,"Share of Global CO2 (%)":0.607180953,"Coal CO2 (Mt)":6.719660759,"Oil CO2 (Mt)":62.40784073,"Gas CO2 (Mt)":136.4083862,"Cement CO2 (Mt)":6.320702076,"Flaring CO2 (Mt)":2.33147788,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2014,"Population":8236880,"GDP (Constant US$)":632000000000.0,"GDP per Capita (Constant US$)":76728.08151,"Total CO2 Emissions (Mt)":214.5303345,"Per Capita CO2 (Mt)":26.04509735,"Share of Global CO2 (%)":0.604895353,"Coal CO2 (Mt)":7.485291004,"Oil CO2 (Mt)":60.2560463,"Gas CO2 (Mt)":133.3393097,"Cement CO2 (Mt)":11.70683289,"Flaring CO2 (Mt)":1.74285996,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2015,"Population":8674633,"GDP (Constant US$)":675000000000.0,"GDP per Capita (Constant US$)":77813.09019,"Total CO2 Emissions (Mt)":225.0448303,"Per Capita CO2 (Mt)":25.94286537,"Share of Global CO2 (%)":0.635656536,"Coal CO2 (Mt)":6.507157803,"Oil CO2 (Mt)":74.30104828,"Gas CO2 (Mt)":134.1551819,"Cement CO2 (Mt)":8.279733658,"Flaring CO2 (Mt)":1.801702976,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2016,"Population":9030873,"GDP (Constant US$)":712000000000.0,"GDP per Capita (Constant US$)":78840.66136,"Total CO2 Emissions (Mt)":227.8977203,"Per Capita CO2 (Mt)":25.23540306,"Share of Global CO2 (%)":0.643909276,"Coal CO2 (Mt)":6.97636795,"Oil CO2 (Mt)":77.71468353,"Gas CO2 (Mt)":134.9143066,"Cement CO2 (Mt)":6.825731754,"Flaring CO2 (Mt)":1.466634989,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2017,"Population":9234330,"GDP (Constant US$)":718000000000.0,"GDP per Capita (Constant US$)":77753.33998,"Total CO2 Emissions (Mt)":196.4928284,"Per Capita CO2 (Mt)":21.27851486,"Share of Global CO2 (%)":0.546198666,"Coal CO2 (Mt)":8.068127632,"Oil CO2 (Mt)":59.60228729,"Gas CO2 (Mt)":119.9593582,"Cement CO2 (Mt)":7.027676105,"Flaring CO2 (Mt)":1.835379958,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2018,"Population":9346870,"GDP (Constant US$)":727000000000.0,"GDP per Capita (Constant US$)":77780.04829,"Total CO2 Emissions (Mt)":204.1047974,"Per Capita CO2 (Mt)":21.83670044,"Share of Global CO2 (%)":0.555629075,"Coal CO2 (Mt)":7.276574135,"Oil CO2 (Mt)":70.02877808,"Gas CO2 (Mt)":117.5756607,"Cement CO2 (Mt)":6.946897984,"Flaring CO2 (Mt)":2.276894093,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2019,"Population":9377855,"GDP (Constant US$)":735000000000.0,"GDP per Capita (Constant US$)":78376.13186,"Total CO2 Emissions (Mt)":204.058075,"Per Capita CO2 (Mt)":21.75956917,"Share of Global CO2 (%)":0.550220966,"Coal CO2 (Mt)":6.734312057,"Oil CO2 (Mt)":58.16495895,"Gas CO2 (Mt)":130.9636688,"Cement CO2 (Mt)":6.50262022,"Flaring CO2 (Mt)":1.692512035,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2020,"Population":9448529,"GDP (Constant US$)":699000000000.0,"GDP per Capita (Constant US$)":73979.76976,"Total CO2 Emissions (Mt)":215.2661743,"Per Capita CO2 (Mt)":22.78303528,"Share of Global CO2 (%)":0.612278223,"Coal CO2 (Mt)":8.086447716,"Oil CO2 (Mt)":67.01455688,"Gas CO2 (Mt)":132.3510132,"Cement CO2 (Mt)":6.017952919,"Flaring CO2 (Mt)":1.79619801,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2021,"Population":9789055,"GDP (Constant US$)":726000000000.0,"GDP per Capita (Constant US$)":74164.46225,"Total CO2 Emissions (Mt)":212.1729584,"Per Capita CO2 (Mt)":21.67450905,"Share of Global CO2 (%)":0.575511277,"Coal CO2 (Mt)":10.05384254,"Oil CO2 (Mt)":69.80532837,"Gas CO2 (Mt)":124.6214828,"Cement CO2 (Mt)":6.05834198,"Flaring CO2 (Mt)":1.633967996,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2022,"Population":10242085,"GDP (Constant US$)":780000000000.0,"GDP per Capita (Constant US$)":76156.36855,"Total CO2 Emissions (Mt)":207.1034088,"Per Capita CO2 (Mt)":20.2208252,"Share of Global CO2 (%)":0.551867008,"Coal CO2 (Mt)":3.939755917,"Oil CO2 (Mt)":60.79308701,"Gas CO2 (Mt)":134.4881439,"Cement CO2 (Mt)":6.139120102,"Flaring CO2 (Mt)":1.743296027,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2023,"Population":10642089,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":210.4251099,"Per Capita CO2 (Mt)":19.77291298,"Share of Global CO2 (%)":0.552383244,"Coal CO2 (Mt)":4.01222086,"Oil CO2 (Mt)":62.89125061,"Gas CO2 (Mt)":135.6773071,"Cement CO2 (Mt)":6.139120102,"Flaring CO2 (Mt)":1.70520699,"Other Industry CO2 (Mt)":null},{"Country":"United Arab Emirates","ISO Code":"ARE","Year":2024,"Population":11027135,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":221.9880829,"Per Capita CO2 (Mt)":20.13107491,"Share of Global CO2 (%)":0.575119853,"Coal CO2 (Mt)":4.316827774,"Oil CO2 (Mt)":65.55870819,"Gas CO2 (Mt)":144.4530182,"Cement CO2 (Mt)":6.139120102,"Flaring CO2 (Mt)":1.520411968,"Other Industry CO2 (Mt)":null},{"Country":"World","ISO Code":null,"Year":2006,"Population":6671452019,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":30594.15234,"Per Capita CO2 (Mt)":4.585831165,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":12136.23828,"Oil CO2 (Mt)":11142.92773,"Gas CO2 (Mt)":5531.005859,"Cement CO2 (Mt)":1047.294189,"Flaring CO2 (Mt)":346.5730896,"Other Industry CO2 (Mt)":390.1127319},{"Country":"World","ISO Code":null,"Year":2007,"Population":6757308776,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":31499.25586,"Per Capita CO2 (Mt)":4.661509037,"Share of Global CO2 (%)":99.99999237,"Coal CO2 (Mt)":12724.45117,"Oil CO2 (Mt)":11184.3125,"Gas CO2 (Mt)":5736.636719,"Cement CO2 (Mt)":1126.199097,"Flaring CO2 (Mt)":342.2504883,"Other Industry CO2 (Mt)":385.4050903},{"Country":"World","ISO Code":null,"Year":2008,"Population":6844457659,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":32049.66016,"Per Capita CO2 (Mt)":4.682570934,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":13149.66895,"Oil CO2 (Mt)":11143.33984,"Gas CO2 (Mt)":5905.500488,"Cement CO2 (Mt)":1137.397217,"Flaring CO2 (Mt)":333.6859436,"Other Industry CO2 (Mt)":380.0678406},{"Country":"World","ISO Code":null,"Year":2009,"Population":6932766416,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":31513.01367,"Per Capita CO2 (Mt)":4.545517921,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":13003.17188,"Oil CO2 (Mt)":10899.59668,"Gas CO2 (Mt)":5765.684082,"Cement CO2 (Mt)":1170.605957,"Flaring CO2 (Mt)":328.6357422,"Other Industry CO2 (Mt)":345.3191223},{"Country":"World","ISO Code":null,"Year":2010,"Population":7021732143,"GDP (Constant US$)":89800000000000.0,"GDP per Capita (Constant US$)":12788.86722,"Total CO2 Emissions (Mt)":33317.67188,"Per Capita CO2 (Mt)":4.744935989,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":13918.22363,"Oil CO2 (Mt)":11253.69434,"Gas CO2 (Mt)":6205.779785,"Cement CO2 (Mt)":1251.813477,"Flaring CO2 (Mt)":339.7408142,"Other Industry CO2 (Mt)":348.4214783},{"Country":"World","ISO Code":null,"Year":2011,"Population":7110923773,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":34479.98828,"Per Capita CO2 (Mt)":4.848875999,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14704.22266,"Oil CO2 (Mt)":11310.14844,"Gas CO2 (Mt)":6389.330078,"Cement CO2 (Mt)":1344.746826,"Flaring CO2 (Mt)":356.250885,"Other Industry CO2 (Mt)":375.2902527},{"Country":"World","ISO Code":null,"Year":2012,"Population":7201202478,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":34954.73438,"Per Capita CO2 (Mt)":4.85401392,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14867.80176,"Oil CO2 (Mt)":11432.71582,"Gas CO2 (Mt)":6523.143066,"Cement CO2 (Mt)":1377.354248,"Flaring CO2 (Mt)":374.0588074,"Other Industry CO2 (Mt)":379.6605835},{"Country":"World","ISO Code":null,"Year":2013,"Population":7291793585,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":35275.82031,"Per Capita CO2 (Mt)":4.837742805,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14953.15332,"Oil CO2 (Mt)":11516.62598,"Gas CO2 (Mt)":6573.115723,"Cement CO2 (Mt)":1441.33374,"Flaring CO2 (Mt)":382.0171204,"Other Industry CO2 (Mt)":409.5744019},{"Country":"World","ISO Code":null,"Year":2014,"Population":7381616239,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":35465.69531,"Per Capita CO2 (Mt)":4.804597378,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":15014.88281,"Oil CO2 (Mt)":11561.83203,"Gas CO2 (Mt)":6604.975586,"Cement CO2 (Mt)":1492.45105,"Flaring CO2 (Mt)":383.7722168,"Other Industry CO2 (Mt)":407.7796326},{"Country":"World","ISO Code":null,"Year":2015,"Population":7470491876,"GDP (Constant US$)":107000000000000.0,"GDP per Capita (Constant US$)":14323.01939,"Total CO2 Emissions (Mt)":35403.52734,"Per Capita CO2 (Mt)":4.739115715,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14655.0166,"Oil CO2 (Mt)":11770.02246,"Gas CO2 (Mt)":6728.989258,"Cement CO2 (Mt)":1440.665527,"Flaring CO2 (Mt)":381.1936646,"Other Industry CO2 (Mt)":427.6400452},{"Country":"World","ISO Code":null,"Year":2016,"Population":7558554527,"GDP (Constant US$)":110000000000000.0,"GDP per Capita (Constant US$)":14553.04709,"Total CO2 Emissions (Mt)":35392.83203,"Per Capita CO2 (Mt)":4.682486534,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14322.98926,"Oil CO2 (Mt)":11900.26367,"Gas CO2 (Mt)":6914.850098,"Cement CO2 (Mt)":1476.147461,"Flaring CO2 (Mt)":371.5081787,"Other Industry CO2 (Mt)":407.072113},{"Country":"World","ISO Code":null,"Year":2017,"Population":7645617952,"GDP (Constant US$)":115000000000000.0,"GDP per Capita (Constant US$)":15041.29564,"Total CO2 Emissions (Mt)":35974.60938,"Per Capita CO2 (Mt)":4.705258846,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14494.16797,"Oil CO2 (Mt)":12085.29199,"Gas CO2 (Mt)":7084.614746,"Cement CO2 (Mt)":1499.946777,"Flaring CO2 (Mt)":384.2122498,"Other Industry CO2 (Mt)":426.3757935},{"Country":"World","ISO Code":null,"Year":2018,"Population":7729902779,"GDP (Constant US$)":119000000000000.0,"GDP per Capita (Constant US$)":15394.76025,"Total CO2 Emissions (Mt)":36734.00391,"Per Capita CO2 (Mt)":4.752194881,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14762.69434,"Oil CO2 (Mt)":12142.82813,"Gas CO2 (Mt)":7419.413086,"Cement CO2 (Mt)":1546.848633,"Flaring CO2 (Mt)":404.040863,"Other Industry CO2 (Mt)":458.1777344},{"Country":"World","ISO Code":null,"Year":2019,"Population":7811293699,"GDP (Constant US$)":122000000000000.0,"GDP per Capita (Constant US$)":15618.41158,"Total CO2 Emissions (Mt)":37086.56641,"Per Capita CO2 (Mt)":4.747813702,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14702.95605,"Oil CO2 (Mt)":12325.9082,"Gas CO2 (Mt)":7574.056152,"Cement CO2 (Mt)":1615.726563,"Flaring CO2 (Mt)":432.3918762,"Other Industry CO2 (Mt)":435.526825},{"Country":"World","ISO Code":null,"Year":2020,"Population":7887001289,"GDP (Constant US$)":119000000000000.0,"GDP per Capita (Constant US$)":15088.11722,"Total CO2 Emissions (Mt)":35158.23047,"Per Capita CO2 (Mt)":4.457743645,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14267.03516,"Oil CO2 (Mt)":10932.3418,"Gas CO2 (Mt)":7520.819824,"Cement CO2 (Mt)":1624.052246,"Flaring CO2 (Mt)":400.0012817,"Other Industry CO2 (Mt)":413.9787903},{"Country":"World","ISO Code":null,"Year":2021,"Population":7954448387,"GDP (Constant US$)":126000000000000.0,"GDP per Capita (Constant US$)":15840.19329,"Total CO2 Emissions (Mt)":36866.86328,"Per Capita CO2 (Mt)":4.634747982,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":14969.24902,"Oil CO2 (Mt)":11513.16602,"Gas CO2 (Mt)":7878.698242,"Cement CO2 (Mt)":1666.88501,"Flaring CO2 (Mt)":402.2161865,"Other Industry CO2 (Mt)":436.6485901},{"Country":"World","ISO Code":null,"Year":2022,"Population":8021407196,"GDP (Constant US$)":130000000000000.0,"GDP per Capita (Constant US$)":16206.63268,"Total CO2 Emissions (Mt)":37527.77344,"Per Capita CO2 (Mt)":4.678452492,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":15449.17676,"Oil CO2 (Mt)":11914.91211,"Gas CO2 (Mt)":7758.745605,"Cement CO2 (Mt)":1578.73938,"Flaring CO2 (Mt)":398.8711243,"Other Industry CO2 (Mt)":427.3265686},{"Country":"World","ISO Code":null,"Year":2023,"Population":8091734933,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":38094.03906,"Per Capita CO2 (Mt)":4.707771778,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":15636.37305,"Oil CO2 (Mt)":12278.24121,"Gas CO2 (Mt)":7802.845215,"Cement CO2 (Mt)":1540.286255,"Flaring CO2 (Mt)":411.3427124,"Other Industry CO2 (Mt)":424.9551697},{"Country":"World","ISO Code":null,"Year":2024,"Population":8161972574,"GDP (Constant US$)":null,"GDP per Capita (Constant US$)":null,"Total CO2 Emissions (Mt)":38598.57813,"Per Capita CO2 (Mt)":4.729074955,"Share of Global CO2 (%)":100.0,"Coal CO2 (Mt)":15805.25391,"Oil CO2 (Mt)":12470.5957,"Gas CO2 (Mt)":8009.827637,"Cement CO2 (Mt)":1472.817505,"Flaring CO2 (Mt)":415.7076416,"Other Industry CO2 (Mt)":424.3755493}]
"""

# ══════════════════════════════════════════════════════════════════════════════
# DATA PREP
# ══════════════════════════════════════════════════════════════════════════════
df = pd.DataFrame(json.loads(RAW_JSON))
df_no_world = df[df["Country"] != "World"].copy()
iran = df[df["Country"] == "Iran"].copy()
world = df[df["Country"] == "World"].copy()
india = df[df["Country"] == "India"].copy()

countries_all = sorted(df_no_world["Country"].unique().tolist())

# Emission sources for stacked charts
SOURCES = ["Coal CO2 (Mt)", "Oil CO2 (Mt)", "Gas CO2 (Mt)", "Cement CO2 (Mt)", "Flaring CO2 (Mt)"]
SOURCE_LABELS = ["Coal", "Oil", "Gas", "Cement", "Flaring"]

# ══════════════════════════════════════════════════════════════════════════════
# COLOUR PALETTE  — Iran flag: green #239f40, white #fff, red #da0000, neutral #1a1a1a
# ══════════════════════════════════════════════════════════════════════════════
C_GREEN   = "#239f40"
C_RED     = "#da0000"
C_CREAM   = "#f5f0e8"
C_DARK    = "#1a1a1a"
C_GREY    = "#6b7280"
C_PANEL   = "#111111"
C_CARD    = "#1c1c1c"
C_BORDER  = "#2e2e2e"
C_ACCENT  = "#c8a84b"   # gold accent

SOURCE_COLORS = [C_GREEN, "#e8a020", C_RED, C_ACCENT, "#7c5cbf"]

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Segoe UI, Arial, sans-serif", color="#e8e8e8", size=11),
    margin=dict(l=12, r=12, t=40, b=40),
    legend=dict(
        bgcolor="rgba(30,30,30,0.8)",
        bordercolor=C_BORDER,
        borderwidth=1,
        font=dict(size=10)
    ),
    xaxis=dict(gridcolor="#2a2a2a", showgrid=True, zeroline=False),
    yaxis=dict(gridcolor="#2a2a2a", showgrid=True, zeroline=False),
)

CITATION = html.Div(
    "📊 Data source: Our World in Data (OWID) — Global Carbon Project & World Bank. "
    "Accessed 2025. ourworldindata.org/co2-and-greenhouse-gas-emissions",
    style={
        "fontSize": "10px", "color": C_GREY, "marginTop": "6px",
        "fontStyle": "italic", "textAlign": "right", "paddingRight": "8px"
    }
)

# ══════════════════════════════════════════════════════════════════════════════
# LAYOUT HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def card(children, style=None):
    base = {
        "background": C_CARD,
        "border": f"1px solid {C_BORDER}",
        "borderRadius": "10px",
        "padding": "16px",
        "marginBottom": "16px",
        "boxShadow": "0 4px 16px rgba(0,0,0,0.5)",
    }
    if style:
        base.update(style)
    return html.Div(children, style=base)


def stat_card(title, value, color=C_GREEN):
    return html.Div([
        html.Div(title, style={"fontSize": "11px", "color": C_GREY, "marginBottom": "4px"}),
        html.Div(value, style={"fontSize": "22px", "fontWeight": "bold", "color": color}),
    ], style={
        "background": "#181818",
        "border": f"1px solid {color}44",
        "borderLeft": f"4px solid {color}",
        "borderRadius": "8px",
        "padding": "14px",
        "flex": "1",
        "minWidth": "120px",
    })


# ══════════════════════════════════════════════════════════════════════════════
# APP
# ══════════════════════════════════════════════════════════════════════════════
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True,
    title="Iran CO₂ Dashboard | TISS"
)

# ── SIDEBAR ──────────────────────────────────────────────────────────────────
sidebar = html.Div([
    # Flag stripe top
    html.Div(style={"height": "6px", "background": f"linear-gradient(to right, {C_GREEN}, white, {C_RED})"}),

    html.Div([
        html.Div("🇮🇷", style={"fontSize": "36px", "textAlign": "center", "marginBottom": "4px"}),
        html.H4("Iran CO₂ Dashboard", style={"color": C_GREEN, "textAlign": "center",
                                              "fontWeight": "bold", "marginBottom": "2px", "fontSize": "15px"}),
        html.P("TISS | M2024BSASS019 | Novid Salhot",
               style={"fontSize": "10px", "color": C_GREY, "textAlign": "center", "marginBottom": "20px"}),

        html.Hr(style={"borderColor": C_BORDER}),

        # KPI stats
        html.Div([
            html.Div("📈 Latest Emissions (2024)", style={"fontSize": "11px", "color": C_GREY, "marginBottom": "6px"}),
            html.Div("792.6 Mt CO₂", style={"fontSize": "20px", "fontWeight": "bold", "color": C_RED}),
        ], style={"marginBottom": "12px"}),
        html.Div([
            html.Div("👤 Per Capita (2024)", style={"fontSize": "11px", "color": C_GREY, "marginBottom": "6px"}),
            html.Div("8.66 t CO₂/person", style={"fontSize": "18px", "fontWeight": "bold", "color": C_ACCENT}),
        ], style={"marginBottom": "12px"}),
        html.Div([
            html.Div("🌍 Global Share (2024)", style={"fontSize": "11px", "color": C_GREY, "marginBottom": "6px"}),
            html.Div("2.05%", style={"fontSize": "18px", "fontWeight": "bold", "color": C_GREEN}),
        ], style={"marginBottom": "20px"}),

        html.Hr(style={"borderColor": C_BORDER}),

        # Year range
        html.Label("📅 Year Range", style={"fontSize": "12px", "color": C_GREEN, "fontWeight": "bold"}),
        dcc.RangeSlider(
            id="year-slider",
            min=2006, max=2024, step=1,
            value=[2006, 2024],
            marks={2006: "2006", 2012: "2012", 2018: "2018", 2024: "2024"},
            tooltip={"placement": "bottom", "always_visible": False},
        ),
        html.Div(style={"marginBottom": "16px"}),

        # Compare country dropdown
        html.Label("🌐 Compare Countries", style={"fontSize": "12px", "color": C_GREEN, "fontWeight": "bold"}),
        dcc.Dropdown(
            id="compare-countries",
            options=[{"label": c, "value": c} for c in countries_all if c not in ["Iran", "World"]],
            value=["India", "Saudi Arabia", "Iraq"],
            multi=True,
            placeholder="Select countries...",
            style={"fontSize": "12px"},
        ),
        html.Div(style={"marginBottom": "16px"}),

        # Source filter
        html.Label("⚡ Emission Source (Chart 5)", style={"fontSize": "12px", "color": C_GREEN, "fontWeight": "bold"}),
        dcc.Dropdown(
            id="source-filter",
            options=[{"label": l, "value": s} for l, s in zip(SOURCE_LABELS, SOURCES)],
            value=SOURCES,
            multi=True,
            placeholder="All sources",
            style={"fontSize": "12px"},
        ),
        html.Div(style={"marginBottom": "20px"}),

        # PNG download
        html.Hr(style={"borderColor": C_BORDER}),
        html.Label("📥 Download Charts", style={"fontSize": "12px", "color": C_GREEN, "fontWeight": "bold", "display": "block", "marginBottom": "8px"}),
        *[html.Button(f"⬇ Chart {i+1}", id=f"btn-dl-{i+1}", n_clicks=0,
                      style={"width": "100%", "marginBottom": "6px", "background": "#222",
                             "color": C_GREEN, "border": f"1px solid {C_GREEN}",
                             "borderRadius": "6px", "padding": "6px", "cursor": "pointer",
                             "fontSize": "12px"})
          for i in range(6)],
        *[dcc.Download(id=f"download-{i+1}") for i in range(6)],

    ], style={"padding": "16px"}),

    # Flag stripe bottom
    html.Div(style={"height": "6px", "background": f"linear-gradient(to right, {C_GREEN}, white, {C_RED})"}),

], style={
    "width": "260px",
    "minWidth": "260px",
    "background": C_PANEL,
    "height": "100vh",
    "overflowY": "auto",
    "position": "sticky",
    "top": "0",
    "borderRight": f"2px solid {C_BORDER}",
})

# ── MAIN CONTENT ─────────────────────────────────────────────────────────────
main = html.Div([

    # Header
    html.Div([
        html.H2("Iran — CO₂ Emissions & Climate Analysis", style={"color": C_GREEN, "marginBottom": "0", "fontWeight": "bold"}),
        html.P("BS Analytics & Sustainability Studies 2024–28 | TISS Mumbai | Assignment I",
               style={"color": C_GREY, "fontSize": "12px", "margin": "0"}),
    ], style={"borderBottom": f"2px solid {C_GREEN}", "paddingBottom": "10px", "marginBottom": "16px"}),

    # Chart 1 & 2  —  time series side by side
    html.Div([
        card([
            html.H5("📊 Chart 1 — Total CO₂ Emissions (2006–2024)", style={"color": C_GREEN, "marginBottom": "8px"}),
            dcc.Graph(id="chart-1", config={"displayModeBar": False}),
            CITATION,
        ], {"flex": "1"}),
        card([
            html.H5("📊 Chart 2 — Per Capita CO₂ Emissions (2006–2024)", style={"color": C_GREEN, "marginBottom": "8px"}),
            dcc.Graph(id="chart-2", config={"displayModeBar": False}),
            CITATION,
        ], {"flex": "1"}),
    ], style={"display": "flex", "gap": "14px"}),

    # Chart 3 — horizontal bar
    card([
        html.H5("📊 Chart 3 — Per Capita CO₂ Comparison with Other Countries (latest year)", style={"color": C_GREEN, "marginBottom": "8px"}),
        dcc.Graph(id="chart-3", config={"displayModeBar": False}),
        CITATION,
    ]),

    # Chart 4 & 6  — scatter + pie side by side
    html.Div([
        card([
            html.H5("📊 Chart 4 — GDP per Capita vs CO₂ Emissions (Scatter)", style={"color": C_GREEN, "marginBottom": "8px"}),
            dcc.Graph(id="chart-4", config={"displayModeBar": False}),
            CITATION,
        ], {"flex": "1"}),
        card([
            html.H5("📊 Chart 6 — Global CO₂ Share (Pie Chart)", style={"color": C_GREEN, "marginBottom": "8px"}),
            dcc.Graph(id="chart-6", config={"displayModeBar": False}),
            CITATION,
        ], {"flex": "1"}),
    ], style={"display": "flex", "gap": "14px"}),

    # Chart 5 — stacked bar source breakdown
    card([
        html.H5("📊 Chart 5 — Iran CO₂ Emissions by Source (Stacked Bar)", style={"color": C_GREEN, "marginBottom": "8px"}),
        dcc.Graph(id="chart-5", config={"displayModeBar": False}),
        CITATION,
    ]),

], style={"flex": "1", "padding": "20px", "overflowY": "auto", "height": "100vh"})

# ── ROOT ─────────────────────────────────────────────────────────────────────
app.layout = html.Div([
    html.Div([sidebar, main],
             style={"display": "flex", "flexDirection": "row", "height": "100vh",
                    "overflow": "hidden", "background": C_DARK, "fontFamily": "Segoe UI, Arial, sans-serif"}),
], style={"background": C_DARK})


# ══════════════════════════════════════════════════════════════════════════════
# CALLBACKS
# ══════════════════════════════════════════════════════════════════════════════

def filtered_iran(yr):
    return iran[(iran["Year"] >= yr[0]) & (iran["Year"] <= yr[1])]

def filtered_world(yr):
    return world[(world["Year"] >= yr[0]) & (world["Year"] <= yr[1])]


# ── CHART 1: Total CO₂ trendline ─────────────────────────────────────────────
@app.callback(Output("chart-1", "figure"), Input("year-slider", "value"))
def chart1(yr):
    d = filtered_iran(yr)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=d["Year"], y=d["Total CO2 Emissions (Mt)"],
        mode="lines+markers",
        name="Iran Total CO₂",
        line=dict(color=C_RED, width=3),
        marker=dict(size=6, color=C_RED),
        fill="tozeroy", fillcolor=f"{C_RED}22",
        hovertemplate="Year: %{x}<br>CO₂: %{y:.1f} Mt<extra></extra>",
    ))
    # Trendline
    import numpy as np
    z = np.polyfit(d["Year"], d["Total CO2 Emissions (Mt)"], 1)
    p = np.poly1d(z)
    fig.add_trace(go.Scatter(
        x=d["Year"], y=p(d["Year"]),
        mode="lines", name="Trend",
        line=dict(color=C_ACCENT, width=2, dash="dot"),
        hoverinfo="skip",
    ))
    fig.update_layout(**PLOTLY_LAYOUT,
                      title=dict(text="", font=dict(size=12)),
                      yaxis_title="Total CO₂ (Mt)",
                      xaxis_title="Year",
                      height=320)
    return fig


# ── CHART 2: Per capita trendline ─────────────────────────────────────────────
@app.callback(Output("chart-2", "figure"), Input("year-slider", "value"))
def chart2(yr):
    import numpy as np
    d = filtered_iran(yr)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=d["Year"], y=d["Per Capita CO2 (Mt)"],
        mode="lines+markers",
        name="Iran Per Capita",
        line=dict(color=C_GREEN, width=3),
        marker=dict(size=6, color=C_GREEN),
        fill="tozeroy", fillcolor=f"{C_GREEN}22",
        hovertemplate="Year: %{x}<br>Per Capita: %{y:.2f} t<extra></extra>",
    ))
    w = filtered_world(yr)
    fig.add_trace(go.Scatter(
        x=w["Year"], y=w["Per Capita CO2 (Mt)"],
        mode="lines", name="World Avg",
        line=dict(color=C_GREY, width=2, dash="dash"),
        hovertemplate="Year: %{x}<br>World: %{y:.2f} t<extra></extra>",
    ))
    z = np.polyfit(d["Year"], d["Per Capita CO2 (Mt)"], 1)
    fig.add_trace(go.Scatter(
        x=d["Year"], y=np.poly1d(z)(d["Year"]),
        mode="lines", name="Trend",
        line=dict(color=C_ACCENT, width=2, dash="dot"),
        hoverinfo="skip",
    ))
    fig.update_layout(**PLOTLY_LAYOUT,
                      yaxis_title="Per Capita CO₂ (t/person)",
                      xaxis_title="Year",
                      height=320)
    return fig


# ── CHART 3: Horizontal bar — per capita comparison ───────────────────────────
@app.callback(
    Output("chart-3", "figure"),
    Input("compare-countries", "value"),
    Input("year-slider", "value"),
)
def chart3(compare, yr):
    all_c = (compare or []) + ["Iran", "India"]
    latest_yr = min(yr[1], 2024)
    rows = []
    for c in set(all_c):
        sub = df_no_world[(df_no_world["Country"] == c) & (df_no_world["Year"] == latest_yr)]
        if sub.empty:
            sub = df_no_world[(df_no_world["Country"] == c)].tail(1)
        if not sub.empty:
            rows.append({"Country": c, "PerCap": sub["Per Capita CO2 (Mt)"].values[0]})
    d = pd.DataFrame(rows).sort_values("PerCap")
    colors = [C_RED if c == "Iran" else (C_GREEN if c == "India" else C_GREY) for c in d["Country"]]
    fig = go.Figure(go.Bar(
        x=d["PerCap"], y=d["Country"],
        orientation="h",
        marker_color=colors,
        hovertemplate="%{y}: %{x:.2f} t CO₂/person<extra></extra>",
        text=[f"{v:.2f}" for v in d["PerCap"]], textposition="outside",
    ))
    fig.update_layout(**PLOTLY_LAYOUT,
                      xaxis_title="Per Capita CO₂ (t/person)",
                      yaxis_title="",
                      height=max(320, len(d) * 40 + 80))
    return fig


# ── CHART 4: Scatter GDP vs CO₂ ──────────────────────────────────────────────
@app.callback(
    Output("chart-4", "figure"),
    Input("compare-countries", "value"),
    Input("year-slider", "value"),
)
def chart4(compare, yr):
    all_c = list(set((compare or []) + ["Iran", "India"]))
    sub = df_no_world[
        (df_no_world["Country"].isin(all_c)) &
        (df_no_world["Year"] >= yr[0]) & (df_no_world["Year"] <= yr[1]) &
        (df_no_world["GDP per Capita (Constant US$)"].notna())
    ]
    fig = go.Figure()
    for c in all_c:
        d = sub[sub["Country"] == c]
        if d.empty:
            continue
        clr = C_RED if c == "Iran" else (C_GREEN if c == "India" else C_GREY)
        sz = 10 if c == "Iran" else 7
        fig.add_trace(go.Scatter(
            x=d["GDP per Capita (Constant US$)"], y=d["Total CO2 Emissions (Mt)"],
            mode="markers+lines", name=c,
            marker=dict(color=clr, size=sz, symbol="circle"),
            line=dict(color=clr, width=1.5),
            hovertemplate=f"<b>{c}</b><br>GDP/cap: $%{{x:,.0f}}<br>CO₂: %{{y:.1f}} Mt<extra></extra>",
        ))
    fig.update_layout(**PLOTLY_LAYOUT,
                      xaxis_title="GDP per Capita (Constant US$)",
                      yaxis_title="Total CO₂ Emissions (Mt)",
                      height=360)
    return fig


# ── CHART 5: Stacked bar by source ───────────────────────────────────────────
@app.callback(
    Output("chart-5", "figure"),
    Input("source-filter", "value"),
    Input("year-slider", "value"),
)
def chart5(sources, yr):
    d = filtered_iran(yr)
    srcs = sources if sources else SOURCES
    fig = go.Figure()
    for src, clr, lbl in zip(SOURCES, SOURCE_COLORS, SOURCE_LABELS):
        if src not in srcs:
            continue
        fig.add_trace(go.Bar(
            x=d["Year"], y=d[src],
            name=lbl, marker_color=clr,
            hovertemplate=f"{lbl}: %{{y:.1f}} Mt<extra></extra>",
        ))
    fig.update_layout(**PLOTLY_LAYOUT,
                      barmode="stack",
                      xaxis_title="Year",
                      yaxis_title="CO₂ Emissions (Mt)",
                      height=360)
    return fig


# ── CHART 6: Pie — global share ────────────────────────────────────────────────
@app.callback(
    Output("chart-6", "figure"),
    Input("compare-countries", "value"),
    Input("year-slider", "value"),
)
def chart6(compare, yr):
    latest_yr = min(yr[1], 2024)
    all_c = list(set((compare or []) + ["Iran", "India"]))
    rows = []
    total_world = world[world["Year"] == latest_yr]["Total CO2 Emissions (Mt)"]
    wv = float(total_world.values[0]) if not total_world.empty else 38598.0
    shown_total = 0
    for c in all_c:
        sub = df_no_world[(df_no_world["Country"] == c) & (df_no_world["Year"] == latest_yr)]
        if sub.empty:
            sub = df_no_world[df_no_world["Country"] == c].tail(1)
        if not sub.empty:
            v = float(sub["Total CO2 Emissions (Mt)"].values[0])
            rows.append({"Country": c, "CO2": v})
            shown_total += v
    rows.append({"Country": "Rest of World", "CO2": max(wv - shown_total, 0)})
    d = pd.DataFrame(rows)
    colors = []
    for c in d["Country"]:
        if c == "Iran": colors.append(C_RED)
        elif c == "India": colors.append(C_GREEN)
        elif c == "Rest of World": colors.append("#333")
        else: colors.append(C_GREY)
    fig = go.Figure(go.Pie(
        labels=d["Country"], values=d["CO2"],
        marker=dict(colors=colors, line=dict(color="#111", width=1.5)),
        hole=0.4,
        hovertemplate="%{label}: %{value:.1f} Mt (%{percent})<extra></extra>",
        textinfo="percent+label",
        textfont=dict(size=10),
    ))
    fig.update_layout(**PLOTLY_LAYOUT,
                      showlegend=False,
                      annotations=[dict(text=f"{latest_yr}", x=0.5, y=0.5, font_size=16,
                                        showarrow=False, font_color=C_GREEN)],
                      height=360)
    return fig


# ══════════════════════════════════════════════════════════════════════════════
# PNG DOWNLOADS  (requires kaleido: pip install kaleido)
# ══════════════════════════════════════════════════════════════════════════════
def make_dl_callback(chart_id, dl_id, btn_id):
    @app.callback(
        Output(dl_id, "data"),
        Input(btn_id, "n_clicks"),
        State(chart_id, "figure"),
        prevent_initial_call=True,
    )
    def dl(n, fig_data):
        if not fig_data:
            return dash.no_update
        import plotly.io as pio
        f = go.Figure(fig_data)
        try:
            img_bytes = pio.to_image(f, format="png", width=1200, height=500, scale=2)
            return dcc.send_bytes(img_bytes, filename=f"{chart_id}.png")
        except Exception:
            return dash.no_update

for i in range(1, 7):
    make_dl_callback(f"chart-{i}", f"download-{i}", f"btn-dl-{i}")


# ══════════════════════════════════════════════════════════════════════════════
# RUN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "="*60)
    print("  IRAN CO₂ DASHBOARD — TISS Mumbai")
    print("  Student: Novid Salhot | M2024BSASS019")
    print("  Data: Our World in Data (OWID)")
    print("="*60)
    print("\n  ▶  Open your browser at: http://127.0.0.1:8050")
    print("  ▶  Press Ctrl+C to stop the server\n")
    app.run(debug=False, host='0.0.0.0', port=10000)