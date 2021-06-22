class Solution {
    fun solution(seoul: Array<String>): String {
        for (i in 0..seoul.size){
            if (seoul[i] == "Kim"){
                return Kim_Here(i)
            }
        }
        return ""
    }
    
    fun Kim_Here(loc:Int) : String {
        return "김서방은 ${loc}에 있다"
    }
}
