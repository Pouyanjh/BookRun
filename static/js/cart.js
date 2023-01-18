var updateBtns = document.getElementsByClassName('update-cart')


for (i=0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productid = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productid, 'action:', action)
        

        console.log('USER:', user)
        if (user=='Anonymoususer'){
            console.log('User is not authenticated')
        }else{
            updateUserOrder(productid, action)
        }

    })
}
function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data....')
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'applicatin/json',
            'X-CSRFToken': csrftoken,

        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) => {
        return response.json();

    })
    .then((data) => {
        console.log('Data:', data)
        location.reload()
    })
}