
describe('log in with test_user and log out', {
},() => {
  it('passes', () => {
    cy.visit('/')
    cy.get(':nth-child(1) > .form-signin > :nth-child(3) > #username').type(Cypress.env('USERNAME'))
    cy.get(':nth-child(1) > .form-signin > :nth-child(4) > #password').type(Cypress.env('PASSWORD'))
    cy.get(':nth-child(1) > .form-signin > .btn').click()
    cy.url().should('include', '/home_page')
    cy.get('.home > h1').should('contain', 'test_user')
    cy.get(':nth-child(3) > a').click()
  })
})