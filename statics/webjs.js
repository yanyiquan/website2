function newf() {
            if ($('#only').checked()) {
                $('#box1').attr('disabled', 'true');
                document.getElementById("box1").disabled = 'disabled';
                document.getElementById("box2").disabled = 'disabled';
                document.getElementById("box3").disabled = 'disabled';
            }
}
