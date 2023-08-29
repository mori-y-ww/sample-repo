const v1:number=1 //constは更新できない
console.log(v1)

let v2:number=2　//letは更新可能
//v2 ='hello' 型エラー
console.log(v2)

let v3=3
console.log(v3)//型推論

let v5:number|string =5
v5 ='hello'
console.log(v5)

const arr1 =[]
arr1.push(1)
console.log(arr1)

const arr2:number[]=[]
arr2.push(2)
console.log(arr2)