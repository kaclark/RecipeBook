<script type="text/javascript" src="https://sdk.userbase.com/2/userbase.js"></script>
<script type="text/javascript">

//this can only be ran with new username and password
//frozen until ready to test with more users
async function start() { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  
  title.innerText = 'Creating an account...'
  await userbase.signUp({ 
    username: "test_acct",
    password: "test_psswrd"
  })

  title.innerText = 'Opening database...'
  await userbase.openDatabase({
    databaseName: 'demo',
    changeHandler: function (items) {     
      if (items.length) {
        title.innerText = items[0].item
      }
    }
  })

  await userbase.insertItem({
    databaseName: 'demo',
    item: 'Hello world!\n\n<end-to-end encrypted>'
  })

}

//should be pressed first
async function get_user(u_name, p_word) { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  title.innerText = 'Retreiving account...'
  //"test_acct",
  //"test_psswrd"
  await userbase.signIn({ username: u_name, password: p_word })
  console.log

}

//pressed second
async function push_data() { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  
  title.innerText = 'Opening database...'
  await userbase.openDatabase({
    databaseName: 'demo',
    changeHandler: function (items) {     
      console.log(items)
      post.innerText = items[items.length -1].item	
      for (let i = 0; i < items.length; i++){
	console.log(items[i].itemId, items[i].item)
      }
      if (items.length) {
        title.innerText = items[0].item
      }
    }
  })
 
  //Frozen until we need to add more posts
  //await userbase.insertItem({
  //  databaseName: 'demo',
  //  item: 'Hegel is always around the Corner'
  //})

  await userbase.getDatabases().then((databases) => {
      console.log(databases)
  })

}


// code for the start button
window.addEventListener("DOMContentLoaded", (event) => {
    //const button = document.getElementById('btn')
    //button.addEventListener('click', function () { 
     //button.style.display = 'none'
     //if (sessionStorage) sessionStorage.clear()
     //start()
    })
    const title = document.getElementById('title')

    //freezing during testing of login form input	
    //const button2 = document.getElementById('btn2')
    //button2.addEventListener('click', function () { 
    //  button2.style.display = 'none'
    //  if (sessionStorage) sessionStorage.clear()
    //  get_user()
    //})
    let loginForm = document.getElementById("loginForm");

    loginForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let usrname = document.getElementById("username");
    let pssword = document.getElementById("password");

    if (usrname.value == "" || pssword.value == "") {
      alert("Ensure you input a value in both fields!");
    } else {
      // perform operation with form input
      get_user(usrname.value, pssword.value)
   alert("This form has been successfully submitted!");
   console.log(
      `This form has a username of ${username.value} and password of ${password.value}`
    );
  }
});

    const button3 = document.getElementById('btn3')
    button3.addEventListener('click', function () { 
      button3.style.display = 'none'
      if (sessionStorage) sessionStorage.clear()
      push_data()
    })

});


</script>
