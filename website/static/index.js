/********** Nav Bar **********/
window.addEventListener("DOMContentLoaded", () => {
    window.addEventListener("DOMContentLoaded", () => {
        const activePage = window.location.pathname;
        document.querySelectorAll(".navlink").forEach((link) => {
            if (link.href === window.location.href) {
                link.classList.add("active");
            }
        });
    });
})

/********** Login / Singup (source: https://www.codingnepalweb.com/login-form-validation-in-html-javascript/) **********/
document.addEventListener("DOMContentLoaded", ()=> {
    const form = document.querySelector("form");
    eField = form.querySelector(".email"),
    eInput = eField.querySelector("input"),
    pField = form.querySelector(".password"),
    pInput = pField.querySelector("input");
    form.onsubmit = (e)=>{
    e.preventDefault(); //preventing from form submitting
    //if email and password is blank then add shake class in it else call specified function
    (eInput.value == "") ? eField.classList.add("shake", "error") : checkEmail();
    (pInput.value == "") ? pField.classList.add("shake", "error") : checkPass();
    setTimeout(()=>{ //remove shake class after 500ms
        eField.classList.remove("shake");
        pField.classList.remove("shake");
    }, 500);
    eInput.onkeyup = ()=>{checkEmail();} //calling checkEmail function on email input keyup
    pInput.onkeyup = ()=>{checkPass();} //calling checkPassword function on pass input keyup
    function checkEmail(){ //checkEmail function
        let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; //pattern for validate email
        if(!eInput.value.match(pattern)){ //if pattern not matched then add error and remove valid class
        eField.classList.add("error");
        eField.classList.remove("valid");
        let errorTxt = eField.querySelector(".error-txt");
        //if email value is not empty then show please enter valid email else show Email can't be blank
        (eInput.value != "") ? errorTxt.innerText = "Enter a valid email address" : errorTxt.innerText = "Email can't be blank";
        }else{ //if pattern matched then remove error and add valid class
        eField.classList.remove("error");
        eField.classList.add("valid");
        }
    }
    function checkPass(){ //checkPass function
        if(pInput.value == ""){ //if pass is empty then add error and remove valid class
        pField.classList.add("error");
        pField.classList.remove("valid");
        }else{ //if pass is empty then remove error and add valid class
        pField.classList.remove("error");
        pField.classList.add("valid");
        }
    }
    // if eField and pField doesn't contains error class that mean user filled details properly
    if(!eField.classList.contains("error") && !pField.classList.contains("error")){
        window.location.href = form.getAttribute("action"); //redirecting user to the specified url which is inside action attribute of form tag
    }
    }
});

/********** Multi step sign in form (source: https://formbold.com/templates/multi-step-form) **********/
document.addEventListener("DOMContentLoaded", ()=> {
    const stepMenuOne = document.querySelector('.formbold-step-menu1')
    const stepMenuTwo = document.querySelector('.formbold-step-menu2')
    const stepMenuThree = document.querySelector('.formbold-step-menu3')
    
    const stepOne = document.querySelector('.formbold-form-step-1')
    const stepTwo = document.querySelector('.formbold-form-step-2')
    const stepThree = document.querySelector('.formbold-form-step-3')
    
    const formSubmitBtn = document.querySelector('.formbold-btn')
    const formBackBtn = document.querySelector('.formbold-back-btn')
    
    formSubmitBtn.addEventListener("click", function(event){
    event.preventDefault()
    if(stepMenuOne.className == 'formbold-step-menu1 active') {
        event.preventDefault()
    
        stepMenuOne.classList.remove('active')
        stepMenuTwo.classList.add('active')
    
        stepOne.classList.remove('active')
        stepTwo.classList.add('active')
    
        formBackBtn.classList.add('active')
        formBackBtn.addEventListener("click", function (event) {
            event.preventDefault()
    
            stepMenuOne.classList.add('active')
            stepMenuTwo.classList.remove('active')
    
            stepOne.classList.add('active')
            stepTwo.classList.remove('active')
    
            formBackBtn.classList.remove('active')
    
        })
    
        } else if(stepMenuTwo.className == 'formbold-step-menu2 active') {
        event.preventDefault()
    
        stepMenuTwo.classList.remove('active')
        stepMenuThree.classList.add('active')
    
        stepTwo.classList.remove('active')
        stepThree.classList.add('active')
    
        formBackBtn.classList.remove('active')
        formSubmitBtn.textContent = 'Submit'
        } else if(stepMenuThree.className == 'formbold-step-menu3 active') {
        document.querySelector('form').submit()
        }
    })
})
