const STONE=0
const PAPER=1
const SCISSORS=2

interface handGenerator{
    generate():number
}

class RandomHandGenerator implements handGenerator{
    generate(): number{
        return Math.floor(Math.random()*3)
    }

    generateArray():number[]{
        return []
    }
}

class Janken{
    play(handGenerator:handGenerator){

        const computerHand = handGenerator.generate()

        console.log(`computerHand = ${computerHand}`)

        //勝敗判定が続く...
    }
}

const janken=new Janken()

const generator =new RandomHandGenerator()
janken.play(generator)

class StoneHandGenerator implements handGenerator{
    generate(): number{
        return STONE
    }   
}


const generator2 = new StoneHandGenerator()
janken.play(generator2)
