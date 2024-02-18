const emails = [{name : 'Adolfo Daniello', email : 'daniellogranda766@gmail.com'}, {name: 'Santiago', email:'srca.alayza@gmail.com'},{name:'María Alexandra',email:'mariaalex2001@gmail.com'},{name:'Freddy Alexander',email:'alexanderjc2024@gmail.com'},{name:'Faviana',email:'favianagarcia21@gmail.com'},{name:'Piero Aderli',email:'pierozeta16@gmail.com'},{name:'Daniela Abigail',email:'danielarivera2604@gmail.com'}]

for (const key of emails) {
    console.log(key);
    console.log(`${key.name}->${key.email}`);
}