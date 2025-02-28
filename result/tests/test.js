const { expect } = require('chai');
const { getPercentages } = require('../views/utils'); // Importando la función con require

describe('getPercentages', function() {
  it('debería devolver 50% - 50% cuando a y b son 0', function() {
    const result = getPercentages(0, 0);
    expect(result).to.deep.equal({ a: 50, b: 50 });
  });

  it('debería calcular correctamente el porcentaje cuando a = 30 y b = 70', function() {
    const result = getPercentages(30, 70);
    expect(result).to.deep.equal({ a: 30, b: 70 });
  });

  it('debería calcular correctamente el porcentaje cuando a = 100 y b = 0', function() {
    const result = getPercentages(100, 0);
    expect(result).to.deep.equal({ a: 100, b: 0 });
  });

  it('debería calcular correctamente el porcentaje cuando a = 0 y b = 100', function() {
    const result = getPercentages(0, 100);
    expect(result).to.deep.equal({ a: 0, b: 100 });
  });

  it('debería calcular correctamente el porcentaje cuando a = 25 y b = 75', function() {
    const result = getPercentages(25, 75);
    expect(result).to.deep.equal({ a: 25, b: 75 });
  });
});
