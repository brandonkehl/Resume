const countBK = document.getElementById('count');

updateVisitCount()

function updateVisitCount(){
  fetch('https://api.countapi.xyz/update/kehlbrandon.com/bkehl?amount=1')
      .then(res => res.json())
      .then(res => {
              countBK.innerHTML = res.value;
    
  })
}