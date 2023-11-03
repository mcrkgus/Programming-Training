import Foundation

let num1 = readLine()!.components(separatedBy: " ")
let num2 = readLine()!.components(separatedBy: " ")
for i in num2 {
    if Int(i)! < Int(num1[1])! {
        print(i, terminator: " ")
    }
}
