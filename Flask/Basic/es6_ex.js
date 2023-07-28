// 변수 선언
//var button = document.getElementById('button1')
const button = document.getElementById('button1')   // 변경 불가능한 변수 const로 선언

let name = "toktokhan"      // 변경 가능한 변수는 let으로 선언
name = "dev"
console.log(name);

// 화살표 함수
// function myFunc(name) {
//   return "TokTokHan" + name;
// }

// console.log(myFunc(".dev"));
// 함수 myFunc는 화살표(=>) 우측의 표현식(expression)을 평가하고, 평가 결과를 반환
const myFunc = (name) => {
    return "TokTokHan ${name}";
}
console.log(myFunc(".dev"));

