<script type="text/javascript" src="https://sdk.userbase.com/2/userbase.js"></script>
<script type="text/javascript">

//this can only be ran with new username and password
//frozen until ready to test with more users
//todo: set up html form submission for this
async function start() { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
 	
  //todo: make new element for this
  load_bar.innerText = 'Creating an account...'
  await userbase.signUp({ 
    username: "test_acct",
    password: "test_psswrd"
  })

  db_item1.innerText = 'Opening database...'
  await userbase.openDatabase({
    databaseName: 'demo',
    changeHandler: function (items) {     
      if (items.length) {
        db_item2.innerText = items[0].item
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
  load_bar.innerText = 'Retreiving account...'
  //"test_acct",
  //"test_psswrd"
  await userbase.signIn({ username: u_name, password: p_word })

}

async function send_data(store_string) { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  
  load_bar.innerText = 'Opening database...'
  await userbase.openDatabase({
    databaseName: 'demo',
    changeHandler: function (items) {     
	console.log(items)
      }
    })
 
  await userbase.insertItem({
    databaseName: 'demo',
    item: store_string
  })
  
  load_bar.innerText = 'Data Sent...'
  console.log(store_string)

}

async function get_data() { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  
  load_bar.innerText = 'Opening database...'
  await userbase.openDatabase({
    databaseName: 'demo',
    changeHandler: function (items) {     
      console.log(items)
      db_item1.innerText = items[0].item	
      db_item2.innerText = items[items.length -1].item	
      for (let i = 0; i < items.length; i++){
	console.log(items[i].itemId, items[i].item)
      }
    }
  })

  await userbase.getDatabases().then((databases) => {
      console.log(databases)
  })

}

// code for the start button
window.addEventListener("DOMContentLoaded", (event) => {
    //Frozen after test account was created
    //const button = document.getElementById('btn')
    //button.addEventListener('click', function () { 
     //button.style.display = 'none'
     //if (sessionStorage) sessionStorage.clear()
     //start()
    //})
    
    //LOGIN
    const load_bar = document.getElementById('load_bar')

    //Frozen when test login was finalized
    //const db_item1 = document.getElementById('db_item1')
    //const db_item2 = document.getElementById('db_item2')

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
	
    //Test User Data Access, written for login verification 
    //const button3 = document.getElementById('get_user_data')
    //button3.addEventListener('click', function () { 
     //button3.style.display = 'none'
     //if (sessionStorage) sessionStorage.clear()
     //get_data()
    //})
    
    let i_name = document.getElementById("Name");            
    let i_e = document.getElementById("Equipment");
    let i_elt1 = document.getElementById("Ingredient1");
    let i_elt2 = document.getElementById("Ingredient2");
    let i_elt3 = document.getElementById("Ingredient3");
    let i_s1 = document.getElementById("Step1");
    let i_s2 = document.getElementById("Step2");
    let i_s3 = document.getElementById("Step3");
  
    const int_button = document.getElementById('send_int')
    int_button.addEventListener('click', function () { 
    int_button.style.display = 'none'
    if (sessionStorage) sessionStorage.clear()
     	send_data("&N;".concat(
		i_name,";","&E;",i_e,";",
	        "&I;",i_elt1,";",i_elt2,";",elt3,
	        "&S;",i_s1,";",i_s2,";",i_s3
	))
    })

});


</script>
