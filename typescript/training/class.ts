class Fraction {
    //private _numerator:number
    //private _denominator: number //フィールドをprivateにすると変更できなくなるこれが基本

    constructor(private _numerator:number,private _denominator:number){
        //this._numerator = numerator
        //this._denominator = denominator
    }

    toString(): string{
        return `${this._numerator}/${this._denominator}`
    }

    add(other: Fraction):Fraction{
        const resultNumerator =
            this._numerator*other._denominator+
            this._denominator*other._numerator
        const resultDenominator = this._denominator*other._denominator

        return new Fraction(resultNumerator,resultDenominator)
    
    }

    get numerator(){
        return this._numerator
    }

    get denominator(){
        return this._denominator  //getter フィールドの内容の変更を防ぎ呼び出すためのもの
    }
}

const f1 =new Fraction(1,2)
console.log(f1.numerator)
console.log(f1.denominator)

// f1.numerator =3
console.log(f1.numerator)

const f2 =new Fraction(1,3)
console.log(f2.toString())

const result=f1.add(f2)
console.log(result.toString())