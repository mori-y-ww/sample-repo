
//
function add1(v1:number,v2:number):number{
    return v1+v2
}

const result5 = add1(1,2)
console.log(`result5 = ${result5}`)


const add2=function(v1:number,v2:number):number{
    return v1+v2
}

console.log(add2)

const result6=add2(1,2)
console.log(`result6 = ${result6}`)

const add3 = (v1:number,v2:number)=>{
    return v1 + v2
}

const result7=add3(1,2)
console.log(`result7 = ${result7}`)

