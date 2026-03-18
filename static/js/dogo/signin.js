document.getElementById("btn-signin").addEventListener("click", login);

function login(){
    const email = document.getElementById("user-email").value;
    const password = document.getElementById("user-password").value;

    if(email == ""){
        alert("Debe ingresar su corrreo electronico")
    }

    if(password == ""){
        alert("Debe ingresar su contraseña")
    }

    const data = {
        name: document.getElementById("user-name").value,
        email: document.getElementById("user-email").value,
        password: document.getElementById("user-password").value

    }

    fetch('api/users', {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(result => {
        if(result.success){
            window.location.href = "/welcome";
        }else{
            alert("Sus datos de acceso no son correctos")
        }
    })
    .catch(error => {
        console.error(error);
    })
}
