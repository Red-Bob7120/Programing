//객체 생성 방법

// 1)Object를 생성해서 객체 생성

const yuJin = {
    name : '안유진',
    year : 2003,
};
console.log(yuJin)

// 2) class를 인스턴스화 해서 생성

class IdolModel {
    name;
    year;

    constructor(name,year){
        this.name = name;
        this.year = year;
    }
}

console.log(new IdolModel('안유진',2003));

// 3) function을 사용해서 객체 생성(생성자 함수)
//      class의 constructor 처럼 "this" 키워드를 사용함
//      Function으로 객체를 생성 할 때는 "this"키워드를 사용하여 프로퍼터를 할당했을경우에 "new "키워드를 사용하여 객체 생성한다
function IdolFunction(name,year){
    this.name = name;
    this.year = year;
}
const gaEul = new IdolFunction('가을',2002);
console.log(gaEul);