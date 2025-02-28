function getPercentages(a, b) {
  var result = {};

  if (a + b > 0) {
    result.a = Math.round(a / (a + b) * 100);
    result.b = 100 - result.a;
  } else {
    result.a = result.b = 50;
  }

  return result;
}

// Exportar la función para Jest
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { getPercentages };
}

