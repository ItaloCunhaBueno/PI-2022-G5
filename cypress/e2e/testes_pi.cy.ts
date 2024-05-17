describe('Cenários de testes', () => {
  const urlHome = 'https://pi-2022-g5.vercel.app/';
  const urlProfissional = 'https://pi-2022-g5.vercel.app/#profissional';
  const urlFuncionamento = 'https://pi-2022-g5.vercel.app/#funcionamento';
  const urlBeneficios = 'https://pi-2022-g5.vercel.app/#beneficios';
  const profissionalButton = '#id-profissionalButton';
  const funcionamentoButton = '#id-funcionamentoButton';
  const beneficiosButton = '#id-beneficiosButton';
  const contatoButton = '#id-contatoButton';
  const nomeInput = '#id-nomeInput';
  const telefoneInput = '#id-telefoneInput';
  const emailInput = '#id-emailInput';
  const msgInput = '#id-msgInput';
  const enviarMsgButton = '#id-enviarMsgButton'
  const contatoCard = '#contato'
  const msgAVisoErro = '#id-msgAvisoErro'

  beforeEach(() => {
    cy.visit(urlHome);
  });

  it('Deve acessar a Home e validar se a página está abrindo corretamente', () => {
    cy.url().should('eq', urlHome);
  });

  it('Deve acessar a Home, clicar em O profissional e validar se a página tem o comportamento correto', () => {
    cy.get(profissionalButton).click();
    cy.url().should('eq', urlProfissional);
  });

  it('Deve acessar a Home, clicar em Como Funciona e validar se a página tem o comportamento correto', () => {
    cy.get(funcionamentoButton).click();
    cy.url().should('eq', urlFuncionamento);
  });

  it('Deve acessar a Home, clicar em Benefícios e validar se a página tem o comportamento correto', () => {
    cy.get(beneficiosButton).click();
    cy.url().should('eq', urlBeneficios);
  });

  it('Deve acessar a Home, clicar em Entre em Contato e validar se a página tem o comportamento correto', () => {
    cy.get(contatoButton).click();
    cy.get(contatoCard).should('be.visible');
  });

  it('Deve preencher o formulário de contato e validar se recebemos a resposta correta da API junto com a mensagem de sucesso', () => {
    
    cy.intercept('POST', '/api/novamensagem', (req) => {
      req.continue((res) => {
        expect(res.statusCode).to.equal(200);
        expect(res.body).to.have.property('status', 200);
        expect(res.body).to.have.property('mensagem', 'Mensagem enviada com sucesso!');
      });
    }).as('postContato');
  
    cy.get(nomeInput).type('Teste Teste Teste');
    cy.get(telefoneInput).type('1234567890');
    cy.get(emailInput).type('teste@teste.com');
    cy.get(msgInput).type('Teste Teste Teste');
    
    cy.get(enviarMsgButton).click();
    
    cy.wait('@postContato');
  });






})