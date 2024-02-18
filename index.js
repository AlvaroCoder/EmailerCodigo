const nodemailer = require('nodemailer');
const {HTML_TEMPLATE} = require('./html_template')

const transporter = nodemailer.createTransport({
    service : 'gmail',
    auth : {
        user : 'ieeecs.directiva@gmail.com',
        pass : "whxgdpygtrrsvtwm"
    }
});

const emails = [
    {name : 'Adolfo Daniello', email : 'daniellogranda766@gmail.com'}, 
    {name: 'Santiago', email:'srca.alayza@gmail.com'},
    {name:'María Alexandra',email:'mariaalex2001@gmail.com'},{name:'Freddy Alexander',email:'alexanderjc2024@gmail.com'},{name:'Faviana',email:'favianagarcia21@gmail.com'},{name:'Piero Aderli',email:'pierozeta16@gmail.com'},{name:'Daniela Abigail',email:'danielarivera2604@gmail.com'}]

for (const key of emails) {
    const mailOptions = {
        from : 'ieeecs.directiva@gmail.com',
        to : key.email,
        subject : 'Bienvenido a CS',
        text : 'Bienvenido a CS UDEP es un honor tenerte aquí',
        html : HTML_TEMPLATE(key.name)
    }
    transporter.sendMail(mailOptions, (err, info)=>{
        if (err) {
            throw err;
        }
        console.log(`Email enviado : ${info.response}`);
    })
}
