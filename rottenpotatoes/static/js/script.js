$(document).ready(function () {
  $(".comprarBtn").click(handleCompraClick);
  $("#lista-carrito").on("click", ".eliminarBtn", handleEliminarClick);
});

function handleCompraClick() {
  var nombre = $(this).data("nombre");
  var precio = $(this).data("precio");
  var id = generarIdUnico();
  var existe = verificarDuplicado(nombre, precio);

  // Desactivar el botón temporalmente para e-vitar clics repetidos
  $(this).prop("disabled", true);

  if (!existe) {
    $("#lista-carrito").append(
      '<li id="' +
        id +
        '">' +
        nombre +
        " - Precio: $" +
        precio +
        '<button class="eliminarBtn" data-id="' +
        id +
        '">Eliminar</button></li>'
    );

    var total = parseInt($("#total").text());
    total += precio;
    $("#total").text(total);
  } else {
    alert("Este producto ya está en el carrito.");
  }
}

function handleEliminarClick() {
  var id = $(this).data("id");
  var precio = parseInt(
    $("#" + id)
      .text()
      .match(/\d+/)[0]
  );
  $("#" + id).remove();

  var total = parseInt($("#total").text());
  total -= precio;
  $("#total").text(total);
}

function verificarDuplicado(nombre, precio) {
  var existe = false;

  $("#lista-carrito li").each(function () {
    if ($(this).text() === nombre + " - Precio: $" + precio) {
      existe = true;
      // Habilitar el botón nuevamente si el producto ya existe en el carrito
      $(
        '.comprarBtn[data-nombre="' +
          nombre +
          '"][data-precio="' +
          precio +
          '"]'
      ).prop("disabled", false);
      return false;
    }
  });

  return existe;
}

function generarIdUnico() {
  return "item-" + Math.random().toString(36).substr(2, 9);
}

$("#btn-cargar").click(function (event) {
  event.preventDefault();

  var url =
    "https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key= live_QHEoEd9Rx2DNEwjudLKprwA4cHdP3Rna428SOoVrbM7HAHSTwJaCtxoztIpOl8KI";

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      var imageUrl = data[0].url;
      var $foto_animal = $(
        "<p><img id='imagen-gato' src='" + imageUrl + "' alt='Gato'>"
      );

      // Limpiar el contenedor antes de desplegar
      $("#info").empty();
      $("#info").append($foto_animal);

      // Establecer dimensiones más pequeñas para la imagen
      $("#imagen-gato").css({
        "max-width": "500px", // Ancho máximo deseado
        height: "auto", // Altura ajustada automáticamente
      });
    })
    .catch((error) => console.error(error));
});

$(document).ready(function () {
  $("#password").on("input", function () {
    var password = $(this).val();
    var passwordTip = $("#passwordTip");

    // Validar la contraseña
    var isValid =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>]).{8,}$/.test(
        password
      );

    // Mostrar u ocultar el mensaje de consejos de contraseña según la validez de la contraseña
    if (isValid) {
      passwordTip.hide();
    } else {
      passwordTip.show();
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var dropdowns = document.querySelectorAll(".dropdown");

  dropdowns.forEach(function (dropdown) {
    var dropbtn = dropdown.querySelector(".dropbtn");
    var dropdownContent = dropdown.querySelector(".dropdown-content");

    dropbtn.addEventListener("click", function (event) {
      event.preventDefault(); 
      dropdownContent.classList.toggle("show");
    });

    window.addEventListener("click", function (event) {
      if (!dropdown.contains(event.target)) {
        dropdownContent.classList.remove("show");
      }
    });
  });
});


document.getElementById('password').addEventListener('input', function () {
  var password = this.value;
  var passwordTip = document.getElementById('passwordTip');
  var requirementsMet = true;

  if (password.length < 8) {
      requirementsMet = false;
  }
  if (!/[A-Z]/.test(password)) {
      requirementsMet = false;
  }
  if (!/[a-z]/.test(password)) {
      requirementsMet = false;
  }
  if (!/\d/.test(password)) {
      requirementsMet = false;
  }
  if (!/[$&+,:;=?@#|'<>.^*()%!-]/.test(password)) {
      requirementsMet = false;
  }

  if (requirementsMet) {
      passwordTip.style.color = 'green';
  } else {
      passwordTip.style.color = 'red';
  }
});
