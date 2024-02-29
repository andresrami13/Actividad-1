function ConsumirApiUsuarios() {
    var endPoint = "http://127.0.0.1:5000/consume_json";

    fetch(endPoint)

        .then(response => response.json())

        .then(data => {
            console.log(data);
            const Categoria = []
            const Valor = []

            for (const element in data) {
                Categoria.push("Password > 8 caracteres")
                Valor.push(data[element]['conteoPasswordChar'])
                Categoria.push("Dominios diferentes")
                Valor.push(data[element]['dominiosDiferentes'])
            }
            
            console.log(Valor);
            var datosGrafico = [
                {
                    x: Categoria,
                    y: Valor,
                    type: 'bar'
                }
                ];
                  
           
            
            Plotly.newPlot('myDiv', datosGrafico);    
        })

        .catch(error => {
            console.log(error);
        })
    

}