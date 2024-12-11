// 상속의 정의
//객체들간의 관계를 구축하는 방법이다
//수퍼 클래스, 또는 부모 클래스 등의 기존의 클래스로부터 속성과 동작을 상속 받을수 있다


//부모 클래스
class IdolModel{
    name;
    year;

    constructor(name,year){
        this.name = name;
        this.year = year;
    }
    sayHello(){
        return `안녕하세요 ${this.name}입니다`
    }
}

//상속 받은 자식 클래스
    //상속을 할 때에는 extends 라는 키워드를 사용한다
    //상속을 할 때는 proprtey 및 construtor 도 부모의 클래스를 상속 받는다
    
    
class FemaleIdolModel extends IdolModel{
    part

    constructor(name,year,part) {
        super(name,year)

    //super라는 keyword는  부모클래스를 의미하고 자식의constrytor를 override 한다

        this.part = part
    }
    sayHello(){
        return `${super.sayHello()} ${this.part}를 맏고 있습니다.`
    }
    
    dance(name){
        return `${this.name}이 춤을 춥니다`
    }
}

class MaleIdolModel extends IdolModel{
    dance(){
        return '남자 아이돌이 춤을 춥니다'
    }
}

const yuJin = new FemaleIdolModel('안유진',2001,'보컬')
console.log(yuJin)
console.log(yuJin.dance())

const wonYoung = new IdolModel('장원영',2002);
console.log(wonYoung)

console.log('==================================')


console.log(wonYoung.sayHello())
console.log(yuJin.sayHello())