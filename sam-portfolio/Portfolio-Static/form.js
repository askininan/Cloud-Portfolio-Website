const send = document.querySelector('button')
const input = document.querySelector('form')

window.addEventListener('DOMContentLoaded', (event) => {
    send.addEventListener('click',function() {
        Email.send({
            Host: "smtp.mailtrap.io",
            Username: "b703e360e72539",
            Password: "0b29b331f4f09c",
            To: "askininan@gmail.com",
            From: input.elements["email"].value,
            Subject: "Contact Me Message from:" + input.elements["email"].value ,
            Body: "Name:" + input.elements["name"].value + "<br/> E-mail:" + input.elements["email"].value + "<br/>" + "<br/>" + input.elements["message"].value
        }).then(alarmmessage => alert("Your message is successfully sent."))
        setTimeout(function(){
            document.getElementById('form').reset();
        }, 1);
        ;
    })
});