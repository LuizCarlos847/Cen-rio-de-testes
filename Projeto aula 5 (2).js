describe('CT-05: Informações básicas do filme', () => {
  it('Deve exibir informações como título, capa e sinopse', () => {
    cy.visit('/filme/1');
    cy.contains('Título do Filme').should('be.visible');
    cy.get('[data-testid="capa-filme"]').should('be.visible');
    cy.contains('Sinopse curta').should('be.visible');
  });
});