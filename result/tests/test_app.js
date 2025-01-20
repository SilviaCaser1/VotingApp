// este es un archivo de prueba 
const assert = require('chai').assert;
const app = require('../server'); // Ajusta según la ruta real de tu archivo server

describe('Service Tests', () => {
  it('should return a valid response', (done) => {
    // Suponiendo que app expone algún servicio que podemos probar
    app.someServiceFunction((response) => {
      assert.equal(response.status, 200);
      done();
    });
  });
});
