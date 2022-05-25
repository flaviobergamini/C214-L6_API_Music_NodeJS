const Constants = require('../src/utils/Constants');
const Validation = require('../src/utils/validation');

test('Caso válido', () => {
    const result = Validation.create({
        name: "Moonlight Sonata",
        band: "Ludwig Van Beethoven"
    });
    expect(result).toEqual(undefined);
});

test('Caso inválido - Retirando nome', () => {
    const result = Validation.create({
        band: "Ludwig Van Beethoven"
    });
    expect(result.name).toEqual(Constants.ErrorValidation.name);
});
