// 자바스크립트 엔진은 프로퍼터를 생성 할 때 프로퍼터의 상태를 나타내는
// property attribute를 기본값으로자동 정의 한다
// (status : value, writable,enumberable,configuarble)

//객체에 키, value 이외에 더 섬세하게 객체를  Control 할 수 있다

//property Attribute에는 2가지 정류가 있다
    // 데이터 프로퍼터 : 키와 값으로 형성된 실질적 값을 가지고 있는 프로퍼터
    // 엑세서 프로퍼터 : 자체적으로 값을 가지고 있지 않지만 다른 값을 가져 오거나 설정 할 때 
    // 호출되는 함수로 구성된 프로퍼터 (예 : getter와 setter)


//데이터 프로퍼티

const yuJin = {
    name : '안유진',
    year : 2003,
}
console.log(Object.getOwnPropertyDescriptor(yuJin,'name'))
console.log(Object.getOwnPropertyDescriptor(yuJin,'year'))
console.log('value : 실제 프러퍼터의 값')
console.log('writable : 값을 수정 할 수 있는지의 여부이다. Flase로 설정하면 프로퍼터 값을 수정 할 수 없다')
console.log('enumerable(열거) : 키 값을 열거가 가능 한지 여부이다. for...in루프 등을사용할 수 있으면 true를 반환')
console.log('configurable(재정의) : 프로퍼터 어트리뷰트의 재정의가 가응한지 여부를 판단한다')
console.log('false 일 경우 프로터티 삭제나 어트리뷰트 변경이 금지 된다')
console.log('단 , writable 이 true 인 경우 값 변경은 가능하고 writable을 true-> false로 변경하는건 가능하다')
console.log('그러나 writalbe을 false -> true로 변경은 안된다.(유일한 예외')

console.log(Object.getOwnPropertyDescriptor(yuJin,'name'));
console.log(Object.getOwnPropertyDescriptors(yuJin));
// 모든 프로퍼터 attribute가 출력된다
console.log('----------------------------------')

//엑서서 프로퍼터 (getter와 setter 사용)
    //-  자체적으로 값을 가지고 있지 않고, 다른 데이터 프로퍼터(date property)의 값을 읽거나 저장할 때,
    //   사용하는 접근자 함수(accessor function)으로 구성된 프로퍼터이다
    //- get,set,enumbearable, configurable 사용

const yuJin2 = {
    name : '안유진',
    year : 2003,

    get age() {
        return new Date().getFullYear()-this.year
    },

    set age(age){
        this.year = new Date().getFullYear() - age;
    }

}
console.log('나이를 get 한 경우')
console.log(yuJin2)
console.log(yuJin2.age)// 나이를 get 한 경우

console.log('나이를 set 한 경우')
yuJin2.age = 32; //나이를 set 한경우
console.log(yuJin2.age);
console.log(yuJin2.year);

console.log('=============================')

//엑세서 프로퍼티 (getter와 setter 사용)를 통해 프로퍼티 attribute를 가져올 경우

console.log(Object.getOwnPropertyDescriptor(yuJin2,'age'))

//yuJin2 라는 객체에 키 와 어트리뷰트를 추가 하고 싶을 경우

Object.defineProperty(yuJin2,'height',{
    value : 172,
    writable : true,
    enumerable : true,
    configurable : true,
});
console.log(yuJin2)
console.log(Object.getOwnPropertyDescriptor(yuJin2,'height'));

//만약에 프로퍼티 어티리뷰트를 코드상에서 제외하면, 모든 어트리뷰트 값들이 false로 되어짐

//writable 값을 변경 할 경우

//객체 yuJin2에 height를 180으로 추가하면 변경됨
//writable 값이 false 경우 변경이 안됨

yuJin2.height = 180;
console.log(yuJin2)

//enumerable 값을 false로 변경할 경우

console.log(Object.keys(yuJin2));
for(let key in yuJin2){
    console.log(key)
}

Object.defineProperty(yuJin2,'name',{
    enumerable : false,
});

console.log(Object.getOwnPropertyDescriptor(yuJin2,'name'));

console.log('==========================')
console.log(Object.keys(yuJin2));
//false로 지정해서 name이 안나온다
for(let key in yuJin2){
    console.log(key)
}

console.log(yuJin2)
console.log(yuJin2.name) // 하지만 name 실제 값은 있어서 name을 불러오면 안유진이 출력

console.log('=========================================')

//configurable 값을 false로 변경 할 경우
// enumberable를 faslse로 할 경우 에러 메시지가 출력 된다

Object.defineProperty(yuJin2,'height',{
    writable : true ,
    configurable : false,
})
console.log(Object.getOwnPropertyDescriptor(yuJin2,'height'));
Object.defineProperty(yuJin2,'height',{
    value : 172,
})
console.log(Object.getOwnPropertyDescriptor(yuJin2,'height'))

//writable을 true - > false 로 변경하는건 가능하지만 그 반대는 안된다