describe('CT-04: Navegação pelas recomendações do dia', () => {
  it('Deve permitir navegar pelas recomendações', () => {
    cy.visit('/recomendacoes');
    cy.get('[data-testid="botao-proximo"]').click();
    cy.get('[data-testid="filme-recomendado"]').should('have.length.at.least', 1);
  });
});