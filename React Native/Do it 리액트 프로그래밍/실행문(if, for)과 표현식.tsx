import React from 'react'
import {SafeAreaView, Text} from 'react-native'

export default function App() {
  //const isLoading = false

  // -------- for 문 사용법 --------
  const children = new Array(10).fill(null).map((notUsed, index) => <Text>Hello JSX~</Text>)
  return <SafeAreaView>{children}</SafeAreaView>


  // -------- if 문 사용법 ---------
  /*
  const children = isLoading ? (
    <Text>Loading...</Text>
  ) : (
    <Text>Hello JSX~</Text>
  )
  return <SafeAreaView>{children}</SafeAreaView>
  */
  
  /*
  return (
    <SafeAreaView>
      {isLoading && <Text>Loading...</Text>}
      {!isLoading && <Text>Hello JSX~</Text>}
    </SafeAreaView>
  )
  */
  
  /*
  if (isLoading) {
    return (
      <SafeAreaView>
        <Text>
          Loading...
        </Text>
      </SafeAreaView>
    )
  }

  return (
    <SafeAreaView>
      <Text>
        Hello JSX~
      </Text>
    </SafeAreaView>
  )
  */
  
  // ------------------
  /*
  return (
    <SafeAreaView>
      <Text>
        Hello JSX
      </Text>
    </SafeAreaView>
  )
  */
}
