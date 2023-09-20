function mul1(v1:number,v2:number):number{
    return v1 *v2
}//引数と戻り値の型指定

const result = mul1(1,2)
console.log(result)

function mul2(v1:number ,v2: number){
    return v1*v2
}

const result1 =mul2(10,20)
console.log(result1)//データ型any

//const result2 =mul2('hello','world')
//console.log(result2)  エラー

function mul3(v1:any,v2:any):any{
    return v1 * v2
} 

const result2 = mul3(100,200)
console.log(result2)

const result3=mul3('hello','world')
console.log(result3)