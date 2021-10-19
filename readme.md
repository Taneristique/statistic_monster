# ABOUT CROQUIES TEMPLATE

This template will be used in statisticmonster v1.1 but it is specifically designed to help traders.Do not consider this template like a bot what it will give is that will  provide real time 
spot market data in daily chart with macd and momentum values.And it will make you compare the behaviors of two different assets via pearson corelation and also it will help you to make prediction on asset's prices via linear regression and this will also help you to decide which way you will trade let me give an example let us think ethusdt and adausdt pairs.Here adausdt is dependent variable y, ethusdt is independent variable x we will use the last 100 data from selected pairs sources['let assume our source is Close prices and also this code gets always last 100data from the selected databases' sources.'].Here are the results on their regression,standart deviation,standart deviations product and pearson correlation:

standard deviation of ADAUSDT 0.41445938283687733
standard deviation of ETHUSDT 78.64974811771361
the covariance is cov(x,y) =  30.94366775689899
the product of standard deviations is  32.59712606514344
the corellation is r =  0.9492759482863575

and let's also look to the coefficient of determination for this regression:

coefficient of determination r**2 is  0.9011248259949636 which means model regression and corelation of adausdt and ethusdt is a 90 percent meaningful method and it is statistically meaningful.
What it provides you as a trader it means to predict adausdt's price looking ethusdt's price behavior is a logical manner.As you see it helps you to compare assets and according to this result we see that if ethusdt price decreases adausdt price will probably decrease too and vice versa if ethusdt price increases because r =  0.9492759482863575 is a positive strong correlation.

And we have also graphics who give momentum,macd(I did not include histogram),candlestick data and the relation between 50,100,200 simple moving avarages and close price.Via momentum you can look to faster price moves becuse momentum is m(c)=ct-ct-10 where t is time,m momentum and c is closing prices and you can confirm momentum via macd'moving avarages convergent divergent' and its signal which 
[macd=fastema-slowema,
signal=ema(macd),
histogram=macd-signal but I did not include the last formula in the code] and default values for variables:
[
    fastema=ema length 12 bar(in our case 12 days' expotential moving avarage)
    shortema=ema length 26 bar(in our case 26 days' expotential moving avarage)
    signal=ema of macd length 9(9 macd data's expotential moving avarage)
    histogram is same as histogram=macd-signal
]

also for simple moving avarage 50 day sma crossover 200 day sma is a bullish case called golden cross and vice versa called death cross and it is bearish also if 50 day ma crossover 100 day ma it is bullish as well because this means demand increases on asset.And one last thing is you can continously got first selected asset's last price in our regression example it is adausdt which is dependent variable y.
Lastly code provided in both form as python file and interactive python file.

# HOW TO USE IT 

All you have to do putting config.json to your api_key and api_secret after you got api from binance.You can use this template in you project as including following info:
"""// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Taneristique"""