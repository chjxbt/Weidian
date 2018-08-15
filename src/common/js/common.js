// document.getElementsByTagName('title')[0].innerHTML = val;
// window.setDocumentTitle = function(title) {
//   var i = document.createElement('iframe');
//   i.src = '../favicon.ico';
//   i.style.display = 'none';
//   i.onload = function() {
//     setTimeout(function(){
//       i.remove();
//     }, 9)
//   }
//   document.body.appendChild(i);
// };//ios
const common = {
  changeTitle:function (val){
    document.getElementsByTagName('title')[0].innerHTML = val;
    window.setDocumentTitle = function(title) {
      var i = document.createElement('iframe');
      i.src = '../favicon.ico';
      i.style.display = 'none';
      i.onload = function() {
        setTimeout(function(){
          i.remove();
        }, 9)
      }
      document.body.appendChild(i);
    };//ios
  }
}
export default common
