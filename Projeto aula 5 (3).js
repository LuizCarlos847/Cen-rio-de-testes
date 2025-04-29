describe('CT-04: Atualização da lista de filmes conforme o usuário digita', () => {
  it('Deve atualizar a lista dinamicamente', () => {
    cy.visit('/busca');
    cy.get('[data-testid="campo-busca"]').type('Titanic');
    cy.contains('Titanic').should('be.visible');
  });
});