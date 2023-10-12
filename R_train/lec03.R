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
customer <- read.table("R_train/customer.txt", header=T)
# 来店回数freqを年齢ageとDMに回帰
model.multi <- lm(freq ~ age + DM, data=customer)
summary(model.multi)
# age = 30, DM = 1 のときの予測
b <- coef(model.multi)
sum(b * c(1, 30, 1))


### ロジスティック回帰 ###

# 購買回数をnum, 応募の有無をapplyに代入
num <- c(16,19,8,9,11,6,13,22,15,11,18,3)
apply <- c(1,1,0,0,1,0,0,1,1,0,1,0)

# ロジスティック回帰分析
model.apply <- glm(apply ~ num, family="binomial")
summary(model.apply)

# パラメータの推定値
b0 <- model.apply$coefficients[[1]]
b1 <- model.apply$coefficients[[2]]
b0
b1

# 購買回数が10回の顧客が応募する確率
exp(b0+b1*10) / (1 + exp(b0+b1*10))

# パラメータの推定値を用いた応募確率の予測値
plot(num, apply, xlim=c(0,25))
par(new=T)
curve(exp(b0+b1*x) / (1 + exp(b0+b1*x)), 0, 25, xlab=NA, ylab=NA, axes=F)



