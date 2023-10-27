### １つの変数の特徴を記述する ###

# ブランド選択データbrand.txtをbrandとして読み込む
brand <- read.table("R_train/brand.txt", header=T)
# 度数分布表
table(brand$buy)
# 購買ブランドのヒストグラム（棒グラフ）
barplot(table(brand$buy))

# 売上データsales.txtをsalesとして読み込む
sales <- read.table("R_train/sales.txt", header=T)
# 売上数量の度数分布表
table(sales$units)
# 売上数量のヒストグラム
barplot(table(sales$units))
hist(sales$units)
# 売上数量をunitsに代入
units <- sales$units
# 売上数量の合計値
sum(units)
# 売上数量の観測数
length(units)
# 売上数量の平均値
sum(units) / length(units)
mean(units)

## 演習 ##
# (1)
sum(sales$price)
mean(sales$price)
# (2)
sum(sales$temp)
mean(sales$temp)
# (3)
length(sales$feat)
# (4)
mean(sales$feat)
# (5)
mean(sales$disp)

# 売上数量の中央値
median(units)

## 演習 ##
# (1)
hist(sales$price)
hist(sales$temp)
# (2)
c(mean(sales$price), median(sales$price))
c(mean(sales$temp), median(sales$temp))

# レンジ
max(sales$units)
min(sales$units)
max(sales$units) - min(sales$units)
range(sales$units)

# 平均偏差
sum(sales$units - mean(sales$units))
sum(abs(sales$units - mean(sales$units)))
sum(abs(sales$units - mean(sales$units))) / length(sales$units)
mean(abs(sales$units - mean(sales$units)))

# 分散と標準偏差
m <- mean(sales$units)
m
s2 <- mean((sales$units - m)^2)
s2
s <- sqrt(s2)
s

# 標準化
z <- (sales$units - m) / s
mean(z)
sqrt(mean((z - mean(z))^2))

## 演習 ##
# (1)
max(sales$temp) - min(sales$temp)
range(sales$temp)
# (2)
m <- mean(sales$temp)
s2 <- mean((sales$temp - m)^2)
s2
s <- sqrt(s2)
s
# (3)
z <- (sales$temp - m) / s
mean(z)
mean((z - mean(z))^2)



### ２つの変数間の特徴を記述する ###

# 散布図
sales <- read.table("R_train/sales.txt", header=T)
plot(sales$price, sales$units)
plot(sales$temp, sales$units)
# Assuming 'sales' is your data frame with columns 'price' and 'quantity'



# 価格と売上数量の偏差の積
(sales$price - mean(sales$price)) * (sales$units - mean(sales$units))
# 価格と売上数量の共分散
mean((sales$price - mean(sales$price)) * (sales$units - mean(sales$units)))

## 演習 ##
mean((sales$temp - mean(sales$temp)) * (sales$units - mean(sales$units)))

# 価格と売上数量の共分散を「s.xy」に代入
s.xy <- mean((sales$price - mean(sales$price)) * (sales$units - mean(sales$units)))
# 価格の標準偏差を「s.x」に代入
s.x <- sqrt(mean((sales$price - mean(sales$price))^2))
# 売上数量の標準偏差を「s.y」に代入
s.y <- sqrt(mean((sales$units - mean(sales$units))^2))
# 価格と売上数量の相関係数
s.xy / (s.x * s.y)
cor(sales$price, sales$units)
# 最高気温と売上数量の相関係数
cor(sales$temp, sales$units)

## 練習問題 ##
# 顧客データsales.txtをsalesとして読み込む
customer <- read.table("customer.txt", header=T)
# 散布図
plot(customer$age, customer$freq)
# 相関係数
cor(customer$age, customer$freq)



### 単回帰分析 ###

# 年齢をage, 来店回数をfreqに代入
age <- c(22,21,29,37,27,41,43,36)
freq <- c(13,14,20,27,18,23,21,24)
# 単回帰分析
model.store <- lm(freq ~ age)
summary(model.store)
# 散布図と回帰直線
plot(age, freq)
abline(model.store, col='blue')
# 年齢が40歳の顧客の来店回数の予測値
b0 <- model.store$coefficients[[1]] #切片
b1 <- model.store$coefficients[[2]] #傾き
b0 + b1 * 40

# データフレームの作成
df <- data.frame(age, freq)
model.store <- lm(freq ~ age, data = df)
summary(model.store)

### 重回帰分析 ###

# 顧客データsales.txtをsalesとして読み込む
customer <- read.table("customer.txt", header=T)
# 来店回数freqを年齢ageとDMに回帰
model.multi <- lm(freq ~ age + DM, data=customer)
summary(model.multi)
# age = 30, DM = 1 のときの予測
b <- coef(model.multi)
sum(b * c(1, 30, 1))







