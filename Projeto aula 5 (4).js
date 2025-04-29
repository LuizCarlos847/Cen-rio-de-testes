describe('CT-03: Inclusão de capa e título nas recomendações', () => {
  it('Deve exibir capa e título para cada filme recomendado', () => {
    cy.visit('/recomendacoes');
    cy.get('[data-testid="capa-filme-recomendado"]').should('be.visible');
    cy.get('[data-testid="titulo-filme-recomendado"]').should('be.visible');
  });
});