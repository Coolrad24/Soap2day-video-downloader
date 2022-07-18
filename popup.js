document.querySelector('#download').addEventListener('click',function(){
    chrome.tabs.query({currentWindow:true,active: true},function(tabs){
        chrome.tabs.sendMessage(tabs[0].id,{command:'download'})
    })
})