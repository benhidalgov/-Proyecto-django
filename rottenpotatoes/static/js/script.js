$(document).ready(function () {
  // Evento click para añadir productos al carrito
  $(".comprarBtn").click(function () {
    var nombre = $(this).closest(".card").find(".card-title").text().trim();
    var precio = parseFloat(
      $(this)
        .closest(".card")
        .find(".card-text:last")
        .text()
        .trim()
        .replace("Precio: $", "")
    );

    agregarAlCarrito(nombre, precio);
  });

  $("#lista-carrito").on("click", ".eliminarBtn", function () {
    var precioEliminar = parseFloat($(this).data('precio'));

    var totalActual = parseFloat($("#total").text().replace(/[^\d.-]/g, ""));
    var nuevoTotal = totalActual - precioEliminar;

    $("#total").text("$" + nuevoTotal.toFixed(2));

    $(this).closest("li").remove();
  });

  function agregarAlCarrito(nombre, precio) {
    var listItem = $('<li></li>');
    listItem.addClass('list-group-item d-flex justify-content-between align-items-center');
    listItem.html(`${nombre} - Precio: $${precio.toFixed(2)} <button class="btn btn-danger btn-sm eliminarBtn" data-precio="${precio}">Eliminar</button>`);

    $("#lista-carrito").append(listItem);

    var totalActual = parseFloat($("#total").text().replace(/[^\d.-]/g, ""));
    var nuevoTotal = totalActual + precio;

    $("#total").text("$" + nuevoTotal.toFixed(2));
  }

  // Función para verificar si el producto ya está en el carrito
  function verificarDuplicado(nombre, precio) {
    var duplicado = false;
    $("#lista-carrito li").each(function () {
      var itemNombre = $(this).text().split(" - ")[0];
      if (itemNombre === nombre) {
        duplicado = true;
        return false;
      }
    });
    return duplicado;
  }

  // Función para actualizar el total del carrito
  function actualizarTotal(cantidad) {
    var total = parseFloat(
      $("#total")
        .text()
        .replace(/[^\d.-]/g, "")
    );
    total += cantidad;
    $("#total").text("$" + total.toFixed(2));
  }

  // Función para generar un ID único para cada item del carrito
  function generarIdUnico() {
    return "item-" + Math.random().toString(36).substr(2, 9);
  }
});

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

document.getElementById("password").addEventListener("input", function () {
  var password = this.value;
  var passwordTip = document.getElementById("passwordTip");
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
    passwordTip.style.color = "green";
  } else {
    passwordTip.style.color = "red";
  }
});
$(document).ready(function () {
  $("#registro-form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
      url: "",
      method: "POST",
      data: $(this).serialize(),
      success: function (response) {
        if (response.success) {
          $("#success-message").show();
          $("#error-message").hide();
          $("#username-success").text(response.username);
          $("#email-success").text(response.email);
          $("#registro-form")[0].reset();
        } else {
          $("#success-message").hide();
          $("#error-message").show();
          $("#errors").empty();
          $.each(response.errors, function (key, errorList) {
            errorList.forEach(function (error) {
              $("#errors").append("<li>" + error + "</li>");
            });
          });
        }
      },
    });
  });
});
$(document).ready(function () {
  $("#login-form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
      url: "",
      method: "POST",
      data: $(this).serialize(),
      success: function (response) {
        if (response.success) {
          $("#success-message").show();
          $("#error-message").hide();
          $("#username-success").text(response.username);
          $("#login-form")[0].reset();
        } else {
          $("#success-message").hide();
          $("#error-message").show();
          $("#errors").text(response.error);
        }
      },
    });
  });
});
$(document).ready(function () {
  $(".comprarBtn").click(handleCompraClick);
  $("#lista-carrito").on("click", ".eliminarBtn", handleEliminarClick);
  $("#logoutLink").click(handleLogoutClick);

  function handleLogoutClick(event) {
    event.preventDefault();

    var csrftoken = getCookie("csrftoken");

    $.ajax({
      url: '{% url "logout" %}',
      method: "POST",
      headers: {
        "X-CSRFToken": csrftoken,
      },
      success: function (response) {
        if (response.success) {
          window.location.href = "/";
        } else {
          alert("Error al cerrar sesión. Inténtalo de nuevo.");
        }
      },
      error: function (xhr, status, error) {
        console.error("Error al cerrar sesión:", error);
        alert("Error al cerrar sesión. Inténtalo de nuevo.");
      },
    });
  }

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
document.addEventListener("DOMContentLoaded", function () {
  var logoutLink = document.getElementById("logoutLink");
  if (logoutLink) {
    logoutLink.addEventListener("click", function (event) {
      event.preventDefault();
      var csrfToken = getCookie("csrftoken"); // Obtén el token CSRF
      fetch("{% url 'logout' %}", {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
        },
      })
        .then(function (response) {
          if (response.ok) {
            window.location.href = "{% url 'base' %}"; // Redirigir a la página base después de cerrar sesión
            // Actualiza la UI aquí si es necesario
            document.getElementById("loginLink").style.display = "block";
          } else {
            console.error("Error al cerrar sesión");
          }
        })
        .catch(function (error) {
          console.error("Error al cerrar sesión:", error);
        });
    });
  }
});

// Función para obtener el valor del token CSRF de las cookies
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Buscar el nombre del token CSRF en las cookies
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
