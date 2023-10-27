## 応用例：変量効果モデルの推定

#データの読み込み
life <- read.table("R_train/life_xt.csv", header = TRUE, sep = ",")

#パネル・データ分析用パッケージインストール
#install.packages("plm") # 1度インストールしたら2回目以降は必要ない
#パネル・データ分析用パッケージ読み込む
library(plm)

#変量効果モデル（random）を用いた回帰
preg1 <- plm(life ~ shock + y2 + shock_y2 + income, data = life, effect ="individual", 
             model = "random", index = c("id", "t"))
summary(preg1)


## 固定効果か変量効果か

#固定効果モデル（within）を用いた回帰
fe <- plm(life ~ shock + y2 + shock_y2 + income, data = life, effect ="individual", 
          model = "within", index = c("id", "t"))

#変量効果モデル（random）を用いた回帰
re <- plm(life ~ shock + y2 + shock_y2 + income, data = life, effect ="individual", 
          model = "random", index = c("id", "t"))

#ハウスマン検定
phtest(fe, re)



## 静学的パネルデータ分析

# パッケージからデータを読み込む
library(plm)
data("Grunfeld", package = "plm")
head(Grunfeld)

# 並べ替え
df <- Grunfeld[order(Grunfeld$value),] #valueの小さい順に並べ替え
head(df, n = 5) #最初の5行を表示
df <- df[order(df$firm, df$year),] #企業、年の順に並べ替え
head(df, n = 5) #最初の5行を表示

# pooled OLS
pool <- plm(inv ~ value, data = Grunfeld, model = "pooling")
summary(pool)

# LSDV
fe <- plm(inv ~ value, data = Grunfeld, model = "within")
summary(fe)

# 個別効果の推定値
mu <- fixef(fe)
summary(mu)
summary(mu)[summary(mu)[, 4] < 0.05, ] #有意な係数を抽出
mean(mu) # 個別効果の平均

# 個別効果のその平均からの乖離
mu2 <- fixef(fe, type = "dmean")
summary(mu2)
summary(mu2)[summary(mu2)[, 4] < 0.05, ] #有意な係数を抽出


# 個別効果があるかどうかのF検定
ftest <- pFtest(fe, pool)
ftest

# GLS
re <- plm(inv ~ value, data = Grunfeld, model = "random")
summary(re)

# ハウスマン検定
phtest(fe, re)

