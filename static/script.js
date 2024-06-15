// Botao (Finalizar) da pag Home

document.getElementById('but_fin').addEventListener('click', function() {
    // Seleciona a tabela original
    let table = document.getElementById('table_list');
    
    // Clona a tabela
    let cloneTable = table.cloneNode(true);

    // Remove a coluna de ações da tabela clonada
    let headerRow = cloneTable.rows[0];
    headerRow.deleteCell(-1); // Remove o último cabeçalho (Ações)

    for (let i = 1; i < cloneTable.rows.length; i++) {
        cloneTable.rows[i].deleteCell(-1); // Remove a última célula de cada linha
    }
    
    // Obtem o conteúdo HTML da tabela clonada
    let tableContent = cloneTable.outerHTML;

    // Cria uma nova aba para impressão ao lado da aba atual
    let printWindow = window.open('', '_blank', 'height=600,width=800');
    
    // Adiciona o conteúdo HTML para impressão na nova aba
    printWindow.document.write('<html><head><title>Itens</title>');
    printWindow.document.write('<style>');
    printWindow.document.write('table {width: 100%; border-collapse: collapse;}');
    printWindow.document.write('th, td {border: 1px solid black; padding: 8px; text-align: center; color: #424242;}');
    printWindow.document.write('th {background-color: #f2f2f2;}');
    printWindow.document.write('h1 {text-align: center; color: gray;}');
    printWindow.document.write('</style>');
    printWindow.document.write('</head><body>');
    printWindow.document.write('<h1>Lista para Reposição</h1>');
    printWindow.document.write(tableContent);
    printWindow.document.write('</body></html>');
    
    // Fecha o documento para concluir a escrita
    printWindow.document.close();
    
    // Inicia a impressão
    printWindow.print();
});