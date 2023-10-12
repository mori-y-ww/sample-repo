# 横断面データ
customer <- read.table("R_train/customer.txt", header = T)
head(customer)

# 時系列データ
sales <- read.table("R_train/sales.txt", header = T)
head(sales)

# パネルデータ
life <- read.csv("life_xt.csv")
head(life)

## 2期間パネルデータ

#データの読み込み
life <- read.csv("life_xt.csv", header = TRUE)
head(life)

### 応用例：2期間パネルによる政策効果 ###

#t=2期目（2009年）のデータを使って最小2乗法で回帰
reg1 <- lm(life ~ shock + income, data = subset(life, t==2))
summary(reg1)

#t=1のデータを抽出
life_s1 <- subset(life, t == 1)
head(life_s1)

#t=2のデータを抽出
life_s2 <- subset(life, t == 2)
head(life_s2)

#t=2とt=1の差分を取る
life_ds <- life_s2 - life_s1
head(life_ds)

#差分を取ったデータを使って最小2乗法で回帰
reg2 <- lm(life ~ shock_y2 + income , data = life_ds)
summary(reg2)

#パネル・データ分析用パッケージインストール
# install.packages("plm") # 一度インストールすれば再度行う必要なし
#うまくいかない場合は以下のサイトの4.2を参照
# https://syunsuke.github.io/r_install_guide_for_beginners/05_installation_of_packages.html

#パネル・データ分析用パッケージ読み込み
library(plm) 

#plmパッケージを用いて，1階差分法（fd）による回帰
preg1 <- plm(life ~ shock_y2 + income, data = life, effect = "individual", 
             model = "fd", index = c("id", "t"))
summary(preg1)

#固定効果モデル（within）を用いた回帰
preg1 <- plm(life ~ shock + y2 + shock_y2 + income, data = life, effect = "individual", 
             model = "within", index = c("id", "t"))
summary(preg1)
