// $( document ).ready(function() {
//     $("#form-tolerance").submit(function(e){
//         e.preventDefault();
//         var data = {};

//         var data_arr = $( this ).serializeArray();
//         data_arr.forEach(function(element){
//             data[element["name"]] = element["value"];
            
//         });
//         localStorage.setItem("form-tolerance", JSON.stringify(data));
//         this.submit();
//     });

//     $("#form-tolerance-prev").click(function(){
//         var data = localStorage.getItem("form-tolerance");
//         data = JSON.parse(data);
//         console.log(data);
//     });
// });