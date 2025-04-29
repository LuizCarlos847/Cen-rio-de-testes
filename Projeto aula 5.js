describe('CT-01: Exibição de 4 a 5 filmes recomendados', () => {
  it('Deve exibir entre 4 e 5 filmes recomendados', () => {
    cy.visit('/recomendacoes');
    cy.get('[data-testid="filme-recomendado"]').should('have.length.within', 4, 5);
  });
});