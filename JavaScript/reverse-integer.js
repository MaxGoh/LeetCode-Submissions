/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  var isAbsolute = true
  var absNum = Math.abs(x)
  var reverseNum = 0
  var multiplier = 1

  if (x < 0) {
    isAbsolute = false
  }

  while (absNum > 0) {
    var remainder = absNum % 10
    reverseNum = reverseNum * 10 + remainder

    absNum = Math.floor(absNum / 10)
    multiplier = multiplier * 10
  }

  if (!isAbsolute) {
    reverseNum = -Math.abs(reverseNum)
  }

  if (reverseNum < -Math.pow(2, 31) || reverseNum > Math.pow(2, 31) - 1) {
    return 0
  }

  return reverseNum
}
