class IdolModel {
    name;
    year;
// name,year를 생략해도 countructor를 사용하기에 결과는 똑같다
    constructor(name,year){
        this.name = name;
        this.year = year;
    }
//class 안에 함수(메서드)를 생성하는 부분
    sayName(){
        return `안녕하세요 ${this.name}입니다.`
    }
//원래는 메소드 정의 할 때 function 이라는 키워드를 사용하지만 class안에서는 함수의 이름만 사용함
}

const yuJin = new IdolModel('안유진',2003);
console.log(yuJin)
const gaeul = new IdolModel('가을',2002);
console.log(gaeul)
const ray = new IdolModel('레이',2004);
console.log(ray)
const wonYoung = new IdolModel('장원영',2004);
console.log(wonYoung)
const liz = new IdolModel('리즈',2004);
console.log(liz)
const eseo = new IdolModel('이서',2007);
console.log(eseo)

console.log('------------------------------------')
//Class의 객체로 생성된 yuJin으로 name/year 값을 알고 싶을 때
console.log('Class의 객체로 생성된 yuJin으로 name/year 값을 알고 싶을 때')
console.log(yuJin.name)
console.log(yuJin.year)

console.log(yuJin.sayName())
console.log(wonYoung.sayName())

//class의 type을 체크해보면 function이고, 생성된 instance(객체)인 yuJin은 Objcet 타입이다

console.log('-----------------------------------')
console.log('class의 type을 체크해보면 function이고, 생성된 instance(객체)인 yuJin은 Objcet 타입이다')
console.log(typeof IdolModel)
console.log(typeof yuJin)