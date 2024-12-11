class IdolModel {
    name;
    year;

    constructor(name,year){
        this.name = name
        this.year = year
    }
    /*
    1) 데이터를 가공해서 새로운 데이터를 반환할 때
    2) private한 값을 반환할때
     */
    get nameAndYear(){
        return `${this.name}-${this.year}`
    }
    /*
    setter는 항상 parameter를 한개 지정해야함 (변경해야 할 프로퍼터) 
    */    
    set setName(name){
        this.name = name
    }

}

const yuJin = new IdolModel('안유진',2003)
console.log(yuJin)
console.log(yuJin.nameAndYear)

yuJin.setName = '장원영'
console.log(yuJin)

console.log('-----------------------------------------------------')
class IdolModel2 {
    #name
    year
    constructor(name,year){
        this.#name = name
        this.year = year
    }
    // name을 access 하기 위해 getter 와 setter를 사용
    get name(){
        return this.#name
    }

    set name(name){
        this.#name = name
    }
}
const yuJin2 = new IdolModel2('안유진',2003)
console.log(yuJin2) // private 한 name 이기때문에 year 만 출력된다

console.log(yuJin2.name)

yuJin2.name = '연암공대'
console.log(yuJin2.name)

class IdolModel3 {
    name
    year

    constructor(name,year){
        this.name =name
        this.year = year
    }

    //static 으로 Object 일때
    static fromObjcet(objcet){
        return new IdolModel(
            objcet.name,
            objcet.year,
        )
    }
    //static 으로 List 일때
    
    static fromList(list){
        return new IdolModel3(
            list[0],
            list[1]
        )
    }
}

const yuJin3 = IdolModel3.fromObjcet({
    name : '안유진',
    year : 2003,
})
console.log(yuJin3)