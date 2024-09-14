let guitar = document.querySelector('#guitar')
let sitar = document.querySelector('#sitar')

let arr = [guitar,sitar]
let userEmail = document.querySelector('#email').innerHTML  
let data = ''






guitar.addEventListener('click',(e)=>{
    console.log(e.target)
    data = 'guitar'
})



sitar.addEventListener('click',(e)=>{
    console.log(e.target)
    data = 'sitar'
})

let submit = document.querySelector("#submit")
submit.addEventListener('click',(e)=>{
  let word_1 = document.getElementById('word_1')
  let word_2 = document.getElementById('word_2')
  let word_3 = document.getElementById('word_3')
  let word_4 = document.getElementById('word_4')
  
  word_list = [word_1.value,word_2.value,word_3.value,word_4.value]
  console.log("clikced")
    if(data!=''){
        fetch('/submit_instrument', { 
            method: 'POST', 
            headers: { 
              "Content-type": "application/json"
            }, 
            
            body: JSON.stringify({'email':userEmail,'instrument':data,'word_list':word_list})
          }).then((a)=>{
            location.href('/signup')
          }) 
           
    }
})