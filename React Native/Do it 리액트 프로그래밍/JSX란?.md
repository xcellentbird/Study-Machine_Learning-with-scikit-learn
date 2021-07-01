JSX(JavaScript XML): XML에 JS을 결합할 용도로 만들어진 구문입니다. 이는 표준 ESNext JS나 Type Script 문법의 확장 방식으로 사용됩니다. 이렇게 확장이 가능한 이유는 JS 컴파일러 'babel'(Type Script에서는 'tsc')이 플러그인 구조(:설치 후 바로 적용시킬 수 있는 구조)로 작동하기 때문입니다.  

바벨은 ESNext JS 코드를 만나고 여러 플러그인을 파이프라인 형태로 차례로 동작 가능한 구문만 컴파일하여 ES5 JS 코드로 변환합니다. 여기에서 '@babel/plugiin-transform-react-jsx' 플러그인을 통하여 JSX 구문의 ESNext JS를 React.createElement를 호출하는 평범한 JS로 변환합니다.

또한 JSX구문이 있는 TS(Type Script)는 '.tsx'형식이고, 'import react from 'react'같은 import가 필요합니다.   
React.createElement는 컴포넌트(import {컴포넌트} from 'react_native' 과 같이 불러온 것)를 가상 DOM 객체로 만드는 역할을 합니다.   

가상 DOM 객체는 다음과 같이 생성할 수 있습니다.
```
가상_DOM_객체 = createElement(컴포넌트 이름 또는 문자열, 속성 객체, 자식 컴포넌트)
```
그리고...
```html
 <Text>Hello!</Text>
```
는 아래와 같이 사용할 수 있습니다.
```
const textElement = React.createElement(Text, null, 'Hello!')
```

