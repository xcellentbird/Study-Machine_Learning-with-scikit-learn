import React from 'react'
import {SafeAreaView, Text} from 'react-native'
import * as D from './src/data'

const person = D.createRandomPerson()
export default function App() {
  return (
    // <Text>{person}</Text>와 같은 형태로 사용할 수 없다. <Text> 자식 요소는 문자열이나 xml 요소여야 하기 때문이다.
    // JSON,stringfy(객체, null, 공백 수) 함수를 사용하여 객체를 문자열로 변환하여 사용한다.
    <SafeAreaView>
      <Text>
        {JSON.stringify(person, null, 1)}
      </Text>
    </SafeAreaView>
  )
}
