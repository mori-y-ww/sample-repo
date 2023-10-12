### Rの基本操作 ###

# 作業ディレクトリの確認
getwd()


# 売上データsales.txtをsalesとして読み込む
sales <- read.table("R_train/sales.txt", header=T)

# salesの最初の6行を表示
head(sales)

# salesの概要
summary(sales)

