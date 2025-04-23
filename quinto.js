//1. convertir la siguiente funcion a una funcion flecha  ennuna solo linea sin llaves(1p)
function esPar(numero) {
    if (numero % 2 === 0) {
      return true;
    } else {
      return false;
    }
  }
console.log(esPar(3));


////////////////////////////////////////////
const esPar = (numero) => (numero % 2 ===0);console.log(esPar(3))
//////////////////////////////////////////////

//2. Crear unha funcion callback que acepte un arreglo de numeros y una funcion callback donde duplique cada elemento del arreglo 
function doble(a, callback) {
    for (let b in a) {
      a[b] = callback(a[b]);
    }
    return a;
  }
  const duplicar = (a) => a * 2;
  const numeros = [1, 2, 3, 4, 5];
  const resultado = doble(numeros, duplicar);
  console.log(resultado);
//3. Usando los metodos setTimeOut y setInterval crear un contador que disminuya del 5 al 0 


let contador = 5;

const intervalId = setInterval(() => {
  console.log("disminuyendo:", contador);
  contador--;

  if (contador < 0) {
    clearInterval(intervalId);
   
  }
}, 1000);

// Dado el siguiente arreglo:
const libros = [
    { id: 1, titulo: "Cien años de soledad", autor: "Gabriel García Márquez", año: 1967 },
    { id: 2, titulo: "La casa de lo Espiritus", autor: "Isabel Allende", año: 1982 },
    { id: 3, titulo: "Rayuela", autor: "Julio Cortázar", año: 1963 },
    { id: 4, titulo: "El código Da Vinci", autor: "Dan Brown", año: 2005 }
  ];

//4. Cambiar el nombre del libro con id 3 a Final del juego usando for..of

const libros1 = [
    { id: 1, titulo: "grich", autor: "NDEL GUZMAN ADELA", año: 1967 },
    { id: 2, titulo: "los 7 enanos", autor: "NAIS MOON DE PERRERIRA", año: 1995 },
    { id: 3, titulo: "IT", autor: "NAEL GUZMAN ", año: 1983 },
    { id: 4, titulo: "interestelar", autor: "DAN GRIEZMAN", año: 2016 }
  ];
  
  for (let libro of libros1) {
    if (libro.id === 3) {
      libro.titulo = "Final del juego";
    }
  }
  
  console.log("Libros actualizados:", libros1);


//5. Crear una  funcion que muestre solo los titulos de arreglo libros usando for..of


const libros2 = [
    { id: 1, titulo: "grich", autor: "NDEL GUZMAN ADELA", año: 1967 },
    { id: 2, titulo: "los 7 enanos", autor: "NAIS MOON DE PERRERIRA", año: 1995 },
    { id: 3, titulo: "IT", autor: "NAEL GUZMAN ", año: 1983 },
    { id: 4, titulo: "interestelar", autor: "DAN GRIEZMAN", año: 2016 }
  ];
  
  function mostrarTitulos(libros) {
    console.log("Títulos de libros:");
    for (let libro of libros) {
      console.log(libro.titulo);
    }
  }
  
  mostrarTitulos(libros2);